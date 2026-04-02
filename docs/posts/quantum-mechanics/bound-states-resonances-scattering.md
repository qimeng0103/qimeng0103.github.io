---
title: "Bound States, Resonances, and Scattering Theory"
description: "Comprehensive analysis of bound state existence conditions, resonance phenomena, and scattering theory with detailed mathematical derivations"
date: 2026-04-02
tags: ["quantum mechanics", "bound states", "resonance", "scattering theory", "partial wave analysis"]
category: "quantum-mechanics"
math: true
---

# Bound States, Resonances, and Scattering Theory

This article presents a comprehensive treatment of three interconnected topics in quantum mechanics: the existence conditions for bound states in various potentials, the nature of resonance states and their relationship to bound states, and the general framework of scattering theory. Detailed mathematical derivations are provided throughout.

---

## Part I: Existence Conditions for Bound States

### 1.1 One-Dimensional Symmetric Finite Square Well

Consider the potential:

$$V(x) = \begin{cases} -V_0, & |x| < a \\ 0, & |x| > a \end{cases}$$

where $V_0 > 0$. We seek bound state solutions with energy $E < 0$.

**Schrödinger Equation**

Inside the well ($|x| < a$):
$$-\frac{\hbar^2}{2\mu}\frac{d^2\psi}{dx^2} - V_0\psi = E\psi$$

Outside the well ($|x| > a$):
$$-\frac{\hbar^2}{2\mu}\frac{d^2\psi}{dx^2} = E\psi$$

**Wave Numbers**

Define:
- Inside: $k = \sqrt{2\mu(E+V_0)}/\hbar$ (real for $E > -V_0$)
- Outside: $\kappa = \sqrt{-2\mu E}/\hbar$ (real and positive for $E < 0$)

Note the constraint:
$$k^2 + \kappa^2 = \frac{2\mu V_0}{\hbar^2}$$

**Even Parity Solutions**

For $\psi(-x) = \psi(x)$:

$$\psi(x) = \begin{cases} Ae^{\kappa x}, & x < -a \\ B\cos(kx), & -a < x < a \\ Ae^{-\kappa x}, & x > a \end{cases}$$

Matching $\psi$ and $\psi'$ at $x = a$:

From continuity of $\psi$: $B\cos(ka) = Ae^{-\kappa a}$

From continuity of $\psi'$: $-Bk\sin(ka) = -A\kappa e^{-\kappa a}$

Dividing the second equation by the first:

$$\boxed{k\tan(ka) = \kappa}$$

**Odd Parity Solutions**

For $\psi(-x) = -\psi(x)$:

$$\psi(x) = \begin{cases} -Ae^{\kappa x}, & x < -a \\ B\sin(kx), & -a < x < a \\ Ae^{-\kappa x}, & x > a \end{cases}$$

Matching at $x = a$:

From continuity of $\psi$: $B\sin(ka) = Ae^{-\kappa a}$

From continuity of $\psi'$: $Bk\cos(ka) = -A\kappa e^{-\kappa a}$

Dividing:

$$\boxed{-k\cot(ka) = \kappa}$$

**Existence Conditions**

Introduce dimensionless variables:
$$\xi = ka, \quad \eta = \kappa a, \quad R = \sqrt{\frac{2\mu V_0}{\hbar^2}}a$$

The constraint becomes: $\xi^2 + \eta^2 = R^2$

For even parity: $\eta = \xi\tan\xi$

For odd parity: $\eta = -\xi\cot\xi$

**Key Results:**

1. **Even parity states always exist** (at least one bound state). The curve $\eta = \xi\tan\xi$ always intersects the circle $\xi^2 + \eta^2 = R^2$ at least once for any $R > 0$.

2. **Odd parity states require**: $R > \pi/2$, or equivalently:
   $$\frac{2\mu V_0 a^2}{\hbar^2} > \frac{\pi^2}{4}$$
   $$8\mu V_0 a^2 > \pi^2\hbar^2$$

The physical reason is that odd parity requires a node at $x = 0$, demanding more "room" in the well.

