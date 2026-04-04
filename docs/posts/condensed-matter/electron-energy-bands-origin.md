# Electron Energy Bands: From Atomic Orbitals to Bloch States

📅 **Date:** 2026-04-04 | 🏷️ **Tags:** Condensed Matter, Electronic Structure, Band Theory | 📂 **Category:** Condensed Matter Notes

---

## Introduction

The concept of electron energy bands represents a paradigm shift in our understanding of matter. Unlike atomic, nuclear, or particle physics where we typically deal with interactions of just a few particles, solid state physics involves systems with more than $10^{23}$ particles per cubic centimeter. Remarkably, this "infinity" of particles often proves simpler to analyze than systems of just three particles.

This note develops the theory of electron bands from first principles, covering: the fundamental mechanism of energy splitting due to wave function overlap, the Kronig-Penney model, Bloch's theorem, reciprocal space, Bravais lattices, X-ray scattering, Bloch function properties, density of states, and the three major approximation methods for band structure calculations (tight-binding, nearly free electron, and k·p theory).

---

## Part I: The Origin of Energy Bands

### From Isolated Wells to Coupled Systems

**The single quantum well:**

Consider a particle of mass $m$ in a one-dimensional square well of width $a$. The time-independent Schrödinger equation is:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + U(x)\psi = E\psi
$$

Inside the well ($U = 0$), the eigenstates are:

$$
\psi(x) = A\sin(kx), \quad k = \frac{N\pi}{a}, \quad N = 1, 2, 3, \ldots
$$

with quantized energies:

$$
E_N = \frac{\hbar^2 k^2}{2m} = \frac{\hbar^2 \pi^2 N^2}{2ma^2}
$$

**Two independent wells:**

When two identical wells are separated by a high or wide barrier, the systems are decoupled. Each well has the same energy eigenvalues, and the states are degenerate.

**Coupled wells — the emergence of splitting:**

When the barrier between wells is reduced, allowing tunneling, the two wells become **coupled**. The potential is:

$$
U(x) = \begin{cases}
\infty & x < -\frac{b}{2}-a \\
0 & -\frac{b}{2}-a < x < -\frac{b}{2} \\
U_0 & -\frac{b}{2} < x < \frac{b}{2} \\
0 & \frac{b}{2} < x < \frac{b}{2}+a \\
\infty & x > \frac{b}{2}+a
\end{cases}
$$

The wave function is divided into three regions with boundary conditions requiring continuity of $\psi$ and $d\psi/dx$ at all interfaces.

### Symmetric and Antisymmetric Solutions

Instead of two degenerate states, the coupled system exhibits **symmetric** and **antisymmetric** linear combinations:

$$
\psi_+(x) = \frac{1}{\sqrt{2}}[\psi_L(x) + \psi_R(x)] \quad \text{(symmetric, lower energy)}
$$

$$
\psi_-(x) = \frac{1}{\sqrt{2}}[\psi_L(x) - \psi_R(x)] \quad \text{(antisymmetric, higher energy)}
$$

**Physical origin of energy splitting:**

The antisymmetric solution must have a node at $x = 0$ (since $\psi(-x) = -\psi(x)$). This node forces the wave function to change more rapidly within the barrier region, requiring shorter wavelength Fourier components. Since shorter wavelength corresponds to higher kinetic energy:

$$
E_{\text{antisymmetric}} > E_{\text{symmetric}}
$$

### Extension to N Wells — The Band Formation

With three wells, there are three distinct eigenstates. With $N$ coupled wells, we obtain $N$ eigenstates with energies distributed across a range. States with more nodes have higher energy; states with fewer nodes have lower energy.

As $N \to \infty$:

1. The number of states in the energy range becomes very large
2. The spacing between adjacent energy levels becomes infinitesimally small
3. The discrete levels merge into a continuous **energy band**

Between these bands exist **energy gaps** — ranges of energy with no allowed states.

---

## Part II: The LCAO Approximation

### Linear Combination of Atomic Orbitals

The **Linear Combination of Atomic Orbitals (LCAO)** approximation assumes that atomic orbitals are essentially unchanged when atoms are brought together.

**Ansatz:**

