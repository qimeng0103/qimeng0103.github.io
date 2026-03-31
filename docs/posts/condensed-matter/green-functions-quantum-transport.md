# Green's Functions in Condensed Matter: From Equilibrium to Non-Equilibrium Quantum Transport

📅 **Date:** 2026-03-31 | 🏷️ **Tags:** Condensed Matter, Quantum Transport, Many-Body Physics | 📂 **Category:** Condensed Matter Notes

---

## Introduction

Green's functions provide the unifying language for quantum many-body physics. They encode:
- **Single-particle propagation** in disordered potentials
- **Spectral properties** (density of states, band structure)
- **Response functions** (conductivity, susceptibility)
- **Non-equilibrium dynamics** (quantum transport, relaxation)

This note develops Green's functions from quantum mechanical foundations through equilibrium many-body theory to non-equilibrium quantum transport, with the minimal formalism needed for practical calculations.

---

## Part I: Single-Particle Green's Functions

### Definition and Physical Meaning

Consider a single-particle quantum system with Hamiltonian $\hat{H} = \hat{H}_0 + \hat{V}$. The **time-ordered Green's function** is:

$$
G(\mathbf{r}, t; \mathbf{r}', t') = -i\langle T \psi(\mathbf{r}, t) \psi^\dagger(\mathbf{r}', t') \rangle
$$

where $T$ is the time-ordering operator, $\psi(\mathbf{r}, t) = e^{i\hat{H}t}\psi(\mathbf{r})e^{-i\hat{H}t}$ in Heisenberg picture, and the bracket denotes ground state expectation (zero temperature) or thermal average (finite temperature).

**Physical interpretation:**
- $G$ describes the amplitude for a particle created at $(\mathbf{r}', t')$ to propagate to $(\mathbf{r}, t)$
- For $t > t'$: particle propagation; for $t < t'$: hole propagation
- The spectral information (poles of $G$) gives excitation energies and lifetimes

### Free Particle Green's Function

For $\hat{H}_0 = -\hbar^2\nabla^2/2m$ (free particle), in momentum-frequency space:

$$
G_0(\mathbf{k}, \omega) = \frac{1}{\omega - \varepsilon_k + i\eta}
$$

with $\varepsilon_k = \hbar^2 k^2/2m$ and $\eta \to 0^+$.

The imaginary part gives the spectral function:

$$
A_0(\mathbf{k}, \omega) = -\frac{1}{\pi}\text{Im}\,G_0(\mathbf{k}, \omega) = \delta(\omega - \varepsilon_k)
$$

This shows the free particle has well-defined energy $\varepsilon_k$ (infinite lifetime, delta function peak).

### Retarded and Advanced Green's Functions

For response theory, we need **causal** Green's functions:

