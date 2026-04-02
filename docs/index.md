---
layout: home

hero:
  name: "Qi Meng"
  text: "Research Blog"
  tagline: Topological Superconductivity · Majorana Physics · Quantum Simulation
  actions:
    - theme: brand
      text: Articles
      link: /posts/
    - theme: alt
      text: About
      link: /about
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

.intro-header {
  display: flex;
  align-items: flex-start;
  gap: 32px;
  margin-bottom: 32px;
}

.intro-avatar {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid var(--vp-c-brand-1);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
  flex-shrink: 0;
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
  .intro-header {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .intro-avatar {
    width: 150px;
    height: 150px;
  }
  
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
  <div class="intro-header">
    <img src="/images/avatar.png" alt="Qi Meng" class="intro-avatar">
    <div>
      <h2>Welcome</h2>
      <p class="intro-text">
        I am Qi Meng, a researcher in condensed matter physics. This website documents my research notes, 
        numerical methods, and reflections on physics. My primary interests include topological superconductivity, 
        Majorana zero modes, topological quantum computation, and quantum simulation based on superconducting quantum processors.
      </p>
    </div>
  </div>
  
  <div class="contact-section">
    <h3>Contact</h3>
    <ul class="contact-list">
      <li>Email: <a href="mailto:mengq8@mail2.sysu.edu.cn">mengq8@mail2.sysu.edu.cn</a></li>
      <li>GitHub: <a href="https://github.com/qimeng0103" target="_blank">github.com/qimeng0103</a></li>
    </ul>
  </div>
</div>

<div class="latest-articles">
  <h2>Recent Articles</h2>
  
  <div class="article-entry">
    <div class="article-date">2026-04-02</div>
    <div class="article-info">
      <h3><a href="/posts/condensed-matter/metal-electron-theory-fermi-statistics-transport">Metal Electron Theory: Fermi Statistics and Transport</a></h3>
      <p>Fermi-Dirac statistics, electronic heat capacity, Boltzmann equation, conductivity, Hall effect</p>
    </div>
  </div>
  
  <div class="article-entry">
    <div class="article-date">2026-04-02</div>
    <div class="article-info">
      <h3><a href="/posts/condensed-matter/semiconductor-electron-theory">Semiconductor Electron Theory</a></h3>
      <p>Band structure, doping, carrier statistics, transport properties, and p-n junction physics</p>
    </div>
  </div>
  
  <div class="article-entry">
    <div class="article-date">2026-04-02</div>
    <div class="article-info">
      <h3><a href="/posts/quantum-mechanics/bound-states-resonances-scattering">Bound States, Resonances, and Scattering</a></h3>
      <p>Existence conditions for bound states, resonance phenomena, and scattering theory connections</p>
    </div>
  </div>
  
  <div class="article-entry">
    <div class="article-date">2026-03-31</div>
    <div class="article-info">
      <h3><a href="/posts/condensed-matter/phonons-lattice-dynamics">Phonons and Lattice Dynamics</a></h3>
      <p>Classical and quantum treatment of lattice vibrations, acoustic and optical phonons</p>
    </div>
  </div>
  
  <div class="article-entry">
    <div class="article-date">2026-03-31</div>
    <div class="article-info">
      <h3><a href="/posts/condensed-matter/green-functions-quantum-transport">Green's Functions for Quantum Transport</a></h3>
      <p>Single-particle and many-body Green's functions, Matsubara formalism, Dyson equation</p>
    </div>
  </div>
  
</div>

</div>
