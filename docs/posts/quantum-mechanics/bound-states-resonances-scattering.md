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

Consider a particle of mass $\mu$ moving in the potential:

$$V(x) = \begin{cases} -V_0, & |x| < a \\ 0, & |x| > a \end{cases}$$

where $V_0 > 0$ represents the well depth. We seek bound state solutions with energy $E < 0$.

**Time-Independent Schrödinger Equation**

The stationary Schrödinger equation is:

$$-\frac{\hbar^2}{2\mu}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi$$

Inside the well region where $|x| < a$:
$$-\frac{\hbar^2}{2\mu}\frac{d^2\psi}{dx^2} - V_0\psi = E\psi$$

Rearranging:
$$\frac{d^2\psi}{dx^2} = -\frac{2\mu(E+V_0)}{\hbar^2}\psi$$

Since $-V_0 < E < 0$ for bound states, we have $E + V_0 > 0$. Defining:
$$k = \frac{\sqrt{2\mu(E+V_0)}}{\hbar}$$

The equation becomes:
$$\frac{d^2\psi}{dx^2} = -k^2\psi$$

The general solution is:
$$\psi(x) = A\cos(kx) + B\sin(kx)$$

Outside the well where $|x| > a$ and $V(x) = 0$:
$$\frac{d^2\psi}{dx^2} = -\frac{2\mu E}{\hbar^2}\psi = \frac{2\mu|E|}{\hbar^2}\psi$$

Defining:
$$\kappa = \frac{\sqrt{-2\mu E}}{\hbar} = \frac{\sqrt{2\mu|E|}}{\hbar}$$

The equation becomes:
$$\frac{d^2\psi}{dx^2} = \kappa^2\psi$$

For normalizable bound states, the solution must decay exponentially:
$$\psi(x) = \begin{cases} Ce^{\kappa x}, & x < -a \\ De^{-\kappa x}, & x > a \end{cases}$$

**Key Constraint**

Adding the squares of $k$ and $\kappa$:
$$k^2 + \kappa^2 = \frac{2\mu(E+V_0)}{\hbar^2} + \frac{-2\mu E}{\hbar^2} = \frac{2\mu V_0}{\hbar^2}$$

This can be written as:
$$\xi^2 + \eta^2 = R^2$$

where $\xi = ka$, $\eta = \kappa a$, and $R = \sqrt{2\mu V_0}a/\hbar$ is a dimensionless measure of the well strength.

**Even Parity Solutions**

For $\psi(-x) = \psi(x)$, we have $B = 0$ inside the well, and by symmetry $C = D$ outside. The wavefunction is:

$$\psi(x) = \begin{cases} Ce^{\kappa x}, & x < -a \\ A\cos(kx), & -a < x < a \\ Ce^{-\kappa x}, & x > a \end{cases}$$

**Applying Boundary Conditions at $x = a$**

Continuity of $\psi$:
$$A\cos(ka) = Ce^{-\kappa a}$$

Continuity of $\psi'$:
$$\frac{d\psi}{dx}\bigg|_{x=a^-} = -Ak\sin(ka)$$
$$\frac{d\psi}{dx}\bigg|_{x=a^+} = -C\kappa e^{-\kappa a}$$

Therefore:
$$-Ak\sin(ka) = -C\kappa e^{-\kappa a}$$

Dividing the derivative continuity equation by the wavefunction continuity equation:
$$\frac{-Ak\sin(ka)}{A\cos(ka)} = \frac{-C\kappa e^{-\kappa a}}{Ce^{-\kappa a}}$$

Simplifying:
$$-k\tan(ka) = -\kappa$$

$$\boxed{k\tan(ka) = \kappa}$$

**Odd Parity Solutions**

For $\psi(-x) = -\psi(x)$, we have $A = 0$ inside, and by antisymmetry $C = -D$ outside (with the sign convention that $\psi(x < -a) = -Ce^{\kappa x}$ gives continuity). The wavefunction is:

$$\psi(x) = \begin{cases} -Ce^{\kappa x}, & x < -a \\ B\sin(kx), & -a < x < a \\ Ce^{-\kappa x}, & x > a \end{cases}$$

**Applying Boundary Conditions at $x = a$**

Continuity of $\psi$:
$$B\sin(ka) = Ce^{-\kappa a}$$

Continuity of $\psi'$:
$$Bk\cos(ka) = -C\kappa e^{-\kappa a}$$

Dividing:
$$\frac{Bk\cos(ka)}{B\sin(ka)} = \frac{-C\kappa e^{-\kappa a}}{Ce^{-\kappa a}}$$