**Number of Bound States**

The number of bound states equals the number of intersections. For even parity, there are $n$ solutions when:
$$(2n-1)\frac{\pi}{2} < R < (2n+1)\frac{\pi}{2}$$

For odd parity, there are $n$ solutions when:
$$n\pi < R < (n+1)\pi$$

### 1.2 One-Dimensional Semi-Infinite Square Well

Consider:

$$V(x) = \begin{cases} \infty, & x < 0 \\ -V_0, & 0 < x < a \\ 0, & x > a \end{cases}$$

**Boundary condition at $x = 0$:** $\psi(0) = 0$

The solution inside is $\psi(x) = B\sin(kx)$, automatically satisfying $\psi(0) = 0$.

Matching at $x = a$ gives:
$$\boxed{\kappa = -k\cot(ka)}$$

This is identical to the odd parity condition of the symmetric well! The infinite wall forces a node at the origin.

**Existence condition:**
$$8\mu V_0 a^2 > \pi^2\hbar^2$$

Unlike the symmetric well, there is no guaranteed bound state here.

### 1.3 Delta Function Potential

For $V(x) = -\gamma\delta(x)$ with $\gamma > 0$:

**Schrödinger equation:**
$$-\frac{\hbar^2}{2\mu}\frac{d^2\psi}{dx^2} - \gamma\delta(x)\psi = E\psi$$

Integrate across $x = 0$ from $-\epsilon$ to $+\epsilon$:
$$-\frac{\hbar^2}{2\mu}\left[\psi'(0^+) - \psi'(0^-)\right] - \gamma\psi(0) = 0$$

For even parity: $\psi'(0^+) = -\psi'(0^-)$, so:
$$-\frac{\hbar^2}{\mu}\psi'(0^+) = \gamma\psi(0)$$

For $x > 0$: $\psi(x) = Ae^{-\kappa x}$ where $\kappa = \sqrt{-2\mu E}/\hbar$

Then $\psi'(0^+) = -A\kappa$ and $\psi(0) = A$:
$$\frac{\hbar^2\kappa}{\mu} = \gamma$$

Solving for energy:
$$\boxed{E = -\frac{\mu\gamma^2}{2\hbar^2}}$$

**Normalized wavefunction:**
$$\psi(x) = \sqrt{\frac{\mu\gamma}{\hbar^2}}\exp\left(-\frac{\mu\gamma|x|}{\hbar^2}\right) = \frac{1}{\sqrt{L}}e^{-|x|/L}$$

where the characteristic length is $L = \hbar^2/(\mu\gamma)$.

**Key insight:** There is exactly one bound state, regardless of how weak the potential is. This is a characteristic feature of 1D attractive potentials.

### 1.4 Shallow Well Approximation

For a finite square well with $R \ll 1$ (shallow or narrow):

For the even parity ground state, when $R \ll 1$, we have $ka \ll 1$ and $\tan(ka) \approx ka$.

From $k\tan(ka) = \kappa$:
$$k^2 a \approx \kappa$$

Using $k^2 + \kappa^2 = R^2/a^2$ and $\kappa \ll k$:
$$k \approx \frac{R}{a}, \quad \kappa \approx \frac{R^2}{a}$$

Energy:
$$E = -\frac{\hbar^2\kappa^2}{2\mu} = -\frac{\hbar^2 R^4}{2\mu a^2} = -\frac{2\mu V_0^2 a^2}{\hbar^2}$$

**Probability inside the well:**

The wavefunction inside is $\psi(x) \approx B$ (constant, since $ka \ll 1$).

Normalization:
$$2\int_0^a B^2 dx + 2\int_a^{\infty} A^2 e^{-2\kappa x}dx = 1$$

With $B \approx A$ (continuity at $x = a$) and $\kappa a = R^2 \ll 1$:
$$2B^2 a + \frac{A^2}{\kappa}e^{-2\kappa a} \approx 2B^2 a + \frac{B^2}{\kappa} = B^2\left(2a + \frac{a}{R^2}\right)$$

