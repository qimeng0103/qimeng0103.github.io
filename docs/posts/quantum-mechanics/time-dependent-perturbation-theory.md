# Time-Dependent Perturbation Theory: From Fermi's Golden Rule to Linear Response

📅 **Date:** 2026-03-31 | 🏷️ **Tags:** Quantum Mechanics, Quantum Optics, Condensed Matter | 📂 **Category:** Quantum Mechanics Notes

---

## Introduction

Time-dependent perturbation theory addresses quantum systems where the Hamiltonian carries explicit time dependence:

$$
\hat{H}(t) = \hat{H}_0 + \hat{V}(t)
$$

Unlike stationary perturbation theory where $\hat{V}$ is static and we seek energy eigenstates, here we track the **dynamical evolution** of quantum states under time-varying influences. This framework underlies quantum optics, scattering theory, and condensed matter response functions.

---

## Part I: The Interaction Picture and Dyson Series

### Interaction Picture Formulation

Separate the Hamiltonian into $\hat{H}_0$ (solvable) and $\hat{V}(t)$ (perturbation). States and operators in the interaction picture are defined via:

$$
\vert \psi_I(t)\rangle = e^{i\hat{H}_0 t/\hbar} \vert \psi_S(t)\rangle, \quad \hat{O}_I(t) = e^{i\hat{H}_0 t/\hbar} \hat{O}_S e^{-i\hat{H}_0 t/\hbar}
$$

The Schrödinger equation becomes:

$$
i\hbar \frac{d}{dt}\vert \psi_I(t)\rangle = \hat{V}_I(t)\vert \psi_I(t)\rangle
$$

where $\hat{V}_I(t) = e^{i\hat{H}_0 t/\hbar} \hat{V}(t) e^{-i\hat{H}_0 t/\hbar}$.

### Time-Evolution Operator

Define $\hat{U}(t, t_0)$ such that $\vert \psi_I(t)\rangle = \hat{U}(t, t_0)\vert \psi_I(t_0)\rangle$. The evolution operator satisfies:

$$
i\hbar \frac{d\hat{U}}{dt} = \hat{V}_I(t)\hat{U}, \quad \hat{U}(t_0, t_0) = \hat{\mathbb{1}}
$$

Integrating iteratively yields the **Dyson series**:

$$
\hat{U}(t, t_0) = \hat{\mathbb{1}} + \sum_{n=1}^{\infty} \left(\frac{-i}{\hbar}\right)^n \int_{t_0}^{t} dt_1 \int_{t_0}^{t_1} dt_2 \cdots \int_{t_0}^{t_{n-1}} dt_n \, \hat{V}_I(t_1)\hat{V}_I(t_2)\cdots\hat{V}_I(t_n)
$$

Or with time-ordering:

$$
\hat{U}(t, t_0) = \mathcal{T} \exp\left(-\frac{i}{\hbar}\int_{t_0}^{t} \hat{V}_I(t') dt'\right)
$$

---

## Part II: First-Order Transition Amplitudes

### Transition Probability

Suppose the system starts in eigenstate $\vert i\rangle$ of $\hat{H}_0$ at $t_0 = 0$. To first order in $\hat{V}$:

$$
\vert \psi_I(t)\rangle \approx \vert i\rangle + \frac{1}{i\hbar}\int_0^t \hat{V}_I(t')\vert i\rangle dt'
$$

The amplitude for transition to state $\vert f\rangle$ ($f \neq i$) is:

$$
c_f^{(1)}(t) = \langle f\vert \psi_I(t)\rangle = \frac{1}{i\hbar}\int_0^t \langle f\vert\hat{V}_I(t')\vert i\rangle dt'
$$

With $\hat{V}_I(t) = e^{i\hat{H}_0 t/\hbar}\hat{V}(t)e^{-i\hat{H}_0 t/\hbar}$ and $E_i$, $E_f$ the unperturbed energies:

$$
c_f^{(1)}(t) = \frac{1}{i\hbar}\int_0^t e^{i\omega_{fi}t'} V_{fi}(t') dt'
$$

where $\omega_{fi} = (E_f - E_i)/\hbar$ and $V_{fi}(t) = \langle f\vert\hat{V}(t)\vert i\rangle$.

### Harmonic Perturbation

For monochromatic driving $\hat{V}(t) = \hat{V}e^{-i\omega t} + \hat{V}^\dagger e^{i\omega t}$:

$$
c_f^{(1)}(t) = \frac{1}{\hbar}\left[\frac{e^{i(\omega_{fi}-\omega)t} - 1}{\omega_{fi} - \omega} V_{fi} + \frac{e^{i(\omega_{fi}+\omega)t} - 1}{\omega_{fi} + \omega} V_{fi}^*\right]
$$

The first term dominates when $\omega \approx \omega_{fi}$ (absorption); the second when $\omega \approx -\omega_{fi}$ (stimulated emission).

---

## Part III: Fermi's Golden Rule

### Constant Perturbation

For $\hat{V}(t) = \hat{V}\theta(t)$ turned on at $t=0$:

$$
c_f^{(1)}(t) = \frac{V_{fi}}{i\hbar}\int_0^t e^{i\omega_{fi}t'} dt' = \frac{V_{fi}}{\hbar\omega_{fi}}(1 - e^{i\omega_{fi}t})
$$

The transition probability is:

$$
P_{i\to f}(t) = \vert c_f^{(1)}(t)\vert^2 = \frac{4\vert V_{fi}\vert^2}{\hbar^2}\frac{\sin^2(\omega_{fi}t/2)}{\omega_{fi}^2}
$$

For large $t$, using $\sin^2(xt/2)/x^2 \to \frac{\pi t}{2}\delta(x)$:

$$
P_{i\to f}(t) \approx \frac{2\pi t}{\hbar}\vert V_{fi}\vert^2 \delta(E_f - E_i)
$$

### Transition Rate

The transition rate $W_{i\to f} = dP/dt$ for transitions into a continuum of final states with density $\rho(E_f)$:

$$
\boxed{W_{i\to f} = \frac{2\pi}{\hbar}\vert V_{fi}\vert^2 \rho(E_f)}
$$

This is **Fermi's Golden Rule**—the fundamental result for transitions between discrete and continuous spectra.

---

## Part IV: Propagating States and Scattering Theory

### Lippmann-Schwinger Equation

For scattering where $\hat{H}_0$ describes free particles and $\hat{V}$ is a static potential, stationary scattering states satisfy:

$$
\vert \psi^{(\pm)}\rangle = \vert \phi\rangle + \frac{1}{E - \hat{H}_0 \pm i\epsilon}\hat{V}\vert \psi^{(\pm)}\rangle
$$

where $\vert \phi\rangle$ is the incident plane wave with energy $E$, and $\pm i\epsilon$ selects outgoing $(+)$ or incoming $(-)$ boundary conditions.

### Time-Dependent Scattering

For time-dependent potentials $\hat{V}(t)$, the S-matrix connects asymptotic states:

$$
S_{fi} = \lim_{\substack{t_+ \to +\infty \\ t_- \to -\infty}} \langle f\vert \hat{U}(t_+, t_-)\vert i\rangle
$$

To first order:

$$
S_{fi}^{(1)} = -\frac{i}{\hbar}\int_{-\infty}^{\infty} e^{i\omega_{fi}t} \langle f\vert\hat{V}(t)\vert i\rangle dt
$$

This Fourier-transform relationship between time-dependent potential and S-matrix elements is central to scattering calculations.

### Wave Packet Dynamics

For propagating wave packets (not stationary eigenstates), the time evolution involves both phase accumulation and shape distortion:

$$
\psi(x,t) = \int \frac{dk}{\sqrt{2\pi}} \phi(k) e^{ikx - iE(k)t/\hbar}
$$

Under perturbation, group velocity $v_g = dE/dk$ and wave packet spreading become modified. The WKB approximation connects this to classical trajectories in slowly varying potentials.

---

## Part V: Linear Response Theory and Kubo Formula

### Response Functions

In condensed matter, we probe systems with weak external fields and measure linear response. The general framework: perturbation $\hat{V}(t) = \hat{A}F(t)$ couples operator $\hat{A}$ to external field $F(t)$; we measure response of observable $\hat{B}$.

The first-order change in $\langle\hat{B}\rangle$ is:

$$
\delta\langle\hat{B}(t)\rangle = \int_{-\infty}^{\infty} \chi_{BA}(t-t')F(t') dt'
$$

where $\chi_{BA}(\tau)$ is the **retarded response function**.

### Kubo Formula

From first-order perturbation theory, the response function is:

$$
\boxed{\chi_{BA}(t) = -\frac{i}{\hbar}\theta(t)\langle[\hat{B}_I(t), \hat{A}_I(0)]\rangle_0}
$$

where $\langle\cdots\rangle_0$ denotes thermal/equilibrium average over $\hat{H}_0$, and $[\cdot,\cdot]$ is the commutator.

The frequency-domain version, via Fourier transform:

$$
\chi_{BA}(\omega) = \int_0^{\infty} e^{i\omega t}\chi_{BA}(t)dt
$$

### Fluctuation-Dissipation Theorem

The imaginary part of $\chi(\omega)$ describes dissipation. It relates to equilibrium fluctuations:

$$
\text{Im}\,\chi_{AA}(\omega) = \frac{1}{2\hbar}(1 - e^{-\beta\hbar\omega})S_{AA}(\omega)
$$

where $S_{AA}(\omega)$ is the power spectrum of fluctuations in $\hat{A}$.

For conductivity (Kubo-Greenwood), $\hat{A} = \hat{j}_\alpha$ (current), giving:

$$
\sigma_{\alpha\beta}(\omega) = \frac{1}{\hbar\omega}\int_0^{\infty} e^{i\omega t}\langle[\hat{j}_\alpha(t), \hat{j}_\beta(0)]\rangle dt
$$

---

## Part VI: Quantum Optics Framework

### Jaynes-Cummings Model

The paradigmatic quantum optics system: a two-level atom (states $\vert g\rangle$, $\vert e\rangle$ with spacing $\hbar\omega_0$) coupled to a single cavity mode (frequency $\omega$).

$$
\hat{H} = \frac{\hbar\omega_0}{2}\hat{\sigma}_z + \hbar\omega\hat{a}^\dagger\hat{a} + \hbar g(\hat{\sigma}_+\hat{a} + \hat{\sigma}_-\hat{a}^\dagger)
$$

In the **rotating wave approximation** (RWA), counter-rotating terms $\hat{\sigma}_+\hat{a}^\dagger$ and $\hat{\sigma}_-\hat{a}$ are dropped—valid when $g \ll \omega, \omega_0$.

### Dressed States

The eigenstates of the coupled system (dressed states) are superpositions of bare atom-photon states:

$$
\vert \pm, n\rangle = \frac{1}{\sqrt{2}}(\vert e, n\rangle \pm \vert g, n+1\rangle)
$$

with energies $E_{\pm,n} = \hbar\omega(n+1) \pm \frac{\hbar}{2}\sqrt{4g^2(n+1) + \Delta^2}$, where $\Delta = \omega_0 - \omega$ is the detuning.

### Input-Output Theory

For open quantum systems (cavity with loss $\kappa$, atom with decay $\gamma$), the Heisenberg-Langevin approach gives:

$$
\frac{d\hat{a}}{dt} = -i[\hat{a}, \hat{H}] - \frac{\kappa}{2}\hat{a} + \sqrt{\kappa}\hat{a}_{\text{in}}(t)
$$

The input field $\hat{a}_{\text{in}}$ satisfies $[\hat{a}_{\text{in}}(t), \hat{a}_{\text{in}}^\dagger(t')] = \delta(t-t')$. The output field relates via:

$$
\hat{a}_{\text{out}} = \hat{a}_{\text{in}} + \sqrt{\kappa}\hat{a}
$$

This framework connects cavity QED to scattering theory, with the cavity acting as a frequency-dependent beam splitter for photons.

### Weak Drive Limit

For weak probe fields, linear response applies. The cavity transmission spectrum:

$$
T(\omega_p) = \left\vert\frac{\kappa/2}{\kappa/2 - i(\omega_p - \omega_c) + g^2/\gamma}\right\vert^2
$$

shows vacuum Rabi splitting: two peaks separated by $2g$ when the atom is resonant with the cavity.

---

## Summary and Connections

| Domain | Key Quantity | Perturbation Theory Role |
|--------|--------------|--------------------------|
| Atomic transitions | $W_{i\to f}$ (transition rate) | Fermi's Golden Rule for spontaneous/absorbed photons |
| Scattering | $S$-matrix elements | Born approximation from Dyson series |
| Condensed matter | $\chi_{BA}(\omega)$ (susceptibility) | Kubo formula connects response to correlations |
| Quantum optics | Dressed state spectra | Jaynes-Cummings diagonalization in limited subspace |

The unifying theme: weak perturbations enable systematic approximation, but the choice of basis (bound vs. scattering states, bare vs. dressed) determines the efficiency and physical transparency of the calculation.

---

## References

1. Sakurai, J.J. & Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. (Cambridge University Press, 2020). Chapter 2, 5

2. Scully, M.O. & Zubairy, M.S. *Quantum Optics* (Cambridge University Press, 1997). Chapters 5–6

3. Mahan, G.D. *Many-Particle Physics*, 3rd ed. (Springer, 2000). Chapter 3 (Linear Response)

4. Gerry, C.C. & Knight, P.L. *Introductory Quantum Optics* (Cambridge University Press, 2005). Chapters 3–4, 7