$$k\cot(ka) = -\kappa$$

$$\boxed{-k\cot(ka) = \kappa}$$

**Graphical Solution and Existence Conditions**

Using dimensionless variables $\xi = ka$ and $\eta = \kappa a$:

For even parity: $\eta = \xi\tan\xi$
For odd parity: $\eta = -\xi\cot\xi$

Both subject to: $\xi^2 + \eta^2 = R^2$

**Analysis of Even Parity Solutions**

The function $\eta = \xi\tan\xi$ starts at $\eta = 0$ when $\xi = 0$ and increases monotonically until $\xi = \pi/2$ where it diverges to $+\infty$. The circle $\xi^2 + \eta^2 = R^2$ always intersects this curve at least once for any $R > 0$ because:
- At $\xi = 0$, the curve has $\eta = 0$
- At small $\xi$, $\tan\xi \approx \xi$, so $\eta \approx \xi^2$ which is below the circle
- As $\xi$ increases, the curve $\xi\tan\xi$ eventually rises above the circle

Therefore, **at least one even parity bound state always exists** for any attractive 1D potential well, no matter how shallow.

**Analysis of Odd Parity Solutions**

The function $\eta = -\xi\cot\xi$ starts at $\eta = 1$ when $\xi = 0$ (using $\lim_{\xi\to 0}(-\xi\cot\xi) = 1$) and decreases, crossing zero at $\xi = \pi/2$, then diverging to $-\infty$ at $\xi = \pi$.

For an intersection to exist, the circle must extend beyond $\xi = \pi/2$, requiring:
$$R > \frac{\pi}{2}$$

In physical terms:
$$\frac{\sqrt{2\mu V_0}a}{\hbar} > \frac{\pi}{2}$$

Squaring:
$$\frac{2\mu V_0 a^2}{\hbar^2} > \frac{\pi^2}{4}$$

$$\boxed{8\mu V_0 a^2 > \pi^2\hbar^2}$$

This is the condition for at least one odd parity bound state to exist. The physical interpretation is that odd parity requires a node at the origin, which needs sufficient "space" in the well.

![Finite Square Well Wave Functions](/images/qm-notes/finite-well-wavefunctions.png)
*Figure 1: (Left) The finite square well potential with bound state energy levels. (Right) Even and odd parity wave functions showing the characteristic exponential decay outside the well and oscillatory behavior inside.*

![Wavefunction Matching](/images/qm-notes/wavefunction-matching.png)
*Figure 2: Wave function matching at the potential boundaries. The wave function and its derivative must be continuous at $x = \pm a$, leading to the transcendental equations for bound state energies.*

### 1.2 One-Dimensional Semi-Infinite Square Well

Consider a potential with an infinite wall at $x = 0$:

$$V(x) = \begin{cases} \infty, & x < 0 \\ -V_0, & 0 < x < a \\ 0, & x > a \end{cases}$$

**Boundary Condition at $x = 0$**

The infinite potential requires:
$$\psi(0) = 0$$

Inside the well ($0 < x < a$), the general solution is:
$$\psi(x) = A\sin(kx) + B\cos(kx)$$

Applying $\psi(0) = 0$:
$$B = 0$$

So $\psi(x) = A\sin(kx)$ automatically satisfies the boundary condition.

Outside ($x > a$):
$$\psi(x) = Ce^{-\kappa x}$$

**Matching at $x = a$**

Continuity of $\psi$:
$$A\sin(ka) = Ce^{-\kappa a}$$

Continuity of $\psi'$:
$$Ak\cos(ka) = -C\kappa e^{-\kappa a}$$

Dividing:
$$k\cot(ka) = -\kappa$$

$$\boxed{\kappa = -k\cot(ka)}$$

This is identical to the odd parity condition of the symmetric well. The infinite wall enforces a node at the origin, equivalent to requiring odd parity symmetry.

**Existence Condition**

The condition for at least one bound state is:
$$\boxed{8\mu V_0 a^2 > \pi^2\hbar^2}$$

Unlike the symmetric well, there is no guaranteed bound state here—the infinite wall "wastes" half of the well for the ground state.

### 1.3 Delta Function Potential

For an attractive delta function potential $V(x) = -\gamma\delta(x)$ with $\gamma > 0$:

**Schrödinger Equation**

$$-\frac{\hbar^2}{2\mu}\frac{d^2\psi}{dx^2} - \gamma\delta(x)\psi = E\psi$$

**Boundary Condition at $x = 0$**

Integrate the Schrödinger equation from $-\epsilon$ to $+\epsilon$:

$$-\frac{\hbar^2}{2\mu}\int_{-\epsilon}^{+\epsilon}\frac{d^2\psi}{dx^2}dx - \gamma\int_{-\epsilon}^{+\epsilon}\delta(x)\psi(x)dx = E\int_{-\epsilon}^{+\epsilon}\psi(x)dx$$

Taking the limit $\epsilon \to 0$:
- First term: $-\frac{\hbar^2}{2\mu}[\psi'(0^+) - \psi'(0^-)]$
- Second term: $-\gamma\psi(0)$
- Third term: $0$ (finite integrand over zero width)

Therefore:
$$\psi'(0^+) - \psi'(0^-) = -\frac{2\mu\gamma}{\hbar^2}\psi(0)$$

For an even parity bound state (the only possibility for a single delta function):
$$\psi(x) = \psi(-x) \Rightarrow \psi'(0^+) = -\psi'(0^-)$$

Substituting:
$$2\psi'(0^+) = -\frac{2\mu\gamma}{\hbar^2}\psi(0)$$

$$\psi'(0^+) = -\frac{\mu\gamma}{\hbar^2}\psi(0)$$

**Solution for $x \neq 0$**

For $x > 0$ where $V(x) = 0$:
$$\psi(x) = Ae^{-\kappa x}$$

where $\kappa = \sqrt{-2\mu E}/\hbar$.

At $x = 0^+$:
$$\psi(0^+) = A$$
$$\psi'(0^+) = -A\kappa$$

**Applying the Boundary Condition**

$$-A\kappa = -\frac{\mu\gamma}{\hbar^2}A$$

$$\kappa = \frac{\mu\gamma}{\hbar^2}$$

**Energy Eigenvalue**

$$\sqrt{-2\mu E} = \frac{\mu\gamma}{\hbar}$$

Squaring both sides:
$$-2\mu E = \frac{\mu^2\gamma^2}{\hbar^2}$$

$$\boxed{E = -\frac{\mu\gamma^2}{2\hbar^2}}$$

**Normalization**

$$\int_{-\infty}^{+\infty}|\psi|^2dx = 2\int_0^{\infty}A^2e^{-2\kappa x}dx = 2A^2\cdot\frac{1}{2\kappa} = \frac{A^2}{\kappa} = 1$$

Therefore:
$$A = \sqrt{\kappa} = \sqrt{\frac{\mu\gamma}{\hbar^2}}$$

**Complete Wavefunction**

$$\boxed{\psi(x) = \sqrt{\frac{\mu\gamma}{\hbar^2}}\exp\left(-\frac{\mu\gamma|x|}{\hbar^2}\right)}$$

**Key insight:** There is exactly one bound state, regardless of how weak the potential is. This is a characteristic feature of 1D attractive potentials.

### 1.4 Shallow Well Approximation

For a finite square well with small $R = \sqrt{2\mu V_0}a/\hbar \ll 1$:

**Ground State Energy**

For the even parity ground state, when $R \ll 1$, we expect $ka \ll 1$ and $\kappa a \ll 1$.

Using $\tan(ka) \approx ka$ for small $ka$:
$$k \cdot ka \approx \kappa$$
$$k^2 a \approx \kappa$$

From the constraint $k^2 + \kappa^2 = R^2/a^2$ and the fact that $\kappa \ll k$ when $ka \ll 1$:
$$k^2 \approx \frac{R^2}{a^2}$$
$$k \approx \frac{R}{a}$$

Therefore:
$$\kappa \approx k^2 a = \frac{R^2}{a}$$

The energy is:
$$E = -\frac{\hbar^2\kappa^2}{2\mu} = -\frac{\hbar^2 R^4}{2\mu a^2} = -\frac{2\mu V_0^2 a^2}{\hbar^2}$$

**Probability Inside the Well**

The normalized wavefunction inside is approximately constant $\psi(x) \approx B$ since $ka \ll 1$.

Outside: $\psi(x) = Ae^{-\kappa|x|}$ where $A \approx B$ by continuity at $x = a$.

Normalization integral:
$$\int_{-\infty}^{\infty}|\psi|^2dx = 2\int_0^a B^2dx + 2\int_a^{\infty}A^2e^{-2\kappa x}dx = 1$$

With $A \approx B$:
$$2B^2 a + 2B^2\frac{e^{-2\kappa a}}{2\kappa} = 1$$

Since $\kappa a = R^2 \ll 1$, $e^{-2\kappa a} \approx 1$:
$$2B^2 a + \frac{B^2}{\kappa} \approx B^2\left(2a + \frac{a}{R^2}\right) \approx \frac{B^2 a}{R^2} = 1$$

