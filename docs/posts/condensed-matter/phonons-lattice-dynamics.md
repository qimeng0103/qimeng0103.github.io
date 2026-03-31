# Phonons: From Classical Lattice Dynamics to Quantum Transport

📅 **Date:** 2026-03-31 | 🏷️ **Tags:** Condensed Matter, Lattice Dynamics, Phonons | 📂 **Category:** Condensed Matter Notes

---

## Introduction

This note provides a comprehensive treatment of phonons—the quantized excitations of crystal lattice vibrations. We develop the theory from classical Newtonian mechanics through canonical quantization, covering both monatomic (simple) and diatomic (compound) lattices, acoustic and optical phonon branches, polaritons, and van Hove singularities in the phonon density of states.

---

## Part I: Classical Lattice Dynamics

### The Harmonic Approximation

Consider a crystal with atoms at equilibrium positions $\mathbf{R}_n$. Let $\mathbf{u}_n$ be the displacement of atom $n$ from equilibrium. The potential energy expanded to quadratic order (harmonic approximation):

$$
V = V_0 + \frac{1}{2}\sum_{n,n'} \sum_{\alpha,\beta} u_n^\alpha \Phi_{nn'}^{\alpha\beta} u_{n'}^\beta
$$

where $\Phi_{nn'}^{\alpha\beta} = \frac{\partial^2 V}{\partial u_n^\alpha \partial u_{n'}^\beta}\big|_{\text{eq}}$ is the **force constant matrix**.

The classical equations of motion:

$$
M_n \ddot{u}_n^\alpha = -\sum_{n',\beta} \Phi_{nn'}^{\alpha\beta} u_{n'}^\beta = F_n^\alpha
$$

### Translational Symmetry and Bloch's Theorem

Due to periodicity, $\Phi_{nn'}^{\alpha\beta} = \Phi_{\alpha\beta}(\mathbf{R}_n - \mathbf{R}_{n'})$ depends only on relative positions. We seek plane wave solutions:

$$
u\mathbf{u}_n(t) = \mathbf{e}(\mathbf{q}) e^{i(\mathbf{q}\cdot\mathbf{R}_n - \omega t)}
$$

where $\mathbf{q}$ is the wavevector in the first Brillouin zone, and $\mathbf{e}(\mathbf{q})$ is the **polarization vector**.

Substituting into the equation of motion:

$$
-M\omega^2 \mathbf{e} = -\mathbf{D}(\mathbf{q}) \mathbf{e}$$

where the **dynamical matrix** is:

