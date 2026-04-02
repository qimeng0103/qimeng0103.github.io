# Semiconductor Electron Theory: From Band Structure to p-n Junctions

📅 **Date:** 2026-04-02 | 🏷️ **Tags:** Solid State Physics, Semiconductors, p-n Junctions | 📂 **Category:** Condensed Matter Notes

---

## Introduction

Semiconductors occupy a unique position in condensed matter physics, bridging the gap between insulating and metallic behavior. Unlike metals where the Fermi level lies within a partially filled band, semiconductors have a small band gap separating a filled valence band from an empty conduction band.

This article provides a comprehensive treatment of semiconductor physics, with detailed derivations of all statistical mechanics formulas and explicit explanations of solid-state physics concepts.

---

## Part I: Band Structure and Impurity Levels

### 1.1 The Fundamental Difference: Metals vs. Semiconductors

**Energy Band Diagram**

In the single-electron approximation, electrons in a crystal occupy energy bands. The key distinction between materials arises from the position of the Fermi energy $E_F$ relative to these bands:

- **Metals**: The Fermi level lies within a partially filled band, allowing electrons to move freely and conduct electricity even at $T = 0$.

- **Insulators**: The Fermi level lies in a large band gap ($E_g > 5$ eV). At room temperature, $k_B T \approx 0.025$ eV, so thermal excitation across the gap is negligible: $e^{-E_g/k_B T} \sim e^{-200} \approx 0$.

- **Semiconductors**: The Fermi level lies in a small gap ($E_g \sim 0.1$-$3$ eV). For $E_g = 1$ eV:

$$
\frac{E_g}{k_B T} = \frac{1 \text{ eV}}{0.025 \text{ eV}} \approx 40
$$

While $e^{-40} \approx 4 \times 10^{-18}$ is small, when multiplied by the enormous density of states ($\sim 10^{19}$ cm$^{-3}$), it gives a measurable carrier concentration ($n_i \sim 10^{10}$ cm$^{-3}$ for Si).

### 1.2 Intrinsic Semiconductors: Electron-Hole Pairs

**Thermal Generation of Carriers**

In a pure (intrinsic) semiconductor, thermal energy excites electrons from the valence band to the conduction band. This process creates:

$$
\text{Valence band electron} + \text{thermal energy} \rightarrow \text{Conduction band electron} + \text{Valence band hole}
$$

Each excitation produces an **electron-hole pair**:
- **Electron**: Negative charge ($-e$), resides in conduction band, effective mass $m_e^*$
- **Hole**: Positive charge ($+e$), represents absence of electron in valence band, effective mass $m_h^*$

**Charge Neutrality in Intrinsic Semiconductors**

Since electrons and holes are created in pairs:

$$
n = p = n_i
$$

where $n_i$ is the intrinsic carrier concentration.

### 1.3 Extrinsic Semiconductors: Doping and Impurity Levels

**Donors and Acceptors**

Impurities are intentionally introduced to control carrier concentration:

- **Donors** (e.g., P, As in Si): Have one more valence electron than the host. This extra electron is weakly bound and easily ionized: $N_D \rightarrow N_D^+ + e^-$.

- **Acceptors** (e.g., B, Al in Si): Have one fewer valence electron. They capture electrons from the valence band, creating holes: $N_A + e^- \rightarrow N_A^-$ (or equivalently, $N_A \rightarrow N_A^- + h^+$).

**The Hydrogenic Model for Impurities**

Consider a donor atom with effective charge $+e$ (nucleus + core electrons) and one loosely bound electron. In the semiconductor medium:

1. **Dielectric screening**: The Coulomb potential is reduced by the dielectric constant $\varepsilon$:
   $$
   V(r) = -\frac{e^2}{4\pi\varepsilon_0\varepsilon r}
   $$

2. **Effective mass**: The electron moves with effective mass $m^*$ rather than free electron mass $m_0$.

**Detailed Derivation of Binding Energy**