Therefore:
$$B^2 = \frac{R^2}{a}$$

Probability inside the well:
$$P_{\text{in}} = 2B^2 a = 2R^2 \ll 1$$

**Remarkable Result:** In a shallow well, the particle is mostly found outside the well, even though it is bound. This is consistent with the uncertainty principle—a shallow well corresponds to a weakly bound, spatially extended state.

### 1.5 Three-Dimensional Spherical Square Well

For a central potential:

$$V(r) = \begin{cases} -V_0, & r < a \\ 0, & r > a \end{cases}$$

**Radial Schrödinger Equation**

For a central potential, $\psi(\mathbf{r}) = R_l(r)Y_l^m(\theta,\phi)$. The radial equation is:

$$-\frac{\hbar^2}{2\mu}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dR_l}{dr}\right) + \left[V(r) + \frac{\hbar^2 l(l+1)}{2\mu r^2}\right]R_l = ER_l$$

Substituting $R_l(r) = \chi_l(r)/r$:

$$-\frac{\hbar^2}{2\mu}\frac{d^2\chi_l}{dr^2} + \left[V(r) + \frac{\hbar^2 l(l+1)}{2\mu r^2}\right]\chi_l = E\chi_l$$

**Lowest Energy State ($l = 0$)**

For s-wave ($l = 0$), the effective potential has no centrifugal barrier. The equation becomes:

$$-\frac{\hbar^2}{2\mu}\frac{d^2\chi}{dr^2} + V(r)\chi = E\chi$$

With boundary condition $\chi(0) = 0$ (since $R = \chi/r$ must be finite at $r = 0$).

**Solution**

Inside ($r < a$):
$$\chi(r) = A\sin(kr)$$

Outside ($r > a$):
$$\chi(r) = Be^{-\kappa r}$$

**Matching at $r = a$**

Continuity of $\chi$:
$$A\sin(ka) = Be^{-\kappa a}$$

Continuity of $\chi'$:
$$Ak\cos(ka) = -B\kappa e^{-\kappa a}$$

Dividing:
$$k\cot(ka) = -\kappa$$

$$\boxed{\kappa = -k\cot(ka)}$$

This is identical to the 1D semi-infinite well!

**Existence Condition**

The condition for at least one bound state is:
$$R = \frac{\sqrt{2\mu V_0}a}{\hbar} > \frac{\pi}{2}$$

or:
$$\boxed{\frac{8\mu V_0 a^2}{\hbar^2} > \pi^2}$$

**Key Difference from 1D:** In 3D, a sufficiently shallow well supports no bound states. This contrasts with 1D where any attractive potential binds at least one state. The physical reason is that in 3D, the boundary condition $\chi(0) = 0$ effectively creates a "centrifugal-like" constraint even for s-wave, making it easier for the particle to escape.

---

## Part II: Resonance States and Quasi-Bound States

### 2.1 Physical Picture of Resonance

A resonance state occurs when a particle with energy $E > 0$ has a high probability of being temporarily trapped in a potential region, despite having sufficient energy to escape to infinity.

**Characteristics:**
- The particle remains in the potential region for a characteristic time $\tau$
- The energy is not sharply defined but has a width $\Gamma$
- The energy-time uncertainty relation gives: $\tau \approx \hbar/\Gamma$

### 2.2 Double-Barrier Resonance Structure

Consider a potential well surrounded by finite barriers:

![Double Barrier Resonance](/images/qm-notes/double-barrier.png)
*Figure 3: A double-barrier structure creates a quasi-bound state. The particle is temporarily trapped in the well region, with the wave function amplitude significantly enhanced inside at resonance energies.*

**Model Potential**

$$V(x) = \begin{cases} 0, & 0 < x < a \\ V_0, & a < x < a+b \quad (V_0 > E) \\ 0, & x > a+b \end{cases}$$

with $V(x) = \infty$ for $x < 0$.

**Wavefunctions in Each Region**

For $0 < E < V_0$:

- Region I ($0 < x < a$): $\psi_I = A\sin(kx)$ where $k = \sqrt{2\mu E}/\hbar$
- Region II ($a < x < a+b$): $\psi_{II} = Be^{\alpha x} + Ce^{-\alpha x}$ where $\alpha = \sqrt{2\mu(V_0-E)}/\hbar$
- Region III ($x > a+b$): $\psi_{III} = D\sin(kx + \phi)$

**Matching Conditions at $x = a$**

Continuity of $\psi$:
$$A\sin(ka) = Be^{\alpha a} + Ce^{-\alpha a}$$

