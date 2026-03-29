# 关于我

<style>
.profile-header {
  display: flex;
  gap: 32px;
  align-items: flex-start;
  margin-bottom: 48px;
  padding-bottom: 32px;
  border-bottom: 1px solid var(--vp-c-border);
}

.profile-avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 4px solid var(--vp-c-bg);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.profile-info h1 {
  margin: 0 0 8px 0;
  font-size: 32px;
  border: none;
  padding: 0;
}

.profile-info .title {
  color: var(--vp-c-text-3);
  font-size: 16px;
  margin-bottom: 16px;
}

.profile-links {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.profile-links a {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  border: none;
  transition: all 0.2s ease;
}

.profile-links a:hover {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  padding: 8px 16px;
  margin: 0;
}

.research-areas {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin: 24px 0;
}

.research-card {
  padding: 24px;
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
  border: 1px solid var(--vp-c-border);
}

.research-card h4 {
  margin: 0 0 12px 0;
  font-size: 18px;
  color: var(--vp-c-brand-1);
}

.research-card p {
  margin: 0;
  font-size: 14px;
  color: var(--vp-c-text-2);
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin: 24px 0;
}

.skill-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  border-radius: 10px;
  transition: all 0.2s ease;
}

.skill-item:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-2px);
}

.skill-icon {
  font-size: 24px;
}

.skill-name {
  font-weight: 500;
  color: var(--vp-c-text-1);
}

@media (max-width: 640px) {
  .profile-header {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .profile-links {
    justify-content: center;
  }
}
</style>

<div class="profile-header">
  <img src="/images/avatar.svg" alt="avatar" class="profile-avatar">
  <div class="profile-info">
    <h1>Qi Meng</h1>
    <div class="title">凝聚态物理 | 博士研究生</div>
    <div class="profile-links">
      <a href="mailto:qimeng0103@gmail.com">📧 Email</a>
      <a href="https://github.com/qimeng0103" target="_blank">🐙 GitHub</a>
      <a href="https://scholar.google.com" target="_blank">🎓 Google Scholar</a>
    </div>
  </div>
</div>

## 🔬 研究方向

我的研究兴趣主要集中在凝聚态物理的理论与计算方向，特别是：

<div class="research-areas">
  <div class="research-card">
    <h4>拓扑物态</h4>
    <p>拓扑绝缘体、拓扑超导体、Weyl半金属等新型量子材料的理论研究</p>
  </div>
  <div class="research-card">
    <h4>量子输运</h4>
    <p>利用非平衡格林函数和散射矩阵方法研究介观系统的电子输运性质</p>
  </div>
  <div class="research-card">
    <h4>强关联系统</h4>
    <p>量子多体系统的数值模拟，包括DMRG、量子蒙特卡洛等方法</p>
  </div>
  <div class="research-card">
    <h4>量子计算</h4>
    <p>量子算法设计、量子纠错以及量子模拟的理论研究</p>
  </div>
</div>

## 💻 技术工具

在日常研究工作中，我主要使用以下工具和语言：

<div class="skills-grid">
  <div class="skill-item">
    <span class="skill-icon">🐍</span>
    <span class="skill-name">Python</span>
  </div>
  <div class="skill-item">
    <span class="skill-icon">🔷</span>
    <span class="skill-name">Julia</span>
  </div>
  <div class="skill-item">
    <span class="skill-icon">📊</span>
    <span class="skill-name">MATLAB</span>
  </div>
  <div class="skill-item">
    <span class="skill-icon">⚛️</span>
    <span class="skill-name">Kwant</span>
  </div>
  <div class="skill-item">
    <span class="skill-icon">🔗</span>
    <span class="skill-name">ITensor</span>
  </div>
  <div class="skill-item">
    <span class="skill-icon">🌊</span>
    <span class="skill-name">Quantum ESPRESSO</span>
  </div>
</div>

## 📝 关于本博客

这个博客是我记录学习和研究过程的地方。内容包括：

- **研究笔记** — 对物理概念的理解和推导
- **计算教程** — 数值方法和软件使用的经验分享  
- **文献解读** — 经典论文和重要进展的阅读笔记
- **技术随笔** — 编程技巧和工作效率的提升

## 📮 联系方式

如果你对我的研究感兴趣，或有任何问题想要交流，欢迎通过以下方式联系我：

- **Email**: [qimeng0103@gmail.com](mailto:qimeng0103@gmail.com)
- **GitHub**: [@qimeng0103](https://github.com/qimeng0103)

---

> *"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
> 
> — Richard Feynman