The Schrödinger equation for the donor electron:

$$
\left(-\frac{\hbar^2}{2m_e^*}\nabla^2 - \frac{e^2}{4\pi\varepsilon_0\varepsilon r}\right)\psi(\mathbf{r}) = E\psi(\mathbf{r})
$$

Compare to the hydrogen atom equation:

$$
\left(-\frac{\hbar^2}{2m_0}\nabla^2 - \frac{e^2}{4\pi\varepsilon_0 r}\right)\psi(\mathbf{r}) = E\psi(\mathbf{r})
$$

The hydrogen ground state energy is:

$$
E_H = -\frac{m_0 e^4}{2(4\pi\varepsilon_0)^2\hbar^2} = -13.6 \text{ eV}
$$

By dimensional analysis, replacing $m_0 \rightarrow m_e^*$ and $e^2 \rightarrow e^2/\varepsilon$:

$$
E_D = -\frac{m_e^*}{m_0} \cdot \frac{1}{\varepsilon^2} \cdot 13.6 \text{ eV}
$$

**Numerical Estimate for Silicon**

For Si: $\varepsilon \approx 11.7$, $m_e^*/m_0 \approx 0.26$ (conductivity effective mass)

$$
E_D = -0.26 \times \frac{1}{(11.7)^2} \times 13.6 \text{ eV} \approx -0.026 \text{ eV} = -26 \text{ meV}
$$

This is indeed much smaller than the Si band gap ($E_g = 1.12$ eV), confirming that donor levels lie just below the conduction band edge.

**Effective Bohr Radius**

The Bohr radius in hydrogen is $a_0 = 4\pi\varepsilon_0\hbar^2/(m_0 e^2) \approx 0.53$ Å. The effective Bohr radius for donor states:

$$
a_B^* = \frac{\varepsilon m_0}{m_e^*} a_0 = \frac{11.7}{0.26} \times 0.53 \text{ Å} \approx 24 \text{ Å} = 2.4 \text{ nm}
$$

Since $a_B^* \gg a_{lattice} \approx 0.5$ nm, the electron orbit encompasses many unit cells, justifying the use of effective mass approximation and continuum dielectric theory.

---

## Part II: Statistical Mechanics of Carriers

### 2.1 Why Maxwell-Boltzmann Statistics Apply

**The Fermi-Dirac Distribution**

In equilibrium, the probability of occupying a state with energy $E$ is:

$$
f(E) = \frac{1}{e^{(E-E_F)/k_B T} + 1}
$$

**The Non-Degeneracy Condition**

In semiconductors, the Fermi level lies in the band gap, far from both band edges:

$$
E_C - E_F \gg k_B T \quad \text{and} \quad E_F - E_V \gg k_B T
$$

For the conduction band, since $E \geq E_C$:

$$
E - E_F \geq E_C - E_F \gg k_B T
$$

Therefore:

$$
e^{(E-E_F)/k_B T} \gg 1
$$

And the Fermi-Dirac distribution simplifies to:

$$
f(E) \approx \frac{1}{e^{(E-E_F)/k_B T}} = e^{-(E-E_F)/k_B T} = e^{-(E_C-E_F)/k_B T} \cdot e^{-(E-E_C)/k_B T}
$$

This is the **Maxwell-Boltzmann distribution**. The key difference from metals is:

| Aspect | Metals | Semiconductors |
|--------|--------|----------------|
| Fermi level position | Inside band | In gap |
| Occupation at $E_F$ | $f(E_F) = 1/2$ | $f(E_C) \ll 1$ |
| Statistics | Fermi-Dirac (degenerate) | Maxwell-Boltzmann (non-degenerate) |
| Pauli exclusion | Dominant | Negligible |

**Physical Interpretation**

Because the conduction band is nearly empty ($f(E) \ll 1$), the probability of two electrons occupying the same state is negligible. Electrons behave as distinguishable classical particles, enabling the use of Maxwell-Boltzmann statistics and greatly simplifying calculations.

