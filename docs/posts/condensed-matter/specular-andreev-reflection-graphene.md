# Specular Andreev Reflection in Graphene: From Dirac Fermions to Superconducting Proximity

The interface between a normal metal and a superconductor hosts one of the most elegant phenomena in condensed matter physics: Andreev reflection, where an incident electron is retro-reflected as a hole while a Cooper pair is injected into the superconductor. In ordinary metals this process is governed by non-relativistic Schrödinger electrons, and the reflected hole traces back along the incoming trajectory. Graphene changes this picture fundamentally. Its charge carriers are massless Dirac fermions governed by a linear dispersion, and when the Dirac equation is married to the Bogoliubov–de Gennes theory of superconductivity, the electron-hole conversion acquires new kinematic possibilities — most strikingly, a transition from retro-reflection to **specular reflection** as the chemical potential is tuned through the charge neutrality point.

## 1. Andreev Reflection: The Basic Mechanism

At a normal-metal–superconductor (NS) interface with subgap bias $|\varepsilon| < \Delta_0$, single-electron states cannot propagate into the superconductor. An incident electron from the normal side must therefore be reflected, but the superconducting gap demands that charge be transferred into the condensate in units of $2e$. The microscopic process is:

1. The incident electron approaches the interface.
2. A second electron is pulled from the normal region to form a Cooper pair in the superconductor.
3. The resulting vacancy in the normal region propagates backward as a hole.

Charge is conserved: the normal region loses net charge $-e$ (one electron removed, one hole left behind), while the superconductor gains $-2e$ (one Cooper pair). Particle number, however, is not a conserved quantity across the interface; what matters is the coherent conversion between electron and hole excitations.

In a conventional metal with parabolic dispersion, the reflected hole belongs to the same conduction band as the incident electron. Its group velocity points opposite to its wave vector, so the reflection is **retro-grade**: the hole retraces the incoming path. Graphene introduces two new ingredients that overturn this intuition.

## 2. Why Graphene Needs the Dirac Equation

Before writing down the Bogoliubov–de Gennes Hamiltonian, it is worth recalling why graphene is special. A free electron in vacuum obeys the Schrödinger equation with a parabolic dispersion $E = p^2/2m$. Graphene's charge carriers do not.

### Honeycomb Lattice and Sublattices

Graphene is a single atomic layer of carbon arranged in a honeycomb lattice. The lattice is not Bravais: it consists of two interpenetrating triangular sublattices, conventionally called A and B. Every A atom has three nearest neighbours, all on the B sublattice, and vice versa.

Tight-binding calculations with nearest-neighbour hopping $t$ give the Bloch bands

$$
E(\mathbf{k}) = \pm t \left| \sum_{j=1}^{3} e^{i\mathbf{k}\cdot\boldsymbol{\delta}_j} \right|,
$$

where $\boldsymbol{\delta}_j$ are the three vectors connecting an A site to its nearest B neighbours. The plus sign gives the conduction band ($\pi^*$), the minus sign the valence band ($\pi$). The two bands touch at six points on the edge of the hexagonal Brillouin zone. Only two of these are inequivalent; they are labelled $K$ and $K'$ and are related by time reversal.

### The Dirac Point

Expanding the tight-binding dispersion to linear order around either $K$ or $K'$ gives

$$
E(\mathbf{k}) = \pm \hbar v |\mathbf{k} - \mathbf{K}|,
$$

with $v = 3ta/2\hbar \approx 10^6\,\text{m/s}$. The dispersion is **linear** and **gapless**: the positive and negative branches form two cones touching at a single point. This is the Dirac point.

Linear dispersion means the effective mass vanishes. The low-energy excitations are not Schrödinger electrons; they are **massless Dirac fermions**. Their wave equation is the two-dimensional Dirac equation with zero rest mass:

$$
H = \hbar v \, \mathbf{p} \cdot \boldsymbol{\sigma} = \hbar v (p_x \sigma_x + p_y \sigma_y).
$$