For $R \ll 1$, the second term dominates:
$$B^2 \approx \frac{\kappa}{2} = \frac{R^2}{2a}$$

Probability inside:
$$P_{\text{in}} = 2B^2 a = R^2 \ll 1$$

**Remarkable result:** In a shallow well, the particle is mostly found outside the well, even though it is bound!

### 1.5 Three-Dimensional Spherical Square Well

For $V(r) = -V_0$ for $r < a$ and $0$ for $r > a$:

For $l = 0$ (s-wave), let $R(r) = \chi(r)/r$. The radial equation becomes:

$$-\frac{\hbar^2}{2\mu}\frac{d^2\chi}{dr^2} + V(r)\chi = E\chi$$

with boundary condition $\chi(0) = 0$.

This is mathematically identical to the 1D semi-infinite well! The solution is:

Inside ($r < a$): $\chi(r) = A\sin(kr)$

Outside ($r > a$): $\chi(r) = Be^{-\kappa r}$

Matching condition:
$$\kappa = -k\cot(ka)$$

**Key difference from 1D:** The condition for at least one bound state is:
$$R = \sqrt{\frac{2\mu V_0}{\hbar^2}}a > \frac{\pi}{2}$$

or:
$$\frac{8\mu V_0 a^2}{\hbar^2} > \pi^2$$

In 3D, a sufficiently shallow well supports **no bound states**. This contrasts sharply with 1D where any attractive potential binds at least one state.

**Physical interpretation:** In 3D, the effective potential includes a centrifugal barrier even for $l = 0$ (through the boundary condition at $r = 0$). The particle can "leak" out more easily.

---

## Part II: Resonance States and Quasi-Bound States

### 2.1 Physical Picture of Resonance

A resonance state occurs when a particle with energy $E > 0$ has a high probability of being found in a potential region, despite having sufficient energy to escape to infinity.

**Characteristics:**
- Energy is approximately $E_0$ (the resonance energy)
- The state has a finite lifetime $\tau$
- The energy width is $\Gamma$ where $\tau \approx \hbar/\Gamma$

### 2.2 Resonance in a Single-Barrier Structure

Consider a potential well surrounded by a finite barrier:

$$V(x) = \begin{cases} 0, & 0 < x < a \ V_0, & a < x < a+b \ 0, & x > a+b \ \infty, & x < 0 \end{cases}$$

For $0 < E < V_0$, the particle can tunnel through the barrier.

**Wavefunction regions:**

- Region I ($0 < x < a$): $\psi_I = A\sin(kx)$ where $k = \sqrt{2\mu E}/\hbar$
- Region II ($a < x < a+b$): $\psi_{II} = Be^{\alpha x} + Ce^{-\alpha x}$ where $\alpha = \sqrt{2\mu(V_0-E)}/\hbar$
- Region III ($x > a+b$): $\psi_{III} = D\sin(kx + \phi)$ (standing wave, appropriate for studying probability)

**Matching conditions at $x = a$:**

$$A\sin(ka) = Be^{\alpha a} + Ce^{-\alpha a}$$
$$Ak\cos(ka) = B\alpha e^{\alpha a} - C\alpha e^{-\alpha a}$$

**Matching conditions at $x = a+b$:**

$$Be^{\alpha(a+b)} + Ce^{-\alpha(a+b)} = D\sin(k(a+b) + \phi)$$
$$B\alpha e^{\alpha(a+b)} - C\alpha e^{-\alpha(a+b)} = Dk\cos(k(a+b) + \phi)$$

**Resonance condition:**

When the barrier is thick ($\alpha b \gg 1$), the resonance energy approximately satisfies:
$$ka = n\pi$$

At these energies, the wavefunction inside the well has maximum amplitude (constructive interference of multiply reflected waves).

### 2.3 Breit-Wigner Formula

Near a resonance energy $E_n$, the transmission coefficient takes the form:

$$T(E) = \frac{\Gamma^2/4}{(E-E_n)^2 + \Gamma^2/4}$$

**Derivation:**

The transmission amplitude can be written as:
$$t(E) = \frac{\Gamma/2}{(E-E_n) + i\Gamma/2}$$