$$
G^R(\mathbf{r}, t; \mathbf{r}', t') = -i\theta(t - t')\langle \{\psi(\mathbf{r}, t), \psi^\dagger(\mathbf{r}', t')\} \rangle
$$

$$
G^A(\mathbf{r}, t; \mathbf{r}', t') = +i\theta(t' - t)\langle \{\psi(\mathbf{r}, t), \psi^\dagger(\mathbf{r}', t')\} \rangle
$$

where $\{\cdot, \cdot\}$ is the anticommutator for fermions.

In frequency space:

$$
G^{R/A}(\mathbf{k}, \omega) = \frac{1}{\omega - \varepsilon_k \pm i\eta}
$$

The retarded function $G^R$ has poles in the lower half-plane, ensuring causality (response follows perturbation).

### Connection to Density of States

The **local density of states** (LDOS) is directly related to the retarded Green's function:

$$
\rho(\mathbf{r}, \omega) = -\frac{1}{\pi}\text{Im}\,G^R(\mathbf{r}, \mathbf{r}, \omega) = \sum_n |\phi_n(\mathbf{r})|^2 \delta(\omega - E_n)
$$

where $\phi_n$ are eigenstates of $\hat{H}$ with energies $E_n$.

For homogeneous systems, the **density of states** per unit volume:

$$
\nu(\omega) = -\frac{1}{\pi}\int \frac{d^d k}{(2\pi)^d} \text{Im}\,G^R(\mathbf{k}, \omega)
$$

In $d$ dimensions for free electrons: $\nu(\omega) \propto \omega^{d/2 - 1}$.

---

## Part II: Finite Temperature and Statistical Mechanics

### Imaginary Time (Matsubara) Formalism

At finite temperature $T = 1/(k_B \beta)$, the time evolution operator $e^{-i\hat{H}t}$ becomes problematic due to thermal fluctuations. The **imaginary time formalism** defines:

$$
\tau = it \in [0, \beta\hbar]
$$

The **Matsubara Green's function**:

$$
\mathcal{G}(\mathbf{r}, \tau; \mathbf{r}', \tau') = -\langle T_\tau \psi(\mathbf{r}, \tau) \psi^\dagger(\mathbf{r}', \tau') \rangle
$$

where $T_\tau$ orders in imaginary time, and $\psi(\mathbf{r}, \tau) = e^{\hat{H}\tau}\psi(\mathbf{r})e^{-\hat{H}\tau}$.

**Key property:** $\mathcal{G}$ is periodic (bosons) or antiperiodic (fermions) with period $\beta\hbar$:

$$
\mathcal{G}(\tau + \beta\hbar) = -\mathcal{G}(\tau) \quad \text{(fermions)}
$$

### Matsubara Frequencies

Due to periodicity, Fourier transform yields **discrete frequencies**:

$$
\mathcal{G}(i\omega_n) = \int_0^{\beta\hbar} d\tau \, e^{i\omega_n \tau} \mathcal{G}(\tau)
$$

with $\omega_n = (2n+1)\pi/\beta\hbar$ for fermions and $\omega_n = 2n\pi/\beta\hbar$ for bosons.

For free fermions:

$$
\mathcal{G}_0(\mathbf{k}, i\omega_n) = \frac{1}{i\omega_n - \varepsilon_k + \mu}
$$

where $\mu$ is the chemical potential.

### Analytic Continuation

Physical retarded Green's functions are obtained by analytic continuation:

$$
G^R(\mathbf{k}, \omega) = \mathcal{G}(\mathbf{k}, i\omega_n \to \omega + i\eta)
$$

This prescription connects equilibrium statistical mechanics to real-time response.

### Spectral Representation

The Matsubara Green's function has spectral representation:

$$
\mathcal{G}(\mathbf{k}, i\omega_n) = \int_{-\infty}^{\infty} \frac{d\omega'}{2\pi} \frac{A(\mathbf{k}, \omega')}{i\omega_n - \omega'}
$$

where $A(\mathbf{k}, \omega) = -2\text{Im}\,G^R(\mathbf{k}, \omega)$ is the **spectral function** satisfying:

$$
\int \frac{d\omega}{2\pi} A(\mathbf{k}, \omega) = 1
$$

For non-interacting systems: $A(\mathbf{k}, \omega) = 2\pi\delta(\omega - \varepsilon_k)$. Interactions broaden this into a Lorentzian (or more complex shape) with width related to inverse lifetime.

---

## Part III: Many-Body Green's Functions and Field Theory

### Second Quantization Language

For many-fermion systems, we use field operators satisfying:

$$
\{\psi(\mathbf{r}), \psi^\dagger(\mathbf{r}')\} = \delta(\mathbf{r} - \mathbf{r}'), \quad \{\psi(\mathbf{r}), \psi(\mathbf{r}')\} = 0
$$

The Hamiltonian for interacting electrons:

$$
\hat{H} = \sum_\sigma \int d^3r \, \psi^\dagger_\sigma(\mathbf{r})\left(-\frac{\hbar^2\nabla^2}{2m} + V_{\text{ext}}(\mathbf{r})\right)\psi_\sigma(\mathbf{r}) + \frac{1}{2}\sum_{\sigma,\sigma'} \int d^3r d^3r' \, \psi^\dagger_\sigma(\mathbf{r})\psi^\dagger_{\sigma'}(\mathbf{r}')V(\mathbf{r} - \mathbf{r}')\psi_{\sigma'}(\mathbf{r}')\psi_\sigma(\mathbf{r})
$$

### The Interacting Green's Function

The **interacting single-particle Green's function**:

$$
G_{\sigma\sigma'}(\mathbf{r}, t; \mathbf{r}', t') = -i\langle T \psi_\sigma(\mathbf{r}, t) \psi^\dagger_{\sigma'}(\mathbf{r}', t') \rangle
$$

encodes the full many-body effects. It no longer describes single-particle eigenstates but **quasiparticles**—dressed excitations with renormalized mass, lifetime, and spectral weight.

### Dyson Equation

The Green's function satisfies the **Dyson equation**:

$$
G = G_0 + G_0 \Sigma G
$$

or in matrix form:

$$
G^{-1} = G_0^{-1} - \Sigma
$$

where $\Sigma$ is the **self-energy**, containing all interaction effects. In frequency-momentum space:

$$
G(\mathbf{k}, \omega) = \frac{1}{\omega - \varepsilon_k - \Sigma(\mathbf{k}, \omega)}
$$

**Physical content of self-energy:**

Writing $\Sigma = \text{Re}\Sigma + i\text{Im}\Sigma$:
- $\text{Re}\Sigma$: energy shift (effective mass renormalization)
- $\text{Im}\Sigma$: damping (inverse lifetime $\hbar/\tau_k = -2\text{Im}\Sigma$)

For weak interactions near the Fermi surface, the quasiparticle energy and lifetime are:

$$
E_k = \varepsilon_k + \text{Re}\Sigma(\mathbf{k}, E_k), \quad \frac{\hbar}{\tau_k} = -2\text{Im}\Sigma(\mathbf{k}, E_k)
$$

### Diagrammatic Expansion

The self-energy has a perturbative expansion in the interaction $V$:

$$
\Sigma = \Sigma^{(1)} + \Sigma^{(2)} + \cdots
$$

The **Hartree-Fock approximation** (first order):

$$
\Sigma_{\text{HF}}(\mathbf{r}, \mathbf{r}') = \delta(\mathbf{r} - \mathbf{r}')\int d^3r'' \, V(\mathbf{r} - \mathbf{r}'')\langle n(\mathbf{r}'')\rangle - V(\mathbf{r} - \mathbf{r}')\langle \psi(\mathbf{r})\psi^\dagger(\mathbf{r}')\rangle
$$

gives the mean-field potential plus exchange (Fock) term.

Higher-order diagrams describe correlations: screening, collective modes, etc.

---

## Part IV: Non-Equilibrium Green's Functions

### The Problem

Quantum transport involves systems out of thermal equilibrium: two reservoirs at different chemical potentials connected by a scattering region. The standard equilibrium formalism fails because:
- No global chemical potential $\mu$
- Stationary state carries finite current
- Perturbation theory in interaction must respect non-equilibrium boundary conditions

### Keldysh Contour

The **Keldysh technique** extends the time contour from $-\infty$ to $+\infty$ and back. The contour-ordered Green's function:

$$
G(\tau, \tau') = -i\langle T_C \psi(\tau)\psi^\dagger(\tau')\rangle
$$

where $T_C$ orders along the Keldysh contour $C$.

Decomposing into real-time components yields four Green's functions:

$$
G^<(t, t') = +i\langle \psi^\dagger(t')\psi(t)\rangle \quad \text{(particle/hole correlation)}
$$

$$
G^>(t, t') = -i\langle \psi(t)\psi^\dagger(t')\rangle \quad \text{(hole/particle correlation)}
$$

$$
G^T(t, t') = -i\langle T \psi(t)\psi^\dagger(t')\rangle \quad \text{(time-ordered)}
$$

$$
G^{\bar{T}}(t, t') = -i\langle \bar{T} \psi(t)\psi^\dagger(t')\rangle \quad \text{(anti-time-ordered)}
$$

Only three are independent: $G^T + G^{\bar{T}} = G^< + G^>$.

### Retarded, Advanced, and Keldysh Components

The **retarded** and **advanced** Green's functions retain their definition:

$$
G^R = G^T - G^< = G^> - G^{\bar{T}} = -i\theta(t-t')\langle\{\psi(t), \psi^\dagger(t')\}\rangle
$$

$$
G^A = G^T - G^> = G^< - G^{\bar{T}} = +i\theta(t'-t)\langle\{\psi(t), \psi^\dagger(t')\}\rangle
$$

The **Keldysh** (or correlation) Green's function:

$$
G^K = G^> + G^< = G^T + G^{\bar{T}}
$$

contains distribution information.

### The Keldysh Dyson Equation

In matrix form on the Keldysh contour:

$$
\begin{pmatrix} G^R & G^K \\ 0 & G^A \end{pmatrix} = \begin{pmatrix} G_0^R & G_0^K \\ 0 & G_0^A \end{pmatrix} + \begin{pmatrix} G_0^R & G_0^K \\ 0 & G_0^A \end{pmatrix} \begin{pmatrix} \Sigma^R & \Sigma^K \\ 0 & \Sigma^A \end{pmatrix} \begin{pmatrix} G^R & G^K \\ 0 & G^A \end{pmatrix}
$$

This gives three coupled equations:
1. $G^R = G_0^R + G_0^R \Sigma^R G^R$ (retarded Dyson, same as equilibrium)
2. $G^A = G_0^A + G_0^A \Sigma^A G^A$ (advanced Dyson)
3. $G^K = (1 + G^R \Sigma^R)G_0^K(1 + \Sigma^A G^A) + G^R \Sigma^K G^A$

The third equation couples distribution ($G^K$) to spectral properties ($G^R$, $G^A$).

### Physical Observables from $G^<$

The **lesser** Green's function $G^<(t, t')$ is central because:

$$
G^<(t, t) = i\langle \psi^\dagger(t)\psi(t)\rangle = i n(t)
$$

gives the **density**. The current is:

$$
\mathbf{J}(\mathbf{r}, t) = \frac{\hbar}{2m}\left(\nabla' - \nabla\right)_{\mathbf{r}' \to \mathbf{r}} G^<(\mathbf{r}, t; \mathbf{r}', t)
$$

For stationary transport, we need $G^<(\omega)$ in frequency space.

---

## Part V: Application to Quantum Transport

### Landauer-Buttiker from Green's Functions

Consider a conductor connected to left (L) and right (R) reservoirs with chemical potentials $\mu_L$ and $\mu_R$. The current can be expressed via the transmission function:

$$
I = \frac{e}{h}\int d\omega \, T(\omega)[f_L(\omega) - f_R(\omega)]
$$

where $f_{L/R}$ are Fermi functions.

The transmission $T(\omega)$ is related to the retarded Green's function of the central region and the **self-energies** $\Sigma_{L,R}$ from coupling to leads:

$$
T(\omega) = \text{Tr}[\Gamma_L G^R \Gamma_R G^A]
$$

with $\Gamma_{L/R} = i(\Sigma_{L/R} - \Sigma_{L/R}^\dagger)$ (linewidth functions).

### Meir-Wingreen Formula

For interacting systems, the current through a quantum dot or molecular junction is:

$$
I = \frac{ie}{2h}\int d\omega \, \text{Tr}\left[\Gamma_L\left(G^< + 2if_L\text{Im}\,G^R\right)\right] + (L \leftrightarrow R)
$$

This general form reduces to Landauer-Buttiker for non-interacting systems.

### Kadanoff-Baym Equations

For time-dependent non-equilibrium situations, the **Kadanoff-Baym equations** govern the evolution:

$$
\left[i\hbar\frac{\partial}{\partial t} - h(t)\right]G^\lessgtr(t, t') = \int d\bar{t}\left[\Sigma^R(t, \bar{t})G^\lessgtr(\bar{t}, t') + \Sigma^\lessgtr(t, \bar{t})G^A(\bar{t}, t')\right]
$$

These integro-differential equations describe the full quantum kinetic evolution, including memory effects and collisions. In the Markovian limit, they reduce to quantum Boltzmann equations.

---

## Summary: Hierarchy of Green's Functions

| Level | Green's Function | Physical Information | Key Equation |
|-------|-----------------|---------------------|--------------|
| Single-particle ($T=0$) | $G^R$, $G^A$ | Eigenstates, LDOS | $(\omega - \hat{H})G^R = 1$ |
| Equilibrium ($T>0$) | $\mathcal{G}(i\omega_n)$ | Thermal occupation, excitations | Dyson equation with Matsubara frequencies |
| Interacting | $G$, $\Sigma$ | Quasiparticles, lifetime | $G^{-1} = G_0^{-1} - \Sigma$ |
| Non-equilibrium | $G^<$, $G^>$, $G^K$ | Distribution, current | Keldysh Dyson equation |

The progression is: solve for spectral properties ($G^R$, $G^A$) $\to$ determine distribution ($G^<$, $G^K$) $\to$ calculate observables (current, density).

---

## References

1. Mahan, G.D. *Many-Particle Physics*, 3rd ed. (Springer, 2000). Chapters 2–3 (Green's Functions)

2. Bruus, H. & Flensberg, K. *Many-Body Quantum Theory in Condensed Matter Physics* (Oxford, 2004). Chapters 7–8 (Non-equilibrium)

3. Haug, H. & Jauho, A.-P. *Quantum Kinetics in Transport and Optics of Semiconductors* (Springer, 2008). Chapters 4–5 (Keldysh formalism)

4. Datta, S. *Electronic Transport in Mesoscopic Systems* (Cambridge, 1995). Chapter 2 (Scattering and Green's functions)

5. Rammer, J. *Quantum Field Theory of Non-equilibrium States* (Cambridge, 2007). Chapters 4–5 (Real-time formalism)