Here $\boldsymbol{\sigma} = (\sigma_x, \sigma_y)$ are Pauli matrices, but they do not act on real spin. They act on **sublattice pseudospin**: the two components of the spinor correspond to the amplitude on the A and B sublattices. The eigenstates are plane waves with definite chirality: the pseudospin is locked parallel or antiparallel to the momentum.

The two valleys $K$ and $K'$ are described by the same Hamiltonian with opposite sign of $p_y$ (or, equivalently, by exchanging $\sigma_x \to \sigma_x$, $\sigma_y \to -\sigma_y$). For the NS interface problem the valley index is largely a spectator; the physics is captured by a single-valley Dirac equation.

### What Changes in an NS Junction?

For Andreev reflection the crucial difference between graphene and an ordinary metal is the fate of the **hole**. In a parabolic band the hole sits in the same band as the electron, merely at a different momentum. In graphene's linear band the hole can sit in the **conduction band** (if $E_F > \varepsilon$) or in the **valence band** (if $E_F < \varepsilon$). The two cases correspond to retro-reflection and specular reflection, respectively. This band-structure ambiguity is the root of everything that follows.

## 3. The Dirac–Bogoliubov–de Gennes Equation

To incorporate superconductivity into the Dirac Hamiltonian, one couples electrons and holes through the pairing potential $\Delta$ and writes the four-component Dirac–Bogoliubov–de Gennes (DBdG) equation:

$$
\begin{pmatrix}
\mathbf{p}\cdot\boldsymbol{\sigma} - U - E_F & \Delta \\
\Delta^* & U + E_F - \mathbf{p}\cdot\boldsymbol{\sigma}
\end{pmatrix}
\begin{pmatrix} u \\ v \end{pmatrix}
= \varepsilon \begin{pmatrix} u \\ v \end{pmatrix} .
$$

Here $u$ and $v$ are two-component spinors describing the electron and hole amplitudes, $E_F$ is the Fermi energy in the normal region, and $U$ is a potential shift that can be used to model doping.

#### Doping as a Potential Shift

In pristine graphene the valence and conduction bands touch at the Dirac point, and the Fermi level sits exactly at zero energy. Real samples are never perfectly intrinsic; some mechanism always pushes $E_F$ away from the Dirac point. The scalar term $-U \cdot \mathbb{I}$ in the Hamiltonian captures this by rigidly shifting the entire band structure: $U > 0$ pulls the bands downward so that $E_F$ lies in the conduction band (electron or n-type doping), while $U < 0$ pushes them upward so that $E_F$ lies in the valence band (hole or p-type doping).

Experimentally this shift is achieved in several ways. A back-gate voltage across a dielectric layer electrostatically induces carriers and tunes $E_F$ continuously over hundreds of meV. Chemical adsorbates such as potassium atoms or NH$_3$ molecules donate or accept electrons, producing fixed doping densities as large as $10^{13}\,\text{cm}^{-2}$. The SiO$_2$ substrate itself usually introduces a mild p-type background because of surface trapped charges. Encapsulation in hexagonal boron nitride (hBN) suppresses this substrate-induced disorder and allows the sample to be tuned close to charge neutrality ($U \approx 0$) with high mobility.

In the NS junction model the superconducting electrode is taken to be heavily doped: we set $U = -U_0$ with $U_0 \gg E_F, \varepsilon, \Delta_0$ in the region $x < 0$. This guarantees a large Fermi surface in the superconductor, which simplifies the boundary-condition matching and reflects the experimental fact that metallic superconducting contacts are always strongly n-type. In the normal graphene region ($x > 0$) we set $U = 0$, using the normal region as the energy reference.

The crucial point is that the doping level in the normal region — controlled by $E_F$ relative to the Dirac point — determines whether the reflected hole lives in the conduction band or the valence band, and therefore whether Andreev reflection is retro-grade or specular.

The superconducting proximity effect in graphene is thus a marriage of **relativistic kinematics** (Dirac electrons) and **Cooper-pair correlations** (Bogoliubov quasiparticles). The cross-term $\Delta$ couples states that live in different valleys of the band structure — a feature absent in conventional metals.

## 4. Normal-Region States: Electrons and Holes

