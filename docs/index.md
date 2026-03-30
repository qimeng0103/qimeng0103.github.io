---
layout: home

hero:
  name: "Qi Meng"
  text: "Research Blog"
  tagline: Condensed Matter Physics · Quantum Computing · Numerical Simulations
  actions:
    - theme: brand
      text: Publications
      link: /posts/
    - theme: alt
      text: About
      link: /about

features:
  - title: Research Notes
    details: Theoretical investigations in condensed matter physics and topological materials
  - title: Computational Methods
    details: Numerical techniques using Kwant, Julia, and other scientific computing tools
  - title: Data Analysis
    details: Scientific computing and data visualization for physics research
  - title: Literature Review
    details: Reading notes on seminal papers and recent advances in the field
---

<style>
.home-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 60px 24px;
}

.intro-section {
  margin-bottom: 60px;
}

.intro-section h2 {
  font-family: var(--vp-font-family-serif);
  font-size: 24px;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 20px;
  letter-spacing: -0.01em;
}

.intro-text {
  font-size: 16px;
  line-height: 1.8;
  color: var(--vp-c-text-2);
  text-align: justify;
}

.contact-section {
  margin-top: 40px;
  padding-top: 40px;
  border-top: 1px solid var(--vp-c-divider);
}

.contact-section h3 {
  font-family: var(--vp-font-family-serif);
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--vp-c-text-3);
  margin-bottom: 16px;
}

.contact-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.contact-list li {
  margin: 8px 0;
  font-size: 14px;
}

.contact-list a {
  color: var(--vp-c-text-2);
  text-decoration: none;
  border-bottom: 1px solid var(--vp-c-border);
  transition: border-color 0.2s ease, color 0.2s ease;
}

.contact-list a:hover {
  color: var(--vp-c-brand-1);
  border-bottom-color: var(--vp-c-brand-1);
}

.latest-articles {
  margin-top: 60px;
}

.latest-articles h2 {
  font-family: var(--vp-font-family-serif);
  font-size: 20px;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--vp-c-brand-1);
  letter-spacing: -0.01em;
}

.article-entry {
  display: flex;
  align-items: baseline;
  gap: 24px;
  padding: 20px 0;
  border-bottom: 1px solid var(--vp-c-divider);
}

.article-entry:last-child {
  border-bottom: none;
}

.article-date {
  font-family: var(--vp-font-family-mono);
  font-size: 13px;
  color: var(--vp-c-text-3);
  white-space: nowrap;
  min-width: 100px;
}

.article-info h3 {
  font-family: var(--vp-font-family-serif);
  font-size: 17px;
  font-weight: 600;
  margin: 0 0 6px 0;
  line-height: 1.4;
}

.article-info h3 a {
  color: var(--vp-c-text-1);
  text-decoration: none;
  border-bottom: none;
  transition: color 0.2s ease;
}

.article-info h3 a:hover {
  color: var(--vp-c-brand-1);
}

.article-info p {
  margin: 0;
  font-size: 14px;
  color: var(--vp-c-text-3);
  line-height: 1.5;
}

@media (max-width: 640px) {
  .article-entry {
    flex-direction: column;
    gap: 8px;
  }
  
  .article-date {
    min-width: auto;
  }
}
</style>

<div class="home-content">

<div class="intro-section">
  <h2>Welcome</h2>
  <p class="intro-text">
    I am Qi Meng, a researcher in condensed matter physics. This website documents my research notes, 
    numerical methods, and reflections on physics. My primary interests include topological phases of matter, 
    quantum transport, and strongly correlated systems.
  </p>
  
  <div class="contact-section">
    <h3>Contact</h3>
    <ul class="contact-list">
      <li>Email: <a href="mailto:qimeng0103@gmail.com">qimeng0103@gmail.com</a></li>
      <li>GitHub: <a href="https://github.com/qimeng0103" target="_blank">github.com/qimeng0103</a></li>
    </ul>
  </div>
</div>

<div class="latest-articles">
  <h2>Recent Articles</h2>
  
  <div class="article-entry">
    <div class="article-date">2024-01-15</div>
    <div class="article-info">
      <h3><a href="/posts/example">Example: Mathematical Formulas and Code</a></h3>
      <p>Demonstration of LaTeX equations, syntax highlighting, and other features</p>
    </div>
  </div>
  
</div>

</div>
