# Green's Functions in Condensed Matter: From Quantum Mechanics to Quantum Transport

📅 **Date:** 2026-03-31 | 🏷️ **Tags:** Condensed Matter, Quantum Transport, Many-Body Physics | 📂 **Category:** Condensed Matter Notes

---

## Introduction

This note develops Green's functions from elementary quantum mechanics, assuming familiarity with the Schrödinger equation, eigenstates, and Dirac notation, but **no prior knowledge of statistical mechanics or condensed matter physics**. Every concept is derived explicitly.

---

## Part I: The Single-Particle Propagator

### Motivation: Why Propagators?

In single-particle quantum mechanics, the time evolution of a state is governed by the Schrödinger equation:

$$
i\hbar \frac{\partial}{\partial t}\vert\psi(t)\rangle = \hat{H}\vert\psi(t)\rangle
$$

For a time-independent Hamiltonian, the formal solution is:

$$
\vert\psi(t)\rangle = e^{-i\hat{H}(t-t_0)/\hbar}\vert\psi(t_0)\rangle = \hat{U}(t, t_0)\vert\psi(t_0)\rangle
$$

where $\hat{U}(t, t_0) = e^{-i\hat{H}(t-t_0)/\hbar}$ is the **time evolution operator**.

The **propagator** (or Green's function) is the position-space matrix element of this operator:

$$
G(\mathbf{r}, t; \mathbf{r}', t') \equiv \langle\mathbf{r}\vert\hat{U}(t, t')\vert\mathbf{r}'\rangle = \langle\mathbf{r}\vert e^{-i\hat{H}(t-t')/\hbar}\vert\mathbf{r}'\rangle
$$

**Physical meaning:** $G(\mathbf{r}, t; \mathbf{r}', t')$ is the probability amplitude for a particle starting at position $\mathbf{r}'$ at time $t'$ to be found at position $\mathbf{r}$ at time $t$.

### Evolution of Wavefunctions

Given an initial wavefunction $\psi(\mathbf{r}', t') = \langle\mathbf{r}'\vert\psi(t')\rangle$, the wavefunction at later time is:

$$
\psi(\mathbf{r}, t) = \int d^3r' \, G(\mathbf{r}, t; \mathbf{r}', t') \psi(\mathbf{r}', t')
$$

**Proof:** Insert complete set $\int d^3r' \vert\mathbf{r}'\rangle\langle\mathbf{r}'\vert = \hat{\mathbb{1}}$:

$$
\psi(\mathbf{r}, t) = \langle\mathbf{r}\vert\psi(t)\rangle = \langle\mathbf{r}\vert\hat{U}(t, t')\vert\psi(t')\rangle = \int d^3r' \langle\mathbf{r}\vert\hat{U}(t, t')\vert\mathbf{r}'\rangle\langle\mathbf{r}'\vert\psi(t')\rangle
$$

### The Free Particle Propagator

For a free particle: $\hat{H}_0 = \frac{\hat{\mathbf{p}}^2}{2m} = -\frac{\hbar^2}{2m}\nabla^2$

The eigenstates are plane waves $\vert\mathbf{k}\rangle$ with $\langle\mathbf{r}\vert\mathbf{k}\rangle = \frac{1}{\sqrt{V}}e^{i\mathbf{k}\cdot\mathbf{r}}$ and eigenvalues $E_k = \frac{\hbar^2 k^2}{2m}$.

Insert two complete sets $\sum_\mathbf{k}\vert\mathbf{k}\rangle\langle\mathbf{k}\vert = \hat{\mathbb{1}}$:

$$
G_0(\mathbf{r}, t; \mathbf{r}', t') = \sum_{\mathbf{k},\mathbf{k}'} \langle\mathbf{r}\vert\mathbf{k}\rangle\langle\mathbf{k}\vert e^{-i\hat{H}_0(t-t')/\hbar}\vert\mathbf{k}'\rangle\langle\mathbf{k}'\vert\mathbf{r}'\rangle
$$

Since $\hat{H}_0\vert\mathbf{k}'\rangle = E_{k'}\vert\mathbf{k}'\rangle$:

$$
\langle\mathbf{k}\vert e^{-i\hat{H}_0(t-t')/\hbar}\vert\mathbf{k}'\rangle = e^{-iE_{k'}(t-t')/\hbar}\delta_{\mathbf{k}\mathbf{k}'}
$$

Thus:

$$
G_0(\mathbf{r}, t; \mathbf{r}', t') = \frac{1}{V}\sum_\mathbf{k} e^{i\mathbf{k}\cdot(\mathbf{r}-\mathbf{r}')} e^{-iE_k(t-t')/\hbar}
$$

Taking the continuum limit $\frac{1}{V}\sum_\mathbf{k} \to \int \frac{d^3k}{(2\pi)^3}$:

$$
G_0(\mathbf{r}, t; \mathbf{r}', t') = \int \frac{d^3k}{(2\pi)^3} \exp\left[i\mathbf{k}\cdot(\mathbf{r}-\mathbf{r}') - i\frac{\hbar k^2}{2m}(t-t')\right]
$$

This is a Gaussian integral. Completing the square in the exponent:

Let $\mathbf{q} = \mathbf{k} - \frac{m(\mathbf{r}-\mathbf{r}')}{\hbar(t-t')}$, then:

$$
G_0(\mathbf{r}, t; \mathbf{r}', t') = \left(\frac{m}{2\pi i \hbar(t-t')}\right)^{3/2} \exp\left(\frac{im(\mathbf{r}-\mathbf{r}')^2}{2\hbar(t-t')}\right)
$$

This is the free particle propagator. Note the phase factor and the spreading with time $\sim (t-t')^{-3/2}$.

### The Differential Equation for G

From the definition $G(\mathbf{r}, t; \mathbf{r}', t') = \langle\mathbf{r}\vert e^{-i\hat{H}(t-t')/\hbar}\vert\mathbf{r}'\rangle$, differentiate with respect to $t$:

$$
i\hbar \frac{\partial}{\partial t}G = \langle\mathbf{r}\vert\hat{H}e^{-i\hat{H}(t-t')/\hbar}\vert\mathbf{r}'\rangle = \langle\mathbf{r}\vert\hat{H}\vert\mathbf{r}'\rangle_{\text{matrix element}}
$$

For $\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})$:

$$
\langle\mathbf{r}\vert\hat{H}\vert\mathbf{r}'\rangle = \left(-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})\right)\delta(\mathbf{r}-\mathbf{r}')
$$

Therefore:

$$
\boxed{\left(i\hbar \frac{\partial}{\partial t} + \frac{\hbar^2}{2m}\nabla^2 - V(\mathbf{r})\right)G(\mathbf{r}, t; \mathbf{r}', t') = \hbar\delta(\mathbf{r}-\mathbf{r}')\delta(t-t')}
$$

This shows $G$ is the Green's function for the Schrödinger operator, with a delta-function source.

---

## Part II: From Quantum Mechanics to Statistical Mechanics

### The Problem: $N \sim 10^{23}$ Particles

Condensed matter systems contain macroscopic numbers of particles. Tracking each particle's wavefunction is impossible. We need a statistical description.

**Key insight:** Even for a single particle at finite temperature, we don't know the exact quantum state—the system is in a **mixed state** described by probabilities.

### The Density Matrix: Definition

A **pure state** is described by a state vector $\vert\psi\rangle$. Expectation values are $\langle\hat{A}\rangle = \langle\psi\vert\hat{A}\vert\psi\rangle$.

A **mixed state** is a statistical ensemble: the system is in state $\vert\psi_i\rangle$ with probability $p_i$, where $\sum_i p_i = 1$.

The expectation value of an observable is the weighted average:

$$
\langle\hat{A}\rangle = \sum_i p_i \langle\psi_i\vert\hat{A}\vert\psi_i\rangle
$$

Define the **density operator** (density matrix):

$$
\hat{\rho} \equiv \sum_i p_i \vert\psi_i\rangle\langle\psi_i\vert
$$

Then:

$$
\langle\hat{A}\rangle = \sum_i p_i \langle\psi_i\vert\hat{A}\vert\psi_i\rangle = \sum_i p_i \text{Tr}(\vert\psi_i\rangle\langle\psi_i\vert\hat{A}) = \text{Tr}(\hat{\rho}\hat{A})
$$

**Proof of the cyclic property used above:**

For any states $\vert\alpha\rangle$, $\vert\beta\rangle$ and operator $\hat{A}$:

$$
\langle\alpha\vert\hat{A}\vert\beta\rangle = \sum_n \langle\alpha\vert\hat{A}\vert n\rangle\langle n\vert\beta\rangle = \sum_n \langle n\vert\beta\rangle\langle\alpha\vert\hat{A}\vert n\rangle = \text{Tr}(\vert\beta\rangle\langle\alpha\vert\hat{A})
$$

### Properties of the Density Matrix

1. **Hermiticity:** $\hat{\rho}^\dagger = \hat{\rho}$ (since $p_i$ are real)

2. **Normalization:** $\text{Tr}(\hat{\rho}) = 1$ (probabilities sum to 1)

3. **Positivity:** $\langle\phi\vert\hat{\rho}\vert\phi\rangle \geq 0$ for all $\vert\phi\rangle$

4. **Pure vs. Mixed:**
   - Pure state: $\hat{\rho} = \vert\psi\rangle\langle\psi\vert$, so $\hat{\rho}^2 = \hat{\rho}$ and $\text{Tr}(\hat{\rho}^2) = 1$
   - Mixed state: $\text{Tr}(\hat{\rho}^2) < 1$

### Thermal Equilibrium: The Canonical Ensemble

For a system at temperature $T$ in contact with a heat bath, the probability of being in eigenstate $\vert n\rangle$ with energy $E_n$ follows the **Boltzmann distribution**:

$$
p_n = \frac{e^{-\beta E_n}}{\mathcal{Z}}, \quad \beta = \frac{1}{k_B T}
$$

where $\mathcal{Z}$ is the **partition function** ensuring normalization:

$$
\mathcal{Z} = \sum_n e^{-\beta E_n} = \text{Tr}(e^{-\beta\hat{H}})
$$

The **canonical density matrix** is:

$$
\hat{\rho} = \frac{e^{-\beta\hat{H}}}{\mathcal{Z}} = \frac{e^{-\beta\hat{H}}}{\text{Tr}(e^{-\beta\hat{H}})}
$$

### Time Evolution of the Density Matrix

From the Schrödinger equation $i\hbar \frac{d}{dt}\vert\psi_i(t)\rangle = \hat{H}\vert\psi_i(t)\rangle$:

$$
i\hbar \frac{d}{dt}\hat{\rho}(t) = \sum_i p_i \left(i\hbar \frac{d}{dt}\vert\psi_i\rangle\right)\langle\psi_i\vert + \sum_i p_i \vert\psi_i\rangle\left(i\hbar \frac{d}{dt}\langle\psi_i\vert\right)
$$

$$
= \sum_i p_i \hat{H}\vert\psi_i\rangle\langle\psi_i\vert - \sum_i p_i \vert\psi_i\rangle\langle\psi_i\vert\hat{H} = [\hat{H}, \hat{\rho}]
$$

This is the **von Neumann equation**:

$$
\boxed{i\hbar \frac{d}{dt}\hat{\rho}(t) = [\hat{H}, \hat{\rho}(t)]}
$$

Note the sign difference from the Heisenberg equation for operators.

---

## Part III: Imaginary Time and Matsubara Green's Functions

### The Problem with Real Time at $T > 0$

For $T > 0$, we need thermal averages like $\langle\hat{A}(t)\hat{B}(0)\rangle = \text{Tr}(\hat{\rho}\hat{A}(t)\hat{B}(0))$.

The operator $e^{-i\hat{H}t/\hbar}$ oscillates forever. Thermal weights $e^{-\beta E_n}$ decay exponentially. These two exponentials behave very differently.

**Key insight:** Define $\tau = it/\hbar$ (imaginary time, with units of inverse energy). Then:

$$
e^{-i\hat{H}t/\hbar} = e^{-\hat{H}\tau}
$$

Both the thermal factor $e^{-\beta\hat{H}}$ and the "evolution" factor $e^{-\hat{H}\tau}$ are now decaying exponentials—same mathematical structure!

### The Matsubara Green's Function: Definition

For fermions (we'll specialize to electrons in condensed matter), define the **imaginary-time Green's function**:

$$
\mathcal{G}(\mathbf{r}, \tau; \mathbf{r}', \tau') \equiv -\langle T_\tau \psi(\mathbf{r}, \tau) \psi^\dagger(\mathbf{r}', \tau') \rangle
$$

where:
- $\tau, \tau' \in [0, \beta\hbar]$ are imaginary times
- $T_\tau$ is the imaginary-time ordering operator (larger $\tau$ to the left)
- Field operators in imaginary-time Heisenberg picture:

$$
\psi(\mathbf{r}, \tau) = e^{\hat{H}\tau}\psi(\mathbf{r})e^{-\hat{H}\tau}
$$

$$
\psi^\dagger(\mathbf{r}', \tau') = e^{\hat{H}\tau'}\psi^\dagger(\mathbf{r}')e^{-\hat{H}\tau'}
$$

Note: $\psi^\dagger(\mathbf{r}, \tau) \neq [\psi(\mathbf{r}, \tau)]^\dagger$ in general! The $\dagger$ on the field operator is part of the notation, not Hermitian conjugation of the operator at imaginary time.

### Explicit Form

For $\tau > \tau'$:

$$
\mathcal{G}(\tau, \tau') = -\text{Tr}\left(\hat{\rho} \, e^{\hat{H}\tau}\psi(\mathbf{r})e^{-\hat{H}\tau} e^{\hat{H}\tau'}\psi^\dagger(\mathbf{r}')e^{-\hat{H}\tau'}\right)
$$

For $\tau < \tau'$:

$$
\mathcal{G}(\tau, \tau') = +\text{Tr}\left(\hat{\rho} \, e^{\hat{H}\tau'}\psi^\dagger(\mathbf{r}')e^{-\hat{H}\tau'} e^{\hat{H}\tau}\psi(\mathbf{r})e^{-\hat{H}\tau}\right)
$$

### The Antiperiodicity Property (KMS Condition)

**Theorem:** For fermions, $\mathcal{G}(\tau + \beta\hbar) = -\mathcal{G}(\tau)$ for $-\beta\hbar < \tau < 0$.

**Proof:**

Consider $\tau \in [0, \beta\hbar]$ and examine $\mathcal{G}(\tau - \beta\hbar)$ where $\tau - \beta\hbar < 0$:

$$
\mathcal{G}(\tau - \beta\hbar) = +\text{Tr}\left(\hat{\rho} \psi^\dagger(\tau) \psi(\tau - \beta\hbar)\right)
$$

since $\tau - \beta\hbar < 0 < \tau$, the operator with larger time ($\tau$) goes left.

Now use cyclic property of trace and $\hat{\rho} = e^{-\beta\hat{H}}/\mathcal{Z}$:

$$
\text{Tr}(\hat{\rho} \hat{A}\hat{B}) = \text{Tr}(e^{-\beta\hat{H}}\hat{A}\hat{B})/\mathcal{Z} = \text{Tr}(\hat{B}e^{-\beta\hat{H}}\hat{A})/\mathcal{Z}
$$

Insert $e^{\beta\hat{H}}e^{-\beta\hat{H}} = \hat{\mathbb{1}}$:

$$
= \text{Tr}(e^{-\beta\hat{H}}e^{\beta\hat{H}}\hat{B}e^{-\beta\hat{H}}\hat{A})/\mathcal{Z} = \text{Tr}(\hat{\rho} \, e^{\beta\hat{H}}\hat{B}e^{-\beta\hat{H}}\hat{A})
$$

For $\hat{B} = \psi^\dagger(\tau) = e^{\hat{H}\tau}\psi^\dagger e^{-\hat{H}\tau}$:

$$
e^{\beta\hat{H}}\psi^\dagger(\tau)e^{-\beta\hat{H}} = e^{\beta\hat{H}}e^{\hat{H}\tau}\psi^\dagger e^{-\hat{H}\tau}e^{-\beta\hat{H}} = e^{\hat{H}(\tau-\beta\hbar)}\psi^\dagger e^{-\hat{H}(\tau-\beta\hbar)} = \psi^\dagger(\tau - \beta\hbar)
$$

Therefore:

$$
\mathcal{G}(\tau - \beta\hbar) = +\text{Tr}(\hat{\rho} \psi^\dagger(\tau - \beta\hbar)\psi(\tau - \beta\hbar)) = +\langle \psi^\dagger(\tau - \beta\hbar)\psi(\tau - \beta\hbar)\rangle
$$

Wait, let's be more careful. Let $\tau' = \tau - \beta\hbar < 0$:

Actually, let me restart more carefully. Define $\tau \in [0, \beta\hbar]$. We want to relate $\mathcal{G}(\tau)$ to $\mathcal{G}(\tau - \beta\hbar)$.

For $\tau > 0$, $\mathcal{G}(\tau) = -\langle \psi(\tau)\psi^\dagger(0)\rangle$.

For the argument $\tau - \beta\hbar < 0$, since this is negative, we have $\tau - \beta\hbar < 0$, so:

$$\mathcal{G}(\tau - \beta\hbar) = +\langle \psi^\dagger(0)\psi(\tau - \beta\hbar)\rangle$$

Now using the cyclic property with $\hat{\rho} = e^{-\beta\hat{H}}/\mathcal{Z}$:

$$\langle \psi^\dagger(0)\psi(\tau - \beta\hbar)\rangle = \text{Tr}(e^{-\beta\hat{H}}\psi^\dagger(0)\psi(\tau - \beta\hbar))/\mathcal{Z}$$

$$= \text{Tr}(\psi(\tau - \beta\hbar)e^{-\beta\hat{H}}\psi^\dagger(0))/\mathcal{Z}$$

$$= \text{Tr}(e^{-\beta\hat{H}}e^{\beta\hat{H}}\psi(\tau - \beta\hbar)e^{-\beta\hat{H}}\psi^\dagger(0))/\mathcal{Z}$$

$$= \text{Tr}(\hat{\rho} \, e^{\beta\hat{H}}\psi(\tau - \beta\hbar)e^{-\beta\hat{H}}\psi^\dagger(0))$$

Now $e^{\beta\hat{H}}\psi(\tau - \beta\hbar)e^{-\beta\hat{H}} = e^{\beta\hat{H}}e^{\hat{H}(\tau-\beta\hbar)}\psi e^{-\hat{H}(\tau-\beta\hbar)}e^{-\beta\hat{H}} = e^{\hat{H}\tau}\psi e^{-\hat{H}\tau} = \psi(\tau)$.

Therefore:

$$\mathcal{G}(\tau - \beta\hbar) = +\langle \psi(\tau)\psi^\dagger(0)\rangle = -\mathcal{G}(\tau)$$

$$
\boxed{\mathcal{G}(\tau + \beta\hbar) = -\mathcal{G}(\tau)}$$

This is the **Kubo-Martin-Schwinger (KMS) boundary condition**.

### Fourier Series and Matsubara Frequencies

Due to antiperiodicity on $[0, \beta\hbar]$, we expand $\mathcal{G}(\tau)$ in a Fourier series with odd harmonics:

$$
\mathcal{G}(\tau) = \frac{1}{\beta\hbar}\sum_{n=-\infty}^{\infty} e^{-i\omega_n\tau} \mathcal{G}(i\omega_n)
$$

where $\omega_n = \frac{(2n+1)\pi}{\beta\hbar}$ are **Matsubara frequencies** for fermions.

**Why these frequencies?** The condition $e^{-i\omega_n(\tau+\beta\hbar)} = -e^{-i\omega_n\tau}$ requires $e^{-i\omega_n\beta\hbar} = -1$, so $\omega_n\beta\hbar = (2n+1)\pi$.

The inverse transform:

$$
\mathcal{G}(i\omega_n) = \int_0^{\beta\hbar} d\tau \, e^{i\omega_n\tau} \mathcal{G}(\tau)
$$

### Free Fermions

For non-interacting fermions with $\hat{H}_0 = \sum_\mathbf{k} \varepsilon_k \hat{c}^\dagger_\mathbf{k}\hat{c}_\mathbf{k}$:

$$\mathcal{G}_0(\mathbf{k}, \tau) = -\langle T_\tau \hat{c}_\mathbf{k}(\tau)\hat{c}^\dagger_\mathbf{k}(0)\rangle$$

For $\tau > 0$: $\mathcal{G}_0 = -\langle \hat{c}_\mathbf{k}(\tau)\hat{c}^\dagger_\mathbf{k}(0)\rangle = -e^{-\varepsilon_k\tau}\langle \hat{c}_\mathbf{k}\hat{c}^\dagger_\mathbf{k}\rangle = -e^{-\varepsilon_k\tau}(1 - f_k)$

where $f_k = \langle \hat{c}^\dagger_\mathbf{k}\hat{c}_\mathbf{k}\rangle = \frac{1}{e^{\beta\varepsilon_k}+1}$ is the Fermi function.

For $\tau < 0$: $\mathcal{G}_0 = +\langle \hat{c}^\dagger_\mathbf{k}(0)\hat{c}_\mathbf{k}(\tau)\rangle = +e^{-\varepsilon_k\tau}\langle \hat{c}^\dagger_\mathbf{k}\hat{c}_\mathbf{k}\rangle = +e^{-\varepsilon_k\tau}f_k$

Fourier transforming:

$$\mathcal{G}_0(i\omega_n) = \int_0^{\beta\hbar} d\tau \, e^{i\omega_n\tau} (-e^{-\varepsilon_k\tau}(1-f_k)) = -\frac{1-f_k}{\varepsilon_k - i\omega_n}(1 - e^{-(\varepsilon_k - i\omega_n)\beta\hbar})$$

Using $e^{i\omega_n\beta\hbar} = -1$ and $e^{-\beta\hbar\varepsilon_k}(1-f_k) = f_k$:

$$\mathcal{G}_0(i\omega_n) = \frac{1}{i\omega_n - \varepsilon_k}$$

---

## Part IV: The Spectral Function, LDOS, and Density of States

### Retarded and Advanced Green's Functions: Definition

In Part I, we defined the time-ordered Green's function. For calculating physical response, we need the **retarded** and **advanced** Green's functions defined directly in real frequency.

The **retarded Green's function** is defined as:

$$G^R(\mathbf{r}, \mathbf{r}', \omega) = \int_{-\infty}^{\infty} dt \, e^{i\omega t} G^R(\mathbf{r}, t; \mathbf{r}', 0)$$

where the real-time retarded function is:

$$G^R(\mathbf{r}, t; \mathbf{r}', t') = -i\theta(t-t')\langle\{\psi(\mathbf{r}, t), \psi^\dagger(\mathbf{r}', t')\}\rangle$$

The **advanced Green's function** is:

$$G^A(\mathbf{r}, t; \mathbf{r}', t') = +i\theta(t'-t)\langle\{\psi(\mathbf{r}, t), \psi^\dagger(\mathbf{r}', t')\}\rangle$$

For a single-particle system with eigenstates $\hat{H}\vert n\rangle = E_n\vert n\rangle$, we can compute $G^R$ explicitly. Inserting complete sets of eigenstates:

$$G^R(\mathbf{r}, \mathbf{r}', \omega) = \sum_{n,m} \phi_n(\mathbf{r})\phi_m^*(\mathbf{r}')\int_{-\infty}^{\infty} dt \, e^{i\omega t} (-i)\theta(t) \langle n\vert\{\vert n\rangle\langle n\vert, \vert m\rangle\langle m\vert\}\vert m\rangle e^{-i(E_n-E_m)t/\hbar}$$

For fermions, $\{\hat{c}_n, \hat{c}_m^\dagger\} = \delta_{nm}$, giving:

$$G^R(\mathbf{r}, \mathbf{r}', \omega) = \sum_n \frac{\phi_n(\mathbf{r})\phi_n^*(\mathbf{r}')}{\omega - E_n/\hbar + i\eta}$$

where $\eta \to 0^+$ ensures the retarded nature (poles in lower half-plane).

### The Spectral Function

From the above, the **spectral function** is defined as:

$$A(\mathbf{r}, \mathbf{r}', \omega) = -2\text{Im}\,G^R(\mathbf{r}, \mathbf{r}', \omega)$$

Computing the imaginary part using $\text{Im}\frac{1}{x+i\eta} = -\pi\delta(x)$:

$$A(\mathbf{r}, \mathbf{r}', \omega) = 2\pi\sum_n \phi_n(\mathbf{r})\phi_n^*(\mathbf{r}')\delta(\omega - E_n/\hbar)$$

For the diagonal case $\mathbf{r} = \mathbf{r}'$, this relates to the local density of states.

### Local Density of States (LDOS)

The **local density of states** at position $\mathbf{r}$ and frequency $\omega$ is:

$$\rho(\mathbf{r}, \omega) = \sum_n |\phi_n(\mathbf{r})|^2 \delta(\omega - E_n/\hbar)$$

Comparing with the spectral function:

$$\boxed{\rho(\mathbf{r}, \omega) = -\frac{1}{\pi}\text{Im}\,G^R(\mathbf{r}, \mathbf{r}, \omega) = \frac{1}{2\pi}A(\mathbf{r}, \mathbf{r}, \omega)}$$

**Physical interpretation:** $\rho(\mathbf{r}, \omega)d\omega$ is the probability density of finding a state with energy in $[\hbar\omega, \hbar(\omega+d\omega)]$ at position $\mathbf{r}$.

### Free Particle: Deriving the Spectral Function

For free particles, we found $G_0(\mathbf{k}, \omega) = \frac{1}{\omega - \varepsilon_k/\hbar + i\eta}$. The spectral function is:

$$A_0(\mathbf{k}, \omega) = -2\text{Im}\frac{1}{\omega - \varepsilon_k/\hbar + i\eta} = 2\pi\delta(\omega - \varepsilon_k/\hbar)$$

This shows the free particle has well-defined energy $\varepsilon_k$ (infinite lifetime, delta function peak).

### Density of States in $d$ Dimensions

For homogeneous systems, the **density of states per unit volume** is:

$$\nu(\omega) = \int \frac{d^d k}{(2\pi)^d} \delta(\omega - \varepsilon_k/\hbar)$$

**Derivation:** Integrate the LDOS over all space. Since $|\phi_k(\mathbf{r})|^2 = 1/V$ for plane waves:

$$\nu(\omega) = \frac{1}{V}\sum_{\mathbf{k}} \delta(\omega - \varepsilon_k/\hbar) = \int \frac{d^d k}{(2\pi)^d} \delta(\omega - \varepsilon_k/\hbar)$$

For free electrons with $\varepsilon_k = \frac{\hbar^2 k^2}{2m}$, change variables to energy. The surface area of a $d$-dimensional sphere is $S_{d-1} = \frac{2\pi^{d/2}}{\Gamma(d/2)}$.

In spherical coordinates:

$$\nu(\omega) = \frac{S_{d-1}}{(2\pi)^d} \int_0^{\infty} dk \, k^{d-1} \delta\left(\omega - \frac{\hbar k^2}{2m}\right)$$

Let $\xi = \frac{\hbar k^2}{2m}$, then $k = \sqrt{2m\xi/\hbar}$ and $dk = \frac{m}{\hbar k}d\xi$:

$$\nu(\omega) = \frac{S_{d-1}}{(2\pi)^d} \left(\frac{2m\omega}{\hbar}\right)^{(d-2)/2} \frac{m}{\hbar} \theta(\omega)$$

Simplifying using $\Gamma$ functions:

$$\boxed{\nu(\omega) = \frac{1}{(2\pi)^{d/2}} \left(\frac{m}{\hbar}\right)^{d/2} \frac{\omega^{d/2-1}}{\Gamma(d/2)} \theta(\omega)}$$

**Special cases:**
- **$d=1$:** $\nu(\omega) \propto \omega^{-1/2}$ (van Hove singularity at band bottom)
- **$d=2$:** $\nu(\omega) = \text{constant}$ (independent of energy)
- **$d=3$:** $\nu(\omega) \propto \omega^{1/2}$ (parabolic increase)

### Spectral Representation and Sum Rules

The spectral function satisfies important sum rules. From the definition:

$$\int_{-\infty}^{\infty} \frac{d\omega}{2\pi} A(\mathbf{k}, \omega) = \int_{-\infty}^{\infty} d\omega \sum_n |\langle n\vert\mathbf{k}\rangle|^2 \delta(\omega - E_n/\hbar) = \sum_n |\langle n\vert\mathbf{k}\rangle|^2 = 1$$

This **normalization sum rule** reflects the completeness of eigenstates.

The first moment gives the average energy:

$$\int_{-\infty}^{\infty} \frac{d\omega}{2\pi} \omega A(\mathbf{k}, \omega) = \varepsilon_k$$

### Matsubara to Real Axis: Analytic Continuation

For the Matsubara Green's function, the **spectral representation** is derived by inserting exact eigenstates (Lehmann representation):

$$\mathcal{G}(\mathbf{k}, i\omega_n) = \int_{-\infty}^{\infty} \frac{d\omega'}{2\pi} \frac{A(\mathbf{k}, \omega')}{i\omega_n - \omega'}$$

Comparing with the retarded function form, we obtain the **analytic continuation prescription**:

$$\boxed{G^R(\mathbf{k}, \omega) = \mathcal{G}(\mathbf{k}, i\omega_n \to \omega + i\eta)}$$

This prescription allows us to compute equilibrium quantities at Matsubara frequencies, then obtain real-time response by analytically continuing to just above the real axis.

---

## Part V: Interacting Systems and the Dyson Equation

### Many-Particle Systems

Real materials have interactions: electrons repel via Coulomb force. The Hamiltonian:

$$\hat{H} = \sum_\sigma \int d^3r \, \psi^\dagger_\sigma(\mathbf{r})\left(-\frac{\hbar^2\nabla^2}{2m}\right)\psi_\sigma(\mathbf{r}) + \frac{1}{2}\sum_{\sigma,\sigma'}\int d^3r d^3r' \, V(\mathbf{r}-\mathbf{r}')\psi^\dagger_\sigma(\mathbf{r})\psi^\dagger_{\sigma'}(\mathbf{r}')\psi_{\sigma'}(\mathbf{r}')\psi_\sigma(\mathbf{r})$$

### Self-Energy

The full interacting Green's function $G$ can be related to the free $G_0$ via:

$$G = G_0 + G_0 \Sigma G$$

or equivalently:

$$G^{-1} = G_0^{-1} - \Sigma$$

where $\Sigma$ is the **self-energy**. In momentum-frequency space:

$$G(\mathbf{k}, \omega) = \frac{1}{\omega - \varepsilon_k - \Sigma(\mathbf{k}, \omega)}$$

**Physical meaning of self-energy:**
- $\text{Re}\,\Sigma$: energy shift (effective mass renormalization)
- $\text{Im}\,\Sigma$: damping (inverse lifetime $\hbar/\tau_k = -2\text{Im}\Sigma$)

For a quasiparticle peak at $\omega = E_k$ with small imaginary part:

$$G^R \approx \frac{Z_k}{\omega - E_k + i/2\tau_k}$$

where $Z_k$ is the spectral weight (quasiparticle residue).

---

## Part VI: Non-Equilibrium Quantum Transport

### The Problem

In quantum transport, we have two reservoirs at different chemical potentials $\mu_L \neq \mu_R$ connected by a conductor. There is no global thermal equilibrium.

### The Keldysh Contour

Extend time from $-\infty$ to $+\infty$ then back to $-\infty$. The contour-ordered Green's function is:

$$G_C(\tau, \tau') = -i\langle T_C \psi(\tau)\psi^\dagger(\tau')\rangle$$

Decomposing into real-time components on the forward $(+)$ and backward $(-)$ branches gives four Green's functions. The useful combinations are:

- **Lesser:** $G^<(t, t') = +i\langle \psi^\dagger(t')\psi(t)\rangle$ (particle occupation)
- **Greater:** $G^>(t, t') = -i\langle \psi(t)\psi^\dagger(t')\rangle$ (hole occupation)
- **Retarded:** $G^R = \theta(t-t')[G^> - G^<]$
- **Advanced:** $G^A = \theta(t'-t)[G^< - G^>]$ 

### Physical Observables

The density and current are directly obtained from $G^<$:

$$n(\mathbf{r}, t) = -i G^<(\mathbf{r}, t; \mathbf{r}, t)$$

$$\mathbf{J}(\mathbf{r}, t) = \frac{\hbar}{2m}\left(\nabla' - \nabla\right)_{\mathbf{r}' \to \mathbf{r}} (-i)G^<(\mathbf{r}, t; \mathbf{r}', t)$$

### The Keldysh Dyson Equation

In matrix form:

$$\begin{pmatrix} G^R & G^< \\ 0 & G^A \end{pmatrix} = \begin{pmatrix} G_0^R & G_0^< \\ 0 & G_0^A \end{pmatrix} + \begin{pmatrix} G_0^R & G_0^< \\ 0 & G_0^A \end{pmatrix} \begin{pmatrix} \Sigma^R & \Sigma^< \\ 0 & \Sigma^A \end{pmatrix} \begin{pmatrix} G^R & G^< \\ 0 & G^A \end{pmatrix}$$

The equation for $G^<$ decouples:

$$G^< = (1 + G^R\Sigma^R)G_0^<(1 + \Sigma^AG^A) + G^R\Sigma^<G^A$$

For non-interacting systems with no $\Sigma^<$, and using the boundary conditions from the reservoirs, this yields the Landauer formula.

---

## Summary

| Level | Quantity | Key Result |
|-------|----------|------------|
| Single-particle QM | $G(\mathbf{r}, t; \mathbf{r}', t')$ | Propagator for Schrödinger equation |
| Statistical mechanics | $\hat{\rho}$, $\mathcal{G}(\tau)$ | Thermal averages, Matsubara formalism |
| Many-body physics | $\Sigma$, Dyson equation | Quasiparticles with renormalized mass and lifetime |
| Non-equilibrium | $G^<$, $G^R$ | Density and transport from contour-ordered Green's functions |

---

## References

1. Mahan, G.D. *Many-Particle Physics*, 3rd ed. (Springer, 2000)
2. Bruus, H. & Flensberg, K. *Many-Body Quantum Theory in Condensed Matter Physics* (Oxford, 2004)
3. Haug, H. & Jauho, A.-P. *Quantum Kinetics in Transport and Optics of Semiconductors* (Springer, 2008)
4. Datta, S. *Electronic Transport in Mesoscopic Systems* (Cambridge, 1995)
