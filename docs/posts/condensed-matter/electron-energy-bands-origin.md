# Electron Energy Bands: From Atomic Orbitals to Bloch States

📅 **Date:** 2026-04-04 | 🏷️ **Tags:** Condensed Matter, Electronic Structure, Band Theory | 📂 **Category:** Condensed Matter Notes

---

## Introduction

The concept of electron energy bands represents a paradigm shift in our understanding of matter. Unlike atomic, nuclear, or particle physics where we typically deal with interactions of just a few particles, solid state physics involves systems with more than $10^{23}$ particles per cubic centimeter. Remarkably, this "infinity" of particles often proves simpler to analyze than systems of just three particles. This note develops the theory of electron bands from first principles, beginning with the fundamental mechanism of energy splitting due to wave function overlap, progressing through exactly solvable models, and culminating in the general framework of Bloch's theorem.

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

When two identical wells are separated by a high or wide barrier, the systems are decoupled. Each well has the same energy eigenvalues, and the states are degenerate. The eigenstate for each well can acquire any overall phase factor without changing physical observables.

**Coupled wells — the emergence of splitting:**

When the barrier between wells is reduced, allowing tunneling, the two wells become **coupled**. We must solve a single Schrödinger equation for the entire system with potential:

$$
U(x) = \begin{cases}
\infty & x < -\frac{b}{2}-a \\
0 & -\frac{b}{2}-a < x < -\frac{b}{2} \\
U_0 & -\frac{b}{2} < x < \frac{b}{2} \\
0 & \frac{b}{2} < x < \frac{b}{2}+a \\
\infty & x > \frac{b}{2}+a
\end{cases}
$$

The wave function is divided into three regions:

$$
\psi(x) = \begin{cases}
\psi_1(x) & -\frac{b}{2}-a < x < -\frac{b}{2} \\
\psi_2(x) & -\frac{b}{2} < x < \frac{b}{2} \\
\psi_3(x) & \frac{b}{2} < x < \frac{b}{2}+a
\end{cases}
$$

**Boundary conditions:**

At the well boundaries:

$$
\psi_1\left(-\frac{b}{2}-a\right) = 0, \quad \psi_3\left(\frac{b}{2}+a\right) = 0
$$

At the interfaces:

$$
\psi_1\left(-\frac{b}{2}\right) = \psi_2\left(-\frac{b}{2}\right), \quad \psi_2\left(\frac{b}{2}\right) = \psi_3\left(\frac{b}{2}\right)
$$

$$
\left.\frac{d\psi_1}{dx}\right|_{-b/2} = \left.\frac{d\psi_2}{dx}\right|_{-b/2}, \quad \left.\frac{d\psi_2}{dx}\right|_{b/2} = \left.\frac{d\psi_3}{dx}\right|_{b/2}
$$

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
E_\text{antisymmetric} > E_\text{symmetric}
$$

**Dependence on coupling strength:**

The energy splitting $\Delta E = E_- - E_+$ increases with stronger coupling:
- As the barrier becomes lower or thinner, tunneling probability increases
- The symmetric wave function within the barrier region becomes more similar to the antisymmetric one when the barrier is high
- Lower barriers allow the symmetric function to remain flatter (longer effective wavelength)

### Extension to N Wells — The Band Formation

**Three coupled wells:**

With three wells, there are three distinct eigenstates formed from linear combinations of the single-well ground states. Considering all combinations of phase factors $\pm 1$:
- $(+++)$ — all in phase (lowest energy)
- $(+--)$, $(-+-)$, $(--+)$ — one node
- $(---)$ — equivalent to $(+++)$ with overall phase factor

After accounting for linear dependence and overall phase equivalence, three independent states remain with distinct energies.

**N coupled wells:**

Starting with $N$ degenerate single-well states and introducing coupling, we obtain $N$ eigenstates with energies distributed across a range. States with more nodes have higher energy; states with fewer nodes have lower energy.

**The infinite limit — continuous bands:**

As $N \to \infty$:

1. The number of states in the energy range becomes very large
2. The spacing between adjacent energy levels becomes infinitesimally small
3. The discrete levels merge into a continuous **energy band**

Between these bands exist **energy gaps** — ranges of energy with no allowed states. These gaps correspond to the energy separations between single-well quantized states.

---

## Part II: The LCAO Approximation

### Linear Combination of Atomic Orbitals

When starting from atomic orbitals rather than square wells, exact calculations become challenging. The **Linear Combination of Atomic Orbitals (LCAO)** approximation provides a practical framework.

**Ansatz:**

$$
|\psi\rangle = c_1|\psi_1\rangle + c_2|\psi_2\rangle
$$