Setting $\Delta = 0$ and $U = 0$ in the normal region, the DBdG equation decouples into two independent $2 \times 2$ Dirac equations.

### Electron States

For electron states $(v = 0)$ the equation reads $(\mathbf{p}\cdot\boldsymbol{\sigma} - E_F)u = \varepsilon u$. 

#### Plane-Wave Ansatz and Its Motivation

The NS interface is taken to lie in the $y$-$z$ plane at $x = 0$, so the Hamiltonian is **translationally invariant along $y$**. Momentum in the transverse direction is therefore conserved, and every eigenstate can be labelled by a definite wave number $q$. This justifies the factor $e^{iqy}$.

In the longitudinal direction $x$ the system is not uniform — the interface breaks translational symmetry — but away from $x = 0$ both the normal and superconducting regions are themselves homogeneous. In each bulk region the wave function must therefore be a superposition of plane waves $e^{ik_x x}$. Because the Dirac equation is first-order in momentum, a given energy and transverse momentum $q$ admit two values of $k_x$: one positive (right-moving) and one negative (left-moving). The ansatz

$$
u(x,y) = e^{iqy} e^{ik_x x} \chi
$$

encodes precisely this structure: $e^{iqy}$ fixes the conserved transverse momentum, $e^{ik_x x}$ describes propagation toward or away from the interface, and the two-component spinor $\chi$ carries the sublattice (pseudospin) degree of freedom. The parameter $\alpha$ is introduced to package $q$ and $k_x$ into a single propagation angle measured from the normal to the interface:

$$
\sin\alpha = \frac{\hbar v q}{E_F + \varepsilon}, \qquad \alpha \in (-\pi/2, \pi/2).
$$

With this definition the longitudinal wave number becomes $k = (E_F + \varepsilon)/(\hbar v) \cos\alpha$. The two eigen spinors are

$$
\Psi_{e\pm} = e^{iqy \pm ikx} \frac{1}{\sqrt{\cos\alpha}} \begin{pmatrix} e^{\mp i\alpha/2} \\ \pm e^{\pm i\alpha/2} \\ 0 \\ 0 \end{pmatrix},
$$

with $\Psi_{e-}$ describing the incident wave (propagating toward the interface at $x=0$) and $\Psi_{e+}$ the normally reflected wave (propagating away).

### Hole States

For hole states $(u = 0)$ the sign of the energy term flips: $(\mathbf{p}\cdot\boldsymbol{\sigma})v = (E_F - \varepsilon)v$. The hole propagation angle $\alpha'$ is defined analogously,

$$
\sin\alpha' = \frac{\hbar v q}{|E_F - \varepsilon|},
$$

and the corresponding spinors are

$$
\Psi_{h\pm} = e^{iqy \pm ik'x} \frac{1}{\sqrt{\cos\alpha'}} \begin{pmatrix} 0 \\ 0 \\ e^{\mp i\alpha'/2} \\ \mp e^{\pm i\alpha'/2} \end{pmatrix},
$$

with $k' = |E_F - \varepsilon|/(\hbar v) \cos\alpha'$.

The critical observation is that the hole lives at energy $E_F - \varepsilon$ rather than $E_F + \varepsilon$. When $\varepsilon < E_F$, this places the hole in the **conduction band**; when $\varepsilon > E_F$, it falls into the **valence band**. The sign of the group velocity relative to the wave vector is opposite in the two cases, and this single fact controls whether reflection is retro-grade or specular.

## 5. The Critical Angle

The angle $\alpha'$ is real only when $|\sin\alpha'| \leq 1$, which defines a **critical angle**

$$
\alpha_c = \arcsin\!\left(\frac{|E_F - \varepsilon|}{E_F + \varepsilon}\right).
$$

For $|\alpha| < \alpha_c$, Andreev reflection is kinematically allowed and four scattering states coexist in the normal region: $\Psi_{e-}$ (incident electron), $\Psi_{e+}$ (normal reflection), $\Psi_{h-}$ (incident hole), and $\Psi_{h+}$ (Andreev-reflected hole). For $|\alpha| > \alpha_c$, the hole cannot propagate and Andreev reflection is suppressed; only normal reflection survives.

