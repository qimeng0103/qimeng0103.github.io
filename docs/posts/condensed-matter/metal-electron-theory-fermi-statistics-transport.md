# Metal Electron Theory: From Fermi Statistics to Transport Properties

📅 **Date:** 2026-04-02 | 🏷️ **Tags:** Solid State Physics, Fermi Statistics, Electron Transport | 📂 **Category:** Condensed Matter Notes

---

## Introduction

The electron theory of metals represents one of the most elegant applications of quantum statistical mechanics to condensed matter physics. While classical Drude-Lorentz theory successfully explained Ohm's law and the Wiedemann-Franz law, it fundamentally failed to account for the absence of a significant electronic contribution to the heat capacity of metals. This paradox was resolved only with the advent of quantum mechanics and Fermi-Dirac statistics.

This article provides a comprehensive treatment of metal electron theory, emphasizing the transition from single-particle thinking to many-body statistical concepts. We derive all results step-by-step, explaining the statistical mechanics foundations that are often taken for granted.

---

## Part I: Fermi Statistics and Electronic Heat Capacity

### 1.1 The Fermi-Dirac Distribution: Why Classical Statistics Fails

**The Classical Paradox**

In classical statistical mechanics, each particle in a gas is treated as an independent entity. For an ideal gas of $N$ particles in volume $V$ at temperature $T$, each degree of freedom contributes $\frac{1}{2}k_B T$ to the average energy (equipartition theorem). For electrons with three translational degrees of freedom, the classical prediction is:

$$
U_{\text{classical}} = \frac{3}{2} N k_B T
$$

This gives a heat capacity:

$$
C_V^{\text{classical}} = \frac{\partial U}{\partial T} = \frac{3}{2} N k_B
$$

For one mole of electrons, this would be $\frac{3}{2} R \approx 12.5 \, \text{J/(mol·K)}$, comparable to the lattice heat capacity. However, experimentally, the electronic heat capacity at room temperature is orders of magnitude smaller—typically $10^{-2}$ to $10^{-3}$ of the classical value.

**The Resolution: Pauli Exclusion Principle**

Electrons are fermions with spin-$\frac{1}{2}$, obeying the Pauli exclusion principle: no two electrons can occupy the same quantum state. This fundamentally changes the statistical distribution.

In quantum statistics, we must think not of individual particles, but of the occupation of quantum states. The key insight is that electrons fill up energy states starting from the lowest available level. At $T = 0$, all states below a certain energy $E_F$ (the Fermi energy) are filled, and all states above are empty.

### 1.2 Derivation of the Fermi-Dirac Distribution

**The Grand Canonical Ensemble Approach**

To derive the probability of occupation for a quantum state, we use the grand canonical ensemble. Consider a system of electrons in thermal and chemical equilibrium with a reservoir at temperature $T$ and chemical potential $\mu$.

For a single-particle state with energy $\varepsilon$, the possible occupancies are:
- $n = 0$: empty state, energy $E_0 = 0$
- $n = 1$: occupied by one electron, energy $E_1 = \varepsilon$

The grand partition function for this single state is:

$$
\mathcal{Z} = \sum_{n=0,1} e^{\beta(\mu n - E_n)} = e^{\beta(\mu \cdot 0 - 0)} + e^{\beta(\mu \cdot 1 - \varepsilon)} = 1 + e^{\beta(\mu - \varepsilon)}
$$

where $\beta = 1/(k_B T)$.

The average occupation number is:

$$
\langle n \rangle = \frac{1}{\mathcal{Z}} \sum_{n=0,1} n \cdot e^{\beta(\mu n - E_n)} = \frac{0 \cdot 1 + 1 \cdot e^{\beta(\mu - \varepsilon)}}{1 + e^{\beta(\mu - \varepsilon)}}
$$

Simplifying:

$$
f(\varepsilon) = \langle n \rangle = \frac{e^{\beta(\mu - \varepsilon)}}{1 + e^{\beta(\mu - \varepsilon)}} = \frac{1}{e^{\beta(\varepsilon - \mu)} + 1}
$$

This is the **Fermi-Dirac distribution function**. We often write the chemical potential as $E_F$ (Fermi energy or Fermi level), giving:

$$
f(E) = \frac{1}{e^{(E - E_F)/(k_B T)} + 1} \tag{1.1}
$$

**Physical Interpretation**

The Fermi function has the following key properties:

1. **At $T = 0$:**
   - If $E < E_F$: $(E - E_F) < 0$, so $e^{-\infty} = 0$, and $f(E) = 1$ (fully occupied)
   - If $E > E_F$: $(E - E_F) > 0$, so $e^{+\infty} = \infty$, and $f(E) = 0$ (empty)
   - If $E = E_F$: $f(E_F) = \frac{1}{1+1} = \frac{1}{2}$

2. **At finite temperature:** The transition from 1 to 0 occurs over an energy range of order $k_B T$ around $E_F$.

3. **The meaning of $f(E_F) = \frac{1}{2}$:** At the Fermi energy, the occupation probability is exactly one-half. This is not because half an electron occupies the state, but because at this energy level, the Boltzmann factor $e^{(E-E_F)/k_B T}$ equals 1, making the probability of occupation equal to the probability of vacancy.

### 1.3 Counting States in k-Space: The Density of States

**Quantum States for Free Electrons**

For a free electron in a cubic box of side $L$ with periodic boundary conditions, the allowed wavevectors are:

$$
k_x = \frac{2\pi n_x}{L}, \quad k_y = \frac{2\pi n_y}{L}, \quad k_z = \frac{2\pi n_z}{L}
$$

where $n_x, n_y, n_z = 0, \pm 1, \pm 2, \ldots$

The spacing between adjacent $k$-states is $\Delta k = 2\pi/L$. The volume in $k$-space occupied by each state is:

$$
V_{\text{state}} = \left(\frac{2\pi}{L}\right)^3 = \frac{(2\pi)^3}{V}
$$

where $V = L^3$ is the real-space volume.

**Counting States in a Sphere**

To find the total number of states with wavevector magnitude less than $k$, we calculate the volume of a sphere of radius $k$ in $k$-space and divide by the volume per state:

$$
N(k) = 2 \times \frac{\frac{4}{3}\pi k^3}{(2\pi)^3/V} = 2 \times \frac{V \cdot 4\pi k^3}{3(2\pi)^3} = \frac{V k^3}{3\pi^2}
$$

The factor of 2 accounts for the two spin states (spin up and spin down) for each $k$-value.

**Density of States**

The density of states $D(E)$ is defined such that $D(E)dE$ gives the number of states with energy between $E$ and $E + dE$. Using the free electron dispersion relation:

$$
E = \frac{\hbar^2 k^2}{2m} \implies k = \sqrt{\frac{2mE}{\hbar^2}}
$$

Differentiating $N(E)$:

$$
D(E) = \frac{dN}{dE} = \frac{dN}{dk} \cdot \frac{dk}{dE}
$$

First, compute $\frac{dN}{dk}$:

$$
\frac{dN}{dk} = \frac{V k^2}{\pi^2}
$$

Next, compute $\frac{dk}{dE}$ from the dispersion relation:

$$
\frac{dk}{dE} = \frac{m}{\hbar^2 k} = \frac{m}{\hbar^2} \sqrt{\frac{\hbar^2}{2mE}} = \frac{1}{\hbar}\sqrt{\frac{m}{2E}}
$$

Therefore:

$$
D(E) = \frac{V k^2}{\pi^2} \cdot \frac{m}{\hbar^2 k} = \frac{Vmk}{\pi^2 \hbar^2}
$$

Substituting $k = \sqrt{2mE}/\hbar$:

$$
D(E) = \frac{Vm}{\pi^2 \hbar^2} \cdot \frac{\sqrt{2mE}}{\hbar} = \frac{V(2m)^{3/2}}{2\pi^2 \hbar^3} \sqrt{E}
$$

More commonly written per unit volume:

$$
N(E) = \frac{(2m)^{3/2}}{2\pi^2 \hbar^3} \sqrt{E} = C\sqrt{E} \tag{1.2}
$$

where $C = \frac{(2m)^{3/2}}{2\pi^2 \hbar^3}$.

### 1.4 The Fermi Energy at Zero Temperature

At $T = 0$, all states up to $E_F$ are filled. The total number of electrons is:

$$
N = \int_0^{E_F} D(E) dE = \int_0^{E_F} C\sqrt{E} \, dE = C \cdot \frac{2}{3} E_F^{3/2}
$$

Solving for $E_F$:

$$
E_F = \left(\frac{3N}{2C}\right)^{2/3} = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3} \tag{1.3}
$$