### 2.2 Derivation of Electron and Hole Concentrations

**Density of States in the Conduction Band**

Near the conduction band minimum, electrons behave as free particles with effective mass $m_e^*$:

$$
E(k) = E_C + \frac{\hbar^2 k^2}{2m_e^*}
$$

To find the density of states $g_C(E)$, we count the number of $k$-states per unit energy interval. In 3D, the number of states with wavevector magnitude less than $k$ is:

$$
N(k) = 2 \times \frac{\frac{4}{3}\pi k^3}{(2\pi)^3/V} = \frac{Vk^3}{3\pi^2}
$$

The factor of 2 accounts for spin degeneracy. Converting to energy using $E = E_C + \hbar^2 k^2/(2m_e^*)$:

$$
k = \sqrt{\frac{2m_e^*(E-E_C)}{\hbar^2}}
$$

Taking the derivative:

$$
g_C(E) = \frac{1}{V}\frac{dN}{dE} = \frac{1}{V}\frac{dN}{dk}\frac{dk}{dE} = \frac{k^2}{\pi^2} \cdot \frac{m_e^*}{\hbar^2 k} = \frac{(2m_e^*)^{3/2}}{2\pi^2\hbar^3}\sqrt{E-E_C}
$$

for $E \geq E_C$, and zero otherwise.

**Calculating the Electron Concentration**

The total electron concentration is:

$$
n = \int_{E_C}^{\infty} g_C(E) f(E) dE
$$

Substituting our expressions:

$$
n = \frac{(2m_e^*)^{3/2}}{2\pi^2\hbar^3} \int_{E_C}^{\infty} \sqrt{E-E_C} \cdot e^{-(E-E_F)/k_B T} dE
$$

**Step-by-Step Integration**

Let $x = E - E_C$, so $E - E_F = x + (E_C - E_F)$:

$$
n = \frac{(2m_e^*)^{3/2}}{2\pi^2\hbar^3} e^{-(E_C-E_F)/k_B T} \int_0^{\infty} x^{1/2} e^{-x/k_B T} dx
$$

The integral is a Gamma function. Let $u = x/k_B T$, so $dx = k_B T du$:

$$
\int_0^{\infty} x^{1/2} e^{-x/k_B T} dx = (k_B T)^{3/2} \int_0^{\infty} u^{1/2} e^{-u} du = (k_B T)^{3/2} \Gamma\left(\frac{3}{2}\right)
$$

Since $\Gamma(3/2) = \frac{1}{2}\Gamma(1/2) = \frac{\sqrt{\pi}}{2}$:

$$
n = \frac{(2m_e^*)^{3/2}}{2\pi^2\hbar^3} e^{-(E_C-E_F)/k_B T} \cdot (k_B T)^{3/2} \cdot \frac{\sqrt{\pi}}{2}
$$

Simplifying:

$$
n = 2\left(\frac{m_e^* k_B T}{2\pi\hbar^2}\right)^{3/2} e^{-(E_C-E_F)/k_B T}
$$

**Effective Density of States**

We define the **effective density of states** in the conduction band:

$$
N_C = 2\left(\frac{m_e^* k_B T}{2\pi\hbar^2}\right)^{3/2}
$$

This allows us to write the electron concentration compactly as:

$$
n = N_C e^{-(E_C-E_F)/k_B T}
$$

**Physical Interpretation**: The electron concentration equals the effective number of states at the conduction band edge ($N_C$), multiplied by the Boltzmann factor for the energy difference between the band edge and the Fermi level.

**Hole Concentration**

By similar analysis for holes in the valence band (with effective mass $m_h^*$):

$$
p = N_V e^{-(E_F-E_V)/k_B T}
$$

where:

$$
N_V = 2\left(\frac{m_h^* k_B T}{2\pi\hbar^2}\right)^{3/2}
$$

Note that the exponent is $(E_F - E_V)$ rather than $(E_V - E_F)$ because holes have positive energy when they are lower in the band diagram (closer to the valence band maximum).

