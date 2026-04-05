#!/usr/bin/env python3
"""
Generate Young diagram figures for angular momentum article.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys

# Add utils to path for import
sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style, COLORS

# Output directory
OUTPUT_DIR = 'docs/images/angular-momentum'

def draw_young_diagram(ax, partition, labels=None, title='', box_size=1.0, 
                       linewidth=2, edgecolor='black', facecolor='white',
                       label_color='black', label_fontsize=14):
    """
    Draw a Young diagram on the given axes.
    
    Args:
        ax: matplotlib axes
        partition: list of row lengths, e.g., [3] for (3), [2,1] for (2,1)
        labels: optional labels to put inside boxes
        title: title above the diagram
        box_size: size of each box
    """
    # Calculate dimensions
    n_rows = len(partition)
    max_cols = max(partition) if partition else 0
    
    # Draw boxes
    for i, row_length in enumerate(partition):
        for j in range(row_length):
            # Create rectangle
            rect = patches.Rectangle(
                (j * box_size, -(i + 1) * box_size),  # bottom-left corner
                box_size, box_size,  # width, height
                linewidth=linewidth,
                edgecolor=edgecolor,
                facecolor=facecolor,
                joinstyle='miter'
            )
            ax.add_patch(rect)
            
            # Add label if provided
            if labels and i * max_cols + j < len(labels):
                ax.text(j * box_size + box_size/2, 
                       -(i + 0.5) * box_size,
                       labels[i * max_cols + j],
                       ha='center', va='center',
                       fontsize=label_fontsize,
                       color=label_color)
    
    # Set limits and aspect
    ax.set_xlim(-0.2, max_cols * box_size + 0.2)
    ax.set_ylim(-n_rows * box_size - 0.2, 0.8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Add title
    if title:
        ax.set_title(title, fontsize=12, pad=10)


def draw_young_diagram_pure(ax, partition, box_size=1.0, linewidth=2, 
                            edgecolor='black', facecolor='white'):
    """
    Draw a Young diagram without any labels or titles - just the boxes.
    
    Args:
        ax: matplotlib axes
        partition: list of row lengths
        box_size: size of each box
    """
    # Calculate dimensions
    n_rows = len(partition)
    max_cols = max(partition) if partition else 0
    
    # Draw boxes
    for i, row_length in enumerate(partition):
        for j in range(row_length):
            rect = patches.Rectangle(
                (j * box_size, -(i + 1) * box_size),
                box_size, box_size,
                linewidth=linewidth,
                edgecolor=edgecolor,
                facecolor=facecolor,
                joinstyle='miter'
            )
            ax.add_patch(rect)
    
    # Set limits - tight around the diagram
    ax.set_xlim(-0.1, max_cols * box_size + 0.1)
    ax.set_ylim(-n_rows * box_size - 0.1, 0.1)
    ax.set_aspect('equal')
    ax.axis('off')


def young_diagram_single(partition, filename, label='', box_labels=None):
    """Generate a single Young diagram figure."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(3, 2.5))
    
    partition_str = '(' + ','.join(map(str, partition)) + ')'
    title = f'{partition_str}\n{label}'
    
    draw_young_diagram(ax, partition, labels=box_labels, title=title)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=200, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def young_diagram_pure(partition, filename, box_size=1.0):
    """Generate a pure Young diagram figure with no labels."""
    setup_style()
    
    n_rows = len(partition)
    max_cols = max(partition) if partition else 0
    
    # Calculate figure size based on diagram size
    fig_width = max_cols * 0.5 + 0.2
    fig_height = n_rows * 0.5 + 0.2
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    draw_young_diagram_pure(ax, partition, box_size=box_size)
    
    plt.tight_layout(pad=0)
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none', pad_inches=0.02)
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def young_diagram_comparison():
    """Generate comparison figure showing all 3-particle diagrams."""
    setup_style()
    
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))
    
    diagrams = [
        ([3], '(3) Symmetric\nS=3/2, dim=4', 'Totally symmetric'),
        ([2, 1], '(2,1) Mixed\nS=1/2, dim=2', 'Mixed symmetry'),
        ([1, 1, 1], '(1,1,1) Antisymmetric\n(not for spin-1/2)', 'Totally antisymmetric'),
    ]
    
    for ax, (partition, label, desc) in zip(axes, diagrams):
        draw_young_diagram(ax, partition, title=label)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'young_3_all_detailed.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def young_diagram_2particle_comparison():
    """Generate comparison figure for 2-particle diagrams."""
    setup_style()
    
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))
    
    diagrams = [
        ([2], '(2) Symmetric\nTriplet, S=1, dim=3'),
        ([1, 1], '(1,1) Antisymmetric\nSinglet, S=0, dim=1'),
    ]
    
    for ax, (partition, label) in zip(axes, diagrams):
        draw_young_diagram(ax, partition, title=label)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'young_2_detailed.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def young_diagram_with_hook_lengths():
    """Generate diagram showing hook lengths for (2,1) partition - improved design."""
    setup_style()
    
    fig = plt.figure(figsize=(10, 5))
    
    # Create grid layout: left for diagram, right for explanation
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.2], wspace=0.3)
    ax_diagram = fig.add_subplot(gs[0])
    ax_text = fig.add_subplot(gs[1])
    ax_text.axis('off')
    
    # Draw (2,1) diagram with hook length labels
    partition = [2, 1]
    hook_lengths = ['3', '1', '1']
    
    # Draw diagram with colored labels
    draw_young_diagram(ax_diagram, partition, labels=hook_lengths, 
                       title='Partition (2,1) with Hook Lengths',
                       label_color='darkred', label_fontsize=18)
    
    # Add visual hook illustration
    # Top-left box hook
    ax_diagram.annotate('', xy=(1.9, -0.1), xytext=(0.1, -0.9),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    ax_diagram.annotate('', xy=(0.1, -1.9), xytext=(0.9, -1.1),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    
    # Explanation text on the right
    explanation_text = (
        "Hook Length Formula:\n"
        "$d = \\frac{n!}{\\prod_i h_i}$\n\n"
        "For partition (2,1):\n"
        "• $h_1 = 3$ (top-left)\n"
        "• $h_2 = 1$ (top-right)\n"
        "• $h_3 = 1$ (bottom-left)\n\n"
        "Dimension:\n"
        "$d = \\frac{3!}{3 \\times 1 \\times 1} = 2$\n\n"
        "This gives two doublet states ($S=1/2$)"
    )
    
    ax_text.text(0.1, 0.95, explanation_text, transform=ax_text.transAxes,
                fontsize=11, verticalalignment='top', family='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    # Add hook length definition at bottom
    fig.text(0.5, 0.02, 
             'Hook length = 1 (self) + boxes to right + boxes below',
             ha='center', fontsize=10, style='italic')
    
    filepath = os.path.join(OUTPUT_DIR, 'young_21_hook_lengths.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def young_diagram_partition_examples():
    """Generate figure showing various partition examples."""
    setup_style()
    
    fig, axes = plt.subplots(2, 3, figsize=(12, 6))
    axes = axes.flatten()
    
    diagrams = [
        ([3], '(3)\nOne row', 'Symmetric'),
        ([2, 1], '(2,1)', 'Mixed'),
        ([1, 1, 1], '(1,1,1)\nOne column', 'Antisymmetric'),
        ([4], '(4)\nOne row', 'Totally Symmetric'),
        ([2, 2], '(2,2)\nSquare', 'Mixed'),
        ([2, 1, 1], '(2,1,1)', 'Mixed'),
    ]
    
    for ax, (partition, label, symmetry) in zip(axes, diagrams):
        full_title = f'{label}\n{symmetry}'
        draw_young_diagram(ax, partition, title=full_title)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'young_partition_examples.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


if __name__ == '__main__':
    print("Generating Young diagram figures...")
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate comparison figures
    young_diagram_2particle_comparison()
    young_diagram_comparison()
    young_diagram_with_hook_lengths()
    young_diagram_partition_examples()
    
    # Generate individual diagrams with labels for reference
    young_diagram_single([2], 'young_2_symmetric_single.png', 'Symmetric')
    young_diagram_single([1, 1], 'young_11_antisymmetric_single.png', 'Antisymmetric')
    young_diagram_single([3], 'young_3_symmetric_single.png', 'Totally Symmetric')
    young_diagram_single([2, 1], 'young_21_mixed_single.png', 'Mixed')
    young_diagram_single([1, 1, 1], 'young_111_antisymmetric_single.png', 'Totally Antisymmetric')
    
    # Generate pure diagram versions (no labels) for table use
    young_diagram_pure([2], 'young_2_pure.png')
    young_diagram_pure([1, 1], 'young_11_pure.png')
    young_diagram_pure([3], 'young_3_pure.png')
    young_diagram_pure([2, 1], 'young_21_pure.png')
    young_diagram_pure([1, 1, 1], 'young_111_pure.png')
    
    print("\nAll Young diagram figures generated successfully!")
