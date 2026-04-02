# Bound States, Resonances, and Scattering: Insights from Zeng Jinyan's Quantum Mechanics

📅 **Date:** 2026-04-02 | 🏷️ **Tags:** Quantum Mechanics, Scattering Theory, Bound States, Resonances | 📂 **Category:** Quantum Mechanics Notes

---

## Introduction

This note synthesizes key insights from Chapters 3, 4, and 5 of Zeng Jinyan's *Quantum Mechanics: Special Topics Analysis* (量子力学专题分析), focusing on three interconnected quantum phenomena: **bound states in potential wells**, **resonance states**, and **scattering theory**. These topics form the foundation of understanding quantum mechanical behavior in various potential landscapes.

---

## Part I: Bound States in 1D Potential Wells (Chapter 3)

### The Infinite Square Well Revisited

For a particle in an infinite square well of width $a$:

$$
V(x) = \begin{cases}
0, & 0 < x < a \\
\infty, & \text{otherwise}
\end{cases}
$$

The normalized eigenfunctions are:

$$
\psi_n(x) = \sqrt{\frac{2}{a}} \sin\left(\frac{n\pi x}{a}\right), \quad n = 1, 2, 3, ...
$$

With eigenenergies:

$$
E_n = \frac{n^2\pi^2\hbar^2}{2ma^2}
$$

**Key Physical Insight:** The ground state ($n=1$) has no nodes, and each excited state acquires one additional node. The energy spacing increases quadratically with $n$.

### Finite Square Well: Even and Odd Parity States

For a finite square well with depth $V_0$ and width $2a$:

$$
V(x) = \begin{cases}
-V_0, & |x| < a \\
0, & |x| > a
\end{cases}
$$ 

The transcendental equations for bound states ($E < 0$) are:

**Even parity:** $\xi \tan \xi = \eta$

**Odd parity:** $-\xi \cot \xi = \eta$

Where $\xi = k'a$, $\eta = \kappa a$, and $k' = \sqrt{2\mu(V_0 - |E|)}/\hbar$, $\kappa = \sqrt{2\mu|E|}/\hbar$.

**Critical Observation:** Not all potential wells support bound states. For a symmetric finite well:
- There is always at least one even-parity bound state (no matter how shallow)
- Odd-parity states only appear when $V_0 a^2 \geq \frac{\pi^2\hbar^2}{8\mu}$

### The Delta Function Potential

For an attractive delta potential $V(x) = -\gamma\delta(x)$ with $\gamma > 0$:

There exists exactly **one bound state** with:

$$
E = -\frac{\mu\gamma^2}{2\hbar^2}
$$

And wavefunction:

$$
\psi(x) = \sqrt{\frac{\mu\gamma}{\hbar^2}} e^{-\mu\gamma|x|/\hbar^2}
$$

The binding energy scales with $\gamma^2$, highlighting the singular nature of the delta potential.

---

## Part II: Resonance States and Quasi-Bound States (Chapter 4)

### What is a Resonance?

A resonance is a **meta-stable state** that behaves similarly to a bound state but eventually decays. Unlike true bound states with $E < 0$ and infinite lifetime, resonances have complex energies:

$$
E = E_0 - i\frac{\Gamma}{2}
$$

Where $\Gamma$ is the decay width, related to the lifetime by $\tau = \hbar/\Gamma$.

### The Double-Barrier Resonance

Consider a particle incident on a double-barrier potential. When the energy matches a quasi-bound level between the barriers:

1. The particle tunnels through the first barrier
2. Is temporarily trapped between the barriers
3. Eventually tunnels out through the second barrier

The transmission coefficient exhibits a sharp peak:

$$
T(E) \approx \frac{\Gamma^2/4}{(E - E_0)^2 + \Gamma^2/4}
$$

This is the **Breit-Wigner resonance formula**.

### Physical Interpretation

Near a resonance:
- The phase shift $\delta(E)$ changes rapidly by $\pi$
- The time delay is proportional to $d\delta/dE$
- The density of states shows a Lorentzian peak