Continuity of $\psi'$:
$$Ak\cos(ka) = B\alpha e^{\alpha a} - C\alpha e^{-\alpha a}$$

**Matching Conditions at $x = a+b$**

Continuity of $\psi$:
$$Be^{\alpha(a+b)} + Ce^{-\alpha(a+b)} = D\sin(k(a+b) + \phi)$$

Continuity of $\psi'$:
$$B\alpha e^{\alpha(a+b)} - C\alpha e^{-\alpha(a+b)} = Dk\cos(k(a+b) + \phi)$$

**Thick Barrier Limit ($\alpha b \gg 1$)**

When the barrier is thick, the term $e^{\alpha(a+b)}$ dominates. The resonance condition approximately becomes:
$$ka = n\pi$$

At these energies, the wavefunction inside the well has maximum amplitude due to constructive interference of multiply reflected waves.

### 2.3 Breit-Wigner Resonance Formula

Near a resonance energy $E_n$, the transmission coefficient takes the universal form:

![Breit-Wigner Resonance](/images/qm-notes/breit-wigner-resonance.png)
*Figure 4: The Breit-Wigner resonance profile showing the characteristic Lorentzian lineshape. The full width at half maximum (FWHM) equals $\Gamma$.*

**Derivation**

The transmission amplitude can be written using the complex energy pole structure:

$$t(E) = \frac{\Gamma/2}{(E-E_n) + i\Gamma/2}$$

where $E_n$ is the resonance energy and $\Gamma$ is the width.

The transmission coefficient is:
$$T(E) = |t(E)|^2 = \frac{(\Gamma/2)^2}{(E-E_n)^2 + (\Gamma/2)^2}$$

$$\boxed{T(E) = \frac{\Gamma^2/4}{(E-E_n)^2 + \Gamma^2/4}}$$

**Properties:**

1. At $E = E_n$: $T = 1$ (perfect transmission at resonance)
2. At $E = E_n \pm \Gamma/2$: $T = 1/2$ (half-maximum)
3. $\Gamma$ is the full width at half maximum (FWHM)
4. The integral over energy: $\int_{-\infty}^{\infty} T(E)dE = \pi\Gamma/2$

### 2.4 Resonance Above a Potential Barrier

Consider a particle with $E > V_0$ incident on a barrier:

$$V(x) = \begin{cases} \infty, & x < 0 \\ V_0, & 0 < x < a \\ 0, & x > a \end{cases}$$

**Wave Numbers**

Inside the barrier: $k' = \sqrt{2\mu(E-V_0)}/\hbar$
Outside: $k = \sqrt{2\mu E}/\hbar$

**Wavefunctions**

- Region I ($0 < x < a$): $\psi_I = A\sin(k'x)$
- Region II ($x > a$): $\psi_{II} = \sin(kx + \phi)$ (normalized to unit amplitude)

**Matching at $x = a$**

Continuity of $\psi$:
$$A\sin(k'a) = \sin(ka + \phi)$$

Continuity of $\psi'$:
$$Ak'\cos(k'a) = k\cos(ka + \phi)$$

Dividing:
$$k'\cot(k'a) = k\cot(ka + \phi)$$

**Probability Inside**