**Numerical Values at Room Temperature**

For silicon ($m_e^* \approx 1.08m_0$, $m_h^* \approx 0.56m_0$):

$$
N_C = 2\left(\frac{1.08 \times 9.11 \times 10^{-31} \times 1.38 \times 10^{-23} \times 300}{2\pi \times (1.05 \times 10^{-34})^2}\right)^{3/2} \approx 2.8 \times 10^{19} \text{ cm}^{-3}
$$

$$
N_V \approx 1.0 \times 10^{19} \text{ cm}^{-3}
$$

### 2.3 The Law of Mass Action

**Derivation**

Multiply the expressions for electron and hole concentrations:

$$
np = N_C N_V e^{-(E_C-E_F)/k_B T} \cdot e^{-(E_F-E_V)/k_B T} = N_C N_V e^{-(E_C-E_V)/k_B T}
$$

The Fermi level cancels out! Defining the band gap $E_g = E_C - E_V$:

$$
np = N_C N_V e^{-E_g/k_B T}
$$

This is the **law of mass action** for semiconductors. At a given temperature, the product of electron and hole concentrations is constant, independent of doping or Fermi level position.

**Intrinsic Carrier Concentration**

For an intrinsic (pure) semiconductor, charge neutrality requires $n = p = n_i$. From the mass action law:

$$
n_i^2 = N_C N_V e^{-E_g/k_B T}
$$

Therefore:

$$
n_i = \sqrt{N_C N_V} e^{-E_g/2k_B T}
$$

This shows that $n_i$ depends exponentially on $E_g/(2k_B T)$. The factor of 2 in the exponent is crucial—it means that creating an electron-hole pair requires thermal energy of order $E_g/2$ per carrier, not $E_g$.

**Numerical Example for Silicon**

At $T = 300$ K with $E_g = 1.12$ eV:

$$
n_i = \sqrt{2.8 \times 10^{19} \times 1.0 \times 10^{19}} \cdot e^{-1.12/(2 \times 0.025)} \approx 1.5 \times 10^{10} \text{ cm}^{-3}
$$

This is much smaller than the atomic density of Si ($5 \times 10^{22}$ cm$^{-3}$), confirming that only a tiny fraction of atoms contribute carriers.

**Position of Intrinsic Fermi Level**

Setting $n = p$ for intrinsic material:

$$
N_C e^{-(E_C-E_i)/k_B T} = N_V e^{-(E_i-E_V)/k_B T}
$$

Taking the natural logarithm:

$$\ln N_C - \frac{E_C - E_i}{k_B T} = \ln N_V - \frac{E_i - E_V}{k_B T}$$

Solving for $E_i$:

$$
2E_i = E_C + E_V + k_B T \ln\left(\frac{N_C}{N_V}\right)
$$

$$
E_i = \frac{E_C + E_V}{2} + \frac{3}{4}k_B T \ln\left(\frac{m_h^*}{m_e^*}\right)
$$

If $m_h^* = m_e^*$, the intrinsic Fermi level lies exactly at mid-gap. For Si with $m_h^*/m_e^* \approx 0.52$, the correction is small ($\approx k_B T$).

### 2.4 Doped Semiconductors: Charge Neutrality and Fermi Level

**Donor Ionization Statistics**

Consider an n-type semiconductor with donor concentration $N_D$. The fraction of ionized donors is given by:

$$
\frac{N_D^+}{N_D} = 1 - f(E_D) = \frac{1}{1 + e^{-(E_D-E_F)/k_B T}}
$$

At room temperature, since donor binding energies are small ($E_C - E_D \sim 26$ meV $\sim k_B T$), most donors are ionized:

$$
N_D^+ \approx N_D
$$

**Charge Neutrality Equation**

The total positive charge equals the total negative charge:

$$
p + N_D^+ = n + N_A^-
$$

For an n-type semiconductor with negligible acceptors:

$$
n = p + N_D^+
$$

At moderate temperatures where $n_i \ll N_D$, we have $p = n_i^2/n \ll n \approx N_D$. Therefore:

$$
n \approx N_D
$$

**Finding the Fermi Level**

Using $n = N_C e^{-(E_C-E_F)/k_B T} = N_D$:

$$
E_C - E_F = k_B T \ln\left(\frac{N_C}{N_D}\right)
$$

$$
E_F = E_C - k_B T \ln\left(\frac{N_C}{N_D}\right)
$$

**Numerical Example**

For Si with $N_C = 2.8 \times 10^{19}$ cm$^{-3}$ and $N_D = 10^{16}$ cm$^{-3}$:

$$
E_C - E_F = 0.025 \text{ eV} \times \ln(2800) \approx 0.025 \times 7.9 \approx 0.20 \text{ eV}
$$

The Fermi level lies 0.20 eV below the conduction band, well within the gap but much closer to $E_C$ than to mid-gap ($E_g/2 = 0.56$ eV).

---

## Part III: Direct and Indirect Band Gaps

### 3.1 Momentum Conservation in Optical Transitions

**Photon Momentum vs. Electron Momentum**

When a photon is absorbed, exciting an electron from the valence band to the conduction band, both energy and momentum must be conserved.

For a photon with energy $E_{photon} = h\nu = E_g$:

$$
p_{photon} = \frac{h\nu}{c} = \frac{E_g}{c}
$$

For $E_g = 1$ eV:

$$
p_{photon} = \frac{1.6 \times 10^{-19} \text{ J}}{3 \times 10^8 \text{ m/s}} \approx 5.3 \times 10^{-28} \text{ kg m/s}
$$

Compare to the typical electron momentum at the Brillouin zone boundary:

$$
p_{BZ} \sim \frac{\hbar}{a} \sim \frac{1.05 \times 10^{-34}}{0.5 \times 10^{-9}} \approx 2 \times 10^{-25} \text{ kg m/s}
$$

The ratio is:

$$
\frac{p_{photon}}{p_{BZ}} \sim \frac{5 \times 10^{-28}}{2 \times 10^{-25}} \sim 10^{-3}
$$

**Conclusion**: The photon momentum is negligible compared to the Brillouin zone scale. Therefore, optical transitions are essentially **vertical** in $k$-space—the electron wavevector does not change during the transition.

### 3.2 Direct Band Gap Semiconductors

**Band Structure**

In a direct gap semiconductor (e.g., GaAs, InP), the conduction band minimum and valence band maximum occur at the same $k$-point (typically $k = 0$, the $\Gamma$ point).

**Absorption Coefficient**

Since momentum conservation is automatically satisfied, the absorption coefficient for direct transitions is:

$$
\alpha(h\nu) \propto \sqrt{h\nu - E_g}
$$

for $h\nu > E_g$. Above the band gap, absorption is strong ($\alpha \sim 10^4$ cm$^{-1}$), meaning light is absorbed within about 1 $\mu$m of the surface.

### 3.3 Indirect Band Gap Semiconductors

**Band Structure of Silicon**

In Si (indirect gap):
- Valence band maximum: at $k = 0$ ($\Gamma$ point)
- Conduction band minimum: at $k \approx 0.85 \times (2\pi/a)$ along the [100] direction (near the X point)

The minimum energy gap is $E_g = 1.12$ eV, but a vertical transition from the valence band maximum to the conduction band minimum would violate momentum conservation by $\Delta k \approx 0.85 \times (2\pi/a)$.

**Phonon-Assisted Transitions**

To conserve momentum, the transition requires assistance from a phonon (quantized lattice vibration). The process is:

1. Photon is absorbed (provides energy, negligible momentum)
2. Phonon is absorbed or emitted (provides momentum $\hbar q \approx \hbar \Delta k$)

**Transition Rate**