$$
|\psi\rangle = c_1|\psi_1\rangle + c_2|\psi_2\rangle
$$

**Key quantities:**

- **On-site energies:** $E_1 = \langle\psi_1|H|\psi_1\rangle$, $E_2 = \langle\psi_2|H|\psi_2\rangle$
- **Coupling (hopping) matrix element:** $U_{12} = \langle\psi_1|H|\psi_2\rangle = U_{21}^*$
- **Overlap integral:** $I_{12} = \langle\psi_1|\psi_2\rangle$

### Derivation of the Eigenvalue Equation

The eigenvalue equation $H|\psi\rangle = E|\psi\rangle$ yields:

$$
c_1 E_1 + c_2(U_{12} - EI_{12}) = c_1 E
$$

$$
c_1(U_{12}^* - EI_{12}^*) + c_2 E_2 = c_2 E
$$

In matrix form with $\tilde{U}_{12} = U_{12} - \bar{E}I_{12}$ where $\bar{E} = (E_1 + E_2)/2$:

$$
\begin{pmatrix} E_1 & \tilde{U}_{12} \\ \tilde{U}_{12}^* & E_2 \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = E \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}
$$

### Solutions for Identical Atoms

For identical atoms ($E_1 = E_2 = E_0$) with real $\tilde{U}_{12} < 0$:

$$
E = E_0 \pm |\tilde{U}_{12}|
$$

**Bonding state** (lower energy):

$$
|\psi_{\text{bonding}}\rangle = \frac{1}{\sqrt{2(1+I_{12})}}(|\psi_1\rangle + |\psi_2\rangle)
$$

**Antibonding state** (higher energy):

$$
|\psi_{\text{antibonding}}\rangle = \frac{1}{\sqrt{2(1-I_{12})}}(|\psi_1\rangle - |\psi_2\rangle)
$$

**Fundamental insight:** The existence of energy bands is **not fundamentally dependent on periodicity**. Amorphous materials, glasses, and alloys can also exhibit bands and band gaps.

---

## Part III: The Kronig-Penney Model

### Model Definition

The Kronig-Penney model provides an exactly solvable one-dimensional periodic potential:

$$
U(x) = \begin{cases}
0 & 0 < x < a \quad \text{(well)} \\
U_0 & -b < x < 0 \quad \text{(barrier)}
\end{cases}
$$

repeated periodically with period $a + b$.

### Wave Function Ansatz

**In the well region ($0 < x < a$):**

$$
\psi_1(x) = A_1 e^{iKx} + B_1 e^{-iKx}, \quad \frac{\hbar^2 K^2}{2m} = E
$$

**In the barrier region ($-b < x < 0$):**

For $E < U_0$:

$$
\psi_2(x) = A_2 e^{\kappa x} + B_2 e^{-\kappa x}, \quad \frac{\hbar^2 \kappa^2}{2m} = U_0 - E
$$

**Bloch periodicity condition:**

$$
\psi_3(x) = \psi_2(x - a - b)e^{ik(a+b)}
$$

### The Kronig-Penney Equation

Applying boundary conditions and setting the determinant to zero yields:

$$
\frac{\kappa^2 - K^2}{2\kappa K}\sinh(\kappa b)\sin(Ka) + \cosh(\kappa b)\cos(Ka) = \cos(k(a+b))
$$

### Simplified Form: Delta Function Limit

Taking $b \to 0$, $U_0 \to \infty$ with $U_0 b = \text{constant}$:

$$
\boxed{P\frac{\sin(Ka)}{Ka} + \cos(Ka) = \cos(ka)}
$$

where $P = \frac{mU_0ba}{\hbar^2}$ measures barrier strength.

### Key Features

**1. Band gaps at zone boundaries:** Solutions exist only when LHS $\in [-1, 1]$, creating allowed bands separated by gaps.

**2. Vanishing derivative at zone boundaries:**

$$
\frac{dE}{dk} \propto \sin(ka) = 0 \quad \text{at} \quad ka = n\pi
$$

This corresponds to zero group velocity — standing waves due to Bragg reflection.

**3. Weak and strong coupling limits:**

