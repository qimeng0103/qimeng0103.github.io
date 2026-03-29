# About Me

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
  <img src="/images/avatar.svg" alt="Qi Meng" class="profile-avatar">
  <div class="profile-info">
    <h1>Qi Meng</h1>
    <div class="title">Condensed Matter Physics | PhD Student</div>
    <div class="profile-links">
      <a href="mailto:qimeng0103@gmail.com">📧 Email</a>
      <a href="https://github.com/qimeng0103" target="_blank">🐙 GitHub</a>
      <a href="https://scholar.google.com" target="_blank">🎓 Google Scholar</a>
    </div>
  </div>
</div>

## 🔬 Research Interests

My research focuses on theoretical and computational condensed matter physics, particularly:

<div class="research-areas">
  <div class="research-card">
    <h4>Topological Phases</h4>
    <p>Topological insulators, topological superconductors, Weyl semimetals and other novel quantum materials</p>
  </div>
  <div class="research-card">
    <h4>Quantum Transport</h4>
    <p>Electronic transport in mesoscopic systems using non-equilibrium Green's functions and scattering matrix methods</p>
  </div>
  <div class="research-card">
    <h4>Strongly Correlated Systems</h4>
    <p>Numerical simulations of quantum many-body systems, including DMRG and quantum Monte Carlo methods</p>
  </div>
  <div class="research-card">
    <h4>Quantum Computing</h4>
    <p>Quantum algorithm design, quantum error correction, and quantum simulation theory</p>
  </div>
</div>

## 💻 Technical Tools

In my daily research, I primarily use the following tools and languages:

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

## 📝 About This Blog

This blog is where I document my learning and research journey. It includes:

- **Research Notes** — Understanding and derivations of physics concepts
- **Computing Tutorials** — Experience sharing on numerical methods and software
- **Paper Reviews** — Reading notes on classic papers and important developments
- **Tech Essays** — Programming tips and productivity improvements

## 📮 Contact

If you're interested in my research or have any questions, feel free to reach out:

- **Email**: [qimeng0103@gmail.com](mailto:qimeng0103@gmail.com)
- **GitHub**: [@qimeng0103](https://github.com/qimeng0103)

---

> *"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
> 
> — Richard Feynman
