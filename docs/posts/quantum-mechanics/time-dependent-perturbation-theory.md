# Time-Dependent Perturbation Theory: From Fermi's Golden Rule to Linear Response

📅 **Date:** 2026-03-31 | 🏷️ **Tags:** Quantum Mechanics, Condensed Matter, Statistical Mechanics | 📂 **Category:** Quantum Mechanics Notes

---

## Introduction

Time-dependent perturbation theory addresses quantum systems where the Hamiltonian carries explicit time dependence:

$$
\hat{H}(t) = \hat{H}_0 + \hat{V}(t)
$$

Unlike stationary perturbation theory where $\hat{V}$ is static and we seek energy eigenstates, here we track the **dynamical evolution** of quantum states under time-varying influences. This framework underlies scattering theory and condensed matter response functions.

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

---

## Part II: First-Order Transition Amplitudes

### Transition Probability

Suppose the system starts in eigenstate $\vert i\rangle$ of $\hat{H}_0$ at $t_0 = 0$. To first order in $\hat{V}$:

$$
\vert \psi_I(t)\rangle \approx \vert i\rangle + \frac{1}{i\hbar}\int_0^t \hat{V}_I(t')\vert i\rangle dt'
$$

The amplitude for transition to state $\vert f\rangle$ ($f \neq i$) is:

$$
c_f^{(1)}(t) = \langle f\vert \psi_I(t)\rangle = \frac{1}{i\hbar}\int_0^t e^{i\omega_{fi}t'} V_{fi}(t') dt'
$$

where $\omega_{fi} = (E_f - E_i)/\hbar$ and $V_{fi}(t) = \langle f\vert\hat{V}(t)\vert i\rangle$.

### Harmonic Perturbation and Fermi's Golden Rule

For monochromatic driving $\hat{V}(t) = \hat{V}e^{-i\omega t} + \hat{V}^\dagger e^{i\omega t}$, the first term dominates near resonance $\omega \approx \omega_{fi}$ (absorption). The transition probability to a continuum of final states with density $\rho(E_f)$ gives the transition rate:

$$
\boxed{W_{i\to f} = \frac{2\pi}{\hbar}\vert V_{fi}\vert^2 \rho(E_f)}
$$

This is **Fermi's Golden Rule**—the fundamental result for transitions between discrete and continuous spectra.

---

## Part III: Scattering Theory and Propagating States

### From Time-Dependent to Stationary Scattering

Scattering problems involve particles approaching from infinity, interacting via potential $\hat{V}$, and emerging to infinity. While the full problem is time-dependent, the S-matrix connects asymptotic states at $t \to \pm\infty$.

The first-order S-matrix element for transition $\vert i\rangle \to \vert f\rangle$ under perturbation $\hat{V}(t)$ is:

$$
S_{fi}^{(1)} = -\frac{i}{\hbar}\int_{-\infty}^{\infty} e^{i\omega_{fi}t} \langle f\vert\hat{V}(t)\vert i\rangle dt
$$

For a time-independent potential, this becomes:

$$
S_{fi}^{(1)} = -2\pi i \delta(E_f - E_i) \langle f\vert\hat{V}\vert i\rangle
$$

The energy-conserving delta function reflects that elastic scattering preserves energy.

### The Lippmann-Schwinger Equation

Stationary scattering states $\vert \psi^{(\pm)}\rangle$ with energy $E$ satisfy an integral equation derived from the Schrödinger equation. Starting from:

$$
(E - \hat{H}_0)\vert \psi\rangle = \hat{V}\vert \psi\rangle
$$

Formally inverting $(E - \hat{H}_0)$ requires care due to the singularity at $E = E_n$. The resolution is the **resolvent operator** with appropriate boundary conditions:

$$
\hat{G}_0^{(\pm)}(E) = \frac{1}{E - \hat{H}_0 \pm i\epsilon}
$$

The $\pm i\epsilon$ prescription ($\epsilon \to 0^+$) selects:
- **$+i\epsilon$**: outgoing spherical waves (retarded Green's function)
- **$-i\epsilon$**: incoming spherical waves (advanced Green's function)

The Lippmann-Schwinger equation is:

$$
\boxed{\vert \psi^{(\pm)}\rangle = \vert \phi\rangle + \hat{G}_0^{(\pm)}(E)\hat{V}\vert \psi^{(\pm)}\rangle}
$$

where $\vert \phi\rangle$ is the incident plane wave satisfying $(E - \hat{H}_0)\vert \phi\rangle = 0$.

### Born Approximation

Iterating the Lippmann-Schwinger equation generates the Born series:

$$
\vert \psi^{(+)}\rangle = \vert \phi\rangle + \hat{G}_0^{(+)}\hat{V}\vert \phi\rangle + \hat{G}_0^{(+)}\hat{V}\hat{G}_0^{(+)}\hat{V}\vert \phi\rangle + \cdots
$$

The first-order **Born approximation** keeps only the single-scattering term:

$$
\vert \psi^{(+)}\rangle \approx \vert \phi\rangle + \frac{1}{E - \hat{H}_0 + i\epsilon}\hat{V}\vert \phi\rangle
$$

The scattering amplitude $f(\mathbf{k}', \mathbf{k})$ relates to the transition matrix element:

$$
f(\mathbf{k}', \mathbf{k}) = -\frac{m}{2\pi\hbar^2} \langle \mathbf{k}'\vert\hat{V}\vert \psi^{(+)}\rangle
$$

To first order in $\hat{V}$, replace $\vert \psi^{(+)}\rangle \to \vert \mathbf{k}\rangle$:

$$
f_B(\mathbf{k}', \mathbf{k}) = -\frac{m}{2\pi\hbar^2} \langle \mathbf{k}'\vert\hat{V}\vert \mathbf{k}\rangle = -\frac{m}{2\pi\hbar^2} \tilde{V}(\mathbf{k}' - \mathbf{k})
$$

where $\tilde{V}(\mathbf{q}) = \int d^3r \, e^{-i\mathbf{q}\cdot\mathbf{r}} V(\mathbf{r})$ is the Fourier transform of the potential.

### Propagating Wave Packets

Real scattering experiments involve localized wave packets, not plane waves. A wave packet at $t=0$:

$$
\psi(\mathbf{r}, 0) = \int \frac{d^3k}{(2\pi)^{3/2}} \phi(\mathbf{k}) e^{i\mathbf{k}\cdot\mathbf{r}}
$$

evolves as:

$$
\psi(\mathbf{r}, t) = \int \frac{d^3k}{(2\pi)^{3/2}} \phi(\mathbf{k}) e^{i\mathbf{k}\cdot\mathbf{r} - iE(k)t/\hbar}
$$

For a narrow momentum distribution around $\mathbf{k}_0$, expand $E(k) \approx E(k_0) + \hbar\mathbf{v}_g\cdot(\mathbf{k} - \mathbf{k}_0)$ with group velocity $\mathbf{v}_g = \nabla_k E/\hbar$. The wave packet propagates without distortion (in free space) at velocity $\mathbf{v}_g$:

$$
\psi(\mathbf{r}, t) \approx e^{-iE(k_0)t/\hbar} \psi(\mathbf{r} - \mathbf{v}_g t, 0)
$$

Under scattering, the outgoing wave packet is a superposition of scattered spherical waves from each momentum component, leading to the differential cross section.

---

## Part IV: Linear Response Theory

### The Setting: Systems in Thermal Equilibrium

Linear response theory addresses a fundamental question: **How does a macroscopic quantum system respond to weak external probes?**

Consider a system described by $\hat{H}_0$ at temperature $T$, with equilibrium density matrix:

$$
\hat{\rho}_0 = \frac{e^{-\beta\hat{H}_0}}{\mathcal{Z}}, \quad \mathcal{Z} = \text{Tr}(e^{-\beta\hat{H}_0})
$$

where $\beta = 1/(k_B T)$. The expectation value of any observable $\hat{B}$ in equilibrium is:

$$
\langle\hat{B}\rangle_0 = \text{Tr}(\hat{\rho}_0 \hat{B})
$$

At $t = t_0$, we turn on a weak perturbation coupled to some operator $\hat{A}$:

$$
\hat{V}(t) = -\hat{A}F(t)\theta(t - t_0)
$$

where $F(t)$ is a classical external field. We wish to compute the induced change in $\langle\hat{B}\rangle$.

### Single-Particle vs. Many-Particle Settings

**Single-particle quantum mechanics:** The system is in a pure state $\vert \psi(t)\rangle$. Expectation values are $\langle\hat{B}\rangle = \langle\psi(t)\vert\hat{B}\vert\psi(t)\rangle$. The density matrix is $\hat{\rho} = \vert\psi\rangle\langle\psi\vert$ (a projector).

**Statistical mechanics/condensed matter:** The system is an ensemble described by $\hat{\rho}$. For $N \sim 10^{23}$ particles, pure states are intractable. We work with:
- **Canonical ensemble:** $\hat{\rho} = e^{-\beta\hat{H}}/\mathcal{Z}$
- **Grand canonical ensemble:** $\hat{\rho} = e^{-\beta(\hat{H} - \mu\hat{N})}/\mathcal{Z}$

The unified language is the **density matrix formalism**, where $\langle\hat{B}\rangle = \text{Tr}(\hat{\rho}\hat{B})$ reduces to the quantum average for pure states ($\hat{\rho}^2 = \hat{\rho}$) and statistical average for mixed states.

### Density Matrix Evolution

In the interaction picture, the density matrix evolves as:

$$
\hat{\rho}_I(t) = \hat{U}(t, t_0)\hat{\rho}_0\hat{U}^\dagger(t, t_0)
$$

To first order in $\hat{V}$:

$$
\hat{\rho}_I(t) \approx \hat{\rho}_0 + \frac{1}{i\hbar}\int_{t_0}^t [\hat{V}_I(t'), \hat{\rho}_0] dt'
$$

### Deriving the Kubo Formula

The change in $\langle\hat{B}\rangle$ is:

$$
\delta\langle\hat{B}(t)\rangle = \text{Tr}[\hat{\rho}_I(t)\hat{B}_I(t)] - \text{Tr}[\hat{\rho}_0\hat{B}_I(t)]
$$

Using the cyclic property of trace and noting $\hat{\rho}_0$ commutes with $\hat{H}_0$ (hence $[\hat{\rho}_0, \hat{B}_I(t)] \neq 0$ in general, but $\hat{\rho}_0$ is time-independent):

$$
\delta\langle\hat{B}(t)\rangle = \frac{1}{i\hbar}\int_{t_0}^t \text{Tr}\{[\hat{V}_I(t'), \hat{\rho}_0]\hat{B}_I(t)\} dt'
$$

With $\hat{V}_I(t') = -\hat{A}_I(t')F(t')$ and using $\text{Tr}([\hat{X}, \hat{Y}]\hat{Z}) = \text{Tr}(\hat{X}[\hat{Y}, \hat{Z}])$:

$$
\delta\langle\hat{B}(t)\rangle = \frac{1}{i\hbar}\int_{t_0}^t F(t')\text{Tr}\{\hat{\rho}_0[\hat{A}_I(t'), \hat{B}_I(t)]\} dt'
$$

Recognizing $\text{Tr}(\hat{\rho}_0[\cdot, \cdot]) = \langle[\cdot, \cdot]\rangle_0$:

$$
\delta\langle\hat{B}(t)\rangle = \int_{t_0}^t \chi_{BA}(t - t')F(t') dt'
$$

where the **retarded response function** (Kubo formula) is:

$$
\boxed{\chi_{BA}(t) = -\frac{i}{\hbar}\theta(t)\langle[\hat{B}_I(t), \hat{A}_I(0)]\rangle_0}
$$

**Key features:**
1. **Causality:** The $\theta(t)$ ensures response follows stimulus
2. **Equilibrium correlation:** The commutator is evaluated in the unperturbed thermal state
3. **Quantum structure:** The commutator encodes both classical and quantum fluctuations

### Frequency Domain and Spectral Representation

For harmonic driving $F(t) = F_0 e^{-i\omega t + \epsilon t}$ (adiabatic turn-on), the response is:

$$
\delta\langle\hat{B}(\omega)\rangle = \chi_{BA}(\omega)F(\omega)
$$

with the susceptibility:

$$
\chi_{BA}(\omega) = \int_0^{\infty} e^{i\omega t}\chi_{BA}(t)dt
$$

Insert a complete set of eigenstates $\vert n\rangle$ of $\hat{H}_0$ with energies $E_n$:

$$
\chi_{BA}(\omega) = \frac{1}{\mathcal{Z}}\sum_{n,m} e^{-\beta E_n}\left(\frac{\langle n\vert\hat{B}\vert m\rangle\langle m\vert\hat{A}\vert n\rangle}{\hbar\omega + E_n - E_m + i\epsilon} - \frac{\langle n\vert\hat{A}\vert m\rangle\langle m\vert\hat{B}\vert n\rangle}{\hbar\omega + E_m - E_n + i\epsilon}\right)
$$

This **spectral representation** reveals the poles at excitation energies $\hbar\omega = E_m - E_n$.

### Fluctuation-Dissipation Theorem

Consider the symmetrized correlation function:

$$
S_{BA}(\omega) = \int_{-\infty}^{\infty} e^{i\omega t}\frac{1}{2}\langle\{\hat{B}_I(t), \hat{A}_I(0)\}\rangle_0 dt
$$

and the response function's imaginary part $\chi''_{BA}(\omega) = \text{Im}\,\chi_{BA}(\omega)$. Using the spectral representation and detailed balance $e^{-\beta E_n} - e^{-\beta E_m} = (1 - e^{-\beta\hbar\omega})e^{-\beta E_n}$ for $\omega = (E_m - E_n)/\hbar$:

$$
\boxed{\chi''_{AA}(\omega) = \frac{1}{2\hbar}(1 - e^{-\beta\hbar\omega})S_{AA}(\omega)}
$$

**Physical interpretation:** The imaginary part of the susceptibility (dissipation) is proportional to the power spectrum of equilibrium fluctuations. At high temperatures ($\beta\hbar\omega \ll 1$), this reduces to the classical form $\chi'' = (\omega/2k_B T)S$.

### Connection to Single-Particle Formulas

For a **pure state** at $T=0$, the density matrix is $\hat{\rho}_0 = \vert\psi_0\rangle\langle\psi_0\vert$ where $\vert\psi_0\rangle$ is the ground state. The Kubo formula reduces to:

$$
\chi_{BA}(t) = -\frac{i}{\hbar}\theta(t)\langle\psi_0\vert[\hat{B}_I(t), \hat{A}_I(0)]\vert\psi_0\rangle
$$

For a **single-particle system**, insert complete set of excited states:

$$
\chi_{BA}(t) = -\frac{i}{\hbar}\theta(t)\sum_{n\neq 0}\left(e^{i\omega_{n0}t}\langle 0\vert\hat{B}\vert n\rangle\langle n\vert\hat{A}\vert 0\rangle - e^{-i\omega_{n0}t}\langle 0\vert\hat{A}\vert n\rangle\langle n\vert\hat{B}\vert 0\rangle\right)
$$

This matches the time-dependent perturbation theory result for transition amplitudes—the same physics expressed in the language of response functions. The many-body generalization simply replaces the ground state expectation with a thermal average, accounting for temperature and interactions.

### Conductivity: The Kubo-Greenwood Formula

For electrical conductivity, the perturbation is $\hat{V} = -e\hat{\mathbf{r}}\cdot\mathbf{E}(t)$ and the response current is $\hat{\mathbf{j}}$. The current-current response gives:

$$
\sigma_{\alpha\beta}(\omega) = \frac{1}{\hbar\omega}\int_0^{\infty} e^{i\omega t}\langle[\hat{j}_\alpha(t), \hat{j}_\beta(0)]\rangle_0 dt
$$

At $T=0$ for non-interacting electrons, this reduces to the Greenwood formula:

$$
\sigma_{\alpha\beta}(\omega) = \frac{\pi e^2}{\hbar}\sum_{n,m}(f_n - f_m)\langle n\vert\hat{v}_\alpha\vert m\rangle\langle m\vert\hat{v}_\beta\vert n\rangle\delta(E_m - E_n - \hbar\omega)
$$

where $f_n$ are Fermi occupation factors. The connection is clear: conductivity measures the ease of inducing transitions (current) by an electric field, directly related to the density of states and transition matrix elements.

---

## Summary and Connections

| Domain | Initial State | Perturbation | Key Quantity | Physical Content |
|--------|--------------|--------------|--------------|------------------|
| Atomic transitions | $\vert i\rangle$ (discrete) | $\hat{V}e^{-i\omega t}$ | $W_{i\to f}$ | Transition rate to continuum |
| Scattering | $\vert\mathbf{k}\rangle$ (plane wave) | Static $\hat{V}$ | $f(\mathbf{k}', \mathbf{k})$ | Differential cross section |
| Single-particle response | $\vert\psi_0\rangle$ (pure state) | $-\hat{A}F(t)$ | $\chi_{BA}(t)$ | Ground state correlations |
| Many-body response | $\hat{\rho}_0 = e^{-\beta\hat{H}_0}/\mathcal{Z}$ | $-\hat{A}F(t)$ | $\chi_{BA}(\omega)$ | Thermal/fluctuation properties |

The unifying framework is time-dependent perturbation theory in the interaction picture. The differences lie in:
1. **Initial conditions:** Pure states vs. thermal ensembles
2. **Observables:** Transition probabilities vs. induced expectation values  
3. **Time domains:** Transient evolution vs. steady-state response

The Kubo formula generalizes single-particle transition amplitudes to correlated many-body systems through the density matrix formalism.

---

## References

1. Sakurai, J.J. & Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. (Cambridge University Press, 2020). Chapter 2, 5

2. Taylor, J.R. *Scattering Theory: The Quantum Theory of Nonrelativistic Collisions* (Dover, 2006). Chapters 2–3, 9–10

3. Mahan, G.D. *Many-Particle Physics*, 3rd ed. (Springer, 2000). Chapter 3 (Linear Response)

4. Kubo, R. *Statistical-Mechanical Theory of Irreversible Processes. I.* J. Phys. Soc. Jpn. 12, 570 (1957)

5. Fetter, A.L. & Walecka, J.D. *Quantum Theory of Many-Particle Systems* (Dover, 2003). Chapter 6 (Linear Response)