- *Strong barriers ($P \to \infty$):* Narrow bands, wide gaps; $Ka = n\pi$ giving isolated well energies
- *Weak barriers ($P \to 0$):* $K = k$, free particle dispersion

---

## Part IV: Bloch's Theorem

### Statement of the Theorem

**Bloch's Theorem:** For a periodic potential satisfying $U(\mathbf{r} + \mathbf{R}) = U(\mathbf{r})$ for all lattice vectors $\mathbf{R}$, the eigenstates take the form:

$$
\psi_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}) = \psi_{n\mathbf{k}}(\mathbf{r})e^{i\mathbf{k} \cdot \mathbf{R}}
$$

Equivalently:

$$
\boxed{\psi_{n\mathbf{k}}(\mathbf{r}) = \frac{1}{\sqrt{V}}u_{n\mathbf{k}}(\mathbf{r})e^{i\mathbf{k} \cdot \mathbf{r}}}
$$

where $u_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}) = u_{n\mathbf{k}}(\mathbf{r})$ has the same periodicity as the lattice.

### Proof via Translation Operators

**Step 1:** Define the translation operator $T_{\mathbf{R}}$ such that $T_{\mathbf{R}}\psi(\mathbf{r}) = \psi(\mathbf{r} + \mathbf{R})$.

**Step 2:** Show $[T_{\mathbf{R}}, H] = 0$ using periodicity of $U(\mathbf{r})$.

**Step 3:** Since commuting operators have common eigenstates:

$$
T_{\mathbf{R}}\psi(\mathbf{r}) = C_{\mathbf{R}}\psi(\mathbf{r})
$$

**Step 4:** Two successive translations give $C_{\mathbf{R}+\mathbf{R}'} = C_{\mathbf{R}}C_{\mathbf{R}'}$.

**Step 5:** Normalization requires $|C_{\mathbf{R}}|^2 = 1$, so $C_{\mathbf{R}} = e^{i\phi_{\mathbf{R}}}$.

**Step 6:** The multiplicative property implies $C_{\mathbf{R}} = e^{i\mathbf{k} \cdot \mathbf{R}}$ for some vector $\mathbf{k}$.

### Consequences of Bloch's Theorem

**1. Reduced zone scheme:** Due to periodicity $e^{i(\mathbf{k}+\mathbf{G})\cdot\mathbf{R}} = e^{i\mathbf{k}\cdot\mathbf{R}}$, all physically distinct states are in the first Brillouin zone.

**2. Band structure:** For each $\mathbf{k}$, multiple solutions labeled by band index $n$, giving $E_n(\mathbf{k})$.

**3. Group velocity:**

$$
\mathbf{v}_n(\mathbf{k}) = \frac{1}{\hbar}\nabla_{\mathbf{k}}E_n(\mathbf{k})
$$

**4. Effective mass:** Near band extrema:

$$
E_n(\mathbf{k}) \approx E_0 + \frac{\hbar^2}{2}\sum_{i,j}k_i\left(\frac{1}{m^*}\right)_{ij}k_j
$$

---

## Part V: Bravais Lattices and Reciprocal Space

### Bravais Lattice Definition

A **Bravais lattice** consists of all points with position vectors:

$$
\mathbf{R} = N_1\mathbf{a}_1 + N_2\mathbf{a}_2 + N_3\mathbf{a}_3
$$

where $N_i$ are integers and $\mathbf{a}_i$ are primitive vectors.

**Primitive cell volume:**

$$
V_{\text{cell}} = |\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)|
$$

### Reciprocal Lattice

**Definition:** Reciprocal lattice vectors $\mathbf{Q}$ satisfy:

$$
e^{i\mathbf{Q}\cdot\mathbf{R}} = 1 \quad \Rightarrow \quad \mathbf{Q} \cdot \mathbf{R} = 2\pi N
$$

**Primitive reciprocal vectors:**

$$
\mathbf{q}_1 = 2\pi\frac{\mathbf{a}_2 \times \mathbf{a}_3}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
$$

$$
\mathbf{q}_2 = 2\pi\frac{\mathbf{a}_3 \times \mathbf{a}_1}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
$$

$$
\mathbf{q}_3 = 2\pi\frac{\mathbf{a}_1 \times \mathbf{a}_2}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
$$

