---
title: "Bound States, Resonances, and Scattering: Notes on Zeng Jinyan's Quantum Mechanics Special Topics (Chapters 3-5)"
description: "Detailed analysis of bound state existence conditions, resonance states, and scattering theory from Zeng Jinyan's classic quantum mechanics textbook"
date: 2026-04-02
tags: ["quantum mechanics", "bound states", "resonance", "scattering theory", "Zeng Jinyan", "USTC"]
category: "quantum-mechanics"
math: true
---

# Bound States, Resonances, and Scattering Theory

*Notes from Zeng Jinyan's "Quantum Mechanics Special Topics Analysis" (量子力学专题分析), Chapters 3-5*

These three chapters from Zeng Jinyan's classic text form a coherent narrative about the deep connections between bound states, resonance states, and scattering processes in quantum mechanics. The discussion progresses from the existence conditions for bound states in one-dimensional potentials, through the nature of resonance states and their relationship to bound states, to the general scattering theory framework that unifies these concepts.

---

## Part I: Existence Conditions for Bound States (Chapter 3)

### 3.1 One-Dimensional Symmetric Square Well

The chapter begins with the canonical example: a symmetric finite square well potential defined by:

$$V(x) = \begin{cases} -W_0, & |x| < a \\ 0, & |x| > a \end{cases}$$

**Key insight**: The existence of bound states ($E < 0$) depends critically on the relationship between the well depth $W_0$ and width $a$.

For bound states, the Schrödinger equation yields solutions with:
- **Even parity states**: $\psi(x) = A\cos(k'x)$ inside the well
- **Odd parity states**: $\psi(x) = A\sin(k'x)$ inside the well

where $k' = \sqrt{2\mu(E+W_0)}/\hbar$ and $\beta = \sqrt{-2\mu E}/\hbar$.

The boundary conditions at $x = \pm a$ give the transcendental equations:

**Even parity**: $\beta = k'\tan(k'a)$  
**Odd parity**: $\beta = -k'\cot(k'a)$

Combined with the constraint: $\beta^2 + k'^2 = 2\mu W_0/\hbar^2$

**Critical result**: The even parity state always exists (at least one bound state), but the odd parity state requires:
$$8\mu W_0 a^2 \geq \pi^2\hbar^2$$

This gives the minimum well depth/width product needed for odd parity bound states.

### 3.2 One-Dimensional Semi-Infinite Square Well

For the potential:
$$V(x) = \begin{cases} \infty, & x < 0 \\ -W_0, & 0 < x < a \\ 0, & x > a \end{cases}$$

The boundary condition at $x = 0$ ($\psi(0) = 0$) forces the wavefunction to be a sine function inside the well. The matching conditions give:
$$\beta = -k'\cot(k'a)$$

Interestingly, this requires $8\mu W_0 a^2 \geq \pi^2\hbar^2$ for *any* bound state to exist—a stricter condition than the symmetric well due to the infinite wall constraining the wavefunction.

### 3.3 δ-Potential Well

For $V(x) = -\gamma\delta(x)$ with $\gamma > 0$:

**Exact solution**: There exists exactly one bound state with energy:
$$E = -\frac{\mu\gamma^2}{2\hbar^2}$$

The normalized wavefunction is:
$$\psi(x) = \frac{1}{\sqrt{L}}e^{-|x|/L}, \quad L = \frac{\hbar^2}{\mu\gamma}$$

where $L$ is the characteristic length scale. This shows the fundamental result that in 1D, an attractive potential (no matter how weak) always supports at least one bound state.

### 3.4 Two-Dimensional and Three-Dimensional Cases

**Theorem**: For central potentials in 3D, the lowest energy state is always an s-state ($l = 0$).

The radial equation for $l = 0$ with the substitution $R(r) = \chi(r)/r$ becomes:
$$-\frac{\hbar^2}{2\mu}\frac{d^2\chi}{dr^2} + V(r)\chi = E\chi$$

This is mathematically equivalent to a 1D problem with an effective potential and the boundary condition $\chi(0) = 0$.

**Key difference from 1D**: In 3D, a potential well must exceed a certain depth to support bound states. For a spherical square well:
$$V(r) = \begin{cases} -W_0, & r < a \\ 0, & r > a \end{cases}$$

The condition for at least one bound state is related to the dimensionless parameter:
$$R = \frac{\sqrt{2\mu W_0}a}{\hbar} > \frac{\pi}{2}$$

### 3.5 The General Theorem: When Do Bound States Exist?

**Theorem (Zeng Jinyan)**: For a one-dimensional potential $V(x) < 0$ everywhere with $V(x) \to 0$ as $|x| \to \infty$, there exists at least one bound state.

The proof uses the variational principle: construct a trial wavefunction and show that the expectation value of the Hamiltonian can be made negative.

**Corollary**: For 3D spherical wells, the condition is more stringent. A shallow well may not support any bound state—this is a crucial difference between 1D and 3D quantum mechanics.