Then $T = |t|^2$ gives the Breit-Wigner form.

**Properties:**
- At $E = E_n$: $T = 1$ (perfect transmission)
- At $E = E_n \pm \Gamma/2$: $T = 1/2$ (half-maximum)
- $\Gamma$ is the full width at half maximum (FWHM)

### 2.4 Resonance Above a Potential Barrier

Consider:

$$V(x) = \begin{cases} \infty, & x < 0 \\ V_0, & 0 < x < a \\ 0, & x > a \end{cases}$$

For $E > V_0$, define:
- Inside: $k' = \sqrt{2\mu(E-V_0)}/\hbar$
- Outside: $k = \sqrt{2\mu E}/\hbar$

**Wavefunctions:**
- Region I ($0 < x < a$): $\psi_I = A\sin(k'x)$
- Region II ($x > a$): $\psi_{II} = \sin(kx + \phi)$

Matching at $x = a$:
$$A\sin(k'a) = \sin(ka + \phi)$$
$$Ak'\cos(k'a) = k\cos(ka + \phi)$$

Dividing:
$$k'\cot(k'a) = k\cot(ka + \phi)$$

**Probability inside the well:**

$$P_{\text{in}} \propto |A|^2 = \frac{1}{\sin^2(k'a) + (k'/k)^2\cos^2(k'a)}$$

When $\sin(k'a) = 0$, i.e., $k'a = n\pi$:
$$|A|^2 = \left(\frac{k}{k'}\right)^2 = \frac{E}{E-V_0} \gg 1 \text{ (for } E \approx V_0^+)$$

This gives the **resonance condition**: $k'a = n\pi$

**Resonance width:**

Expanding near resonance $E_n$ where $k'_n a = n\pi$:

Let $k'a = n\pi + \epsilon$ with $\epsilon \ll 1$:
$$\sin(k'a) \approx \epsilon = (k' - k'_n)a = \frac{\mu(E-E_n)}{\hbar^2 k'_n}a$$

The amplitude becomes:
$$|A|^2 \approx \frac{E_n/V_0}{(E_n-V_0)/V_0 + \frac{\mu^2 a^2}{\hbar^4 k_n'^2}(E-E_n)^2}$$

Identifying with the Breit-Wigner form:
$$\Gamma = \frac{4\hbar(E_n-V_0)}{a\sqrt{2\mu V_0}}$$

### 2.5 Decaying States and Complex Energy

For a true decaying state (not a stationary state), we use outgoing wave boundary conditions.

**Wavefunction:**
$$\psi(x) = \begin{cases} A\sin(k'x), & 0 < x < a \\ e^{ikx}, & x > a \end{cases}$$

Matching at $x = a$:
$$A\sin(k'a) = e^{ika}$$
$$Ak'\cos(k'a) = ike^{ika}$$

Dividing:
$$k'\cot(k'a) = ik$$

Since $k$ and $k'$ must be related through energy, this gives a complex solution.

Near resonance $k'a = n\pi + \epsilon$:
$$\cot(k'a) \approx -\epsilon = -(k' - k'_n)a$$

So:
$$-k'(k' - k'_n)a = ik$$

For $k \ll k'$ (low energy outside compared to inside):
$$k' \approx k'_n - \frac{ik}{k'_n a}$$

The energy becomes complex:
$$E = -V_0 + \frac{\hbar^2 k'^2}{2\mu} = -V_0 + \frac{\hbar^2 k_n'^2}{2\mu} - i\frac{\hbar^2 k_n k}{\mu a}$$

Writing $E = E_n - i\Gamma/2$:
$$\Gamma = \frac{2\hbar^2 k_n}{\mu a}$$

**Time evolution:**
$$\psi(t) \sim e^{-iEt/\hbar} = e^{-iE_n t/\hbar}e^{-\Gamma t/(2\hbar)}$$

Probability decays exponentially:
$$|\psi(t)|^2 \sim e^{-\Gamma t/\hbar} = e^{-t/\tau}$$

with lifetime $\tau = \hbar/\Gamma$.

### 2.6 Connection Between Resonance and Bound States

As the barrier height $V_0 \to \infty$:
- Resonance energies approach bound state energies
- Resonance width $\Gamma \to 0$
- Lifetime $\tau \to \infty$

**Unified picture:**
- Bound state: Infinite barrier (particle permanently trapped)
- Resonance: Finite barrier (particle temporarily trapped)
- Scattering state: No barrier or energy far from resonance

---

## Part III: Multi-Channel Resonance and Scattering Theory

### 3.1 Double-Barrier Resonance

Consider a symmetric square well (double-barrier structure):

$$V(x) = \begin{cases} -V_0, & |x| < a \\ 0, & |x| > a \end{cases}$$

For $E > 0$, incident from left:

$$\psi(x) = \begin{cases} e^{ikx} + Re^{-ikx}, & x < -a \\ Ae^{ik'x} + Be^{-ik'x}, & |x| < a \\ Se^{ikx}, & x > a \end{cases}$$

where $k = \sqrt{2\mu E}/\hbar$ and $k' = \sqrt{2\mu(E+V_0)}/\hbar$.

**Matching at $x = \pm a$:**

Four continuity equations allow elimination of $A$, $B$, and $R$ to find $S$.

After algebra:
$$S = e^{-2ika}\left[\cos(2k'a) - \frac{i}{2}\left(\frac{k}{k'} + \frac{k'}{k}\right)\sin(2k'a)\right]^{-1}$$

**Transmission coefficient:**
$$T = |S|^2 = \left[1 + \frac{V_0^2}{4E(E+V_0)}\sin^2(2k'a)\right]^{-1}$$

**Resonance condition:** $2k'a = n\pi$ gives $T = 1$ (perfect transmission).

**Resonance energies:**
$$E_n = -V_0 + \frac{\pi^2\hbar^2}{8\mu a^2}n^2$$

For small $n$, $E_n < 0$ (bound states). For large $n$, $E_n > 0$ (resonance states).

### 3.2 Partial Wave Analysis

For scattering from a central potential, expand the plane wave:

$$e^{ikz} = \sum_{l=0}^{\infty}(2l+1)i^l j_l(kr)P_l(\cos\theta)$$

The scattered wavefunction at large $r$:
$$\psi(\mathbf{r}) \xrightarrow{r\to\infty} e^{ikz} + f(\theta)\frac{e^{ikr}}{r}$$

**Partial wave expansion of scattering amplitude:**
$$f(\theta) = \sum_{l=0}^{\infty}(2l+1)f_l P_l(\cos\theta)$$

**Partial wave amplitude:**
$$f_l = \frac{e^{2i\delta_l} - 1}{2ik} = \frac{1}{k\cot\delta_l - ik}$$

where $\delta_l$ is the phase shift for angular momentum $l$.

**Total cross-section:**
$$\sigma_{\text{tot}} = \frac{4\pi}{k^2}\sum_{l=0}^{\infty}(2l+1)\sin^2\delta_l$$

### 3.3 Low-Energy Scattering and Scattering Length

At low energies ($ka \ll 1$), only s-wave ($l = 0$) contributes significantly.

**Scattering length** $a_s$ is defined by:
$$\lim_{k\to 0} k\cot\delta_0 = -\frac{1}{a_s}$$

The s-wave scattering amplitude becomes:
$$f_0 \xrightarrow{k\to 0} -a_s$$

**Low-energy cross-section:**
$$\sigma_0 = 4\pi a_s^2$$

**Connection to bound states:**

If the potential supports a weakly bound state with energy $E_b = -\hbar^2\beta^2/(2\mu)$, the scattering length is:
$$a_s = \frac{1}{\beta} = \frac{\hbar}{\sqrt{-2\mu E_b}}$$

**Physical interpretation:** The scattering length measures the spatial extent of the bound state. For a loosely bound state (small $|E_b|$), the scattering length is large, leading to a large low-energy cross-section.

### 3.4 Levinson's Theorem

**Theorem:** The phase shift at zero energy is related to the number of bound states:
$$\delta_l(0) = n_l\pi$$

where $n_l$ is the number of bound states with angular momentum $l$.

**Proof sketch:**

Consider the Jost function $f_l(k)$, analytic in the upper half-plane. Bound states correspond to zeros of $f_l(k)$ on the positive imaginary axis at $k = i\kappa_n$.

As $k$ goes from $0$ to $\infty$ along the real axis, the phase of $f_l(k)$ changes by $-\delta_l(k)$.

Using the argument principle, the number of zeros in the upper half-plane equals the change in phase divided by $\pi$:
$$n_l = \frac{1}{\pi}[\delta_l(0) - \delta_l(\infty)]$$

Since $\delta_l(\infty) = 0$ (no scattering at infinite energy):
$$\delta_l(0) = n_l\pi$$

**Physical significance:**
- Each bound state contributes $\pi$ to the zero-energy phase shift
- The phase shift encodes information about the discrete spectrum
- For attractive potentials, $\delta_0(0) > 0$

### 3.5 Bound States as Poles of the Scattering Amplitude

**Key insight:** Bound state energies correspond to poles of the scattering amplitude in the complex momentum plane.

For s-wave:
$$f_0(k) = \frac{1}{k\cot\delta_0 - ik}$$

**Bound state condition:** $k = i\beta$ (imaginary momentum for $E < 0$)

At $k = i\beta$:
$$f_0(i\beta) = \frac{1}{i\beta\cot\delta_0(i\beta) + \beta}$$

For a bound state, the wavefunction outside is $\sim e^{-\beta r}$, which corresponds to the residue condition.

The condition for a pole is:
$$k\cot\delta_0 = ik \quad \text{at } k = i\beta$$

This gives:
$$\cot\delta_0(i\beta) = -1$$

**Resonances** correspond to poles in the complex $k$-plane near the real axis (in the lower half-plane for decaying states).

### 3.6 Unitarity Bound and Resonant Scattering

From the optical theorem:
$$\sigma_{\text{tot}} = \frac{4\pi}{k}\text{Im}f(0)$$

For a single partial wave:
$$\sigma_l = \frac{4\pi}{k^2}(2l+1)\sin^2\delta_l \leq \frac{4\pi}{k^2}(2l+1)$$

**Maximum cross-section** (unitarity limit): Achieved when $\delta_l = \pi/2$.

**Resonant scattering:** Near a resonance, the phase shift changes rapidly through $\pi/2$.

Near resonance:
$$\tan\delta_l(E) = \frac{\Gamma/2}{E_r - E}$$

At $E = E_r$: $\delta_l = \pi/2$, giving the maximum cross-section.

---

## Summary and Key Formulas

### Bound State Existence

| Dimension | Condition |
|-----------|-----------|
| 1D (symmetric well) | At least one bound state always exists |
| 1D (semi-infinite) | Requires $8\mu V_0 a^2 > \pi^2\hbar^2$ |
| 3D (spherical well) | Requires $8\mu V_0 a^2 > \pi^2\hbar^2$ |

### Resonance Phenomena

- **Breit-Wigner formula:** $T(E) = \frac{\Gamma^2/4}{(E-E_r)^2 + \Gamma^2/4}$
- **Lifetime-width relation:** $\tau = \hbar/\Gamma$
- **Phase shift near resonance:** $\tan\delta = \frac{\Gamma/2}{E_r - E}$

### Scattering Theory

- **Scattering length:** $a_s = -\lim_{k\to 0}f_0(k)$
- **Low-energy cross-section:** $\sigma_0 = 4\pi a_s^2$
- **Levinson's theorem:** $\delta_l(0) = n_l\pi$
- **Unitarity limit:** $\sigma_l^{\text{max}} = 4\pi(2l+1)/k^2$

### Unified Picture

Bound states, resonances, and scattering states are unified through the analytic properties of the scattering amplitude:
- Bound states: Poles on positive imaginary $k$-axis
- Resonances: Poles near real axis in complex $k$-plane
- Scattering: Behavior along real $k$-axis