where $|\psi_1\rangle$ and $|\psi_2\rangle$ are atomic orbitals centered on atoms 1 and 2.

**Key quantities:**

- **On-site energies:** $E_1 = \langle\psi_1|H|\psi_1\rangle$, $E_2 = \langle\psi_2|H|\psi_2\rangle$
- **Coupling (hopping) matrix element:** $U_{12} = \langle\psi_1|H|\psi_2\rangle = U_{21}^*$
- **Overlap integral:** $I_{12} = \langle\psi_1|\psi_2\rangle$ (measures non-orthogonality)

### Derivation of the Eigenvalue Equation

The eigenvalue equation $H|\psi\rangle = E|\psi\rangle$ yields:

$$
c_1 E_1 + c_2(U_{12} - EI_{12}) = c_1 E
$$

$$
c_1(U_{12}^* - EI_{12}^*) + c_2 E_2 = c_2 E
$$

In matrix form:

$$
\begin{pmatrix} E_1 & \tilde{U}_{12} \\ \tilde{U}_{12}^* & E_2 \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = E \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}
$$

where $\tilde{U}_{12} = U_{12} - \bar{E}I_{12}$ with $\bar{E} = (E_1 + E_2)/2$.

### Solutions for Identical Atoms

For identical atoms ($E_1 = E_2 = E_0$) with real $\tilde{U}_{12} < 0$:

$$
E = E_0 \pm |\tilde{U}_{12}|
$$

**Bonding state** (lower energy, $E = E_0 - |\tilde{U}_{12}|$):

$$
|\psi_\text{bonding}\rangle = \frac{1}{\sqrt{2(1+I_{12})}}(|\psi_1\rangle + |\psi_2\rangle)
$$

Symmetric combination — electrons accumulate in the bonding region between nuclei.

**Antibonding state** (higher energy, $E = E_0 + |\tilde{U}_{12}|$):

$$
|\psi_\text{antibonding}\rangle = \frac{1}{\sqrt{2(1-I_{12})}}(|\psi_1\rangle - |\psi_2\rangle)
$$

Antisymmetric combination — node between nuclei, reduced electron density in bonding region.

### Physical Interpretation of Band Formation

The coupling parameter $\tilde{U}_{12}$ determines the degree of band formation:

- **Large interatomic spacing:** $\tilde{U}_{12} \approx 0$, discrete atomic energy levels
- **Decreasing spacing:** Increasing $\tilde{U}_{12}$, levels broaden into bands
- **Strong overlap:** Bands widen, gaps may shrink or bands may cross (in 2D/3D)

**Fundamental insight:** The existence of energy bands is **not fundamentally dependent on periodicity**. Amorphous materials, glasses, and alloys can also exhibit bands and band gaps. Periodicity provides sharp, well-defined gaps; disorder produces gaps with fuzzy boundaries.

---

## Part III: The Kronig-Penney Model

### Model Definition

The Kronig-Penney model provides an exactly solvable one-dimensional periodic potential:

$$
U(x) = \begin{cases}
0 & 0 < x < a \quad \text{(well region)} \\
U_0 & -b < x < 0 \quad \text{(barrier region)}
\end{cases}
$$

repeated periodically with period $a + b$.

### Wave Function Ansatz

**In the well region ($0 < x < a$):**

$$
\psi_1(x) = A_1 e^{iKx} + B_1 e^{-iKx}
$$

where $\frac{\hbar^2 K^2}{2m} = E$ (positive energy solution).

**In the barrier region ($-b < x < 0$):**

For $E < U_0$:

$$
\psi_2(x) = A_2 e^{\kappa x} + B_2 e^{-\kappa x}
$$

where $\frac{\hbar^2 \kappa^2}{2m} = U_0 - E$.

**Bloch periodicity condition:**

Due to lattice periodicity, the wave function in adjacent cells differs only by a phase factor:

$$
\psi_3(x) = \psi_2(x - a - b)e^{ik(a+b)}, \quad a < x < a + b
$$

### Boundary Conditions and Derivation

The boundary conditions require continuity of $\psi$ and $d\psi/dx$ at $x = 0$ and $x = a$:

At $x = 0$:

$$
\psi_1(0) = \psi_2(0) \Rightarrow A_1 + B_1 = A_2 + B_2
$$

$$
\left.\frac{d\psi_1}{dx}\right|_0 = \left.\frac{d\psi_2}{dx}\right|_0 \Rightarrow iK(A_1 - B_1) = \kappa(A_2 - B_2)
$$

At $x = a$:

$$
\psi_1(a) = \psi_3(a) = \psi_2(-b)e^{ik(a+b)}
$$

