---
layout: home

hero:
  name: "Qi Meng"
  text: "Research Blog"
  tagline: Condensed Matter Physics · Quantum Computing · Numerical Simulations
  image:
    src: /images/avatar.svg
    alt: Qi Meng
  actions:
    - theme: brand
      text: Browse Articles
      link: /en/posts/
    - theme: alt
      text: About Me
      link: /en/about

features:
  - icon: 🔬
    title: Research Notes
    details: Theoretical studies on topological materials and condensed matter physics
  - icon: 💻
    title: Numerical Methods
    details: Computational tools including Kwant, Julia, and scientific computing
  - icon: 📊
    title: Data Analysis
    details: Practical experience in scientific computing and data visualization
  - icon: 📝
    title: Paper Reviews
    details: Reading notes on classic papers and frontier research progress
---

<style>
.home-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 24px;
}

.intro-section {
  text-align: center;
  margin-bottom: 48px;
}

.intro-section h2 {
  font-size: 28px;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 16px;
}

.intro-text {
  font-size: 16px;
  line-height: 1.8;
  color: var(--vp-c-text-2);
  max-width: 600px;
  margin: 0 auto;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-top: 32px;
}

.contact-item {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 16px 24px;
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
  color: var(--vp-c-text-2);
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  border: 1px solid var(--vp-c-border);
}

.contact-item:hover {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
  transform: translateY(-2px);
}

.latest-articles {
  margin-top: 64px;
}

.latest-articles h2 {
  font-size: 24px;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--vp-c-brand-soft);
}

.article-card {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 20px;
  margin: 12px 0;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  transition: all 0.3s ease;
}

.article-card:hover {
  transform: translateX(8px);
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 4px 20px rgba(79, 70, 229, 0.1);
}

.article-date {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-width: 60px;
  padding: 12px;
  background: var(--vp-c-brand-soft);
  border-radius: 10px;
  color: var(--vp-c-brand-1);
}

.article-date .day {
  font-size: 24px;
  font-weight: 700;
  line-height: 1;
}

.article-date .month {
  font-size: 12px;
  font-weight: 500;
  text-transform: uppercase;
  margin-top: 4px;
}

.article-info h3 {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 8px 0;
}

.article-info h3 a {
  color: var(--vp-c-text-1);
  text-decoration: none;
  border-bottom: none;
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
  .article-card {
    flex-direction: column;
    gap: 12px;
  }
  
  .article-date {
    flex-direction: row;
    gap: 8px;
    padding: 8px 16px;
    min-width: auto;
    align-self: flex-start;
  }
  
  .article-date .day {
    font-size: 18px;
  }
}
</style>

<div class="home-content">

<div class="intro-section">
  <h2>👋 Welcome to My Research Space</h2>
  <p class="intro-text">
    I'm Qi Meng, a researcher in condensed matter physics. This blog documents my research notes, 
    computational experiences, and thoughts on physics. My primary interests include topological phases, 
    quantum transport, and strongly correlated systems.
  </p>
  
  <div class="contact-grid">
    <a href="mailto:qimeng0103@gmail.com" class="contact-item">
      <span>📧</span> qimeng0103@gmail.com
    </a>
    <a href="https://github.com/qimeng0103" class="contact-item" target="_blank">
      <span>🐙</span> GitHub
    </a>
    <a href="/" class="contact-item">
      <span>🌐</span> 中文
    </a>
  </div>
</div>

<div class="latest-articles">
  <h2>📝 Latest Articles</h2>
  
  <div class="article-card">
    <div class="article-date">
      <span class="day">15</span>
      <span class="month">Jan</span>
    </div>
    <div class="article-info">
      <h3><a href="/en/posts/example">Example: Formulas and Code</a></h3>
      <p>Demonstrating mathematical formulas, code highlighting, and other supported features</p>
    </div>
  </div>
  
</div>

</div>