Using second-order perturbation theory, the transition rate involves:
- Photon-electron matrix element
- Phonon-electron matrix element
- Energy denominator from intermediate virtual state

The absorption coefficient is:

$$
\alpha_{indirect}(h\nu) \propto (h\nu - E_g \pm \hbar\omega_{phonon})^2
$$

The $\pm$ corresponds to phonon absorption or emission. The quadratic dependence (vs. square root for direct gaps) reflects the phase space available for two-particle processes.

**Comparison**

| Property | Direct Gap (GaAs) | Indirect Gap (Si) |
|----------|-------------------|-------------------|
| Absorption coefficient at $h\nu = E_g + 0.1$ eV | $\sim 10^4$ cm$^{-1}$ | $\sim 10^2$ cm$^{-1}$ |
| Radiative recombination rate | Fast ($\sim$ ns) | Slow ($\sim$ ms) |
| Application | LEDs, lasers | Electronics, solar cells |

---

## Part IV: Transport Properties

### 4.1 Drift Current and Mobility

**Equation of Motion**

Under an electric field $\mathbf{E}$, electrons experience force $\mathbf{F} = -e\mathbf{E}$. Between collisions, they accelerate. With collision time $\tau_n$, the average drift velocity is:

$$
\mathbf{v}_{d,n} = -\frac{e\tau_n}{m_e^*} \mathbf{E} = -\mu_n \mathbf{E}
$$

where the **electron mobility** is defined as:

$$
\mu_n = \frac{e\tau_n}{m_e^*}
$$

Similarly for holes:

$$
\mu_p = \frac{e\tau_p}{m_h^*}
$$

**Conductivity**

The total current density is the sum of electron and hole contributions:

$$
\mathbf{J} = (-en)\mathbf{v}_{d,n} + (ep)\mathbf{v}_{d,p} = e(n\mu_n + p\mu_p)\mathbf{E}
$$

The conductivity is:

$$
\sigma = e(n\mu_n + p\mu_p)
$$

**Resistivity**

$$
\rho = \frac{1}{\sigma} = \frac{1}{e(n\mu_n + p\mu_p)}
$$

### 4.2 Temperature Dependence of Mobility

**Scattering Mechanisms**

Three main processes limit mobility:

1. **Acoustic Phonon Scattering** (dominant at moderate temperatures):
   - Scattering rate: $1/\tau \propto T$
   - Mobility: $\mu \propto T^{-3/2}$

2. **Ionized Impurity Scattering** (dominant at low temperatures):
   - Coulomb scattering from charged donors/acceptors
   - Brooks-Herring formula: $\mu \propto T^{3/2}/N_{imp}$

3. **Optical Phonon Scattering** (dominant at high temperatures):
   - Requires $\hbar\omega_{optical} \sim k_B T$
   - Strong temperature dependence: $\mu \propto e^{\hbar\omega/k_B T}$

**Matthiessen's Rule**

When multiple scattering mechanisms are present:

$$
\frac{1}{\mu} = \frac{1}{\mu_{phonon}} + \frac{1}{\mu_{impurity}} + \ldots
$$

The mechanism with the shortest mean free time (highest scattering rate) dominates.

### 4.3 The Hall Effect

**Experimental Geometry**

Current $J_x$ flows in x-direction, magnetic field $B_z$ is applied in z-direction. A transverse electric field $E_y$ (Hall field) develops to balance the Lorentz force.

**Steady-State Condition**

For electrons with velocity $v_x$:

$$
F_y = -e(E_y - v_x B_z) = 0
$$

Therefore:

$$
E_y = v_x B_z = -\frac{J_x}{ne} B_z
$$

**Hall Coefficient**

Defining $R_H = E_y/(J_x B_z)$:

$$
R_H = -\frac{1}{ne}
$$

For holes (positive charge):

$$
R_H = +\frac{1}{pe}
$$

**Significance**

The sign of $R_H$ directly identifies the carrier type:
- $R_H < 0$: n-type (electron conduction)
- $R_H > 0$: p-type (hole conduction)

