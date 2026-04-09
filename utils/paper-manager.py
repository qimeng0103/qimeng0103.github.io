#!/usr/bin/env python3
"""
Paper Library Manager
=====================
A smart literature management system for physics research.

Usage:
    paper-manager.py add <url> [options]
    paper-manager.py list [--tag TAG] [--status STATUS]
    paper-manager.py search <query>
    paper-manager.py today
    paper-manager.py stats
    paper-manager.py tags
    paper-manager.py to-blog <paper-file>
    paper-manager.py journal <text>
"""

import os
import sys
import re
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from urllib.parse import urlparse
from dataclasses import dataclass, asdict

# Configuration
LIBRARY_DIR = Path(__file__).parent.parent / "paper-library"
PAPERS_DIR = LIBRARY_DIR / "papers"
TAGS_DIR = LIBRARY_DIR / "tags"
AESTHETICS_DIR = LIBRARY_DIR / "aesthetics"
TEMPLATE_FILE = LIBRARY_DIR / ".templates" / "paper-template.md"
TASTE_JOURNAL = AESTHETICS_DIR / "taste-journal.md"

# Classification rules for auto-tagging
CLASSIFICATION_RULES = {
    "topology": [
        "topological", "Chern number", "Berry phase", "Berry curvature",
        "Weyl", "Dirac cone", "Majorana", "edge state", "surface state",
        "topological invariant", "band topology", "Z2 invariant"
    ],
    "superconductivity": [
        "superconductor", "superconductivity", "BCS", "pairing", "gap",
        "Cooper pair", "Josephson", "Meissner", "vortex", "critical temperature"
    ],
    "quantum-info": [
        "quantum computing", "qubit", "quantum information", "entanglement",
        "quantum error", "quantum algorithm", "quantum circuit", "quantum gate"
    ],
    "many-body": [
        "many-body", "strongly correlated", "Hubbard", "Mott",
        "quantum Hall", "Luttinger liquid", "spin liquid", "fractional"
    ],
    "qft-condmat": [
        "field theory", "path integral", "Green function", "diagrammatic",
        "renormalization", "effective field theory", "bosonization"
    ],
    "symmetry": [
        "symmetry", "group theory", "representation", "character table",
        "irreducible", "Lie group", "gauge symmetry", "spontaneous symmetry breaking"
    ],
    "transport": [
        "transport", "conductance", "conductivity", "scattering", "ballistic",
        "diffusive", "Landauer", "Nernst", "thermoelectric", "quantum dot"
    ],
    "numerics": [
        "DMRG", "tensor network", "MPS", "PEPS", "MERA", "QMC", "Monte Carlo",
        "DMFT", "DFT", "density functional", "exact diagonalization", "numerical"
    ],
    "graphene-2d": [
        "graphene", "2D material", "van der Waals", "TMD", "hBN", "transition metal dichalcogenide"
    ],
    "cft-holography": [
        "conformal field theory", "CFT", "AdS/CFT", "holography", "holographic",
        "anti-de Sitter", "conformal"
    ],
}

# Status emojis
STATUS_EMOJI = {
    "unread": "📖",
    "reading": "👀",
    "skimmed": "📝",
    "deep-read": "🔬",
    "implemented": "✅"
}


@dataclass
class Paper:
    """Represents a paper entry."""
    title: str
    authors: str
    date_added: str
    source: str
    url: str
    tags: List[str]
    status: str = "unread"
    rating: str = "⭐⭐⭐☆☆"
    filename: str = ""
    arxiv_id: str = ""
    abstract: str = ""
    year: str = ""
    
    def to_dict(self) -> Dict:
        return asdict(self)


def get_year_dir() -> Path:
    """Get the directory for current year."""
    year = datetime.now().year
    year_dir = PAPERS_DIR / str(year)
    year_dir.mkdir(parents=True, exist_ok=True)
    return year_dir


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text[:50]  # Limit length