The amplitude inside the well:
$$|A|^2 = \frac{1}{\sin^2(k'a) + (k'/k)^2\cos^2(k'a)}$$

When $\sin(k'a) = 0$, i.e., $k'a = n\pi$:
$$|A|^2 = \left(\frac{k}{k'}\right)^2 = \frac{E}{E-V_0}$$

For $E \approx V_0^+$, this ratio becomes very large, indicating resonance.

**Resonance Condition**

$$\boxed{k'a = n\pi}$$

**Resonance Width**

Expanding near resonance where $k'_n a = n\pi$ and $E \approx E_n$:

Let $k'a = n\pi + \epsilon$ with $\epsilon \ll 1$:
$$\sin(k'a) = \sin(n\pi + \epsilon) = (-1)^n\epsilon \approx (-1)^n(k' - k'_n)a$$

Using $k'^2 = 2\mu(E-V_0)/\hbar^2$, we have $2k'dk' = 2\mu dE/\hbar^2$, so:
$$k' - k'_n = \frac{\mu(E-E_n)}{\hbar^2 k'_n}$$

Therefore:
$$\sin(k'a) \approx (-1)^n\frac{\mu a(E-E_n)}{\hbar^2 k'_n}$$

The amplitude becomes:
$$|A|^2 = \frac{E_n/V_0}{(E_n-V_0)/V_0 + \frac{\mu^2 a^2}{\hbar^4 k_n'^2}(E-E_n)^2}$$

Comparing with the Breit-Wigner form, the width is:
$$\boxed{\Gamma = \frac{4\hbar(E_n-V_0)}{a\sqrt{2\mu V_0}}}$$

### 2.5 Decaying States and Complex Energy

For a true decaying state, we use outgoing wave boundary conditions.

**Wavefunction Ansatz**

$$\psi(x) = \begin{cases} A\sin(k'x), & 0 < x < a \\ e^{ikx}, & x > a \end{cases}$$

Note: The outgoing wave $e^{ikx}$ in region $x > a$ represents a particle escaping to $+\infty$.

**Matching at $x = a$**

Continuity of $\psi$:
$$A\sin(k'a) = e^{ika}$$

Continuity of $\psi'$:
$$Ak'\cos(k'a) = ike^{ika}$$

Dividing:
$$k'\cot(k'a) = ik$$

**Complex Solution**

Since $k = \sqrt{2\mu E}/\hbar$ and $k' = \sqrt{2\mu(E-V_0)}/\hbar$ are related through energy, and the right side is imaginary while the left side is real for real $E$, we need complex energy.

Near resonance where $k'a = n\pi + \epsilon$:
$$\cot(k'a) \approx -\epsilon = -(k' - k'_n)a$$

So:
$$-k'(k' - k'_n)a = ik$$

For $k \ll k'$ (low energy outside compared to inside):
$$k' - k'_n = -\frac{ik}{k'a}$$

The energy is:
$$E = V_0 + \frac{\hbar^2 k'^2}{2\mu} = V_0 + \frac{\hbar^2 k_n'^2}{2\mu} - i\frac{\hbar^2 k_n k}{\mu a}$$

Writing $E = E_n - i\Gamma/2$:
$$\boxed{\Gamma = \frac{2\hbar^2 k_n}{\mu a}}$$

**Time Evolution**

With complex energy:
$$\psi(t) \sim e^{-iEt/\hbar} = e^{-iE_n t/\hbar}e^{-\Gamma t/(2\hbar)}$$

Probability decays exponentially:
$$|\psi(t)|^2 \sim e^{-\Gamma t/\hbar} = e^{-t/\tau}$$

where the lifetime is:
$$\boxed{\tau = \frac{\hbar}{\Gamma}}$$

This is consistent with the energy-time uncertainty principle.

### 2.6 Connection Between Resonance and Bound States

As the barrier height $V_0 \to \infty$:
- The resonance energy $E_r$ approaches the bound state energy $E_b$
- The width $\Gamma \to 0$
- The lifetime $\tau \to \infty$

**Unified Picture:**
- **Bound state**: Infinite barrier height (particle permanently trapped)
- **Resonance**: Finite barrier (particle temporarily trapped)
- **Scattering state**: No barrier or energy far from resonance

---

## Part III: Multi-Channel Resonance and Scattering Theory

### 3.1 Double-Barrier Transmission

Consider a symmetric square well that acts as a double-barrier structure:

$$V(x) = \begin{cases} -V_0, & |x| < a \\ 0, & |x| > a \end{cases}$$

**Incident Wave Setup**

For $E > 0$, a wave incident from the left has the form:

$$\psi(x) = \begin{cases} e^{ikx} + Re^{-ikx}, & x < -a \\ Ae^{ik'x} + Be^{-ik'x}, & |x| < a \\ Se^{ikx}, & x > a \end{cases}$$

where $k = \sqrt{2\mu E}/\hbar$ and $k' = \sqrt{2\mu(E+V_0)}/\hbar$.

**Matching at $x = -a$**

Continuity of $\psi$:
$$e^{-ika} + Re^{ika} = Ae^{-ik'a} + Be^{ik'a}$$

Continuity of $\psi'$:
$$ike^{-ika} - ike^{ika} = ik'Ae^{-ik'a} - ik'Be^{ik'a}$$

**Matching at $x = a$**

Continuity of $\psi$:
$$Ae^{ik'a} + Be^{-ik'a} = Se^{ika}$$

Continuity of $\psi'$:
$$ik'Ae^{ik'a} - ik'Be^{-ik'a} = ikSe^{ika}$$

**Solving for Transmission Amplitude**

After algebraic manipulation (eliminating $A$, $B$, and $R$):

$$Se^{2ika} = \left[\cos(2k'a) - \frac{i}{2}\left(\frac{k}{k'} + \frac{k'}{k}\right)\sin(2k'a)\right]^{-1}$$

**Transmission Coefficient**

$$T = |S|^2 = \left[1 + \frac{V_0^2}{4E(E+V_0)}\sin^2(2k'a)\right]^{-1}$$

**Resonance Condition**

When $\sin(2k'a) = 0$, i.e., $2k'a = n\pi$:
$$T = 1$$

**Resonance Energies**

$$E_n = -V_0 + \frac{\pi^2\hbar^2}{8\mu a^2}n^2$$

For small $n$ where $E_n < 0$, these are bound states. For large $n$ where $E_n > 0$, these are resonance states.

### 3.2 Partial Wave Analysis

For scattering from a central potential, the plane wave can be expanded in spherical harmonics:

$$e^{ikz} = \sum_{l=0}^{\infty}(2l+1)i^j j_l(kr)P_l(\cos\theta)$$

**Asymptotic Behavior**

At large $r$, using $j_l(kr) \sim \sin(kr - l\pi/2)/(kr)$:

$$e^{ikz} \xrightarrow{r\to\infty} \sum_{l=0}^{\infty}(2l+1)i^l \frac{\sin(kr - l\pi/2)}{kr}P_l(\cos\theta)$$

**Scattered Wavefunction**

The full wavefunction including scattering:
$$\psi(\mathbf{r}) \xrightarrow{r\to\infty} e^{ikz} + f(\theta)\frac{e^{ikr}}{r}$$

**Partial Wave Expansion**

$$f(\theta) = \sum_{l=0}^{\infty}(2l+1)f_l P_l(\cos\theta)$$

**Partial Wave Amplitude**

$$f_l = \frac{e^{2i\delta_l} - 1}{2ik} = \frac{1}{k\cot\delta_l - ik}$$

where $\delta_l$ is the phase shift for angular momentum $l$.

**Total Cross-Section**

$$\sigma_{\text{tot}} = \int|f(\theta)|^2d\Omega = \frac{4\pi}{k^2}\sum_{l=0}^{\infty}(2l+1)\sin^2\delta_l$$

This is the partial wave expansion of the total cross-section.

### 3.3 Low-Energy Scattering and Scattering Length

At low energies where $ka \ll 1$, only s-wave ($l = 0$) contributes significantly to scattering.

**Scattering Length Definition**

The s-wave scattering length $a_s$ is defined by:
$$\lim_{k\to 0} k\cot\delta_0 = -\frac{1}{a_s}$$

**Low-Energy Scattering Amplitude**

$$f_0 = \frac{1}{k\cot\delta_0 - ik} \xrightarrow{k\to 0} \frac{1}{-1/a_s - ik} \xrightarrow{k\to 0} -a_s$$

**Low-Energy Cross-Section**

$$\sigma_0 = 4\pi|f_0|^2 \xrightarrow{k\to 0} 4\pi a_s^2$$

**Connection to Bound States**

If the potential supports a weakly bound state with energy $E_b = -\hbar^2\beta^2/(2\mu)$, the scattering length is:

$$\boxed{a_s = \frac{1}{\beta} = \frac{\hbar}{\sqrt{-2\mu E_b}}}$$

**Physical Interpretation:** The scattering length measures the spatial extent of the bound state. For a loosely bound state (small $|E_b|$), the scattering length is large, leading to a large low-energy cross-section. This explains why low-energy nucleon-nucleon scattering has a large cross-section—the deuteron is a very loosely bound state.

### 3.4 Levinson's Theorem

![Levinson's Theorem](/images/qm-notes/levinson-theorem.png)
*Figure 5: Illustration of Levinson's theorem showing the difference in zero-energy phase shifts for potentials with and without bound states. Each bound state contributes $\pi$ to $\delta_0(0)$.*

**Theorem Statement**

The phase shift at zero energy is related to the number of bound states by:
$$\boxed{\delta_l(0) = n_l\pi}$$

where $n_l$ is the number of bound states with angular momentum $l$.

**Proof Outline**

Consider the Jost function $f_l(k)$, which is analytic in the upper half of the complex $k$-plane. Bound states correspond to zeros of $f_l(k)$ on the positive imaginary axis at $k_n = i\kappa_n$.

The phase shift is related to the argument of the Jost function:
$$\delta_l(k) = -\arg f_l(k)$$

As $k$ varies from $0$ to $\infty$ along the real axis, the change in the argument of $f_l(k)$ is related to the number of zeros in the upper half-plane by the argument principle.

Since $f_l(k) \to 1$ as $k \to \infty$ (no scattering at infinite energy), we have $\delta_l(\infty) = 0$.

The number of bound states equals the change in phase divided by $\pi$:
$$n_l = \frac{1}{\pi}[\delta_l(0) - \delta_l(\infty)] = \frac{\delta_l(0)}{\pi}$$

Therefore:
$$\delta_l(0) = n_l\pi$$

**Physical Significance**
- Each bound state contributes $\pi$ to the zero-energy phase shift
- The phase shift encodes information about the discrete spectrum
- For attractive potentials that support bound states, $\delta_0(0) > 0$

### 3.5 Bound States as Poles of the Scattering Amplitude

**Key Insight:** Bound state energies correspond to poles of the scattering amplitude in the complex momentum plane.

For s-wave scattering:
$$f_0(k) = \frac{1}{k\cot\delta_0 - ik}$$

**Pole Condition**

A pole occurs when:
$$k\cot\delta_0 = ik$$

For a bound state, the energy is negative: $E = -|E| < 0$, so:
$$k = \frac{\sqrt{2\mu E}}{\hbar} = i\frac{\sqrt{2\mu|E|}}{\hbar} = i\beta$$

where $\beta > 0$.

At $k = i\beta$:
$$i\beta\cot\delta_0(i\beta) = i(i\beta) = -\beta$$

$$\cot\delta_0(i\beta) = i$$

This condition is satisfied for potentials that support bound states. The residue of the pole is related to the normalization of the bound state wavefunction.

**Resonances as Poles**

Resonances correspond to poles in the complex $k$-plane near the real axis (in the lower half-plane for decaying states with the physical sheet choice). The proximity to the real axis determines the width $\Gamma$.

### 3.6 Unitarity Bound and Resonant Scattering

**Optical Theorem**

From probability conservation:
$$\sigma_{\text{tot}} = \frac{4\pi}{k}\text{Im}f(0)$$

**Partial Wave Unitarity**

For a single partial wave, the maximum cross-section occurs when $\sin^2\delta_l = 1$ (i.e., $\delta_l = \pi/2$):

$$\sigma_l^{\text{max}} = \frac{4\pi}{k^2}(2l+1)$$

This is called the **unitarity limit**.

**Resonant Scattering**

Near a resonance, the phase shift behaves as:
$$\tan\delta_l(E) = \frac{\Gamma/2}{E_r - E}$$

At $E = E_r$:
$$\delta_l = \frac{\pi}{2}$$

The cross-section reaches its maximum value:
$$\sigma_l(E_r) = \frac{4\pi}{k^2}(2l+1)$$

The rapid change of the phase shift by $\pi$ as energy passes through $E_r$ is the hallmark of resonant scattering.

---

## Summary and Key Formulas

### Bound State Existence

| Dimension | Condition |
|-----------|-----------|
| 1D (symmetric well) | At least one bound state always exists |
| 1D (semi-infinite) | Requires $8\mu V_0 a^2 > \pi^2\hbar^2$ |
| 3D (spherical well) | Requires $8\mu V_0 a^2 > \pi^2\hbar^2$ |

### Key Equations

**Matching Conditions:**
- Even parity (1D symmetric well): $k\tan(ka) = \kappa$
- Odd parity (1D symmetric well): $-k\cot(ka) = \kappa$

**Delta Potential:**
- Energy: $E = -\frac{\mu\gamma^2}{2\hbar^2}$
- Wavefunction: $\psi(x) = \sqrt{\frac{\mu\gamma}{\hbar^2}}e^{-\mu\gamma|x|/\hbar^2}$

**Resonance Phenomena:**
- Breit-Wigner formula: $T(E) = \frac{\Gamma^2/4}{(E-E_r)^2 + \Gamma^2/4}$
- Lifetime-width relation: $\tau = \hbar/\Gamma$
- Phase shift near resonance: $\tan\delta = \frac{\Gamma/2}{E_r - E}$

**Scattering Theory:**
- Scattering length: $a_s = -\lim_{k\to 0}f_0(k)$
- Low-energy cross-section: $\sigma_0 = 4\pi a_s^2$
- Levinson's theorem: $\delta_l(0) = n_l\pi$
- Unitarity limit: $\sigma_l^{\text{max}} = \frac{4\pi(2l+1)}{k^2}$

### Unified Picture

Bound states, resonances, and scattering states are unified through the analytic properties of the scattering amplitude:
- **Bound states**: Poles on the positive imaginary $k$-axis ($k = i\beta$, $\beta > 0$)
- **Resonances**: Poles near the real axis in the complex $k$-plane
- **Scattering states**: Behavior along the real $k$-axis

This mathematical unity reflects the deep physical connection between these quantum mechanical phenomena.