where $n = N/V$ is the electron density.

**Numerical Estimate**

For typical metals, $n \sim 10^{28}$-$10^{29} \, \text{m}^{-3}$. Using $n = 10^{29} \, \text{m}^{-3}$:

$$
E_F = \frac{(1.05 \times 10^{-34})^2}{2 \times 9.11 \times 10^{-31}} \times (3\pi^2 \times 10^{29})^{2/3}
$$

$$
E_F \approx 6.1 \times 10^{-39} \times (3 \times 9.87 \times 10^{29})^{2/3} \approx 6.1 \times 10^{-39} \times 3.0 \times 10^{20}
$$

$$
E_F \approx 1.8 \times 10^{-18} \, \text{J} \approx 11 \, \text{eV}
$$

This is indeed several electron volts, much larger than room temperature thermal energy $k_B T \approx 0.025$ eV.

**The Fermi Temperature**

We define the Fermi temperature $T_F = E_F/k_B$:

$$
T_F = \frac{E_F}{k_B} \sim \frac{10 \, \text{eV}}{8.6 \times 10^{-5} \, \text{eV/K}} \sim 10^5 \, \text{K}
$$

For all practical temperatures ($T \ll T_F$), electrons are in a highly degenerate state.

### 1.5 Electronic Heat Capacity: The Sommerfeld Expansion

**Why Heat Capacity is Small**

The key insight is that only electrons within $\sim k_B T$ of the Fermi surface can participate in thermal excitations. Electrons deep below the Fermi energy cannot absorb thermal energy because all nearby states are already occupied (Pauli exclusion principle).

**Quantitative Calculation**

The total energy of the electron gas is:

$$
U = \int_0^{\infty} E \cdot f(E) \cdot D(E) \, dE \tag{1.4}
$$

At low temperatures ($T \ll T_F$), we use the **Sommerfeld expansion**. For an integral of the form:

$$
I = \int_0^{\infty} \phi(E) f(E) dE
$$

where $\phi(E)$ is a smooth function, the expansion gives:

$$
I = \int_0^{E_F} \phi(E) dE + \frac{\pi^2}{6}(k_B T)^2 \phi'(E_F) + O(T^4)
$$

For the total energy, $\phi(E) = E \cdot D(E) = C E^{3/2}$:

$$
U = \int_0^{E_F} C E^{3/2} dE + \frac{\pi^2}{6}(k_B T)^2 \cdot \frac{3}{2} C E_F^{1/2}
$$

The first term is the zero-temperature energy:

$$
U_0 = \frac{2}{5} C E_F^{5/2} = \frac{3}{5} N E_F
$$

The second term gives the temperature-dependent correction. Using $D(E_F) = C\sqrt{E_F}$:

$$
U = U_0 + \frac{\pi^2}{6} D(E_F) (k_B T)^2 E_F
$$

Wait—let us be more careful. Actually:

$$\phi(E) = E \cdot D(E) = CE^{3/2}$$

$$\phi'(E) = \frac{3}{2} C E^{1/2} = \frac{3}{2} D(E)$$

So:

$$
\phi'(E_F) = \frac{3}{2} D(E_F)
$$

Therefore:

$$
U = \int_0^{E_F} ED(E)dE + \frac{\pi^2}{6}(k_B T)^2 \cdot \frac{3}{2} D(E_F)
$$

But we must also account for the shift in $E_F$ with temperature. The complete result is:

$$
U = U_0 + \frac{\pi^2}{6} D(E_F) (k_B T)^2 \tag{1.5}
$$

The electronic heat capacity is:

$$
C_V = \frac{\partial U}{\partial T} = \frac{\pi^2}{3} D(E_F) k_B^2 T \tag{1.6}
$$

Using $D(E_F) = \frac{3N}{2E_F}$ (from $N = \int_0^{E_F} D(E)dE = \frac{2}{3}D(E_F)E_F$):

$$
C_V = \frac{\pi^2}{3} \cdot \frac{3N}{2E_F} \cdot k_B^2 T = \frac{\pi^2}{2} N k_B \frac{T}{T_F}
$$

Or more commonly:

$$
C_V = \gamma T \tag{1.7}
$$

where $\gamma = \frac{\pi^2}{2} \frac{N k_B}{T_F} = \frac{\pi^2}{3} D(E_F) k_B^2$.

**Comparison with Classical Result**

The ratio of quantum to classical heat capacity:

$$
\frac{C_V^{\text{quantum}}}{C_V^{\text{classical}}} = \frac{\frac{\pi^2}{2} N k_B \frac{T}{T_F}}{\frac{3}{2} N k_B} = \frac{\pi^2}{3} \frac{T}{T_F} \sim \frac{T}{T_F}
$$

At room temperature ($T \sim 300$ K) with $T_F \sim 10^4$-$10^5$ K, this ratio is $\sim 10^{-2}$-$10^{-3}$, explaining the experimental observations.

### 1.6 Temperature Dependence of the Fermi Energy

The chemical potential $\mu$ (or $E_F$ at finite $T$) shifts slightly with temperature. From the particle number constraint:

$$
N = \int_0^{\infty} D(E) f(E) dE
$$

Using Sommerfeld expansion with $\phi(E) = D(E)$:

$$
N = \int_0^{\mu} D(E) dE + \frac{\pi^2}{6}(k_B T)^2 D'(\mu)
$$

At $T = 0$: $N = \int_0^{E_F^0} D(E) dE$ where $E_F^0$ is the $T=0$ Fermi energy.

Expanding around $E_F^0$:

$$
\int_0^{\mu} D(E) dE = \int_0^{E_F^0} D(E) dE + D(E_F^0)(\mu - E_F^0) + \ldots
$$

Equating:

$$N = N + D(E_F^0)(\mu - E_F^0) + \frac{\pi^2}{6}(k_B T)^2 D'(E_F^0)$$

Solving:

$$
\mu - E_F^0 = -\frac{\pi^2}{6}(k_B T)^2 \frac{D'(E_F^0)}{D(E_F^0)}
$$

For free electrons, $D(E) \propto \sqrt{E}$, so $D'(E)/D(E) = 1/(2E)$:

$$
\mu = E_F^0 \left[1 - \frac{\pi^2}{12}\left(\frac{k_B T}{E_F^0}\right)^2\right] \tag{1.8}
$$

The Fermi energy decreases slightly with temperature, but the correction is of order $(T/T_F)^2 \sim 10^{-8}$ at room temperature.

---

## Part II: Transport Theory—The Boltzmann Equation

### 2.1 From Equilibrium to Non-Equilibrium

**The Distribution Function**

In equilibrium, the electron distribution is given by the Fermi-Dirac function $f_0(E)$. When external fields (electric field $\mathbf{E}$, magnetic field $\mathbf{B}$, temperature gradients $\nabla T$) are applied, the system is driven out of equilibrium.

The central quantity in transport theory is the **distribution function** $f(\mathbf{k}, \mathbf{r}, t)$, which gives the probability of finding an electron in state $\mathbf{k}$ at position $\mathbf{r}$ and time $t$.

**Physical Interpretation of $f(\mathbf{k}, \mathbf{r}, t)$**

- $f(\mathbf{k}, \mathbf{r}, t) \cdot d^3k/(2\pi)^3$ is the number density of electrons with wavevectors in $d^3k$ around $\mathbf{k}$.
- In equilibrium, $f = f_0(E_k)$ depends only on energy.
- In non-equilibrium, $f$ can vary with position and time.

### 2.2 The Boltzmann Equation: Derivation

**The Continuity Equation in Phase Space**

Consider electrons as a fluid in $(\mathbf{r}, \mathbf{k})$ phase space. The total time derivative of $f$ along a trajectory is determined by collisions:

$$
\frac{df}{dt} = \left(\frac{\partial f}{\partial t}\right)_{\text{collision}}
$$

Expanding the total derivative:

$$
\frac{df}{dt} = \frac{\partial f}{\partial t} + \frac{d\mathbf{r}}{dt} \cdot \nabla_r f + \frac{d\mathbf{k}}{dt} \cdot \nabla_k f
$$

Using $\dot{\mathbf{r}} = \mathbf{v} = \frac{1}{\hbar}\nabla_k E$ and $\hbar\dot{\mathbf{k}} = \mathbf{F}$ (force):

$$
\frac{\partial f}{\partial t} + \mathbf{v} \cdot \nabla_r f + \frac{1}{\hbar}\mathbf{F} \cdot \nabla_k f = \left(\frac{\partial f}{\partial t}\right)_{\text{collision}} \tag{2.1}
$$

This is the **Boltzmann transport equation**.

**The Collision Term**

The collision term describes scattering processes that change an electron's state from $\mathbf{k}$ to $\mathbf{k}'$. Let $W_{\mathbf{k}\mathbf{k}'}$ be the transition rate from $\mathbf{k}$ to $\mathbf{k}'$.

The rate of change of $f(\mathbf{k})$ due to collisions has two contributions:
- **Out-scattering**: Electrons leaving state $\mathbf{k}$ to all other states $\mathbf{k}'$:
  $$\left(\frac{\partial f(\mathbf{k})}{\partial t}\right)_{\text{out}} = -\sum_{\mathbf{k}'} W_{\mathbf{k}\mathbf{k}'} f(\mathbf{k})[1-f(\mathbf{k}')]
  $$
  The factor $[1-f(\mathbf{k}')]$ ensures Pauli exclusion (state $\mathbf{k}'$ must be empty).

- **In-scattering**: Electrons entering state $\mathbf{k}$ from all other states $\mathbf{k}'$:
  $$\left(\frac{\partial f(\mathbf{k})}{\partial t}\right)_{\text{in}} = \sum_{\mathbf{k}'} W_{\mathbf{k}'\mathbf{k}} f(\mathbf{k}')[1-f(\mathbf{k})]
  $$

In equilibrium, detailed balance requires that in-scattering equals out-scattering for each pair of states.

### 2.3 The Relaxation Time Approximation

**Physical Motivation**

The full collision integral is complex. The **relaxation time approximation** assumes that collisions drive the distribution back to equilibrium exponentially:

$$
\left(\frac{\partial f}{\partial t}\right)_{\text{collision}} = -\frac{f - f_0}{\tau(\mathbf{k})} \tag{2.2}
$$

where $\tau(\mathbf{k})$ is the relaxation time—a characteristic time for return to equilibrium.

**Validity and Microscopic Derivation**

The relaxation time approximation is valid when:
1. Scattering is elastic (energy-conserving)
2. The system is isotropic
3. Scattering probabilities depend only on the angle between $\mathbf{k}$ and $\mathbf{k}'$

For elastic scattering in an isotropic system, one can show:

$$
\frac{1}{\tau(\mathbf{k})} = \sum_{\mathbf{k}'} W_{\mathbf{k}\mathbf{k}'}(1 - \cos\theta) \tag{2.3}
$$

where $\theta$ is the angle between $\mathbf{k}$ and $\mathbf{k}'$. The $(1-\cos\theta)$ factor weights large-angle scattering more heavily because it is more effective at randomizing momentum.

### 2.4 Steady-State Electrical Conductivity

**Setup and Linearization**

Consider a uniform electric field $\mathbf{E}$ at steady state ($\partial f/\partial t = 0$) with no spatial gradients ($\nabla_r f = 0$). The Boltzmann equation becomes:

$$
-\frac{e}{\hbar}\mathbf{E} \cdot \nabla_k f = -\frac{f - f_0}{\tau}
$$

Assuming weak fields, we write:

$$
f = f_0 + f_1
$$

where $f_1 \ll f_0$ is the deviation from equilibrium. To first order in $\mathbf{E}$:

$$
\nabla_k f \approx \nabla_k f_0 = \frac{\partial f_0}{\partial E} \nabla_k E = \frac{\partial f_0}{\partial E} \hbar \mathbf{v}
$$

The Boltzmann equation becomes:

$$
-e\mathbf{E} \cdot \mathbf{v} \frac{\partial f_0}{\partial E} = -\frac{f_1}{\tau}
$$

Solving for $f_1$:

$$
f_1 = e\tau (\mathbf{E} \cdot \mathbf{v}) \frac{\partial f_0}{\partial E} \tag{2.4}
$$

**Calculating the Current**

The electrical current density is:

$$
\mathbf{j} = -2e \int \frac{d^3k}{(2\pi)^3} \mathbf{v}(\mathbf{k}) f(\mathbf{k})
$$

The factor of 2 accounts for spin. The equilibrium distribution $f_0$ gives no current (by symmetry, $\mathbf{v}$ averages to zero), so:

$$
\mathbf{j} = -2e \int \frac{d^3k}{(2\pi)^3} \mathbf{v}(\mathbf{k}) f_1(\mathbf{k})
$$

Substituting $f_1$:

$$
\mathbf{j} = -2e^2 \int \frac{d^3k}{(2\pi)^3} \tau \mathbf{v}(\mathbf{v} \cdot \mathbf{E}) \frac{\partial f_0}{\partial E}
$$

For an isotropic system with $\tau$ depending only on energy, we can write:

$$
j_\alpha = \sum_\beta \sigma_{\alpha\beta} E_\beta
$$

where the conductivity tensor is:

$$
\sigma_{\alpha\beta} = -2e^2 \int \frac{d^3k}{(2\pi)^3} \tau v_\alpha v_\beta \frac{\partial f_0}{\partial E}
$$

**Evaluating the Integral**

The derivative $\partial f_0/\partial E$ is sharply peaked at $E = E_F$ (like a negative delta function). We use:

$$
-\frac{\partial f_0}{\partial E} = \frac{1}{k_B T} \frac{e^{(E-E_F)/k_B T}}{(e^{(E-E_F)/k_B T}+1)^2} \approx \delta(E - E_F)
$$

at low temperatures. More precisely:

$$
\int_0^\infty \phi(E) \left(-\frac{\partial f_0}{\partial E}\right) dE = \phi(E_F) + O((k_B T/E_F)^2)
$$

For isotropic systems, $\langle v_\alpha v_\beta \rangle = \frac{1}{3}v^2 \delta_{\alpha\beta}$, giving:

$$
\sigma = \frac{ne^2\tau(E_F)}{m^*} \tag{2.5}
$$

where $n$ is the electron density and $m^*$ is the effective mass. This is the **Drude formula**, but now with quantum mechanical justification.

### 2.5 Temperature Dependence of Resistivity

**Electron-Phonon Scattering**

At high temperatures ($T > \Theta_D$, the Debye temperature), phonon occupation numbers are:

$$
n_q = \frac{1}{e^{\hbar\omega_q/k_B T} - 1} \approx \frac{k_B T}{\hbar\omega_q} \gg 1
$$

Since scattering rates are proportional to phonon numbers, we expect:

$$
\frac{1}{\tau} \propto T
$$

Therefore:

$$
\rho \propto T \quad \text{(high T)} \tag{2.6}
$$

At low temperatures ($T \ll \Theta_D$), only low-energy phonons with $\omega \sim k_B T/\hbar$ are available. Phase space restrictions give:

$$
\frac{1}{\tau} \propto T^3 \times (1-\cos\theta)_{\text{avg}} \propto T^3 \times \left(\frac{T}{\Theta_D}\right)^2 = T^5
$$

Therefore:

$$
\rho \propto T^5 \quad \text{(low T)} \tag{2.7}
$$

This is the **Bloch-Grüneisen law**.

---

## Part III: The Hall Effect and Magnetotransport

### 3.1 Electrons in a Magnetic Field

**The Lorentz Force**

With both electric and magnetic fields, the force on an electron is:

$$
\mathbf{F} = -e\left(\mathbf{E} + \frac{1}{c}\mathbf{v} \times \mathbf{B}\right)
$$

(in Gaussian units) or $\mathbf{F} = -e(\mathbf{E} + \mathbf{v} \times \mathbf{B})$ in SI units.

The Boltzmann equation becomes:

$$
-e\mathbf{E} \cdot \mathbf{v} \frac{\partial f}{\partial E} - \frac{e}{\hbar}(\mathbf{v} \times \mathbf{B}) \cdot \nabla_k f = -\frac{f - f_0}{\tau}
$$

**Cyclotron Motion**

Note that $(\mathbf{v} \times \mathbf{B}) \cdot \nabla_k f_0 = 0$ because $\nabla_k f_0 \propto \mathbf{v}$ and $(\mathbf{v} \times \mathbf{B}) \perp \mathbf{v}$. The magnetic field alone does not change the energy distribution.

### 3.2 Derivation of the Hall Coefficient

**Setup**

Consider $\mathbf{B} = B\hat{z}$ and $\mathbf{E} = (E_x, E_y, 0)$. We look for a steady-state solution with current $\mathbf{j} = (j_x, 0, 0)$ (no current in the $y$-direction).

**Iterative Solution**

Writing $f = f_0 + f_1 + f_2 + \ldots$ where subscripts indicate powers of $\mathbf{B}$:

**Zero order** (no fields):
$$f^{(0)} = f_0$$

**First order** (electric field only):
$$f^{(1)} = e\tau \mathbf{E} \cdot \mathbf{v} \frac{\partial f_0}{\partial E}$$

**Second order** (includes magnetic effects):

The magnetic term involves $\nabla_k f^{(1)}$. Since $f^{(1)} \propto \mathbf{E} \cdot \mathbf{v} = \mathbf{E} \cdot (\hbar\mathbf{k}/m^*)$:

$$
\nabla_k f^{(1)} \propto \mathbf{E}
$$

The magnetic contribution to the Boltzmann equation is:

$$
-\frac{e}{\hbar}(\mathbf{v} \times \mathbf{B}) \cdot \nabla_k f^{(1)} = -\frac{f^{(2)}}{\tau}
$$

After detailed calculation (see below), this gives a correction to the distribution function proportional to $\mathbf{B} \times \mathbf{E}$.

**Detailed Derivation**

For the isotropic case with $E(k) = \hbar^2 k^2/2m^*$:

$$f^{(1)} = \frac{e\tau}{m^*} \frac{\partial f_0}{\partial E} \hbar \mathbf{E} \cdot \mathbf{k} = \chi(E) \mathbf{E} \cdot \mathbf{k}$$

where $\chi(E) = (e\tau\hbar/m^*)(\partial f_0/\partial E)$.

Now:

$$\nabla_k f^{(1)} = \mathbf{E}\chi(E) + \mathbf{k}(\mathbf{E} \cdot \mathbf{k})\frac{\partial\chi}{\partial E}\frac{\hbar^2}{m^*}$$

The first term gives:

$$(\mathbf{v} \times \mathbf{B}) \cdot \mathbf{E} = (\mathbf{E} \times \mathbf{v}) \cdot \mathbf{B} = \frac{\hbar}{m^*}(\mathbf{E} \times \mathbf{k}) \cdot \mathbf{B}$$

The magnetic term in the Boltzmann equation becomes:

$$-\frac{e}{\hbar}(\mathbf{v} \times \mathbf{B}) \cdot \nabla_k f^{(1)} = -\frac{e\hbar}{m^{*2}}\chi(E)(\mathbf{E} \times \mathbf{k}) \cdot \mathbf{B} + \ldots$$

Setting this equal to $-f^{(2)}/\tau$:

$$f^{(2)} = \frac{e\tau\hbar}{m^{*2}}\chi(E)(\mathbf{E} \times \mathbf{k}) \cdot \mathbf{B} = \frac{e^2\tau^2\hbar^2}{m^{*3}}\frac{\partial f_0}{\partial E}(\mathbf{E} \times \mathbf{k}) \cdot \mathbf{B}$$

**Current Calculation**

The current from $f^{(2)}$:

$$j_\alpha^{(2)} = -2e \int \frac{d^3k}{(2\pi)^3} v_\alpha f^{(2)} = -2e \int \frac{d^3k}{(2\pi)^3} \frac{\hbar k_\alpha}{m^*} f^{(2)}$$

Substituting $f^{(2)}$ and evaluating the angular integrals:

$$j_\alpha^{(2)} = -\frac{2e^3\tau^2\hbar^3}{m^{*4}}(\mathbf{E} \times \mathbf{B})_\beta \int \frac{d^3k}{(2\pi)^3} k_\alpha k_\beta \frac{\partial f_0}{\partial E}$$

For isotropic systems, $\langle k_\alpha k_\beta \rangle = \frac{1}{3}k^2\delta_{\alpha\beta}$, giving:

$$\mathbf{j}^{(2)} = \frac{ne^3\tau^2}{m^{*2}}(\mathbf{E} \times \mathbf{B})$$

**Total Current and Hall Effect**

Combining contributions:

$$\mathbf{j} = \sigma_0 \mathbf{E} + \frac{ne^3\tau^2}{m^{*2}}(\mathbf{E} \times \mathbf{B})$$

where $\sigma_0 = ne^2\tau/m^*$.

In component form with $\mathbf{B} = B\hat{z}$:

$$j_x = \sigma_0 E_x + \omega_c\tau \sigma_0 E_y$$
$$j_y = \sigma_0 E_y - \omega_c\tau \sigma_0 E_x$$

where $\omega_c = eB/m^*$ is the cyclotron frequency.

Setting $j_y = 0$ (Hall geometry):

$$E_y = \omega_c\tau E_x = \frac{eB\tau}{m^*} E_x$$

Substituting into $j_x$:

$$j_x = \sigma_0 E_x + (\omega_c\tau)^2 \sigma_0 E_x = \sigma_0 E_x [1 + (\omega_c\tau)^2]$$

For weak fields ($\omega_c\tau \ll 1$), $j_x \approx \sigma_0 E_x$.

The **Hall coefficient** is defined by:

$$R_H = \frac{E_y}{B j_x} = \frac{\omega_c\tau E_x}{B \sigma_0 E_x} = \frac{e\tau/m^*}{(ne^2\tau/m^*)} = \frac{1}{ne} \tag{3.1}$$

For electrons, $R_H < 0$. The magnitude gives the carrier density directly.

**Quantum Corrections**

In real metals with complex Fermi surfaces, the Hall coefficient may deviate from this simple form. For materials with both electron and hole pockets, the Hall coefficient can even be positive despite electrons being the dominant charge carriers in some regions of the Fermi surface.

---

## Part IV: Thermoelectric Effects

### 4.1 The Seebeck Effect

**Physical Origin**

When a temperature gradient exists in a metal, electrons diffuse from hot to cold regions. However, this diffusion creates a charge imbalance, generating an electric field that opposes further diffusion. In steady state, there is no net current, but there is a potential difference proportional to the temperature difference.

**Calculation**

With $\nabla T \neq 0$ and $\mathbf{E} \neq 0$, the Boltzmann equation in the relaxation time approximation gives:

$$\mathbf{v} \cdot \nabla_r f - \frac{e}{\hbar}\mathbf{E} \cdot \nabla_k f = -\frac{f - f_0}{\tau}$$

Writing $f = f_0 + f_1$ and keeping first order:

$$\mathbf{v} \cdot \frac{\partial f_0}{\partial T}\nabla T - e\mathbf{E} \cdot \mathbf{v} \frac{\partial f_0}{\partial E} = -\frac{f_1}{\tau}$$

Using $\frac{\partial f_0}{\partial T} = -\frac{\partial f_0}{\partial E}\frac{E - E_F}{T}$:

$$f_1 = \tau \frac{\partial f_0}{\partial E} \mathbf{v} \cdot \left[\frac{E - E_F}{T}\nabla T + e\mathbf{E}\right]$$

Setting $\mathbf{j} = 0$ for the open-circuit condition:

$$\mathbf{j} = -2e \int \frac{d^3k}{(2\pi)^3} \mathbf{v} f_1 = 0$$

This requires:

$$e\mathbf{E} = -\frac{\nabla T}{T} \frac{\int \tau v^2 (E - E_F) (-\partial f_0/\partial E) d^3k}{\int \tau v^2 (-\partial f_0/\partial E) d^3k}$$

The **thermopower** (Seebeck coefficient) is:

$$S = \frac{E}{|\nabla T|} = -\frac{1}{eT}\frac{\int \tau v^2 (E - E_F) (-\partial f_0/\partial E) d^3k}{\int \tau v^2 (-\partial f_0/\partial E) d^3k}$$

For free electrons with $\tau \propto E^r$, using Sommerfeld expansion:

$$S = -\frac{\pi^2}{3}\frac{k_B}{e}\frac{k_B T}{E_F}(r + \frac{3}{2}) \tag{4.1}$$

Typical values are $\mu$V/K—much smaller than in semiconductors due to the degeneracy of the electron gas in metals.

---

## Summary

| Quantity | Formula | Physical Meaning |
|----------|---------|------------------|
| Fermi energy | $E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$ | Highest occupied energy at $T=0$ |
| Fermi temperature | $T_F = E_F/k_B$ | Scale for quantum degeneracy |
| Electronic heat capacity | $C_V = \frac{\pi^2}{2}Nk_B\frac{T}{T_F}$ | Only electrons near $E_F$ participate |
| Electrical conductivity | $\sigma = \frac{ne^2\tau}{m^*}$ | Drude formula, quantum justified |
| Hall coefficient | $R_H = -\frac{1}{ne}$ | Direct measure of carrier density |
| Thermopower | $S \sim \frac{k_B}{e}\frac{k_B T}{E_F}$ | Entropy per carrier |

The theory of metal electrons demonstrates the power of quantum statistical mechanics. The key insight is the transition from thinking about individual electron trajectories (classical mechanics) to thinking about the occupation of quantum states (statistical mechanics). The Pauli exclusion principle dominates the physics, leading to the suppression of electronic heat capacity and the existence of a well-defined Fermi surface that governs all transport properties.