def generate_filename(title: str) -> str:
    """Generate a filename from title and date."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title) if title else "untitled"
    return f"{date_str}-{slug}.md"


def auto_classify(text: str) -> List[str]:
    """Auto-classify paper based on text content."""
    text_lower = text.lower()
    tags = []
    
    for tag, keywords in CLASSIFICATION_RULES.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                tags.append(tag)
                break
    
    return tags if tags else ["general"]


def extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arXiv ID from URL."""
    patterns = [
        r'arxiv\.org/abs/(\d+\.\d+)',
        r'arxiv\.org/abs/(\d+\.\d+v\d+)',
        r'arXiv:(\d+\.\d+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def fetch_arxiv_info(arxiv_id: str) -> Optional[Dict]:
    """Fetch paper information from arXiv API."""
    try:
        import urllib.request
        import xml.etree.ElementTree as ET
        
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read().decode('utf-8')
        
        # Parse XML
        root = ET.fromstring(data)
        
        # Define namespace
        ns = {
            'atom': 'http://www.w3.org/2005/Atom',
            'arxiv': 'http://arxiv.org/schemas/atom'
        }
        
        entry = root.find('atom:entry', ns)
        if entry is None:
            return None
        
        title = entry.find('atom:title', ns)
        summary = entry.find('atom:summary', ns)
        published = entry.find('atom:published', ns)
        
        authors = entry.findall('atom:author', ns)
        author_names = [a.find('atom:name', ns).text for a in authors if a.find('atom:name', ns) is not None]
        
        return {
            'title': title.text.strip() if title else "",
            'abstract': summary.text.strip() if summary else "",
            'authors': ', '.join(author_names[:3]) + (' et al.' if len(author_names) > 3 else ''),
            'year': published.text[:4] if published else datetime.now().year,
            'arxiv_id': arxiv_id
        }
    except Exception as e:
        print(f"Warning: Could not fetch arXiv info: {e}")
        return None


def create_paper_file(paper: Paper) -> Path:
    """Create a new paper file from template."""
    if not TEMPLATE_FILE.exists():
        print(f"Error: Template file not found: {TEMPLATE_FILE}")
        sys.exit(1)
    
    with open(TEMPLATE_FILE, 'r') as f:
        template = f.read()
    
    # Replace placeholders
    content = template
    content = content.replace("{{TITLE}}", paper.title or "Unknown Title")
    content = content.replace("{{AUTHORS}}", paper.authors or "Unknown")
    content = content.replace("{{DATE}}", paper.date_added)
    content = content.replace("{{SOURCE}}", paper.source or "Unknown")
    content = content.replace("{{URL}}", paper.url)
    content = content.replace("{{DOI}}", "")
    content = content.replace("{{ARXIV_ID}}", paper.arxiv_id or "")
    content = content.replace("{{YEAR}}", str(paper.year or datetime.now().year))
    content = content.replace("{{JOURNAL}}", "")
    content = content.replace("{{CITATIONS}}", "N/A")
    content = content.replace("{{TAGS}}", ", ".join(paper.tags))
    content = content.replace("{{TAG1}}", paper.tags[0] if paper.tags else "general")
    content = content.replace("{{TAG2}}", paper.tags[1] if len(paper.tags) > 1 else "")
    content = content.replace("{{TAG3}}", paper.tags[2] if len(paper.tags) > 2 else "")
    
    # Write file
    year_dir = get_year_dir()
    filename = generate_filename(paper.title) if not paper.filename else paper.filename
    filepath = year_dir / filename
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    return filepath


def update_tags_index(paper: Paper, filepath: Path):
    """Update tag index files."""
    TAGS_DIR.mkdir(parents=True, exist_ok=True)
    
    for tag in paper.tags:
        tag_file = TAGS_DIR / f"{tag}.md"
        
        # Create tag file if it doesn't exist
        if not tag_file.exists():
            with open(tag_file, 'w') as f:
                f.write(f"# #{tag}\n\n> Papers tagged with '{tag}'\n\n")
        
        # Append to tag file
        with open(tag_file, 'a') as f:
            rel_path = os.path.relpath(filepath, LIBRARY_DIR)
            f.write(f"- [{paper.title}]({rel_path}) - {paper.date_added}\n")


def cmd_add(args):
    """Add a new paper to the library."""
    url = args.url
    
    print(f"🔍 Processing: {url}")
    
    # Try to extract arXiv ID
    arxiv_id = extract_arxiv_id(url)
    
    paper_info = {}
    if arxiv_id:
        print(f"📄 Found arXiv ID: {arxiv_id}")
        print("🌐 Fetching information from arXiv...")
        paper_info = fetch_arxiv_info(arxiv_id) or {}
        paper_info['source'] = 'arXiv'
    else:
        paper_info = {
            'source': urlparse(url).netloc or 'Unknown',
            'arxiv_id': ''
        }
    
    # Override with command line arguments
    title = args.title or paper_info.get('title', '')
    authors = args.authors or paper_info.get('authors', '')
    tags = args.tags.split(',') if args.tags else []
    abstract = paper_info.get('abstract', '')
    year = str(paper_info.get('year', datetime.now().year))
    
    # Auto-classify if no tags provided
    if not tags:
        classify_text = f"{title} {abstract}"
        tags = auto_classify(classify_text)
        print(f"🏷️  Auto-classified tags: {', '.join(tags)}")
    else:
        tags = [t.strip() for t in tags]
    
    # Create paper object
    paper = Paper(
        title=title,
        authors=authors,
        date_added=datetime.now().strftime("%Y-%m-%d"),
        source=paper_info.get('source', 'Unknown'),
        url=url,
        tags=tags,
        arxiv_id=arxiv_id or '',
        abstract=abstract,
        year=year
    )
    
    # Create file
    filepath = create_paper_file(paper)
    print(f"✅ Created: {filepath}")
    
    # Update tags
    update_tags_index(paper, filepath)
    
    # Print summary
    print(f"\n📋 Paper Summary:")
    print(f"   Title: {paper.title}")
    print(f"   Authors: {paper.authors}")
    print(f"   Tags: {', '.join(paper.tags)}")
    print(f"   Status: {paper.status}")
    
    print(f"\n💡 Next steps:")
    print(f"   1. Edit the file: vim {filepath}")
    print(f"   2. Record your taste: vim {TASTE_JOURNAL}")
    print(f"   3. When done reading, update status with:")
    print(f"      paper-manager.py status {filepath.name} deep-read")


def cmd_list(args):
    """List papers in the library."""
    papers = []
    
    # Collect all paper files
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir():
            for paper_file in year_dir.glob("*.md"):
                papers.append(paper_file)
    
    # Sort by date (newest first)
    papers.sort(reverse=True)
    
    # Filter by tag if specified
    if args.tag:
        filtered = []
        for p in papers:
            content = p.read_text()
            if f"- {args.tag}" in content or f"tags:\n  - {args.tag}" in content:
                filtered.append(p)
        papers = filtered
    
    # Filter by status if specified
    if args.status:
        filtered = []
        for p in papers:
            content = p.read_text()
            if f'status: "{args.status}"' in content:
                filtered.append(p)
        papers = filtered
    
    # Display
    print(f"\n📚 Found {len(papers)} papers:\n")
    print(f"{'Date':<12} {'Status':<10} {'Title':<50} {'Tags'}")
    print("-" * 100)
    
    for p in papers[:args.limit]:
        content = p.read_text()
        
        # Extract metadata
        date_match = re.search(r'date_added: "(\d{4}-\d{2}-\d{2})"', content)
        date = date_match.group(1) if date_match else "????-??-??"
        
        status_match = re.search(r'status: "(\w+)"', content)
        status = status_match.group(1) if status_match else "unknown"
        status_emoji = STATUS_EMOJI.get(status, "📄")
        
        title_match = re.search(r'title: "([^"]+)"', content)
        title = title_match.group(1)[:45] if title_match else p.stem
        
        tags_match = re.findall(r'  - (\w+)', content)
        tags_str = ', '.join(tags_match[:3]) if tags_match else "-"
        
        print(f"{date:<12} {status_emoji} {status:<8} {title:<50} {tags_str}")
    
    if len(papers) > args.limit:
        print(f"\n... and {len(papers) - args.limit} more")


def cmd_search(args):
    """Search papers by keyword."""
    query = args.query.lower()
    matches = []
    
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir():
            for paper_file in year_dir.glob("*.md"):
                content = paper_file.read_text().lower()
                if query in content:
                    # Find context
                    idx = content.find(query)
                    start = max(0, idx - 50)
                    end = min(len(content), idx + len(query) + 50)
                    context = content[start:end].replace('\n', ' ')
                    matches.append((paper_file, context))
    
    print(f"\n🔍 Found {len(matches)} matches for '{args.query}':\n")
    
    for paper_file, context in matches[:20]:
        rel_path = paper_file.relative_to(LIBRARY_DIR)
        print(f"📄 {rel_path}")
        print(f"   ...{context}...")
        print()


def cmd_today(args):
    """Show today's recommended reading."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Get unread papers
    unread = []
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir():
            for paper_file in year_dir.glob("*.md"):
                content = paper_file.read_text()
                if 'status: "unread"' in content:
                    # Get title
                    title_match = re.search(r'title: "([^"]+)"', content)
                    title = title_match.group(1) if title_match else paper_file.stem
                    unread.append((title, paper_file))
    
    print(f"\n📅 Today ({today})\n")
    print("🎯 Recommended Reading:\n")
    
    if unread:
        for i, (title, path) in enumerate(unread[:5], 1):
            rel_path = path.relative_to(LIBRARY_DIR)
            print(f"{i}. {title}")
            print(f"   📖 {rel_path}\n")
    else:
        print("No unread papers! Great job! 🎉")
        print("Consider adding new papers with: paper-manager.py add <url>")


def cmd_tags(args):
    """List all tags."""
    if not TAGS_DIR.exists():
        print("No tags found.")
        return
    
    tag_files = list(TAGS_DIR.glob("*.md"))
    tag_files.sort()
    
    print(f"\n🏷️  Available Tags ({len(tag_files)} total):\n")
    
    # Group by category
    categories = {
        "研究领域": ["topology", "superconductivity", "many-body", "qft-condmat", 
                    "quantum-info", "symmetry", "transport", "graphene-2d", "cft-holography"],
        "方法/风格": ["elegant-proof", "clear-physical-picture", "masterpiece", 
                     "review", "breakthrough", "pedagogical"],
        "阅读状态": ["unread", "reading", "skimmed", "deep-read", "implemented"],
        "其他": []
    }
    
    for category, known_tags in categories.items():
        print(f"\n{category}:")
        for tag_file in tag_files:
            tag_name = tag_file.stem
            if tag_name in known_tags or category == "其他":
                # Count papers in tag
                content = tag_file.read_text()
                count = content.count("- [")
                print(f"  • {tag_name:<25} ({count} papers)")


def cmd_stats(args):
    """Show library statistics."""
    stats = {
        "total": 0,
        "by_status": {},
        "by_year": {},
        "by_tag": {}
    }
    
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir():
            year = year_dir.name
            stats["by_year"][year] = 0
            
            for paper_file in year_dir.glob("*.md"):
                stats["total"] += 1
                stats["by_year"][year] += 1
                
                content = paper_file.read_text()
                
                # Status
                status_match = re.search(r'status: "(\w+)"', content)
                status = status_match.group(1) if status_match else "unknown"
                stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
                
                # Tags
                tags_match = re.findall(r'  - (\w+)', content)
                for tag in tags_match:
                    stats["by_tag"][tag] = stats["by_tag"].get(tag, 0) + 1
    
    print("\n📊 Library Statistics\n")
    print(f"Total Papers: {stats['total']}")
    
    print("\nBy Status:")
    for status, count in sorted(stats["by_status"].items()):
        emoji = STATUS_EMOJI.get(status, "📄")
        print(f"  {emoji} {status:<12} {count}")
    
    print("\nBy Year:")
    for year, count in sorted(stats["by_year"].items()):
        print(f"  {year}: {count}")
    
    print("\nTop Tags:")
    top_tags = sorted(stats["by_tag"].items(), key=lambda x: x[1], reverse=True)[:10]
    for tag, count in top_tags:
        print(f"  #{tag:<20} {count}")


def cmd_status(args):
    """Update paper status."""
    # Find paper file
    pattern = args.paper
    matches = []
    
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir():
            for paper_file in year_dir.glob("*.md"):
                if pattern in paper_file.name:
                    matches.append(paper_file)
    
    if not matches:
        print(f"Error: No paper found matching '{pattern}'")
        return
    
    if len(matches) > 1:
        print(f"Multiple matches found:")
        for i, m in enumerate(matches):
            print(f"  {i+1}. {m}")
        return
    
    paper_file = matches[0]
    new_status = args.new_status
    
    # Update file
    content = paper_file.read_text()
    content = re.sub(r'status: "\w+"', f'status: "{new_status}"', content)
    paper_file.write_text(content)
    
    print(f"✅ Updated {paper_file.name} status to: {new_status}")


def cmd_journal(args):
    """Add an entry to taste journal."""
    entry = args.text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    journal_entry = f"\n### {timestamp}\n\n{entry}\n\n---\n"
    
    with open(TASTE_JOURNAL, 'a') as f:
        f.write(journal_entry)
    
    print(f"✅ Added entry to taste journal")


def cmd_to_blog(args):
    """Convert a paper note to blog post."""
    # Find paper file
    pattern = args.paper
    matches = []
    
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir():
            for paper_file in year_dir.glob("*.md"):
                if pattern in paper_file.name:
                    matches.append(paper_file)
    
    if not matches:
        print(f"Error: No paper found matching '{pattern}'")
        return
    
    paper_file = matches[0]
    
    # Read paper content
    content = paper_file.read_text()
    
    # Extract title
    title_match = re.search(r'title: "([^"]+)"', content)
    title = title_match.group(1) if title_match else paper_file.stem
    
    # Create blog post
    blog_dir = Path(__file__).parent.parent / "docs" / "posts" / "paper-notes"
    blog_dir.mkdir(parents=True, exist_ok=True)
    
    blog_filename = paper_file.name
    blog_path = blog_dir / blog_filename
    
    # Create blog content (modified from paper)
    blog_content = f"""---
title: "Paper Notes: {title}"
date: {datetime.now().strftime("%Y-%m-%d")}
tags: ["paper-notes"]
---

# Paper Notes: {title}

📄 **Original Paper**: [{title}](../paper-library/{paper_file.relative_to(LIBRARY_DIR)})

> This is a reading note based on the original paper. Personal reflections and critical analysis are included.

---

{content}

---

*Generated from paper library on {datetime.now().strftime("%Y-%m-%d")}*
"""
    
    blog_path.write_text(blog_content)
    print(f"✅ Created blog post: {blog_path}")


def cmd_summarize(args):
    """Generate AI summary for a paper."""
    # Import summarizer
    sys.path.insert(0, str(LIBRARY_DIR / "ai_modules"))
    try:
        from summarizer import PaperSummarizer
    except ImportError as e:
        print(f"Error: Could not import summarizer module: {e}")
        return
    
    # Find paper file
    pattern = args.paper
    matches = []
    
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir():
            for paper_file in year_dir.glob("*.md"):
                if pattern in paper_file.name:
                    matches.append(paper_file)
    
    if not matches:
        print(f"Error: No paper found matching '{pattern}'")
        return
    
    if len(matches) > 1:
        print(f"Multiple matches found:")
        for i, m in enumerate(matches):
            print(f"  {i+1}. {m}")
        return
    
    paper_file = matches[0]
    summarizer = PaperSummarizer()
    
    if args.update:
        # Update paper file with summary
        summarizer.update_paper_with_summary(paper_file, args.mode)
    else:
        # Just print summary
        summary = summarizer.summarize_paper(paper_file, args.mode)
        print("\n" + "="*60)
        print(summary)
        print("="*60)


def cmd_review(args):
    """Generate literature review from papers."""
    sys.path.insert(0, str(LIBRARY_DIR / "ai_modules"))
    try:
        from summarizer import PaperSummarizer
    except ImportError as e:
        print(f"Error: Could not import summarizer module: {e}")
        return
    
    # Collect papers
    paper_files = []
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir():
            for paper_file in year_dir.glob("*.md"):
                # Filter by tag if specified
                if args.tag:
                    content = paper_file.read_text()
                    if f"- {args.tag}" in content:
                        paper_files.append(paper_file)
                else:
                    paper_files.append(paper_file)
    
    if not paper_files:
        print("No papers found")
        return
    
    print(f"Generating review from {len(paper_files)} papers...")
    
    summarizer = PaperSummarizer()
    review = summarizer.generate_literature_review(
        paper_files,
        topic=args.topic or "",
        max_papers=args.max_papers
    )
    
    # Save review
    review_dir = LIBRARY_DIR / "reviews"
    review_dir.mkdir(exist_ok=True)
    
    topic_slug = args.topic.replace(" ", "-").lower() if args.topic else "general"
    review_file = review_dir / f"review-{topic_slug}-{datetime.now().strftime('%Y%m%d')}.md"
    review_file.write_text(review)
    
    print(f"\n✅ Literature review saved: {review_file}")
    print(f"\nPreview:\n{'='*60}")
    print(review[:2000] + "..." if len(review) > 2000 else review)


def main():
    parser = argparse.ArgumentParser(
        description="Paper Library Manager - Smart literature management for physics research",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s add https://arxiv.org/abs/2404.12345
    %(prog)s add "https://arxiv.org/abs/2404.12345" --title "Custom Title" --tags "topology,superconductivity"
    %(prog)s list --tag topology --limit 20
    %(prog)s search "Majorana"
    %(prog)s today
    %(prog)s stats
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new paper')
    add_parser.add_argument('url', help='Paper URL (arXiv, journal, etc.)')
    add_parser.add_argument('--title', '-t', help='Paper title')
    add_parser.add_argument('--authors', '-a', help='Paper authors')
    add_parser.add_argument('--tags', help='Comma-separated tags')
    add_parser.add_argument('--status', default='unread', help='Reading status')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List papers')
    list_parser.add_argument('--tag', help='Filter by tag')
    list_parser.add_argument('--status', help='Filter by status')
    list_parser.add_argument('--limit', type=int, default=20, help='Limit results')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search papers')
    search_parser.add_argument('query', help='Search query')
    
    # Today command
    subparsers.add_parser('today', help='Show today\'s recommended reading')
    
    # Tags command
    subparsers.add_parser('tags', help='List all tags')
    
    # Stats command
    subparsers.add_parser('stats', help='Show library statistics')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Update paper status')
    status_parser.add_argument('paper', help='Paper filename pattern')
    status_parser.add_argument('new_status', help='New status (unread/reading/skimmed/deep-read/implemented)')
    
    # Journal command
    journal_parser = subparsers.add_parser('journal', help='Add taste journal entry')
    journal_parser.add_argument('text', help='Journal entry text')
    
    # To-blog command
    to_blog_parser = subparsers.add_parser('to-blog', help='Convert paper to blog post')
    to_blog_parser.add_argument('paper', help='Paper filename pattern')
    
    # Summarize command
    summarize_parser = subparsers.add_parser('summarize', help='Generate AI summary for a paper')
    summarize_parser.add_argument('paper', help='Paper filename pattern')
    summarize_parser.add_argument('--mode', '-m', default='standard',
                                 choices=['quick', 'standard', 'deep'],
                                 help='Summary mode')
    summarize_parser.add_argument('--update', '-u', action='store_true',
                                 help='Update paper file with summary')
    
    # Review command
    review_parser = subparsers.add_parser('review', help='Generate literature review')
    review_parser.add_argument('--topic', '-t', help='Review topic')
    review_parser.add_argument('--tag', help='Filter papers by tag')
    review_parser.add_argument('--max-papers', type=int, default=20,
                              help='Maximum papers to include')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Ensure directories exist
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Execute command
    commands = {
        'add': cmd_add,
        'list': cmd_list,
        'search': cmd_search,
        'today': cmd_today,
        'tags': cmd_tags,
        'stats': cmd_stats,
        'status': cmd_status,
        'journal': cmd_journal,
        'to-blog': cmd_to_blog,
        'summarize': cmd_summarize,
        'review': cmd_review,
    }
    
    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