The magnitude gives the carrier concentration.

---

## Part V: The p-n Junction

### 5.1 Formation and Equilibrium

**Diffusion and Drift**

When p-type and n-type semiconductors are brought together:
1. Electrons diffuse from n-side (high $n$) to p-side (low $n$)
2. Holes diffuse from p-side (high $p$) to n-side (low $p$)
3. This leaves behind:
   - Positive ionized donors ($N_D^+$) on n-side
   - Negative ionized acceptors ($N_A^-$) on p-side
4. The resulting electric field opposes further diffusion
5. At equilibrium: drift current = diffusion current for each carrier type

### 5.2 Built-in Potential

**Fermi Level Alignment**

At equilibrium, the Fermi level must be constant throughout the device. In the bulk regions:

$$
E_{F,n} = E_C - k_B T \ln\left(\frac{N_C}{N_D}\right)
$$

$$
E_{F,p} = E_V + k_B T \ln\left(\frac{N_V}{N_A}\right)
$$

The built-in potential energy is the difference:

$$
eV_{bi} = E_{F,n} - E_{F,p} = E_g - k_B T \ln\left(\frac{N_C}{N_D}\right) - k_B T \ln\left(\frac{N_V}{N_A}\right)
$$

Using $n_i^2 = N_C N_V e^{-E_g/k_B T}$:

$$
eV_{bi} = k_B T \ln\left(\frac{N_D N_A}{n_i^2}\right)
$$

**Numerical Example**

For Si with $N_D = N_A = 10^{16}$ cm$^{-3}$ and $n_i = 1.5 \times 10^{10}$ cm$^{-3}$:

$$
V_{bi} = 0.025 \text{ eV} \times \ln\left(\frac{10^{32}}{2.25 \times 10^{20}}\right) = 0.025 \times \ln(4.4 \times 10^{11}) \approx 0.69 \text{ V}
$$

### 5.3 Depletion Region Analysis

**Charge Density**

Assume abrupt junction at $x = 0$. In the depletion region:
- n-side ($0 < x < x_n$): $\rho = +eN_D$
- p-side ($-x_p < x < 0$): $\rho = -eN_A$

**Poisson's Equation**

$$
\frac{d^2\phi}{dx^2} = -\frac{\rho}{\varepsilon}
$$

On the n-side:

$$
\frac{d^2\phi}{dx^2} = -\frac{eN_D}{\varepsilon}
$$

Integrating with boundary condition $d\phi/dx = 0$ at $x = x_n$:

$$
\frac{d\phi}{dx} = \frac{eN_D}{\varepsilon}(x_n - x)
$$

Integrating again:

$$
\phi(x) = \phi_n - \frac{eN_D}{2\varepsilon}(x_n - x)^2
$$

Similarly for the p-side with $\phi(-x_p) = \phi_p$:

$$
\phi(x) = \phi_p + \frac{eN_A}{2\varepsilon}(x + x_p)^2
$$

**Continuity Conditions**

At $x = 0$:
1. Potential continuous: $\phi(0^-) = \phi(0^+)$
2. Electric field continuous: $d\phi/dx|_{0^-} = d\phi/dx|_{0^+}$

From condition 2:

$$
eN_D x_n = eN_A x_p$$

This expresses charge neutrality: total positive charge equals total negative charge.

**Depletion Width**

Defining total width $W = x_n + x_p$:

$$
x_n = \frac{N_A}{N_D + N_A}W, \quad x_p = \frac{N_D}{N_D + N_A}W
$$

The potential difference is:

$$
V_{bi} = \phi_n - \phi_p = \frac{e}{2\varepsilon}(N_D x_n^2 + N_A x_p^2) = \frac{e}{2\varepsilon}\frac{N_D N_A}{N_D + N_A}W^2
$$

Solving for $W$:

$$
W = \sqrt{\frac{2\varepsilon V_{bi}}{e}\left(\frac{1}{N_D} + \frac{1}{N_A}\right)}
$$