---

## Part II: Resonance States and Quasi-Bound States (Chapter 4)

### 4.1 Physical Picture of Resonance States

**Definition**: A resonance state is a non-stationary state where the particle has a high probability of being "inside" the potential region, even though $E > 0$ (classically allowed to escape).

**Key characteristics**:
1. The particle remains in the potential region for a long time $\tau$
2. The energy is not sharply defined—there is a width $\Gamma$
3. The energy-time uncertainty relation: $\tau\Gamma \sim \hbar/2$

**Physical interpretation**: When $E$ approaches certain "resonant energies," the transmission coefficient or the probability of finding the particle inside the well becomes large.

### 4.2 Resonance in a Finite Square Well with Barriers

Consider a potential with a well region surrounded by finite barriers:
$$V(x) = \begin{cases} 0, & 0 < x < a \ V_0, & a < x < a+b \ 0, & x > a+b \ \infty, & x < 0 \end{cases}$$

For $E < V_0$, the particle can tunnel through the barrier. When the energy satisfies certain conditions, we get resonant enhancement of the wavefunction inside the well.

**Resonance condition**: The phase of the wavefunction inside the well matches the phase after tunneling, creating constructive interference.

Mathematically, for a symmetric double-barrier structure, the resonance condition is related to:
$$2k'a = n\pi$$

where $k' = \sqrt{2\mu E}/\hbar$ inside the well.

### 4.3 Resonance Above a Potential Barrier

Consider a particle with energy $E > V_0$ incident on a potential barrier:
$$V(x) = \begin{cases} 0, & x < 0 \ V_0, & 0 < x < a \ 0, & x > a \end{cases}$$

**Counterintuitive result**: Even when $E > V_0$ (classically allowed everywhere), there can be resonant reflection!