$$
D_{\alpha\beta}(\mathbf{q}) = \sum_{n'} \Phi_{nn'}^{\alpha\beta} e^{-i\mathbf{q}\cdot(\mathbf{R}_n - \mathbf{R}_{n'})}
$$

This is a $3d \times 3d$ Hermitian matrix eigenvalue problem for a lattice with $d$ atoms per unit cell.

---

## Part II: Monatomic Lattice—Acoustic Phonons

### The 1D Chain

Consider a 1D monatomic chain with lattice constant $a$, atom mass $M$, and nearest-neighbor spring constant $K$.

The equation of motion for atom $n$:

$$
M\ddot{u}_n = K(u_{n+1} - u_n) - K(u_n - u_{n-1}) = K(u_{n+1} + u_{n-1} - 2u_n)
$$

**Trial solution:** $u_n = A e^{i(qna - \omega t)}$

Substituting:

$$-M\omega^2 = K(e^{iqa} + e^{-iqa} - 2) = 2K(\cos(qa) - 1) = -4K\sin^2(qa/2)$$

$$
\boxed{\omega(q) = 2\sqrt{\frac{K}{M}}\left|\sin\frac{qa}{2}\right| = \omega_m\left|\sin\frac{qa}{2}\right|}
$$

where $\omega_m = 2\sqrt{K/M}$ is the maximum frequency.

### Properties of the Dispersion

**Long wavelength limit ($qa \ll 1$):**

$$
\omega(q) \approx \omega_m \frac{|q|a}{2} = \sqrt{\frac{K}{M}}a|q| = v_s |q|
$$

This is linear dispersion with **sound velocity** $v_s = a\sqrt{K/M}$.

**Group velocity:**

$$
v_g = \frac{d\omega}{dq} = v_s \cos(qa/2)
$$

- At $q = 0$: $v_g = v_s$ (maximum)
- At $q = \pm\pi/a$: $v_g = 0$ (Brillouin zone boundary, standing wave)

**Physical interpretation:** The acoustic mode corresponds to uniform translation of the crystal at $q=0$, hence $\omega(0) = 0$ (Goldstone mode).

---

## Part III: Diatomic Lattice—Acoustic and Optical Phonons

### Model Setup

Consider a 1D diatomic lattice with:
- Two atoms per unit cell: mass $M_1$ (even sites) and $M_2$ (odd sites)
- Lattice constant $a$ (unit cell length)
- Same spring constant $K$ between nearest neighbors

Let $u_n$ be displacement of $M_1$ at position $2na$, and $v_n$ be displacement of $M_2$ at position $(2n+1)a$.

### Equations of Motion

For $M_1$ (even sites):

$$
M_1 \ddot{u}_n = K(v_n - u_n) + K(v_{n-1} - u_n) = K(v_n + v_{n-1} - 2u_n)
$$

For $M_2$ (odd sites):

$$
M_2 \ddot{v}_n = K(u_{n+1} - v_n) + K(u_n - v_n) = K(u_{n+1} + u_n - 2v_n)
$$

### Trial Solutions

**Bloch ansatz** with wavevector $q$ in the reduced zone $[-\pi/2a, \pi/2a]$:

$$
uu_n = A e^{i(2qna - \omega t)}, \quad v_n = B e^{i(q(2n+1)a - \omega t)}
$$

Note the phase factor $e^{iqa}$ between sublattices.

Substituting:

$$-M_1\omega^2 A = K(B e^{iqa} + B e^{-iqa} - 2A) = 2K(B\cos(qa) - A)$$

$$-M_2\omega^2 B = K(A e^{iqa} + A e^{-iqa} - 2B) = 2K(A\cos(qa) - B)$$

### Matrix Eigenvalue Problem

Writing in matrix form:

$$
\begin{pmatrix} 2K - M_1\omega^2 & -2K\cos(qa) \\ -2K\cos(qa) & 2K - M_2\omega^2 \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} = 0
$$

For nontrivial solutions, the determinant vanishes:

$$
(2K - M_1\omega^2)(2K - M_2\omega^2) - 4K^2\cos^2(qa) = 0$$

$$
M_1M_2\omega^4 - 2K(M_1 + M_2)\omega^2 + 4K^2\sin^2(qa) = 0$$

Let $\Omega^2 = \omega^2$, solve the quadratic:

$$
\Omega^2 = \frac{K(M_1+M_2)}{M_1M_2} \pm \frac{K}{M_1M_2}\sqrt{(M_1+M_2)^2 - 4M_1M_2\sin^2(qa)}
$$

### The Two Branches

**Acoustic branch ($-$ sign):**

At $q = 0$:

$$
\omega_-^2(0) = \frac{K(M_1+M_2) - K|M_1-M_2|}{M_1M_2} = 0 \quad \text{(if } M_1 \neq M_2\text{)}
$$

Actually, expanding at small $q$:

$$
\omega_-^2 \approx \frac{2K^2 q^2 a^2}{K(M_1+M_2)} = \frac{2K}{M_1+M_2}q^2a^2$$

So $\omega_-(q) \approx v_s |q|$ with $v_s = a\sqrt{2K/(M_1+M_2)}$.

At the zone boundary $q = \pi/2a$:

$$
\omega_-^2 = \frac{2K}{M_>} \quad \text{where } M_> = \max(M_1, M_2)
$$

**Optical branch ($+$ sign):**

At $q = 0$:

$$
\omega_+^2(0) = \frac{2K(M_1+M_2)}{M_1M_2} = 2K\left(\frac{1}{M_1} + \frac{1}{M_2}\right)
$$

This is a finite frequency—atoms in the unit cell oscillate out of phase while the center of mass remains fixed.

At the zone boundary $q = \pi/2a$:

$$
\omega_+^2 = \frac{2K}{M_<} \quad \text{where } M_< = \min(M_1, M_2)
$$

### Eigenvectors and Physical Interpretation

**Acoustic mode** at $q = 0$: $A = B$ (both sublattices move in phase—uniform translation).

**Optical mode** at $q = 0$: $M_1 A + M_2 B = 0$ (center of mass fixed, atoms oscillate against each other).

For ionic crystals, this out-of-phase motion creates an oscillating dipole moment, allowing coupling to electromagnetic waves (infrared absorption).

---

## Part IV: Canonical Quantization

### Lagrangian and Hamiltonian

The classical Lagrangian for the 1D monatomic chain:

$$
L = \sum_n \frac{1}{2}M\dot{u}_n^2 - \frac{1}{2}K\sum_n (u_{n+1} - u_n)^2
$$

**Normal mode transformation:**

Define Fourier-transformed coordinates:

$$
uu_q = \frac{1}{\sqrt{N}}\sum_n u_n e^{-iqna}, \quad u_n = \frac{1}{\sqrt{N}}\sum_q u_q e^{iqna}
$$

The Lagrangian becomes diagonal:

$$
L = \sum_q \left(\frac{1}{2}M|\dot{u}_q|^2 - \frac{1}{2}M\omega_q^2|u_q|^2\right)
$$

where $\omega_q = 2\sqrt{K/M}|\sin(qa/2)|$.

### Quantization

Introduce canonical momenta $p_q = M\dot{u}_q^*$ and impose commutation relations:

$$
[u_q, p_{q'}] = i\hbar\delta_{qq'}, \quad [u_q, u_{q'}] = [p_q, p_{q'}] = 0
$$

Define creation and annihilation operators:

$$
a_q = \sqrt{\frac{M\omega_q}{2\hbar}}\left(u_q + \frac{i}{M\omega_q}p_q\right), \quad a_q^\dagger = \sqrt{\frac{M\omega_q}{2\hbar}}\left(u_q - \frac{i}{M\omega_q}p_q\right)
$$

The Hamiltonian becomes:

$$
\hat{H} = \sum_q \hbar\omega_q \left(a_q^\dagger a_q + \frac{1}{2}\right) = \sum_q \hbar\omega_q \left(n_q + \frac{1}{2}\right)
$$

### Phonons as Bosons

The operators satisfy:

$$
[a_q, a_{q'}^\dagger] = \delta_{qq'}, \quad [a_q, a_{q'}] = [a_q^\dagger, a_{q'}^\dagger] = 0
$$

This is the algebra of **bosonic** creation/annihilation operators. The eigenstates $|n_q\rangle$ represent $n_q$ phonons in mode $q$.

**Key properties:**
- Phonon number is not conserved (can be created/destroyed)
- Chemical potential $\mu = 0$
- At temperature $T$, average occupation follows Bose-Einstein: $\langle n_q\rangle = \frac{1}{e^{\beta\hbar\omega_q} - 1}$

---

## Part V: Three-Dimensional Crystals

### The Dynamical Matrix

In 3D with $s$ atoms per unit cell, the dynamical matrix is a $3s \times 3s$ matrix:

$$
D_{\kappa\alpha,\kappa'\beta}(\mathbf{q}) = \frac{1}{\sqrt{M_\kappa M_{\kappa'}}}\sum_{\mathbf{R}} \Phi_{\kappa\alpha,\kappa'\beta}(\mathbf{R}) e^{-i\mathbf{q}\cdot\mathbf{R}}
$$

where $\kappa = 1, \ldots, s$ labels atoms in the unit cell, and $\alpha, \beta = x, y, z$ are Cartesian components.

**Diagonalization:**

$$\sum_{\kappa'\beta} D_{\kappa\alpha,\kappa'\beta}(\mathbf{q}) e_{\kappa'\beta}^{(\lambda)}(\mathbf{q}) = \omega_\lambda^2(\mathbf{q}) e_{\kappa\alpha}^{(\lambda)}(\mathbf{q})
$$

There are $3s$ eigenvalues labeled by $\lambda$, giving $3s$ phonon branches:
- 3 **acoustic** branches (one longitudinal LA, two transverse TA)
- $3(s-1)$ **optical** branches

### Polarization Vectors

The eigenvectors satisfy orthonormality:

$$
\sum_{\kappa\alpha} e_{\kappa\alpha}^{(\lambda)*}(\mathbf{q}) e_{\kappa\alpha}^{(\lambda')}(\mathbf{q}) = \delta_{\lambda\lambda'}
$$

For acoustic modes at $\mathbf{q} = 0$: $\mathbf{e}^{(\text{ac})}_{\kappa}(0) = \frac{1}{\sqrt{sM}}$ (uniform translation).

---

## Part VI: Phonon Density of States and van Hove Singularities

### Definition

The **phonon density of states** (DOS) per unit frequency:

$$
g(\omega) = \sum_\lambda \int_{\text{BZ}} \frac{d^3q}{(2\pi)^3} \delta(\omega - \omega_\lambda(\mathbf{q}))
$$

This counts the number of phonon modes per unit frequency interval.

### van Hove Singularities

Critical points where $\nabla_q \omega_\lambda(\mathbf{q}) = 0$ (stationary points in the dispersion) lead to **van Hove singularities** in $g(\omega)$.

Near a critical point at $\mathbf{q}_c$:

$$
\omega(\mathbf{q}) \approx \omega_c + \frac{1}{2}\sum_i \alpha_i (q_i - q_{c,i})^2$$

**Types of critical points:**

1. **Maximum or minimum:** All $\alpha_i$ have same sign
   - $g(\omega) \propto \sqrt{|\omega - \omega_c|}$ for 3D (square root singularity)

2. **Saddle point:** Mixed signs
   - In 3D: logarithmic singularity or finite discontinuity depending on dimensionality

**Physical origin:** The group velocity $v_g = \nabla_q \omega$ vanishes at critical points, causing a pile-up of modes in the density of states.

**Example—1D chain:**

At the zone boundary $q = \pi/a$ for the monatomic chain:

$$\omega(q) = \omega_m\sin(qa/2) \approx \omega_m - \frac{\omega_m}{4}(qa - \pi)^2$$

The DOS diverges as $g(\omega) \propto (\omega_m - \omega)^{-1/2}$ near $\omega_m$.

**Example—Diatomic chain:**

The gap between acoustic and optical branches at $q = \pi/2a$:

$$\Delta\omega = \sqrt{2K}\left(\frac{1}{\sqrt{M_<}} - \frac{1}{\sqrt{M_>}}\right)$$

This frequency gap contains no phonon states—$g(\omega) = 0$ in the gap.

---

## Part VII: Polaritons—Phonon-Photon Coupling

### Infrared Active Optical Phonons

In ionic crystals, optical phonons at $\mathbf{q} = 0$ carry an oscillating dipole moment. For a diatomic crystal with effective charge $e^*$:

$$\mathbf{P} = n e^*(\mathbf{u}_1 - \mathbf{u}_2)$$

where $n$ is the number density of unit cells.

This couples to the electromagnetic field via the interaction Hamiltonian:

$$
H_{\text{int}} = -\mathbf{P}\cdot\mathbf{E}
$$

### The Dispersion Relation

The coupled phonon-photon system has eigenfrequencies determined by:

$$\frac{\omega^2}{c^2} = \varepsilon(\omega) q^2$$

where the dielectric function has a Lorentz oscillator form:

$$
\varepsilon(\omega) = \varepsilon_\infty + \frac{\omega_p^2}{\omega_{\text{TO}}^2 - \omega^2 - i\gamma\omega}
$$

Here:
- $\varepsilon_\infty$ is the high-frequency (electronic) dielectric constant
- $\omega_{\text{TO}}$ is the transverse optical phonon frequency
- $\omega_p$ is the ionic plasma frequency
- $\gamma$ is the phonon damping rate

### Polariton Branches

The dispersion $\omega(q)$ shows anticrossing behavior near $\omega_{\text{TO}}$:

**Lower branch ($\omega < \omega_{\text{TO}}$):**
- Photon-like at small $q$ (linear $\omega \sim cq$)
- Phonon-like near $\omega_{\text{TO}}$

**Upper branch ($\omega > \omega_{\text{LO}}$):**
- Phonon-like near $\omega_{\text{LO}}$
- Photon-like at large $q$

**The frequency gap ($\omega_{\text{TO}} < \omega < \omega_{\text{LO}}$):**

The longitudinal optical frequency $\omega_{\text{LO}}$ satisfies $\varepsilon(\omega_{\text{LO}}) = 0$, giving:

$$
\omega_{\text{LO}}^2 = \omega_{\text{TO}}^2 + \frac{\omega_p^2}{\varepsilon_\infty}
$$

This is the **Lyddane-Sachs-Teller relation**:

$$
\frac{\omega_{\text{LO}}^2}{\omega_{\text{TO}}^2} = \frac{\varepsilon_0}{\varepsilon_\infty}
$$

where $\varepsilon_0 = \varepsilon(0)$ is the static dielectric constant.

**Physical interpretation:** In the gap, electromagnetic waves cannot propagate through the crystal—they are totally reflected. This is the **Reststrahlen band**.

---

## Part VIII: Phonon Green's Functions

### Definition

The phonon propagator (Green's function) is defined analogously to electrons:

$$
\mathcal{D}(\mathbf{q}, \tau) = -\langle T_\tau \hat{\phi}(\mathbf{q}, \tau) \hat{\phi}(-\mathbf{q}, 0)\rangle$$

where $\hat{\phi}(\mathbf{q})$ is the phonon field operator related to displacements.

For the harmonic crystal:

$$
\mathcal{D}_\lambda(\mathbf{q}, i\omega_n) = \frac{2\omega_\lambda(\mathbf{q})}{(i\omega_n)^2 - \omega_\lambda^2(\mathbf{q})}
$$

with Matsubara frequencies $\omega_n = 2n\pi/\beta$ for bosons.

### Phonon Self-Energy and Lifetime

Anharmonic interactions (cubic and higher-order terms in the potential) give phonons a finite lifetime. The Dyson equation:

$$
\mathcal{D}^{-1} = \mathcal{D}_0^{-1} - \Pi$$

where $\Pi$ is the phonon self-energy (polarization). The imaginary part gives the phonon linewidth:

$$\Gamma_\lambda(\mathbf{q}) = -\text{Im}\,\Pi(\mathbf{q}, \omega_\lambda + i\eta)$$

Physical processes contributing to phonon decay:
1. **Three-phonon processes:** One phonon decays into two (or vice versa)
2. **Four-phonon processes:** Higher-order scattering
3. **Phonon-electron scattering:** In metals
4. **Isotope scattering:** Mass disorder

---

## Summary

| Concept | Key Result | Physical Meaning |
|---------|-----------|------------------|
| Acoustic phonons | $\omega \propto q$ (small $q$) | Sound waves, uniform translation at $q=0$ |
| Optical phonons | $\omega(0) \neq 0$ | Relative oscillation of sublattices |
| Phonon quantization | $[a_q, a_{q'}^\dagger] = \delta_{qq'}$ | Bosonic quasiparticles |
| van Hove singularities | Divergences in $g(\omega)$ | Critical points in dispersion |
| Polaritons | Anticrossing of phonon and photon | Coupled EM-mechanical waves |
| LST relation | $\omega_{\text{LO}}^2/\omega_{\text{TO}}^2 = \varepsilon_0/\varepsilon_\infty$ | Dielectric screening of LO mode |

---

## References

1. Kittel, C. *Introduction to Solid State Physics*, 8th ed. (Wiley, 2005). Chapter 4

2. Ashcroft, N.W. & Mermin, N.D. *Solid State Physics* (Brooks Cole, 1976). Chapters 22-23

3. Li, Z. (李正中). *Solid State Theory* (《固体理论》), 2nd ed. (Higher Education Press, 2002). Chapter 2

4. Cardona, M. & Güntherodt, G. (eds.) *Light Scattering in Solids* (Springer, 1982)

5. Srivastava, G.P. *The Physics of Phonons* (Taylor & Francis, 1990)