$$
e^{iKa}A_1 + e^{-iKa}B_1 = e^{ik(a+b)}(A_2 e^{-\kappa b} + B_2 e^{\kappa b})
$$

$$
iK(e^{iKa}A_1 - e^{-iKa}B_1) = \kappa e^{ik(a+b)}(A_2 e^{-\kappa b} - B_2 e^{\kappa b})
$$

Setting the determinant of the coefficient matrix to zero yields the **Kronig-Penney equation**:

$$
\frac{\kappa^2 - K^2}{2\kappa K}\sinh(\kappa b)\sin(Ka) + \cosh(\kappa b)\cos(Ka) = \cos(k(a+b))
$$

### Simplified Form: Delta Function Limit

Taking the limit $b \to 0$, $U_0 \to \infty$ with $U_0 b = \text{constant}$:

- $\kappa b \to 0$
- $\kappa^2 b = \text{constant}$

The equation simplifies to:

$$
\boxed{P\frac{\sin(Ka)}{Ka} + \cos(Ka) = \cos(ka)}
$$

where $P = \frac{mU_0ba}{\hbar^2}$ is a dimensionless parameter measuring barrier strength.

### Key Features of the Solution

**1. Band gaps at zone boundaries:**

The equation has solutions only when the left-hand side falls within $[-1, 1]$. This occurs in allowed bands separated by forbidden gaps.

At $ka = n\pi$ (zone boundaries), $\cos(ka) = \pm 1$, and the condition for solutions becomes restrictive.

**2. Vanishing derivative at zone boundaries:**

Implicit differentiation shows:

$$
\frac{dE}{dk} \propto \sin(ka) = 0 \quad \text{at} \quad ka = n\pi
$$

This corresponds to zero group velocity — standing waves form due to Bragg reflection.

**3. Physical interpretation of gaps:**

The periodic interfaces act as a **Bragg reflector**. Waves with wavelength $\lambda = 2a/n$ experience constructive interference of reflected waves, creating standing waves with zero group velocity.

**4. Weak and strong coupling limits:**

*Strong barriers ($P \to \infty$):*

The equation reduces to $\sin(Ka) = 0$, giving $Ka = n\pi$ or $E_n = \frac{\hbar^2 \pi^2 n^2}{2ma^2}$. These are the isolated well energies — narrow bands, wide gaps.

*Weak barriers ($P \to 0$):*

The equation becomes $\cos(Ka) = \cos(ka)$, so $K = k$ and $E = \frac{\hbar^2 k^2}{2m}$. Free particle dispersion — bands merge, no gaps.

---

## Part IV: Bloch's Theorem

### Statement of the Theorem

**Bloch's Theorem:** For a periodic potential satisfying $U(\mathbf{r} + \mathbf{R}) = U(\mathbf{r})$ for all lattice vectors $\mathbf{R}$, the eigenstates of the Hamiltonian take the form:

$$
\psi_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}) = \psi_{n\mathbf{k}}(\mathbf{r})e^{i\mathbf{k} \cdot \mathbf{R}}
$$

Equivalently, the wave functions can be written as:

$$
\boxed{\psi_{n\mathbf{k}}(\mathbf{r}) = \frac{1}{\sqrt{V}}u_{n\mathbf{k}}(\mathbf{r})e^{i\mathbf{k} \cdot \mathbf{r}}}
$$

where $u_{n\mathbf{k}}(\mathbf{r})$ has the same periodicity as the lattice: $u_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}) = u_{n\mathbf{k}}(\mathbf{r})$.

Here $n$ is the **band index** and $\mathbf{k}$ is the crystal momentum confined to the first Brillouin zone.

### Proof via Translation Operators

**Step 1: Define the translation operator**

Let $T_{\mathbf{R}}$ be the operator that translates the wave function by lattice vector $\mathbf{R}$:

$$
T_{\mathbf{R}}\psi(\mathbf{r}) = \psi(\mathbf{r} + \mathbf{R})
$$

**Step 2: Show commutation with the Hamiltonian**

For a periodic potential:

$$
T_{\mathbf{R}}[U(\mathbf{r})\psi(\mathbf{r})] = U(\mathbf{r} + \mathbf{R})\psi(\mathbf{r} + \mathbf{R}) = U(\mathbf{r})T_{\mathbf{R}}\psi(\mathbf{r})
$$

The kinetic energy operator also commutes with translations since $\nabla^2$ is translationally invariant.

Therefore: $[T_{\mathbf{R}}, H] = 0$.

**Step 3: Simultaneous eigenstates**

Since commuting operators have common eigenstates, the eigenstates of $H$ are also eigenstates of $T_{\mathbf{R}}$:

$$
T_{\mathbf{R}}\psi(\mathbf{r}) = C_{\mathbf{R}}\psi(\mathbf{r})
$$

**Step 4: Determine the eigenvalues**

Two successive translations:

$$
T_{\mathbf{R} + \mathbf{R}'}\psi = T_{\mathbf{R}}T_{\mathbf{R}'\psi = C_{\mathbf{R}}C_{\mathbf{R}'\psi
$$

But also: $T_{\mathbf{R} + \mathbf{R}'\psi = C_{\mathbf{R} + \mathbf{R}'\psi$

Therefore: $C_{\mathbf{R} + \mathbf{R}'} = C_{\mathbf{R}}C_{\mathbf{R}'}$

**Step 5: Normalization constraint**

From wave function normalization:

$$
\int d^3r \, |\psi(\mathbf{r})|^2 = \int d^3r \, |\psi(\mathbf{r} + \mathbf{R})|^2 = |C_{\mathbf{R}}|^2 \int d^3r \, |\psi(\mathbf{r})|^2
$$

Therefore: $|C_{\mathbf{R}}|^2 = 1$, implying $C_{\mathbf{R}} = e^{i\phi_{\mathbf{R}}}$ for some real phase $\phi_{\mathbf{R}}$.

**Step 6: Identification with crystal momentum**

The multiplicative property $C_{\mathbf{R} + \mathbf{R}'} = C_{\mathbf{R}}C_{\mathbf{R}'}$ with $|C_{\mathbf{R}}| = 1$ is satisfied by:

$$
C_{\mathbf{R}} = e^{i\mathbf{k} \cdot \mathbf{R}}
$$

for some vector $\mathbf{k}$. Thus:

$$
\psi(\mathbf{r} + \mathbf{R}) = e^{i\mathbf{k} \cdot \mathbf{R}}\psi(\mathbf{r})
$$

### Consequences of Bloch's Theorem

**1. Reduced zone scheme:**

Due to the periodicity $e^{i(\mathbf{k} + \mathbf{G}) \cdot \mathbf{R}} = e^{i\mathbf{k} \cdot \mathbf{R}}$ for reciprocal lattice vectors $\mathbf{G}$, all physically distinct states are contained within the first Brillouin zone.

**2. Band structure:**

For each $\mathbf{k}$ in the Brillouin zone, there are multiple solutions labeled by band index $n$, creating the **band structure** $E_n(\mathbf{k})$.

**3. Crystal momentum:**

While $\hbar\mathbf{k}$ is not the physical momentum (the state is not a momentum eigenstate), it behaves similarly under translations and is conserved in periodic potentials.

**4. Group velocity:**

The velocity of a wave packet centered at $\mathbf{k}$ in band $n$ is:

$$
\mathbf{v}_n(\mathbf{k}) = \frac{1}{\hbar}\nabla_{\mathbf{k}}E_n(\mathbf{k})
$$

**5. Effective mass:**

Near band extrema, the dispersion can be approximated as quadratic:

$$
E_n(\mathbf{k}) \approx E_0 + \frac{\hbar^2}{2}\sum_{i,j}k_i\left(\frac{1}{m^*}\right)_{ij}k_j
$$

defining the effective mass tensor.

---

## Summary

| Concept | Physical Meaning | Mathematical Expression |
|---------|-----------------|------------------------|
| **Energy splitting** | Coupling lifts degeneracy | $\Delta E \propto \tilde{U}_{12}$ |
| **Bonding/Antibonding** | Symmetric/antisymmetric combinations | $|\psi_\pm\rangle = \frac{1}{\sqrt{2}}(|\psi_1\rangle \pm |\psi_2\rangle)$ |
| **Kronig-Penney eq.** | Quantization condition | $P\frac{\sin Ka}{Ka} + \cos Ka = \cos ka$ |
| **Bloch theorem** | Periodic potential eigenstates | $\psi_{n\mathbf{k}}(\mathbf{r}) = u_{n\mathbf{k}}(\mathbf{r})e^{i\mathbf{k}\cdot\mathbf{r}}$ |
| **Crystal momentum** | Conserved quantity in lattice | $\mathbf{k}$ (modulo reciprocal lattice vectors) |

---

## References

1. Snoke, D.W. *Solid State Physics: Essential Concepts*, 2nd ed. (Cambridge University Press, 2020). Chapter 1

2. Ashcroft, N.W. & Mermin, N.D. *Solid State Physics* (Brooks Cole, 1976). Chapters 8-9

3. Kittel, C. *Introduction to Solid State Physics*, 8th ed. (Wiley, 2005). Chapters 7-8