## 6. Superconducting Region and the Heavily Doped Limit

In the superconducting region the DBdG equation couples electrons and holes through $\Delta_0$. The dispersion relation is

$$
\varepsilon^2 = \Delta_0^2 + (\hbar v|k| - E_{S0})^2,
$$

with $E_{S0} = U_0 + E_F$. For subgap energies $\varepsilon < \Delta_0$, the wave number $k_x$ acquires an imaginary part and the wave function decays exponentially into the superconductor. There are no propagating single-particle modes; all incident probability current must be reflected.

In the heavily doped limit $U_0 \gg E_F, \varepsilon, \Delta_0$, the superconducting Fermi surface is large and the decay constant simplifies to $\kappa = (\Delta_0/\hbar v) \sin\beta$, where $\beta$ parameterizes the energy through $\varepsilon = \Delta_0 \cos\beta$.

## 7. Boundary Matching

At $x = 0$ the four-component wave function must be continuous. Writing the scattering state in the normal region as a superposition of incident and reflected waves,

$$
\Psi_N = \Psi_{e-} + r\,\Psi_{e+} + r_A\,\Psi_{h+},
$$

and matching it to the decaying superconducting solution $\Psi_S = a\,\Psi_{S+} + b\,\Psi_{S-}$, one obtains four linear equations for the four unknown amplitudes $(r, r_A, a, b)$. The reflection amplitudes are:

$$
r_A = \frac{e^{-i\phi}}{X}\sqrt{\frac{\cos\alpha}{\cos\alpha'}} \quad (|\alpha| < \alpha_c),
\qquad
r = -\frac{1}{X}\left[\cos\beta\,\sin\frac{\alpha'+\alpha}{2} + i\sin\beta\,\sin\frac{\alpha'-\alpha}{2}\right],
$$

where

$$
X = \cos\beta\,\cos\frac{\alpha'-\alpha}{2} + i\sin\beta\,\cos\frac{\alpha'+\alpha}{2}.
$$

Unitarity requires $|r|^2 + |r_A|^2 = 1$ for $\varepsilon < \Delta_0$, which follows directly from these expressions after elementary trigonometric manipulation. All subgap probability current is reflected; nothing propagates into the superconductor.

## 8. Retro-Reflection versus Specular Reflection

The distinction between the two regimes hinges on the relative sign of $\alpha$ and $\alpha'$.

### The Retro-Reflective Regime ($E_F \gg \varepsilon$)

When the normal region is heavily doped, the Fermi energy sits deep in the conduction band. To leading order in $\varepsilon/E_F$,

$$
\sin\alpha' \approx \frac{\hbar v q}{E_F} \approx \sin\alpha \quad \Rightarrow \quad \alpha' \approx -\alpha.
$$

The hole lies in the conduction band, so its group velocity points **opposite** to its wave vector. The reflected hole therefore retraces the incident electron trajectory. This is the conventional **retro-reflection** familiar from non-relativistic metals.

In this limit the amplitudes simplify to

$$
r_A = \frac{e^{-i\phi}\cos\alpha}{(\varepsilon/\Delta_0)\cos\alpha + \zeta}, \qquad
r = -\frac{\zeta\sin\alpha}{(\varepsilon/\Delta_0)\cos\alpha + \zeta},
$$

with $\zeta = \sqrt{1 - (\varepsilon/\Delta_0)^2}$.

### The Specular Regime ($E_F \ll \varepsilon$)

At low doping, or equivalently for injection energies well above the Fermi level, the hole resides in the valence band. Now

$$
\sin\alpha' \approx \frac{\hbar v q}{\varepsilon} \approx \sin\alpha \quad \Rightarrow \quad \alpha' \approx \alpha.
$$

The hole group velocity points **in the same direction** as its wave vector. The reflected hole therefore exits the interface at the same angle as the incident electron, on the same side of the normal — a mirror-like **specular reflection**.

The amplitudes in this limit become

$$
r_A = \frac{e^{-i\phi}\cos\alpha}{\varepsilon/\Delta_0 + \zeta\cos\alpha}, \qquad
r = -\frac{(\varepsilon/\Delta_0)\sin\alpha}{\varepsilon/\Delta_0 + \zeta\cos\alpha}.
$$

The transition from retro- to specular reflection is not merely a change in trajectory geometry; it corresponds to a qualitative shift in the **voltage dependence of the subgap conductance**.

## 9. Perfect Andreev Reflection at Normal Incidence

At normal incidence ($\alpha = 0$, $q = 0$) the expressions collapse to their simplest form. The normal reflection amplitude vanishes identically,

$$
r = 0,
$$

while the Andreev reflection amplitude becomes a pure phase factor,

$$
r_A = e^{-i(\phi + \beta)}.
$$

The reflection probability is therefore $|r_A|^2 = 1$ and $|r|^2 = 0$: **every incident electron is converted into a reflected hole with unit efficiency**.

This result is remarkable because the Fermi wavelength mismatch between the normal and superconducting regions is enormous — in the heavily doped superconductor the Fermi momentum is orders of magnitude larger than in graphene. In a conventional metal such a mismatch would suppress Andreev reflection through normal reflection. The perfect conversion in graphene is protected by **pseudospin (chirality) conservation**: the incident electron, the reflected hole, and the transmitted Cooper pair all share the same sublattice pseudospin at $\alpha = 0$, while normal reflection would require a chirality flip and is therefore forbidden.

The analogy with Klein tunneling is direct. A massless Dirac fermion incident normally on a potential barrier transmits with probability $T = 1$ because chirality cannot be flipped by a scalar potential. At an NS interface the same symmetry ensures perfect electron-to-hole conversion.

## 10. Conductance and the Inversion of Voltage Dependence

The differential conductance of the NS interface at subgap voltages is proportional to the angle-integrated Andreev reflection probability. In the two limiting regimes this integral yields qualitatively different behaviors.

For **retro-reflection** ($E_F \gg \varepsilon$), the conductance increases with applied voltage. The phase space for Andreev reflection grows as $\varepsilon$ approaches $\Delta_0$, and the interface becomes increasingly transparent to Cooper-pair injection.

For **specular reflection** ($E_F \ll \varepsilon$), the opposite occurs: the conductance **decreases** with voltage. The reason is that in the specular regime the hole propagates on the opposite side of the charge-neutrality point from the electron. The angular dependence of the reflection amplitude suppresses the integrated probability as $\varepsilon$ increases, because the condition $|\alpha| < \alpha_c$ becomes progressively more restrictive.

The crossover between these two behaviors occurs when the Fermi energy is tuned through the Dirac point. Experimentally, this means that sweeping the gate voltage (which controls $E_F$) across charge neutrality should produce an **inversion of the subgap conductance curve**: from a rising conductance characteristic of retro-reflection to a falling conductance characteristic of specular reflection.

## 11. Experimental Outlook

The observation of specular Andreev reflection requires graphene samples in which the Fermi energy can be tuned close to the Dirac point while maintaining good electrical contact to a superconducting electrode. Early experiments on graphene–aluminum junctions confirmed the predicted retro-reflective behavior at high doping. The specular regime remains more challenging because disorder and charge inhomogeneity broaden the Dirac point, washing out the sharp crossover.

More recent advances in van der Waals heterostructures — in particular, encapsulating graphene in hexagonal boron nitride — have reduced disorder to levels where the Dirac point is resolved with sub-meV precision. Combined with superconducting contacts made from NbSe$_2$ or other 2D superconductors, these devices offer a realistic platform for observing the full transition from retro- to specular reflection and the associated conductance inversion.

The broader significance extends beyond graphene itself. Any Dirac material — topological insulator surface states, three-dimensional Dirac semimetals, or moiré superlattices — hosts massless charge carriers whose chirality fundamentally alters the Andreev reflection kinematics. Specular reflection is not an exotic curiosity but a generic consequence of linear dispersion married to superconducting proximity.

---

## References

- C. W. J. Beenakker, "Specular Andreev reflection in graphene," *Phys. Rev. Lett.* **97**, 067007 (2006), arXiv:cond-mat/0604594.