These satisfy $\mathbf{a}_i \cdot \mathbf{q}_j = 2\pi\delta_{ij}$.

**General reciprocal lattice vectors:**

$$
\mathbf{Q} = \nu_1\mathbf{q}_1 + \nu_2\mathbf{q}_2 + \nu_3\mathbf{q}_3
$$

**Volume relation:**

$$
V_{\text{recip}} = \frac{(2\pi)^3}{V_{\text{cell}}}
$$

### The Brillouin Zone

The **first Brillouin zone** is the Wigner-Seitz cell of the reciprocal lattice. It defines the fundamental domain in $\mathbf{k}$-space.

**Construction:**
1. Construct the reciprocal lattice
2. Draw lines from origin to nearest neighbors
3. Bisect these lines with planes

---

## Part VI: X-ray Scattering

### Scattering Vector

For incoming wave $\mathbf{k}_0$ and scattered wave $\mathbf{k}$, define:

$$
\mathbf{s} = \mathbf{k} - \mathbf{k}_0
$$

**Phase difference:** For atoms separated by $\mathbf{a}$:

$$
\delta = \mathbf{s} \cdot \mathbf{a}
$$

**Intensity:** For many atoms:

$$
I \propto \left|\sum_{\mathbf{R}} e^{i\mathbf{s}\cdot\mathbf{R}}\right|^2
$$

### Laue Condition

Constructive interference (peaks) occurs when:

$$
\mathbf{s} \cdot \mathbf{a}_i = 2\pi\nu_i \quad \Rightarrow \quad \mathbf{s} = \nu_1\mathbf{q}_1 + \nu_2\mathbf{q}_2 + \nu_3\mathbf{q}_3 = \mathbf{Q}
$$

The scattering vector must equal a reciprocal lattice vector.

### Structure Factor

For a basis with multiple atoms:

$$
C(\mathbf{Q}) = \sum_i e^{i\mathbf{Q}\cdot\mathbf{b}_i}
$$

This can cause certain peaks to vanish.

### Powder Diffraction

For monochromatic X-rays with known $\lambda$:

$$
4\pi\sin\frac{\theta}{2} = \lambda|\mathbf{Q}|
$$

**Miller indices:** The lowest integers giving a reciprocal lattice direction, e.g., $[211]$.

---

## Part VII: General Properties of Bloch Functions

### Fourier Series Representation

Since $u_{n\mathbf{k}}(\mathbf{r})$ is periodic:

$$
u_{n\mathbf{k}}(\mathbf{r}) = \sum_{\mathbf{Q}} C_{n\mathbf{k}}(\mathbf{Q})e^{-i\mathbf{Q}\cdot\mathbf{r}}
$$

The full Bloch function:

$$
\psi_{n\mathbf{k}}(\mathbf{r}) = \frac{1}{\sqrt{V}}\sum_{\mathbf{Q}} C_n(\mathbf{k}-\mathbf{Q})e^{i(\mathbf{k}-\mathbf{Q})\cdot\mathbf{r}}
$$

### Orthogonality Relations

Bloch functions satisfy:

$$
\langle\psi_{n\mathbf{k}}|\psi_{n'\mathbf{k}'}\rangle = \delta_{nn'}\delta_{\mathbf{k}',\mathbf{k}+\mathbf{Q}}
$$

This implies periodicity in $\mathbf{k}$:

$$
\psi_{n,\mathbf{k}+\mathbf{Q}}(\mathbf{r}) = \psi_{n,\mathbf{k}}(\mathbf{r})
$$

### Momentum and Time Reversal

The total momentum carried by an electron:

$$
\langle\psi_{n\mathbf{k}}|\mathbf{p}|\psi_{n\mathbf{k}}\rangle = -i\hbar\int d^3r \, u_{n\mathbf{k}}^*\nabla u_{n\mathbf{k}} + \hbar\mathbf{k}
$$

**Time reversal:** The time-reversed state is $\psi_{n\mathbf{k}}^*(\mathbf{r})$. For non-degenerate bands:

$$
\psi_{n\mathbf{k}}^*(\mathbf{r}) = \psi_{n,-\mathbf{k}}(\mathbf{r})
$$

