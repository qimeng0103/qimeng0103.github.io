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
      <span class="article-date">2026-04-04</span>
      <div>
        <div class="article-title"><a href="./quantum-mechanics/angular-momentum-algebra">Angular Momentum Algebra: From Commutation Relations to Addition of Angular Momenta</a></div>
        <div class="article-desc">Angular momentum commutation relations, ladder operators and eigenvalue spectrum, matrix representations for spin-1/2 and spin-1, and Clebsch-Gordan coefficients for angular momentum addition</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-04-02</span>
      <div>
        <div class="article-title"><a href="./quantum-mechanics/bound-states-resonances-scattering">Bound States, Resonances, and Scattering: Three Pillars of Quantum Mechanics</a></div>
        <div class="article-desc">Existence conditions for bound states in 1D/3D potentials, resonance states and the Breit-Wigner formula, scattering theory with partial wave analysis and Levinson's theorem</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-03-31</span>
      <div>
        <div class="article-title"><a href="./quantum-mechanics/time-dependent-perturbation-theory">Time-Dependent Perturbation Theory: From Fermi's Golden Rule to Linear Response</a></div>
        <div class="article-desc">Interaction picture, Dyson series, Fermi's Golden Rule, scattering theory with Lippmann-Schwinger equation, and linear response theory with Kubo formula</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-03-30</span>
      <div>
        <div class="article-title"><a href="./quantum-mechanics/stationary-perturbation-theory">Stationary Perturbation Theory: Non-Degenerate vs Degenerate Cases</a></div>
        <div class="article-desc">Complete derivation of energy corrections up to third order and wavefunction corrections up to second order for non-degenerate perturbation theory, with detailed discussion of degenerate case</div>
      </div>
    </li>
  </ul>
</div>

<div class="category-section">
  <h2>Bare-Handed</h2>
  <ul class="article-list">
    <li class="article-item">
      <span class="article-date">—</span>
      <div>
        <div class="article-title"><a href="./bare-handed/">Bare-Handed — Daily Training Log</a></div>
        <div class="article-desc">Starting from a blank page without books or notes. Exposing gaps, diagnosing blind spots, rebuilding from scratch.</div>
      </div>
    </li>
  </ul>
</div>

<div class="category-section">
  <h2>Statistical Mechanics Notes</h2>
  <ul class="article-list">
    <li class="article-item">
      <span class="article-date">2026-05-03</span>
      <div>
        <div class="article-title"><a href="./statistical-mechanics/quantum-dice-and-coins">Quantum Dice and Coins: A Gentle Introduction to Bose-Einstein and Fermi-Dirac Statistics</a></div>
        <div class="article-desc">Sethna Exercise 1.1 — mapping quantum statistics onto dice games, from Pauli exclusion to Bose-Einstein condensation in the thermodynamic limit</div>
      </div>
    </li>
  </ul>
</div>

<div class="category-section">
  <h2>Paper Notes</h2>
  <ul class="article-list">
    <li class="article-item">
      <span class="article-date">2026-04-14</span>
      <div>
        <div class="article-title"><a href="./paper-notes/2026-04-14-issue-1">Daily Papers - 2026-04-14 (Issue #1)</a></div>
        <div class="article-desc">RMT statistical signatures distinguishing MZMs from CdGM states in disordered antidot vortices via STM</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-04-10</span>
      <div>
        <div class="article-title"><a href="./paper-notes/2026-04-10-issue-2">Daily Papers - 2026-04-10 (Issue #2)</a></div>
        <div class="article-desc">Majorana braiding emulation; parafermion hybridization in fluxonium; current-phase signatures of parafermions in FQH-SC Josephson junctions; quantum metric control of MZMs in Lieb-Kitaev model</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-04-10</span>
      <div>
        <div class="article-title"><a href="./paper-notes/2026-04-10-issue-1">Daily Papers - 2026-04-10 (Issue #1)</a></div>
        <div class="article-desc">Daily paper collection covering topological superconductivity and quantum simulation</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-04-09</span>
      <div>
        <div class="article-title"><a href="./paper-notes/2026-04-09-issue-1">Daily Papers - 2026-04-09 (Issue #1)</a></div>
        <div class="article-desc">Initial daily paper collection with 6 papers on topological superconductivity and Majorana physics</div>
      </div>
    </li>
  </ul>
</div>

<div class="category-section">
  <h2>Condensed Matter Notes</h2>
  <ul class="article-list">
    <li class="article-item">
      <span class="article-date">2026-04-04</span>
      <div>
        <div class="article-title"><a href="./condensed-matter/crystal-structures-bravais-lattices">Crystal Structures: From Bravais Lattices to Reciprocal Space</a></div>
        <div class="article-desc">Seven crystal systems, fourteen Bravais lattices, Wigner-Seitz cell construction, reciprocal lattice derivation, and first Brillouin zone</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-04-04</span>
      <div>
        <div class="article-title"><a href="./condensed-matter/electron-energy-bands-origin">Electron Energy Bands: From Atomic Orbitals to Bloch States</a></div>
        <div class="article-desc">Origin of energy bands from wavefunction overlap, LCAO approximation, exact solution of Kronig-Penney model, and proof of Bloch's theorem</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-04-03</span>
      <div>
        <div class="article-title"><a href="./condensed-matter/spontaneous-symmetry-breaking">Spontaneous Symmetry Breaking: From Functional Calculus to Goldstone Modes</a></div>
        <div class="article-desc">Functional differentiation vs ordinary calculus, spontaneous symmetry breaking in condensed matter, Goldstone's theorem, and order parameter physics</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-04-02</span>
      <div>
        <div class="article-title"><a href="./condensed-matter/metal-electron-theory-fermi-statistics-transport">Metal Electron Theory: From Fermi Statistics to Transport Properties</a></div>
        <div class="article-desc">Fermi-Dirac statistics, electronic heat capacity, Boltzmann transport equation, conductivity, Hall effect, and thermoelectric effects in metals</div>
      </div>
    </li>
    <li class="article-item">
      <span class="article-date">2026-04-02</span>
      <div>
        <div class="article-title"><a href="./condensed-matter/semiconductor-electron-theory">Semiconductor Electron Theory: From Band Structure to p-n Junctions</a></div>
        <div class="article-desc">Direct and indirect band gaps, Maxwell-Boltzmann statistics for carriers, doping and impurity levels, transport properties, and p-n junction physics</div>
      </div>
    </li>
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