**Key Insight:** Resonances represent **virtual bound states**—states that would be bound if the barriers were infinite, but become leaky due to finite barrier penetration.

---

## Part III: Scattering Theory (Chapter 5)

### Partial Wave Analysis

For spherically symmetric potentials, the scattering wavefunction expands as:

$$
\psi(\mathbf{r}) = \sum_{l=0}^{\infty} \frac{u_l(r)}{r} P_l(\cos\theta)
$$

Each partial wave satisfies:

$$
\frac{d^2u_l}{dr^2} + \left[k^2 - \frac{l(l+1)}{r^2} - \frac{2\mu V(r)}{\hbar^2}\right]u_l = 0
$$

### Phase Shifts and Scattering Amplitude

The asymptotic behavior defines the phase shift $\delta_l$:

$$
u_l(r) \xrightarrow{r\to\infty} \sin(kr - l\pi/2 + \delta_l)
$$

The differential cross section:

$$
\frac{d\sigma}{d\Omega} = |f(\theta)|^2 = \left|\frac{1}{k}\sum_{l=0}^{\infty}(2l+1)e^{i\delta_l}\sin\delta_l P_l(\cos\theta)\right|^2
$$

And total cross section:

$$
\sigma_{\text{tot}} = \frac{4\pi}{k^2}\sum_{l=0}^{\infty}(2l+1)\sin^2\delta_l
$$

### Low-Energy Scattering: The s-Wave Dominance

At low energies ($ka \ll 1$), only the s-wave ($l=0$) contributes significantly. The scattering amplitude becomes:

$$
f(\theta) \approx -\frac{1}{k\cot\delta_0} = -\frac{1}{k^2 + (-1/a_s)}
$$

Where $a_s$ is the **scattering length**.

**Key Results:**
- For hard sphere scattering: $a_s = b$ (sphere radius), $\sigma_0 = 4\pi b^2$
- For attractive potentials: $a_s$ can be positive or negative, with $|a_s| \to \infty$ near bound state formation

### The Levinson Theorem

The theorem relates the number of bound states $n_l$ to the zero-energy phase shift:

$$
\delta_l(0) = n_l \pi
$$

This profound connection between bound states and scattering demonstrates that scattering experiments can reveal information about bound state spectra.

---

## Connections Between the Three Topics

| Aspect | Bound States | Resonances | Scattering |
|--------|--------------|------------|------------|
| Energy | $E < 0$, discrete | $E > 0$, complex | $E > 0$, continuous |
| Lifetime | Infinite | Finite ($\tau = \hbar/\Gamma$) | Temporary interaction |
| Wavefunction | Normalizable ($\int|\psi|^2 = 1$) | Quasi-normalizable | Incoming + outgoing waves |
| Physical Role | Stable configurations | Meta-stable states | Probe of interaction |

---

## Exam-Oriented Insights

**Quick Recognition Guide:**

1. **Delta potential bound state:** Always ask: "Is it attractive ($\gamma > 0$) or repulsive?" Only attractive supports bound states.

2. **Finite well analysis:** Draw the $\xi$-$
abla$ diagram mentally. Even states always exist; odd states require sufficient depth.

3. **Resonance identification:** Look for sharp peaks in cross-sections, rapid phase shift variations, or time delays.

4. **Scattering regime:** Before calculating, estimate $ka$:
   - $ka \ll 1$: s-wave dominant, use effective range theory
   - $ka \sim 1$: Several partial waves needed
   - $ka \gg 1$: Many partial waves, semiclassical approximations

---

## References

1. Zeng Jinyan (曾谨言). *Quantum Mechanics: Special Topics Analysis* (量子力学专题分析), Vol. 1. Science Press, 1987.
2. Sakurai, J.J. *Modern Quantum Mechanics*, 3rd ed. Cambridge, 2020.
3. Landau, L.D. & Lifshitz, E.M. *Quantum Mechanics: Non-Relativistic Theory*, 3rd ed. Pergamon, 1977.

---

**Related Reading:**
- [Stationary Perturbation Theory](./stationary-perturbation-theory)
- [Time-Dependent Perturbation Theory](./time-dependent-perturbation-theory)