**Kramers' theorem:**

$$
E_n(-\mathbf{k}) = E_n(\mathbf{k})
$$

### Critical Points

At zone center ($\mathbf{k} = 0$) and zone boundaries ($\mathbf{k} = \mathbf{Q}/2$):

$$
\nabla_{\mathbf{k}}E = 0
$$

This follows from Kramers' theorem and periodicity.

---

## Part VIII: Density of States

### Definition

The number of states in energy range $(E, E+dE)$:

$$
D(E)dE = dE \frac{V}{(2\pi)^3}\int d^3k \, \delta(E(\mathbf{k})-E)
$$

Converting to surface integral:

$$
D(E) = \frac{V}{(2\pi)^3}\int d\sigma_{\mathbf{k}} \frac{1}{|\nabla_{\mathbf{k}}E|}
$$

### Density of States at Critical Points

Near a band minimum or maximum, expand:

$$
E(\mathbf{k}) = E_0 + \frac{1}{2}\sum_{i,j}\frac{\partial^2 E}{\partial k_i \partial k_j}k_ik_j + \cdots
$$

For 3D isotropic bands:

$$
D(E) \propto \sqrt{E - E_0}
$$

**van Hove singularities:** Discontinuities in the first derivative of $D(E)$ at critical points where $\nabla_{\mathbf{k}}E = 0$.

For 1D systems, $D(E)$ itself diverges as $1/|k|$ near band edges.

### Disorder Effects

Disorder smears out band gaps. The density of states becomes:

$$
D(E) = \int dE_g \, D(E-E_g)P(E_g)
$$

where $P(E_g)$ is a Gaussian distribution of local band gaps.

---

## Part IX: Band Structure Calculation Methods

### Tight-Binding Approximation

**Wannier functions:** Localized orbitals centered at lattice sites:

$$
\phi_n(\mathbf{r}-\mathbf{R}) = \frac{\sqrt{N}V_{\text{cell}}}{(2\pi)^3}\int_{\text{BZ}} d^3k \, \psi_{n\mathbf{k}}(\mathbf{r})e^{-i\mathbf{k}\cdot\mathbf{R}}
$$

**Bloch functions in terms of Wannier functions:**

$$
\psi_{n\mathbf{k}}(\mathbf{r}) = \frac{1}{\sqrt{N}}\sum_{\mathbf{R}}\phi_n(\mathbf{r}-\mathbf{R})e^{i\mathbf{k}\cdot\mathbf{R}}
$$

**Single orbital per site:**

$$
E_n(\mathbf{k}) = E_n(0) + 2U_{12}(\cos k_xa + \cos k_ya + \cos k_za)
$$

for a cubic lattice with nearest-neighbor coupling $U_{12}$.

**Graphene (honeycomb lattice):**

With two atoms per unit cell, the eigenvalues are:

$$
E_{\pm}(\mathbf{k}) = E_0 \pm U_{12}\sqrt{3 + 4\cos\frac{\sqrt{3}k_xa}{2}\cos\frac{k_ya}{2} + 2\cos k_ya}
$$

At certain points (K points), the gap vanishes and energy is linear in $k$.

### Nearly Free Electron Approximation

For electrons in nearly free states, expand:

$$
\psi_{n\mathbf{k}}(\mathbf{r}) = \frac{1}{\sqrt{V}}\sum_{\mathbf{Q}}C_n(\mathbf{k}-\mathbf{Q})e^{i(\mathbf{k}-\mathbf{Q})\cdot\mathbf{r}}
$$

The periodic potential:

$$
U(\mathbf{r}) = \sum_{\mathbf{Q}}U(\mathbf{Q})e^{-i\mathbf{Q}\cdot\mathbf{r}}
$$

Near a zone boundary $\mathbf{k} = \mathbf{Q}_0/2$:

$$
E = \frac{\hbar^2}{2m}\left(|\Delta\mathbf{k}|^2 + \frac{Q_0^2}{4}\right) \pm \sqrt{\left(\frac{\hbar^2\mathbf{Q}_0\cdot\Delta\mathbf{k}}{m}\right)^2 + |U(\mathbf{Q}_0)|^2}
$$