For asymmetric junction with $N_D \gg N_A$:

$$
W \approx \sqrt{\frac{2\varepsilon V_{bi}}{eN_A}}
$$

The depletion region extends primarily into the lightly doped side.

### 5.4 Current-Voltage Characteristics

**Shockley Diode Equation**

Under applied bias $V$:
- **Forward bias** ($V > 0$): Barrier reduced to $e(V_{bi} - V)$
- **Reverse bias** ($V < 0$): Barrier increased to $e(V_{bi} + |V|)$

The current-voltage relationship is:

$$
J = J_0\left(e^{eV/k_B T} - 1\right)
$$

**Saturation Current Derivation**

The saturation current $J_0$ is the sum of minority carrier diffusion currents:

$$
J_0 = e\left(\frac{D_n n_{p0}}{L_n} + \frac{D_p p_{n0}}{L_p}\right)
$$

where:
- $n_{p0} = n_i^2/N_A$ (equilibrium minority electron concentration on p-side)
- $p_{n0} = n_i^2/N_D$ (equilibrium minority hole concentration on n-side)
- $D_n$, $D_p$ are diffusion coefficients
- $L_n = \sqrt{D_n \tau_n}$, $L_p = \sqrt{D_p \tau_p}$ are diffusion lengths

Using the Einstein relation $D = (k_B T/e)\mu$:

$$
J_0 = ek_B T\left(\frac{\mu_n n_{p0}}{L_n} + \frac{\mu_p p_{n0}}{L_p}\right)
$$

**Forward Bias**

For $V \gg k_B T/e$:

$$
J \approx J_0 e^{eV/k_B T}
$$

The current increases exponentially. A 60 mV increase (at room temperature) multiplies current by $e^{0.06/0.025} \approx 10$.

**Reverse Bias**

For $V < 0$ with $|V| \gg k_B T/e$:

$$
J \approx -J_0
$$

The current saturates at the small value $-J_0$.

### 5.5 Junction Capacitance

**Depletion Capacitance**

The depletion region acts as a parallel plate capacitor:

$$
C_j = \frac{\varepsilon A}{W}
$$

Substituting the expression for $W$:

$$
C_j = A\sqrt{\frac{e\varepsilon N_A N_D}{2(N_A + N_D)(V_{bi} - V)}}
$$

For asymmetric junction ($N_D \gg N_A$):

$$
C_j \approx A\sqrt{\frac{e\varepsilon N_A}{2(V_{bi} - V)}}
$$

The capacitance varies as $(V_{bi} - V)^{-1/2}$. This voltage dependence is used in varactor diodes for tuning applications.

---

## Summary

| Parameter | Symbol | Formula |
|-----------|--------|---------|
| Electron concentration | $n$ | $N_C \exp[-(E_C-E_F)/k_B T]$ |
| Hole concentration | $p$ | $N_V \exp[-(E_F-E_V)/k_B T]$ |
| Intrinsic carrier concentration | $n_i$ | $\sqrt{N_C N_V} \exp[-E_g/2k_B T]$ |
| Mass action law | $np$ | $n_i^2$ |
| Conductivity | $\sigma$ | $e(n\mu_n + p\mu_p)$ |
| Built-in potential | $V_{bi}$ | $(k_B T/e) \ln(N_D N_A/n_i^2)$ |
| Depletion width | $W$ | $\sqrt{2\varepsilon V_{bi}/e \cdot (1/N_D + 1/N_A)}$ |
| Diode current | $J$ | $J_0[\exp(eV/k_B T) - 1]$ |

Semiconductors exemplify how quantum mechanics (band theory) and statistical mechanics (carrier distributions) combine to determine macroscopic properties. The transition from degenerate Fermi-Dirac statistics in metals to classical Maxwell-Boltzmann statistics in semiconductors is a key insight that enables the rich variety of phenomena underlying modern electronics.
