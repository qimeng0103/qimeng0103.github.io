# Articles

<style>
.article-index {
  margin-top: 32px;
}

.category-section {
  margin-bottom: 48px;
}

.category-section h2 {
  font-family: var(--vp-font-family-serif);
  font-size: 20px;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--vp-c-divider);
  letter-spacing: -0.01em;
}

.article-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.article-item {
  display: flex;
  align-items: baseline;
  gap: 20px;
  padding: 16px 0;
  border-bottom: 1px solid var(--vp-c-divider);
}

.article-item:last-child {
  border-bottom: none;
}

.article-date {
  font-family: var(--vp-font-family-mono);
  font-size: 13px;
  color: var(--vp-c-text-3);
  white-space: nowrap;
  min-width: 90px;
}

.article-title {
  font-family: var(--vp-font-family-serif);
  font-size: 16px;
  font-weight: 600;
}

.article-title a {
  color: var(--vp-c-text-1);
  text-decoration: none;
  border-bottom: none;
  transition: color 0.2s ease;
}

.article-title a:hover {
  color: var(--vp-c-brand-1);
}

.article-desc {
  font-size: 14px;
  color: var(--vp-c-text-3);
  margin-top: 4px;
}

.tag-list {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 32px;
  padding-top: 32px;
  border-top: 1px solid var(--vp-c-border);
}

.tag {
  font-family: var(--vp-font-family-mono);
  font-size: 12px;
  padding: 4px 10px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  color: var(--vp-c-text-3);
  text-decoration: none;
  transition: all 0.2s ease;
}

.tag:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg);
}

@media (max-width: 640px) {
  .article-item {
    flex-direction: column;
    gap: 4px;
  }
  
  .article-date {
    min-width: auto;
  }
}
</style>

<div class="article-index">

<div class="category-section">
  <h2>Quantum Mechanics Notes</h2>
  <ul class="article-list">
    <li class="article-item">
      <span class="article-date">2026-03-30</span>
      <div>
        <div class="article-title"><a href="./quantum-mechanics/stationary-perturbation-theory">Stationary Perturbation Theory: Non-Degenerate vs Degenerate Cases</a></div>
        <div class="article-desc">Complete derivation of energy corrections up to third order and wavefunction corrections up to second order for non-degenerate perturbation theory, with detailed discussion of degenerate case</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-03-31</span>
      <div>
        <div class="article-title"><a href="./quantum-mechanics/time-dependent-perturbation-theory">Time-Dependent Perturbation Theory: From Fermi's Golden Rule to Linear Response</a></div>
        <div class="article-desc">Interaction picture, Dyson series, Fermi's Golden Rule, scattering theory with Lippmann-Schwinger equation, and linear response theory with Kubo formula</div>
      </div>
    </li>
  </ul>
</div>

<div class="category-section">
  <h2>Condensed Matter Notes</h2>
  <ul class="article-list">
    <li class="article-item">
      <span class="article-date">2026-03-31</span>
      <div>
        <div class="article-title"><a href="./condensed-matter/green-functions-quantum-transport">Green's Functions in Condensed Matter: From Equilibrium to Non-Equilibrium Quantum Transport</a></div>
        <div class="article-desc">Single-particle and many-body Green's functions, Matsubara formalism, Dyson equation, Keldysh non-equilibrium technique, and applications to quantum transport</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-03-31</span>
      <div>
        <div class="article-title"><a href="./condensed-matter/phonons-lattice-dynamics">Phonons: From Classical Lattice Dynamics to Quantum Transport</a></div>
        <div class="article-desc">Classical and quantum treatment of lattice vibrations, acoustic and optical phonons, van Hove singularities, and polaritons in ionic crystals</div>
      </div>
    </li>
  </ul>
</div>

<div class="tag-list">
  <span class="tag">research-notes</span>
</div>

</div>