An energy gap opens proportional to $|U(\mathbf{Q}_0)|$.

### k·p Theory

Write the Schrödinger equation in terms of cell functions:

$$
\left(\frac{1}{2m}|\mathbf{p} + \hbar\mathbf{k}|^2 + U(\mathbf{r})\right)u_{n\mathbf{k}}(\mathbf{r}) = E_n(\mathbf{k})u_{n\mathbf{k}}(\mathbf{r})
$$

Expand for small $\mathbf{k}$:

$$
(H_0 + H_1 + H_2)u_{n\mathbf{k}} = E_n(\mathbf{k})u_{n\mathbf{k}}
$$

where:
- $H_0 = \frac{p^2}{2m} + U(\mathbf{r})$
- $H_1 = \frac{\hbar}{m}\mathbf{k}\cdot\mathbf{p}$ (first order)
- $H_2 = \frac{\hbar^2k^2}{2m}$ (second order)

**Second-order perturbation theory gives:**

$$
E_n(\mathbf{k}) = E_n(0) + \frac{\hbar^2k^2}{2m} + \frac{\hbar^2}{m^2}\sum_{m\neq n}\frac{|\mathbf{k}\cdot\langle u_{m0}|\mathbf{p}|u_{n0}\rangle|^2}{E_n(0)-E_m(0)}
$$

**Effective mass:**

$$
\frac{1}{m_{\text{eff}}} = \frac{1}{m} + \frac{2}{m^2}\sum_m\frac{|p_{nm}|^2}{E_n(0)-E_m(0)}
$$

Level repulsion from nearby bands reduces the effective mass.

**Oscillator strength:**

$$
f_{nm} = \frac{2|p_{nm}|^2}{m(E_n-E_m)}
$$

connects to optical transition rates.

---

## Part X: ARPES and Experimental Band Mapping

### Angle-Resolved Photoemission Spectroscopy

When photons eject electrons from a crystal:

**Conservation laws:**
1. $\mathbf{k}_{\parallel}$ is conserved (parallel to surface)
2. Energy is conserved

**Measurement:**

For ejected electrons with kinetic energy $E_{\text{kin}}$ at angles $(\theta, \phi)$:

$$
\mathbf{k}_{\parallel} = \sqrt{\frac{2mE_{\text{kin}}}{\hbar^2}}(\sin\theta\cos\phi, \sin\theta\sin\phi)
$$

**Band mapping:**

$$
E_n(\mathbf{k}_{\parallel}) = E_{\text{kin}} - \hbar\omega
$$

ARPES directly measures the band structure for 2D materials.

---

## Summary

| Concept | Key Formula | Physical Meaning |
|---------|-------------|------------------|
| **Bloch theorem** | $\psi_{n\mathbf{k}}(\mathbf{r}) = u_{n\mathbf{k}}(\mathbf{r})e^{i\mathbf{k}\cdot\mathbf{r}}$ | Periodic potential eigenstates |
| **Kronig-Penney** | $P\frac{\sin Ka}{Ka} + \cos Ka = \cos ka$ | Quantization condition |
| **Reciprocal lattice** | $\mathbf{Q}\cdot\mathbf{R} = 2\pi N$ | Fourier transform of lattice |
| **Tight-binding** | $E_n(\mathbf{k}) = E_0 + 2U_{12}\sum_i\cos k_ia$ | Atomic orbital bands |
| **Effective mass** | $\frac{1}{m^*} = \frac{1}{m} + \frac{2}{m^2}\sum_m\frac{|p_{nm}|^2}{E_n-E_m}$ | Renormalized by level repulsion |
| **DOS** | $D(E) \propto \sqrt{E-E_0}$ (3D) | States per unit energy |

---

## References

1. Snoke, D.W. *Solid State Physics: Essential Concepts*, 2nd ed. (Cambridge University Press, 2020). Chapter 1

2. Ashcroft, N.W. & Mermin, N.D. *Solid State Physics* (Brooks Cole, 1976). Chapters 8-9

3. Kittel, C. *Introduction to Solid State Physics*, 8th ed. (Wiley, 2005). Chapters 7-8
