# Phonons: From Classical Lattice Dynamics to Quantum Transport

📅 **Date:** 2026-03-31 | 🏷️ **Tags:** Condensed Matter, Lattice Dynamics, Phonons | 📂 **Category:** Condensed Matter Notes

---

## Introduction

This note provides a comprehensive treatment of phonons—the quantized excitations of crystal lattice vibrations. We develop the theory from classical Newtonian mechanics through canonical quantization, covering both monatomic (simple) and diatomic (compound) lattices, acoustic and optical phonon branches, polaritons, and van Hove singularities in the phonon density of states. Every derivation is presented in full detail.

---

## Part I: Classical Lattice Dynamics

### The Harmonic Approximation

Consider a crystal with atoms at equilibrium positions $\mathbf{R}_n^0$. Let $\mathbf{u}_n$ be the displacement of atom $n$ from its equilibrium position. The potential energy $V$ expanded to quadratic order in displacements gives the **harmonic approximation**:

$$
V = V_0 + \frac{1}{2}\sum_{n,n'} \sum_{\alpha,\beta} u_n^\alpha \Phi_{nn'}^{\alpha\beta} u_{n'}^\beta
$$

where $\alpha, \beta \in \{x, y, z\}$ are Cartesian indices, and the **force constant matrix** is:

$$
\Phi_{nn'}^{\alpha\beta} = \left.\frac{\partial^2 V}{\partial u_n^\alpha \partial u_{n'}^\beta}\right|_{\mathbf{u}=0}
$$

**Properties of $\Phi$:**

1. **Symmetry:** $\Phi_{nn'}^{\alpha\beta} = \Phi_{n'n}^{\beta\alpha}$ (from equality of mixed partial derivatives)
2. **Translational invariance:** $\Phi_{nn'}^{\alpha\beta} = \Phi_{\alpha\beta}(\mathbf{R}_n^0 - \mathbf{R}_{n'}^0)$ depends only on relative equilibrium positions
3. **Zero sum rule:** $\sum_{n'} \Phi_{nn'}^{\alpha\beta} = 0$ (uniform translation costs no energy)

The classical equations of motion follow from Newton's second law:

$$
M_n \ddot{u}_n^\alpha = -\frac{\partial V}{\partial u_n^\alpha} = -\sum_{n',\beta} \Phi_{nn'}^{\alpha\beta} u_{n'}^\beta \equiv F_n^\alpha
$$

### Bloch's Theorem and Plane Wave Solutions

Due to lattice periodicity, we seek normal mode solutions of the form:

$$
u\mathbf{u}_n(t) = \mathbf{e}(\mathbf{q}) e^{i(\mathbf{q}\cdot\mathbf{R}_n^0 - \omega t)}
$$

where:
- $\mathbf{q}$ is the wavevector in the first Brillouin zone
- $\mathbf{e}(\mathbf{q})$ is the **polarization vector** (amplitude and direction of oscillation)
- $\omega$ is the mode frequency (to be determined)

Substituting this ansatz into the equation of motion:

$$-M\omega^2 \mathbf{e} e^{i\mathbf{q}\cdot\mathbf{R}_n^0} = -\sum_{n'} \mathbf{\Phi}(\mathbf{R}_n^0 - \mathbf{R}_{n'}^0) \mathbf{e} e^{i\mathbf{q}\cdot\mathbf{R}_{n'}^0}$$

Let $\mathbf{R} = \mathbf{R}_n^0 - \mathbf{R}_{n'}^0$, then:

$$M\omega^2 \mathbf{e} = \sum_{\mathbf{R}} \mathbf{\Phi}(\mathbf{R}) \mathbf{e} e^{-i\mathbf{q}\cdot\mathbf{R}}$$

This defines the **dynamical matrix**:

$$
D_{\alpha\beta}(\mathbf{q}) = \frac{1}{M} \sum_{\mathbf{R}} \Phi_{\alpha\beta}(\mathbf{R}) e^{-i\mathbf{q}\cdot\mathbf{R}}
$$

The eigenvalue equation becomes:

$$
\sum_{\beta} D_{\alpha\beta}(\mathbf{q}) e_{\beta} = \omega^2 e_{\alpha}
$$

This is a $3 \times 3$ Hermitian matrix eigenvalue problem for each $\mathbf{q}$, giving three phonon branches (one longitudinal, two transverse) for a monatomic lattice.

---

## Part II: Monatomic Lattice—Acoustic Phonons

### The 1D Chain: Complete Derivation

Consider a 1D monatomic chain with:
- Lattice constant $a$ (equilibrium spacing)
- Atom mass $M$
- Nearest-neighbor spring constant $K$

**Step 1: Set up the equation of motion**

The potential energy depends on relative displacements:

$$V = \frac{1}{2}K\sum_n (u_{n+1} - u_n)^2$$

The force on atom $n$:
$$F_n = -\frac{\partial V}{\partial u_n} = -K[(u_n - u_{n-1}) - (u_{n+1} - u_n)] = K(u_{n+1} + u_{n-1} - 2u_n)$$

Newton's equation:
$$
M\ddot{u}_n = K(u_{n+1} + u_{n-1} - 2u_n)
$$

**Step 2: Insert plane wave ansatz**

$$u_n(t) = A e^{i(qna - \omega t)}$$

Note: Physical displacement is $\text{Re}[u_n(t)]$.

Computing derivatives:
- $\ddot{u}_n = -\omega^2 u_n$
- $u_{n+1} = A e^{i(q(n+1)a - \omega t)} = u_n e^{iqa}$
- $u_{n-1} = u_n e^{-iqa}$

Substituting:
$$-M\omega^2 u_n = K(e^{iqa} + e^{-iqa} - 2)u_n$$

**Step 3: Solve for dispersion relation**

Cancel $u_n \neq 0$:
$$M\omega^2 = K(2 - e^{iqa} - e^{-iqa}) = 2K(1 - \cos(qa))$$

Using the identity $1 - \cos\theta = 2\sin^2(\theta/2)$:
$$M\omega^2 = 4K\sin^2(qa/2)$$

Taking the positive root (frequency is positive):

$$
\boxed{\omega(q) = 2\sqrt{\frac{K}{M}}\left|\sin\frac{qa}{2}\right| \equiv \omega_m\left|\sin\frac{qa}{2}\right|}
$$

where $\omega_m = 2\sqrt{K/M}$ is the **maximum frequency** at the zone boundary.

### Properties of the Acoustic Dispersion

**1. Long wavelength limit ($|q|a \ll 1$):**

Expand $\sin(x) \approx x$ for small $x$:
$$\omega(q) \approx \omega_m \frac{|q|a}{2} = 2\sqrt{\frac{K}{M}} \frac{|q|a}{2} = \sqrt{\frac{K}{M}}a|q|$$

This is linear dispersion $\omega = v_s |q|$ with **sound velocity**:

$$
v_s = a\sqrt{\frac{K}{M}}
$$

**Physical interpretation:** At long wavelengths, the discrete lattice appears as a continuous elastic medium, and phonons become ordinary sound waves.

**2. Group velocity:**

$$v_g(q) = \frac{d\omega}{dq} = v_s \cos(qa/2) \cdot \text{sgn}(q)$$

- At $q = 0$: $v_g = v_s$ (maximum, wave packet travels at sound speed)
- At $q = \pm\pi/a$: $v_g = 0$ (standing wave at zone boundary)

**3. Phase velocity:**

$$v_p(q) = \frac{\omega}{q} = v_s \frac{|\sin(qa/2)|}{|qa/2|}$$

Dispersion is strongest near the zone boundary where $v_p \neq v_g$.

**4. Symmetry:**

$$\omega(q) = \omega(-q) \quad \text{(time-reversal symmetry)}$$

$$\omega(q + 2\pi/a) = \omega(q) \quad \text{(periodicity in reciprocal space)}$

---

## Part III: Diatomic Lattice—Acoustic and Optical Phonons

### Model Setup

Consider a 1D diatomic chain with:
- Two atoms per primitive cell: masses $M_1$ and $M_2$ (assume $M_1 < M_2$ without loss of generality)
- Lattice constant $a$ (primitive cell length)
- Atoms arranged as: $\cdots - M_1 - M_2 - M_1 - M_2 - \cdots$
- Positions: $M_1$ at $2na$, $M_2$ at $(2n+1)a$ for integer $n$
- Nearest-neighbor spring constant $K$ (same for all bonds)

Let $u_n$ = displacement of $M_1$ at position $2na$
Let $v_n$ = displacement of $M_2$ at position $(2n+1)a$

### Equations of Motion

**For $M_1$ at position $2na$:**

The atom is connected to $M_2$ at $(2n-1)a$ (left) and $(2n+1)a$ (right).

Spring forces:
- Left spring: $K[v_{n-1} - u_n]$ (force to right if $v_{n-1} > u_n$)
- Right spring: $K[v_n - u_n]$

$$M_1 \ddot{u}_n = K(v_{n-1} - u_n) + K(v_n - u_n) = K(v_{n-1} + v_n - 2u_n)$$

**For $M_2$ at position $(2n+1)a$:**

Connected to $M_1$ at $2na$ (left) and $2(n+1)a$ (right).

$$M_2 \ddot{v}_n = K(u_n - v_n) + K(u_{n+1} - v_n) = K(u_n + u_{n+1} - 2v_n)$$

### Bloch Ansatz

Seek plane wave solutions with wavevector $q$ in the reduced zone $[-\pi/2a, \pi/2a]$:

$$
u_n = A e^{i(2qna - \omega t)}$$
$$v_n = B e^{i(q(2n+1)a - \omega t)} = B e^{iqa} e^{i(2qna - \omega t)}$$

Note: The phase factor $e^{iqa}$ accounts for the position offset between sublattices.

### Deriving the Matrix Equation

**Step 1: Substitute into the $M_1$ equation**

$$-M_1\omega^2 A e^{i2qna} = K[Be^{iq(2n-1)a} + Be^{iq(2n+1)a} - 2Ae^{i2qna}]$$

Factor out $e^{i2qna}$:
$$-M_1\omega^2 A = K[Be^{-iqa} + Be^{iqa} - 2A]$$
$$-M_1\omega^2 A = 2K[B\cos(qa) - A]$$

**Step 2: Substitute into the $M_2$ equation**

$$-M_2\omega^2 B e^{iq(2n+1)a} = K[Ae^{i2qna} + Ae^{i2(n+1)qa} - 2Be^{iq(2n+1)a}]$$

Factor out $e^{iq(2n+1)a}$:
$$-M_2\omega^2 B = K[Ae^{-iqa} + Ae^{iqa} - 2B]$$
$$-M_2\omega^2 B = 2K[A\cos(qa) - B]$$

**Step 3: Matrix form**

Rearranging both equations:
$$(2K - M_1\omega^2)A - 2K\cos(qa)B = 0$$
$$-2K\cos(qa)A + (2K - M_2\omega^2)B = 0$$

In matrix form:
$$
\begin{pmatrix} 2K - M_1\omega^2 & -2K\cos(qa) \\ -2K\cos(qa) & 2K - M_2\omega^2 \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} = 0
$$

### Solving the Eigenvalue Problem

For nontrivial solutions, the determinant must vanish:

$$(2K - M_1\omega^2)(2K - M_2\omega^2) - 4K^2\cos^2(qa) = 0$$

Expand:
$$4K^2 - 2K(M_1+M_2)\omega^2 + M_1M_2\omega^4 - 4K^2\cos^2(qa) = 0$$

Using $1 - \cos^2(qa) = \sin^2(qa)$:
$$M_1M_2\omega^4 - 2K(M_1+M_2)\omega^2 + 4K^2\sin^2(qa) = 0$$

Let $\Omega = \omega^2$. This is a quadratic equation:
$$M_1M_2\Omega^2 - 2K(M_1+M_2)\Omega + 4K^2\sin^2(qa) = 0$$

Using the quadratic formula $\Omega = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$:

$$\Omega = \frac{2K(M_1+M_2) \pm \sqrt{4K^2(M_1+M_2)^2 - 16K^2M_1M_2\sin^2(qa)}}{2M_1M_2}$$

$$
\Omega = \frac{K(M_1+M_2)}{M_1M_2} \pm \frac{K}{M_1M_2}\sqrt{(M_1+M_2)^2 - 4M_1M_2\sin^2(qa)}
$$

The two solutions are:

$$
\boxed{\omega_{\pm}^2(q) = \frac{K}{\mu} \pm K\sqrt{\frac{1}{\mu^2} - \frac{4\sin^2(qa)}{M_1M_2}}}
$$

where $\mu = \frac{M_1M_2}{M_1+M_2}$ is the **reduced mass**.

### Explicit Form at Special Points

**At $q = 0$:**

$$\omega_{\pm}^2(0) = \frac{K(M_1+M_2)}{M_1M_2} \pm \frac{K(M_1+M_2)}{M_1M_2}$$

- Acoustic: $\omega_-^2(0) = 0$ → $\omega_-(0) = 0$
- Optical: $\omega_+^2(0) = \frac{2K(M_1+M_2)}{M_1M_2} = 2K\left(\frac{1}{M_1} + \frac{1}{M_2}\right)$

**Long wavelength acoustic branch:**

For small $q$, expand $\sin^2(qa) \approx (qa)^2$:

$$\omega_-^2 \approx \frac{K}{\mu} - \frac{K}{\mu}\sqrt{1 - \frac{4\mu^2(qa)^2}{M_1M_2}}$$

Using $\sqrt{1-x} \approx 1 - x/2$ for small $x$:
$$\omega_-^2 \approx \frac{K}{\mu} - \frac{K}{\mu}\left(1 - \frac{2\mu^2(qa)^2}{M_1M_2}\right) = \frac{2K\mu(qa)^2}{M_1M_2}$$

With $\mu = M_1M_2/(M_1+M_2)$:
$$\omega_-^2 = \frac{2K(qa)^2}{M_1+M_2}$$

$$
\boxed{\omega_-(q) \approx |q|a\sqrt{\frac{2K}{M_1+M_2}} = v_s |q|}$$

Sound velocity: $v_s = a\sqrt{2K/(M_1+M_2)}$

**At zone boundary $q = \pi/2a$:**

$$\sin^2(qa) = \sin^2(\pi/2) = 1$$

$$\omega_{\pm}^2 = \frac{K(M_1+M_2)}{M_1M_2} \pm \frac{K|M_1-M_2|}{M_1M_2}$$

- Acoustic: $\omega_-^2 = \frac{2K}{M_2}$ (assuming $M_2 > M_1$)
- Optical: $\omega_+^2 = \frac{2K}{M_1}$

**Frequency gap at zone boundary:**

$$\Delta\omega = \sqrt{2K}\left(\frac{1}{\sqrt{M_1}} - \frac{1}{\sqrt{M_2}}\right)$$

### Eigenvectors and Physical Interpretation

From the matrix equation, the amplitude ratio is:

$$\frac{B}{A} = \frac{2K - M_1\omega^2}{2K\cos(qa)}$$

**Acoustic mode ($\omega = \omega_-$):**

At $q = 0$: $\omega_- = 0$, so:
$$\frac{B}{A} = \frac{2K}{2K} = 1$$

Both atoms move **in phase** with equal amplitude: $A = B$. This is a uniform translation.

**Optical mode ($\omega = \omega_+$):**

At $q = 0$: $\omega_+^2 = 2K(1/M_1 + 1/M_2)$

$$2K - M_1\omega_+^2 = 2K - 2K(1 + M_1/M_2) = -2K\frac{M_1}{M_2}$$

$$\frac{B}{A} = \frac{-2KM_1/M_2}{2K} = -\frac{M_1}{M_2}$$

Atoms move **out of phase** with amplitude ratio $M_1 A + M_2 B = 0$, meaning the center of mass remains fixed.

For ionic crystals ($M_1$ positive ion, $M_2$ negative ion), this oscillating dipole couples to electromagnetic radiation (infrared absorption).

---

## Part IV: Canonical Quantization

### Classical Normal Mode Coordinates

**Step 1: Define Fourier-transformed coordinates**

For the 1D monatomic chain with periodic boundary conditions (N atoms, length $L = Na$):

$$u_n = \frac{1}{\sqrt{N}}\sum_{q} u_q e^{iqna}, \quad u_q = \frac{1}{\sqrt{N}}\sum_{n} u_n e^{-iqna}$$

Allowed wavevectors: $q = \frac{2\pi m}{Na}$ for $m = 0, \pm 1, \ldots, \pm(N/2-1), N/2$

**Step 2: Transform the Lagrangian**

The classical Lagrangian:
$$L = \sum_n \frac{M}{2}\dot{u}_n^2 - \frac{K}{2}\sum_n (u_{n+1} - u_n)^2$$

Kinetic energy:
$$\sum_n \dot{u}_n^2 = \frac{1}{N}\sum_n \sum_{q,q'} \dot{u}_q \dot{u}_{q'} e^{i(q+q')na} = \sum_q |\dot{u}_q|^2$$

(using $\sum_n e^{i(q+q')na} = N\delta_{q,-q'}$ and $u_{-q} = u_q^*$ for real $u_n$)

Potential energy:
$$\sum_n (u_{n+1} - u_n)^2 = \sum_q |u_q|^2 \cdot 2(1 - \cos(qa)) = \sum_q |u_q|^2 \frac{M\omega_q^2}{K}$$

Thus:
$$L = \sum_q \left(\frac{M}{2}|\dot{u}_q|^2 - \frac{M\omega_q^2}{2}|u_q|^2\right)$$

This is a sum of independent harmonic oscillators, one for each $q$.

### Quantization Procedure

**Step 1: Define canonical momenta**

$$p_q = \frac{\partial L}{\partial \dot{u}_q^*} = M\dot{u}_q$$

(Note: $u_q$ and $u_q^*$ are treated as independent variables in the Lagrangian formalism for complex coordinates.)

**Step 2: Impose commutation relations**

$$[\hat{u}_q, \hat{p}_{q'}^\dagger] = i\hbar\delta_{qq'}$$
$$[\hat{u}_q, \hat{u}_{q'}] = [\hat{p}_q, \hat{p}_{q'}] = 0$$

**Step 3: Define creation and annihilation operators**

For each mode $q$:

$$\hat{a}_q = \sqrt{\frac{M\omega_q}{2\hbar}}\left(\hat{u}_q + \frac{i\hat{p}_q}{M\omega_q}\right)$$

$$\hat{a}_q^\dagger = \sqrt{\frac{M\omega_q}{2\hbar}}\left(\hat{u}_q^\dagger - \frac{i\hat{p}_q^\dagger}{M\omega_q}\right)$$

Note: For standing wave boundary conditions, $\hat{u}_q^\dagger = \hat{u}_{-q}$ and $\hat{p}_q^\dagger = \hat{p}_{-q}$.

**Step 4: Verify commutation relations**

$$[\hat{a}_q, \hat{a}_{q'}^\dagger] = \frac{M\omega_q}{2\hbar}\left[\hat{u}_q + \frac{i\hat{p}_q}{M\omega_q}, \hat{u}_{q'}^\dagger - \frac{i\hat{p}_{q'}^\dagger}{M\omega_{q'}}\right]$$

$$= \frac{M\omega_q}{2\hbar}\left([\hat{u}_q, \hat{u}_{q'}^\dagger] - \frac{i}{M\omega_{q'}}[\hat{u}_q, \hat{p}_{q'}^\dagger] + \frac{i}{M\omega_q}[\hat{p}_q, \hat{u}_{q'}^\dagger] + \frac{1}{M^2\omega_q\omega_{q'}}[\hat{p}_q, \hat{p}_{q'}^\dagger]\right)$$

Using $[\hat{u}_q, \hat{p}_{q'}^\dagger] = i\hbar\delta_{qq'}$ and other commutators vanishing:
$$[\hat{a}_q, \hat{a}_{q'}^\dagger] = \frac{M\omega_q}{2\hbar}\left(\frac{-i(i\hbar)\delta_{qq'}}{M\omega_q} + \frac{i(-i\hbar)\delta_{qq'}}{M\omega_q}\right) = \frac{M\omega_q}{2\hbar} \cdot \frac{2\hbar}{M\omega_q}\delta_{qq'} = \delta_{qq'}$$

Also: $[\hat{a}_q, \hat{a}_{q'}] = [\hat{a}_q^\dagger, \hat{a}_{q'}^\dagger] = 0$

**Step 5: Express Hamiltonian**

$$\hat{H} = \sum_q \hbar\omega_q\left(\hat{a}_q^\dagger\hat{a}_q + \frac{1}{2}\right)$$

### Phonon Number States

The eigenstates are labeled by occupation numbers $|n_{q_1}, n_{q_2}, \ldots\rangle$:

$$\hat{a}_q^\dagger\hat{a}_q |\{n_q\}\rangle = n_q |\{n_q\}\rangle$$

- $n_q = 0, 1, 2, \ldots$ (bosonic occupation)
- $\hat{a}_q^\dagger$ creates a phonon in mode $q$
- $\hat{a}_q$ annihilates a phonon in mode $q$

**Thermal average (Bose-Einstein distribution):**

At temperature $T$:
$$\langle n_q\rangle = \frac{1}{e^{\beta\hbar\omega_q} - 1}$$

---

## Part V: Three-Dimensional Crystals

### The Dynamical Matrix in 3D

For a crystal with $s$ atoms per unit cell at positions $\mathbf{r}_\kappa$ ($\kappa = 1, \ldots, s$), the dynamical matrix is a $3s \times 3s$ matrix:

$$
D_{\kappa\alpha,\kappa'\beta}(\mathbf{q}) = \frac{1}{\sqrt{M_\kappa M_{\kappa'}}}\sum_{\mathbf{R}} \Phi_{\kappa\alpha,\kappa'\beta}(\mathbf{R}) e^{-i\mathbf{q}\cdot\mathbf{R}}
$$

where $\Phi_{\kappa\alpha,\kappa'\beta}(\mathbf{R})$ is the force constant between atom $\kappa$ in the unit cell at origin and atom $\kappa'$ in the unit cell at $\mathbf{R}$.

**Diagonalization:**

$$\sum_{\kappa'\beta} D_{\kappa\alpha,\kappa'\beta}(\mathbf{q}) e_{\kappa'\beta}^{(\lambda)}(\mathbf{q}) = \omega_\lambda^2(\mathbf{q}) e_{\kappa\alpha}^{(\lambda)}(\mathbf{q})$$

There are $3s$ eigenvalues $\omega_\lambda(\mathbf{q})$ labeled by $\lambda = 1, \ldots, 3s$.

### Classification of Phonon Branches

**Acoustic branches (3 modes):**

At $\mathbf{q} = 0$: $\omega(\mathbf{q}=0) = 0$ for all 3 acoustic branches
- One **longitudinal acoustic (LA)**: atomic displacements $\parallel \mathbf{q}$
- Two **transverse acoustic (TA)**: atomic displacements $\perp \mathbf{q}$

Polarization vectors at $\mathbf{q} = 0$:
$$e_{\kappa\alpha}^{(\text{ac})}(0) = \frac{1}{\sqrt{s}}\delta_{\alpha,\text{direction}}$$

All atoms in the unit cell move in the same direction (uniform translation).

**Optical branches ($3s-3$ modes):**

At $\mathbf{q} = 0$: $\omega(0) \neq 0$ (finite frequency)
- Atoms within each unit cell move relative to each other
- Center of mass of each unit cell remains fixed
- For ionic crystals, can couple to electromagnetic fields

---

## Part VI: Phonon Density of States and van Hove Singularities

### Definition of Density of States

The **phonon density of states** $g(\omega)$ counts the number of modes per unit frequency:

$$
g(\omega) = \sum_{\lambda=1}^{3s} \int_{\text{BZ}} \frac{d^3q}{(2\pi)^3} \delta(\omega - \omega_\lambda(\mathbf{q}))$$

**Normalization:**
$$\int_0^\infty g(\omega) d\omega = 3s$$

(total number of phonon modes per unit cell).

### Deriving the van Hove Singularity

Near a critical point $\mathbf{q}_c$ where $\nabla_\mathbf{q}\omega|_{\mathbf{q}_c} = 0$, expand:

$$\omega(\mathbf{q}) = \omega_c + \frac{1}{2}\sum_{i=1}^3 \alpha_i (q_i - q_{c,i})^2$$

where $\alpha_i$ are the principal curvatures (eigenvalues of the Hessian matrix).

**Case 1: Minimum or Maximum (all $\alpha_i > 0$ or all $< 0$)**

For a 3D minimum (all $\alpha_i > 0$):
$$g(\omega) \propto \int d^3q \, \delta(\omega - \omega_c - \frac{1}{2}\sum_i \alpha_i q_i^2)$$

Let $\xi_i = \sqrt{\alpha_i/2} q_i$, then:
$$g(\omega) \propto \frac{1}{\sqrt{\alpha_1\alpha_2\alpha_3}}\int d^3\xi \, \delta(\omega - \omega_c - \xi^2)$$

In spherical coordinates:
$$\int d^3\xi \, \delta(\Delta\omega - \xi^2) = 4\pi \int_0^\infty \xi^2 d\xi \, \delta(\Delta\omega - \xi^2) = 2\pi\sqrt{\Delta\omega}$$

where $\Delta\omega = \omega - \omega_c > 0$.

$$
\boxed{g(\omega) \propto \sqrt{\omega - \omega_c} \quad \text{(for } \omega > \omega_c\text{)}}$$

This is a **square-root singularity** at the band edge.

**Case 2: Saddle Point (mixed signs)**

For example, $\alpha_1, \alpha_2 > 0$ and $\alpha_3 < 0$:

$$g(\omega) \propto \int d\xi_1 d\xi_2 d\xi_3 \, \delta(\Delta\omega - \xi_1^2 - \xi_2^2 + |\alpha_3'|\xi_3^2)$$

This leads to logarithmic singularities or discontinuities depending on dimensionality.

**Physical origin:** Vanishing group velocity $v_g = \nabla_\mathbf{q}\omega = 0$ at critical points causes modes to "pile up," enhancing $g(\omega)$.

### Examples

**1D Monatomic Chain:**

$$\omega(q) = \omega_m |\sin(qa/2)|$$

Near $q = \pi/a$ (zone boundary), let $q = \pi/a - \delta q$:
$$\omega \approx \omega_m\cos(\delta q \cdot a/2) \approx \omega_m\left(1 - \frac{(\delta q)^2 a^2}{8}\right)$$

$$g(\omega) = \frac{L}{\pi} \frac{dq}{d\omega} \propto \frac{1}{\sqrt{\omega_m - \omega}}$$

This diverges as $(\omega_m - \omega)^{-1/2}$ at the zone boundary.

**Diatomic Chain:**

The frequency gap between acoustic and optical branches at $q = \pi/2a$:
$$\omega_{\text{gap}} = \sqrt{2K/M_1} - \sqrt{2K/M_2}$$

No phonon states exist in this gap: $g(\omega) = 0$ for $\omega$ in the gap.

---

## Part VII: Polaritons—Coupled Phonon-Photon Modes

### Infrared-Active Optical Phonons

In ionic crystals, optical phonons at $\mathbf{q} = 0$ carry an oscillating dipole moment. For a diatomic crystal with effective ionic charge $e^*$:

**Dipole moment per unit cell:**
$$\mathbf{P} = n e^* (\mathbf{u}_1 - \mathbf{u}_2)$$

where $n$ is the number density of unit cells.

This polarization couples to the macroscopic electric field $\mathbf{E}$ via:
$$H_{\text{int}} = -\mathbf{P} \cdot \mathbf{E}$$

### Dielectric Function

The dielectric response of the coupled phonon-photon system is described by:

$$\varepsilon(\omega) = \varepsilon_\infty + \frac{\Omega_p^2}{\omega_{\text{TO}}^2 - \omega^2 - i\gamma\omega}$$

where:
- $\varepsilon_\infty$: electronic (high-frequency) dielectric constant
- $\omega_{\text{TO}}$: transverse optical phonon frequency at $\mathbf{q} = 0$
- $\Omega_p = \sqrt{ne^{*2}/\mu\varepsilon_0}$: ionic plasma frequency
- $\gamma$: phonon damping rate

### Lyddane-Sachs-Teller (LST) Relation

The longitudinal optical frequency $\omega_{\text{LO}}$ satisfies $\varepsilon(\omega_{\text{LO}}) = 0$:

$$0 = \varepsilon_\infty + \frac{\Omega_p^2}{\omega_{\text{TO}}^2 - \omega_{\text{LO}}^2}$$

Solving for $\omega_{\text{LO}}$:
$$\omega_{\text{LO}}^2 = \omega_{\text{TO}}^2 + \frac{\Omega_p^2}{\varepsilon_\infty}$$

The static dielectric constant is:
$$\varepsilon_0 = \varepsilon(0) = \varepsilon_\infty + \frac{\Omega_p^2}{\omega_{\text{TO}}^2}$$

Eliminating $\Omega_p^2$:

$$
\boxed{\frac{\omega_{\text{LO}}^2}{\omega_{\text{TO}}^2} = \frac{\varepsilon_0}{\varepsilon_\infty}}
$$

This is the **LST relation**. Since $\varepsilon_0 > \varepsilon_\infty$ for ionic crystals, $\omega_{\text{LO}} > \omega_{\text{TO}}$.

### Polariton Dispersion

The coupled modes satisfy the dispersion relation:
$$\frac{\omega^2}{c^2}\varepsilon(\omega) = q^2$$

This gives two branches separated by a frequency gap (the **Reststrahlen band**) between $\omega_{\text{TO}}$ and $\omega_{\text{LO}}$ where $\varepsilon(\omega) < 0$ and no propagating modes exist.

---

## Summary

| Concept | Mathematical Result | Physical Interpretation |
|---------|---------------------|-------------------------|
| Monatomic dispersion | $\omega = 2\sqrt{K/M}|\sin(qa/2)|$ | Acoustic phonons, $\omega \propto q$ at small $q$ |
| Diatomic dispersion | Two branches with gap | Acoustic (in-phase) and optical (out-of-phase) |
| Sound velocity | $v_s = a\sqrt{K/M}$ or $a\sqrt{2K/(M_1+M_2)}$ | Long-wavelength limit |
| Quantization | $[\hat{a}_q, \hat{a}_{q'}^\dagger] = \delta_{qq'}$ | Bosonic quasiparticles |
| van Hove singularity | $g(\omega) \propto \sqrt{\omega - \omega_c}$ | Critical points where $v_g = 0$ |
| LST relation | $\omega_{\text{LO}}^2/\omega_{\text{TO}}^2 = \varepsilon_0/\varepsilon_\infty$ | Screening of LO mode by ions |

---

## References

1. Kittel, C. *Introduction to Solid State Physics*, 8th ed. (Wiley, 2005). Chapter 4

2. Ashcroft, N.W. & Mermin, N.D. *Solid State Physics* (Brooks Cole, 1976). Chapters 22-23

3. Li, Z. (李正中). *Solid State Theory* (《固体理论》), 2nd ed. (Higher Education Press, 2002). Chapter 2

4. Cardona, M. & Güntherodt, G. (eds.) *Light Scattering in Solids* (Springer, 1982)

5. Srivastava, G.P. *The Physics of Phonons* (Taylor & Francis, 1990)