The transmission coefficient shows oscillatory behavior:
$$T = \left[1 + \frac{V_0^2}{4E(E-V_0)}\sin^2(k'a)\right]^{-1}$$

where $k' = \sqrt{2\mu(E-V_0)}/\hbar$.

**Resonant transmission** occurs when $k'a = n\pi$, giving $T = 1$ (perfect transmission even with a barrier present!).

### 4.4 Decaying States and Complex Energy

To describe true decay (where the particle eventually escapes), we must use the time-dependent Schrödinger equation or apply outgoing wave boundary conditions.

**Key insight**: For a decaying state, the energy is complex:
$$E = E_n - i\frac{\Gamma}{2}$$

The time evolution gives:
$$\psi(t) \sim e^{-iEt/\hbar} = e^{-iE_nt/\hbar}e^{-\Gamma t/(2\hbar)}$$

The probability decays exponentially:
$$|\psi(t)|^2 \sim e^{-\Gamma t/\hbar} = e^{-t/\tau}$$

with lifetime $\tau = \hbar/\Gamma$.

### 4.5 Relationship Between Resonance and Bound States

**Fundamental connection**: As the barrier height $V_0 \to \infty$, resonance states become true bound states.

The resonance energies $E_n$ approach the bound state energies, and the width $\Gamma \to 0$ (infinite lifetime).

**Breit-Wigner formula**: Near a resonance, the cross-section or transmission probability follows:
$$\sigma(E) \propto \frac{\Gamma^2/4}{(E-E_n)^2 + \Gamma^2/4}$$

This Lorentzian lineshape is universal for resonance phenomena.

### 4.6 Metastable States (亚稳态)

**Definition**: A metastable state is a long-lived resonance state with $\Gamma \ll E_n$.

Examples include:
- Alpha decay from nuclei
- Resonant tunneling in semiconductor devices
- Cold atoms in optical traps

The condition for metastability is that the barrier is high and/or wide, making the tunneling probability small.

---

## Part III: Multi-Channel Resonance and Scattering Theory (Chapter 5)

### 5.1 Double-Barrier Resonance

The chapter extends the analysis to a symmetric double-well potential. For $E > 0$, there are no bound states, but resonant transmission can occur.

**Transmission coefficient** for a symmetric square well of width $2a$ and depth $W_0$:
$$T(E) = \left[1 + \frac{W_0^2}{4E(E+W_0)}\sin^2(2k'a)\right]^{-1}$$

**Resonance condition**: $2k'a = n\pi$ gives $T = 1$ (perfect transmission).

The resonant energies are approximately:
$$E_n = -W_0 + \frac{\pi^2\hbar^2}{8\mu a^2}n^2$$

For small $n$, $E_n < 0$ (bound states); for large $n$, $E_n > 0$ (resonance states).

### 5.2 Relationship Between Bound States and Scattering Amplitude

This is one of the most profound results in quantum mechanics.

**Key theorem**: Bound state energies correspond to poles of the scattering amplitude in the complex energy (or momentum) plane.

For s-wave scattering, the scattering amplitude is:
$$f(k) = \frac{1}{k\cot\delta_0 - ik}$$

**Bound states**: Occur when $k = i\beta$ (imaginary momentum), corresponding to poles on the positive imaginary axis in the complex $k$-plane.

**Resonances**: Correspond to poles in the complex $k$-plane near the real axis (in the lower half-plane for decaying states).

### 5.3 Partial Wave Analysis

For scattering from a central potential $V(r)$, the incident plane wave is expanded in spherical waves:
$$e^{ikz} = \sum_{l=0}^{\infty} A_l j_l(kr) Y_{l0}(\theta)$$

The scattering amplitude is:
$$f(\theta) = \sum_{l=0}^{\infty} (2l+1)f_l P_l(\cos\theta)$$

where the partial wave amplitudes are:
$$f_l = \frac{e^{2i\delta_l} - 1}{2ik} = \frac{1}{k\cot\delta_l - ik}$$

**Total cross-section**:
$$\sigma_{\text{tot}} = \frac{4\pi}{k^2}\sum_{l=0}^{\infty}(2l+1)\sin^2\delta_l$$

### 5.4 Low-Energy Scattering and the Scattering Length

At low energies ($ka \ll 1$), only the s-wave ($l = 0$) contributes significantly.

**Scattering length** $a_s$ is defined by:
$$\lim_{k\to 0} k\cot\delta_0 = -\frac{1}{a_s}$$

The low-energy cross-section becomes:
$$\sigma_0 = 4\pi a_s^2$$

**Connection to bound states**: If there is a weakly bound state with binding energy $E_b = -\hbar^2\beta^2/(2\mu)$, then:
$$a_s = \frac{1}{\beta} = \frac{\hbar}{\sqrt{-2\mu E_b}}$$

**Example**: n-p scattering (neutron-proton) has $E_b = -2.23$ MeV (deuteron binding energy), giving $a_s \approx 4.3 \times 10^{-13}$ cm.

### 5.5 Levinson's Theorem

**Theorem**: The phase shift at zero energy is related to the number of bound states:
$$\delta_l(0) = n_l\pi$$

where $n_l$ is the number of bound states with angular momentum $l$.

This is a profound result connecting scattering properties (phase shifts) to the discrete spectrum (bound states).

### 5.6 Resonance in Three Dimensions

**Resonant scattering**: When the energy is near a quasi-bound state energy, the phase shift $\delta_l$ changes rapidly by $\pi$.

Near resonance:
$$\tan\delta_l(E) = \frac{\Gamma/2}{E_r - E}$$

This gives the characteristic behavior:
- $\delta_l$ jumps by $\pi$ at $E = E_r$
- The cross-section peaks at $E = E_r$ with value $\sigma_{\text{max}} = 4\pi(2l+1)/k^2$

The **unitarity limit**: The maximum possible cross-section for a given partial wave.

---

## Summary and Key Takeaways

### 1. Bound State Existence

| Dimension | Condition for Bound States |
|-----------|---------------------------|
| 1D | Any attractive potential supports at least one bound state |
| 2D | Any attractive potential supports at least one bound state (logarithmic divergence) |
| 3D | Potential must be sufficiently deep/strong; shallow wells may have no bound states |

### 2. The Bound State-Resonance-Scattering Continuum

These three phenomena are unified through the analytic properties of the scattering amplitude:

- **Bound states**: Poles on the positive imaginary $k$-axis (real negative $E$)
- **Resonances**: Poles in the complex $k$-plane near the real axis
- **Scattering**: Determined by the phase shifts, which are related to the pole structure

### 3. Key Formulas

**Resonance width-lifetime relation**:
$$\Gamma\tau = \hbar$$

**Breit-Wigner resonance**:
$$\sigma(E) \propto \frac{1}{(E-E_r)^2 + \Gamma^2/4}$$

**Scattering length-bound state connection**:
$$a_s = \frac{1}{\sqrt{-2\mu E_b}/\hbar}$$

**Levinson's theorem**:
$$\delta(0) = n\pi$$

### 4. Physical Applications

1. **Quantum tunneling devices**: Resonant tunneling diodes exploit sharp resonances
2. **Nuclear physics**: Alpha decay as tunneling through Coulomb barrier; compound nucleus resonances
3. **Cold atom physics**: Feshbach resonances allow tuning of scattering lengths
4. **Chemical reactions**: Resonance states as transition states

---

## References

1. Zeng Jinyan (曾谨言). *Quantum Mechanics Special Topics Analysis* (量子力学专题分析), Vol. 1, Chapters 3-5. Higher Education Press.

2. Landau, L.D. & Lifshitz, E.M. *Quantum Mechanics: Non-Relativistic Theory*, Chapter 3 (Scattering Theory).

3. Sakurai, J.J. & Napolitano, J. *Modern Quantum Mechanics*, Chapter 6 (Scattering Theory).

4. Taylor, J.R. *Scattering Theory: The Quantum Theory on Nonrelativistic Collisions*.

---

*These notes were prepared for USTC PhD entrance exam preparation. The original text contains many more detailed derivations and examples.*
