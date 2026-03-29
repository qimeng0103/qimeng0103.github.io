---
layout: home

hero:
  name: "Qi Meng"
  text: "Research Blog"
  tagline: 凝聚态物理 · 量子计算 · 数值模拟
  image:
    src: /images/avatar.png
    alt: Qi Meng
  actions:
    - theme: brand
      text: 浏览文章
      link: /posts/
    - theme: alt
      text: 关于我
      link: /about

features:
  - icon: 🔬
    title: 研究笔记
    details: 凝聚态物理与拓扑材料的理论研究记录
  - icon: 💻
    title: 数值方法
    details: Kwant、Julia 等计算工具的使用与技巧
  - icon: 📊
    title: 数据分析
    details: 科学计算与数据可视化的实践经验
  - icon: 📝
    title: 论文解读
    details: 经典文献与前沿进展的阅读笔记
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
  <h2>👋 欢迎来到我的研究空间</h2>
  <p class="intro-text">
    我是 Qi Meng，一名凝聚态物理领域的科研工作者。这里记录我的研究笔记、数值计算经验以及对物理学的思考。
    主要关注拓扑物态、量子输运和强关联系统。
  </p>
  
  <div class="contact-grid">
    <a href="mailto:qimeng0103@gmail.com" class="contact-item">
      <span>📧</span> qimeng0103@gmail.com
    </a>
    <a href="https://github.com/qimeng0103" class="contact-item" target="_blank">
      <span>🐙</span> GitHub
    </a>
  </div>
</div>

<div class="latest-articles">
  <h2>📝 最新文章</h2>
  
  <div class="article-card">
    <div class="article-date">
      <span class="day">15</span>
      <span class="month">Jan</span>
    </div>
    <div class="article-info">
      <h3><a href="/posts/example">示例文章：公式与代码演示</a></h3>
      <p>展示博客支持的数学公式、代码高亮等功能的使用方法</p>
    </div>
  </div>
  
  <!-- 更多文章会自动添加在这里 -->
  
</div>

</div>
