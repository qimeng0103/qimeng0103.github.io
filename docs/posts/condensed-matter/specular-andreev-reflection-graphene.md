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

![Graphene honeycomb lattice with A/B sublattices (blue and red), the three nearest-neighbour vectors $\boldsymbol{\delta}_j$, and the primitive vectors $\mathbf{a}_1, \mathbf{a}_2$ of the underlying triangular Bravais lattice](/images/condensed-matter/specular-andreev-reflection/graphene_realspace.png)

To make the geometry explicit, place an A atom at the origin. The three vectors connecting this A atom to its nearest B neighbours are

$$
\boldsymbol{\delta}_1 = a\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad
\boldsymbol{\delta}_2 = a\begin{pmatrix} -1/2 \\ \sqrt{3}/2 \end{pmatrix}, \quad
\boldsymbol{\delta}_3 = a\begin{pmatrix} -1/2 \\ -\sqrt{3}/2 \end{pmatrix},
$$

where $a \approx 1.42\,\text{Å}$ is the carbon-carbon bond length. The primitive lattice vectors of the underlying triangular Bravais lattice are

$$
\mathbf{a}_1 = a\begin{pmatrix} 3/2 \\ \sqrt{3}/2 \end{pmatrix}, \qquad
\mathbf{a}_2 = a\begin{pmatrix} 3/2 \\ -\sqrt{3}/2 \end{pmatrix}.
$$

Every lattice site can be written as $\mathbf{R} = n_1\mathbf{a}_1 + n_2\mathbf{a}_2$ for integers $n_1, n_2$; A sites sit at these points, while B sites sit at $\mathbf{R} + \boldsymbol{\delta}_1$.

### From Atomic Orbitals to the Tight-Binding Hamiltonian

The electronic structure follows from the $p_z$ orbitals of carbon, which stick out of the plane and form $\pi$ bonds with their three neighbours. Because the $p_z$ orbital is odd under reflection in the plane, it does not hybridize with the in-plane $sp^2$ bonds; the $\pi$ and $\sigma$ sectors decouple.

In the tight-binding approximation one keeps only the dominant matrix element: the hopping amplitude $t \approx 2.7\,\text{eV}$ between nearest-neighbour $p_z$ orbitals. The Hamiltonian is

$$
H = -t \sum_{\langle i,j \rangle} \big( |i\rangle\langle j| + |j\rangle\langle i| \big),
$$

where the sum runs over all nearest-neighbour pairs $\langle i,j \rangle$ and $|i\rangle$ denotes the $p_z$ orbital on site $i$.

Because the lattice has two atoms per unit cell, it is natural to introduce Bloch states for each sublattice separately:

$$
|\mathbf{k}, A\rangle = \frac{1}{\sqrt{N}} \sum_{\mathbf{R}} e^{i\mathbf{k}\cdot\mathbf{R}} \, |\mathbf{R}, A\rangle, \qquad
|\mathbf{k}, B\rangle = \frac{1}{\sqrt{N}} \sum_{\mathbf{R}} e^{i\mathbf{k}\cdot\mathbf{R}} \, |\mathbf{R}, B\rangle.
$$

In this basis the Hamiltonian becomes a $2 \times 2$ matrix at each $\mathbf{k}$:

$$
H(\mathbf{k}) = \begin{pmatrix} 0 & h(\mathbf{k}) \\ h^*(\mathbf{k}) & 0 \end{pmatrix},
$$

where the off-diagonal element collects the three nearest-neighbour phase factors:

$$
h(\mathbf{k}) = -t \sum_{j=1}^{3} e^{i\mathbf{k}\cdot\boldsymbol{\delta}_j}
= -t \Big[ e^{ik_x a} + 2 e^{-ik_x a/2} \cos\!\Big(\frac{\sqrt{3}k_y a}{2}\Big) \Big].
$$

Diagonalizing $H(\mathbf{k})$ gives the two Bloch bands

$$
E(\mathbf{k}) = \pm |h(\mathbf{k})| = \pm t \left| \sum_{j=1}^{3} e^{i\mathbf{k}\cdot\boldsymbol{\delta}_j} \right|.
$$

The plus sign is the conduction band ($\pi^*$), the minus sign the valence band ($\pi$). The bands touch whenever $h(\mathbf{k}) = 0$, which happens at six points on the edge of the hexagonal Brillouin zone. Only two of these are inequivalent; they are labelled $K$ and $K'$ and are related by time reversal.

### The Dirac Point

In the reciprocal lattice the primitive vectors are

$$
\mathbf{b}_1 = \frac{2\pi}{3a}\begin{pmatrix} 1 \\ -\sqrt{3} \end{pmatrix}, \qquad
\mathbf{b}_2 = \frac{2\pi}{3a}\begin{pmatrix} 1 \\ \sqrt{3} \end{pmatrix}.
$$

![First Brillouin zone (hexagon) with reciprocal lattice vectors $\mathbf{b}_1, \mathbf{b}_2$, the $\Gamma$ point at the centre, and the two inequivalent Dirac points $K$ and $K'$ on the boundary](/images/condensed-matter/specular-andreev-reflection/graphene_bz_only.png)

The two inequivalent corners of the first Brillouin zone are at

$$
\mathbf{K} = \frac{2\pi}{3\sqrt{3}a}\begin{pmatrix} 0 \\ 2 \end{pmatrix}, \qquad
\mathbf{K}' = \frac{2\pi}{3\sqrt{3}a}\begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix}.
$$

Expanding $h(\mathbf{k})$ to linear order around $\mathbf{K}$ by setting $\mathbf{k} = \mathbf{K} + \mathbf{q}$ with $|\mathbf{q}|a \ll 1$ gives

$$
h(\mathbf{K} + \mathbf{q}) \approx \frac{3ta}{2} \big( q_x + i q_y \big) \equiv \hbar v \, q_+,
$$

with $v = 3ta/2\hbar \approx 10^6\,\text{m/s}$. The band energies are therefore

$$
E(\mathbf{q}) = \pm \hbar v |\mathbf{q}| = \pm \hbar v |\mathbf{k} - \mathbf{K}|.
$$

The dispersion is **linear** and **gapless**: the positive and negative branches form two cones touching at a single point. This is the Dirac point.

Linear dispersion means the effective mass vanishes. The low-energy excitations are not Schrödinger electrons; they are **massless Dirac fermions**. Their wave equation is the two-dimensional Dirac equation with zero rest mass:

$$
H = v \, \mathbf{p} \cdot \boldsymbol{\sigma} = v (p_x \sigma_x + p_y \sigma_y).
$$

Here $\boldsymbol{\sigma} = (\sigma_x, \sigma_y)$ are Pauli matrices, but they do not act on real spin. They act on **sublattice pseudospin**: the two components of the spinor correspond to the amplitude on the A and B sublattices. The eigenstates are plane waves with definite chirality: the pseudospin is locked parallel or antiparallel to the momentum.

The two valleys $K$ and $K'$ are described by the same Hamiltonian with opposite sign of $p_y$ (or, equivalently, by exchanging $\sigma_x \to \sigma_x$, $\sigma_y \to -\sigma_y$). For the NS interface problem the valley index is largely a spectator; the physics is captured by a single-valley Dirac equation.

![Graphene tight-binding valence (blue) and conduction (red) bands over an extended momentum region, showing the periodic Dirac-cone touch points](/images/graphene_spectrum.png)

### What Changes in an NS Junction?

For Andreev reflection the crucial difference between graphene and an ordinary metal is the fate of the **hole**. In a parabolic band the hole sits in the same band as the electron, merely at a different momentum. In graphene the situation is different because the conduction and valence bands touch linearly at the Dirac point. After Andreev reflection the hole carries energy $E_F - \varepsilon$ (the electron carried $E_F + \varepsilon$). Whether this energy is positive or negative relative to the Dirac point determines which band the hole state belongs to:

- **Retro-reflection** ($E_F > \varepsilon$): the hole energy $E_F - \varepsilon$ lies above the Dirac point. The hole state is formally in the **conduction band** (positive-energy branch of the Dirac cone), but as a *hole* excitation — an absence of an electron — its group velocity points **opposite** to its wave vector. The reflected hole therefore retraces the incident electron trajectory.
- **Specular reflection** ($E_F < \varepsilon$): the hole energy $E_F - \varepsilon$ lies below the Dirac point. The hole state is in the **valence band** (negative-energy branch). There the group velocity of a hole points **parallel** to its wave vector, so the reflected hole exits at the same angle as the incident electron, on the same side of the normal — a mirror-like specular reflection.

The essential physics is that **the sign of the hole energy relative to the Dirac point controls the relative orientation of its group velocity and wave vector**. This single fact is the root of everything that follows.

## 3. The Dirac–Bogoliubov–de Gennes Equation

To incorporate superconductivity into the Dirac Hamiltonian, one couples electrons and holes through the pairing potential $\Delta$ and writes the four-component Dirac–Bogoliubov–de Gennes (DBdG) equation:

$$
\begin{pmatrix}
v\,\mathbf{p}\cdot\boldsymbol{\sigma} - U - E_F & \Delta \\
\Delta^* & U + E_F - v\,\mathbf{p}\cdot\boldsymbol{\sigma}
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

For electron states $(v = 0)$ the equation reads $(v\,\mathbf{p}\cdot\boldsymbol{\sigma} - E_F)u = \varepsilon u$. 

#### From Two Components to Four Components

In the normal region the DBdG equation decouples: the electron sector ($u$) and the hole sector ($v$) satisfy independent $2 \times 2$ Dirac equations. An electron state therefore has $v = 0$, and a hole state has $u = 0$. In principle one could work entirely with two-component spinors and simply remember which sector is active.

However, the boundary condition at the NS interface requires **continuity of the full four-component wave function** $(u, v)^T$. Matching at $x = 0$ mixes electrons and holes through the superconducting pair potential $\Delta$. It is therefore convenient to keep all four components explicit, padding the inactive sector with zeros. The electron eigen spinors written below are four-component objects with zeros in the lower two (hole) entries; the hole eigen spinors will have zeros in the upper two (electron) entries. This convention makes the boundary-condition matching in §7 transparent.

#### Plane-Wave Ansatz and Its Motivation

The NS interface is taken to lie in the $y$-$z$ plane at $x = 0$, so the Hamiltonian is **translationally invariant along $y$**. Momentum in the transverse direction is therefore conserved, and every eigenstate can be labelled by a definite wave number $q$. This justifies the factor $e^{iqy}$.

In the longitudinal direction $x$ the system is not uniform — the interface breaks translational symmetry — but away from $x = 0$ both the normal and superconducting regions are themselves homogeneous. In each bulk region the wave function must therefore be a superposition of plane waves $e^{ik_x x}$. The ansatz

$$
u(x,y) = e^{iqy} e^{ik_x x} \chi
$$

encodes precisely this structure: $e^{iqy}$ fixes the conserved transverse momentum, $e^{ik_x x}$ describes propagation toward or away from the interface, and the two-component spinor $\chi$ carries the sublattice (pseudospin) degree of freedom.

#### Deriving the Dispersion and the Two $k_x$ Solutions

Substituting the ansatz into $(v\,\mathbf{p}\cdot\boldsymbol{\sigma} - E_F)u = \varepsilon u$ gives

$$
\hbar v (k_x \sigma_x + q \sigma_y) \chi = (E_F + \varepsilon) \chi .
$$

Writing out the Pauli matrices explicitly,

$$
\hbar v \begin{pmatrix} 0 & k_x - iq \\ k_x + iq & 0 \end{pmatrix} \begin{pmatrix} \chi_1 \\ \chi_2 \end{pmatrix} = (E_F + \varepsilon) \begin{pmatrix} \chi_1 \\ \chi_2 \end{pmatrix} .
$$

This is a $2 \times 2$ eigenvalue problem. The characteristic equation is obtained by requiring the determinant to vanish:

$$
\det\!\begin{pmatrix} -(E_F+\varepsilon) & \hbar v(k_x - iq) \\ \hbar v(k_x + iq) & -(E_F+\varepsilon) \end{pmatrix} = 0,
$$

which yields

$$
(E_F + \varepsilon)^2 - \hbar^2 v^2 (k_x^2 + q^2) = 0 \quad \Longrightarrow \quad k_x^2 + q^2 = \frac{(E_F + \varepsilon)^2}{\hbar^2 v^2}.
$$

For fixed energy $\varepsilon$ and fixed transverse momentum $q$, this is a quadratic equation for $k_x$. It has **two roots**,

$$
k_x = \pm \sqrt{\frac{(E_F + \varepsilon)^2}{\hbar^2 v^2} - q^2} \equiv \pm k,
$$

corresponding to right-moving ($+k$) and left-moving ($-k$) waves. This is the physical origin of the incident and reflected waves: the same energy and transverse momentum support both propagation directions.

#### The Propagation Angle

It is convenient to package $q$ and $k$ into a single propagation angle $\alpha$ measured from the normal to the interface. Define

$$
\sin\alpha = \frac{\hbar v q}{E_F + \varepsilon}, \qquad k = \frac{E_F + \varepsilon}{\hbar v} \cos\alpha.
$$

**Why $\alpha$ is restricted to $(-\pi/2, \pi/2)$.**  In the definition $k = \frac{E_F+\varepsilon}{\hbar v}\cos\alpha$, the quantity $k$ is the magnitude of the longitudinal wave number.  The factor $e^{\pm ikx}$ (with the independent sign $\pm$) already distinguishes right- and left-moving waves, so $k$ itself must be real and positive.  This requires $\cos\alpha > 0$, i.e. $\alpha \in (-\pi/2, \pi/2)$.

#### Extracting the Spinor

Return to the explicit matrix equation:

$$
\hbar v \begin{pmatrix} 0 & k_x - iq \\ k_x + iq & 0 \end{pmatrix} \begin{pmatrix} \chi_1 \\ \chi_2 \end{pmatrix} = (E_F + \varepsilon) \begin{pmatrix} \chi_1 \\ \chi_2 \end{pmatrix} .
$$

The two rows give the same ratio.  From the first component,

$$
\frac{\chi_2}{\chi_1} = \frac{E_F + \varepsilon}{\hbar v\,(k_x - iq)} .
\tag{1}
$$

With the polar-angle parametrisation $k_x = \pm k\cos\alpha$ and $q = k\sin\alpha$ from the preceding section, where $k = (E_F + \varepsilon)/(\hbar v)$, Eq. (1) gives two branches.

For the **right-moving** root $k_x = +k$,

$$
k_x - iq = k(\cos\alpha - i\sin\alpha) = k\,e^{-i\alpha} = \frac{E_F + \varepsilon}{\hbar v}\,e^{-i\alpha} ,
$$

so that

$$
\boxed{\frac{\chi_2}{\chi_1} = e^{i\alpha}} .
$$

A convenient symmetric choice is $\chi_1 = e^{-i\alpha/2}$, $\chi_2 = e^{i\alpha/2}$, giving

$$
\chi_+ = \begin{pmatrix} e^{-i\alpha/2} \\ e^{i\alpha/2} \end{pmatrix}
\quad\text{(right-moving, $k_x = +k$)} .
$$

For the **left-moving** root $k_x = -k$,

$$
k_x - iq = k(-\cos\alpha - i\sin\alpha) = -k\,e^{i\alpha} = -\frac{E_F + \varepsilon}{\hbar v}\,e^{i\alpha} ,
$$

so that

$$
\boxed{\frac{\chi_2}{\chi_1} = -e^{-i\alpha}} .
$$

Choosing the symmetric form gives

$$
\chi_- = \begin{pmatrix} e^{i\alpha/2} \\ -e^{-i\alpha/2} \end{pmatrix}
\quad\text{(left-moving, $k_x = -k$)} .
$$

#### Probability-Current Normalization

Plane-wave states cannot be normalized to unit probability density ($\int|\psi|^2 d^3r = \infty$).  In a scattering problem the reflection and transmission probabilities are ratios of probability currents, so every participating state must carry the same current magnitude.

For the Dirac Hamiltonian the current operator is $v\sigma_x$, giving

$$
j_x = v\,\chi^\dagger\sigma_x\chi = v\bigl(\chi_1^*\chi_2 + \chi_2^*\chi_1\bigr) .
$$

The unnormalized spinors above have currents

$$
j_x(\chi_+) = 2v\cos\alpha, \qquad j_x(\chi_-) = -2v\cos\alpha .
$$

The factor $\cos\alpha$ makes the current angle-dependent.  Multiplying every spinor by $1/\sqrt{\cos\alpha}$ removes this dependence, giving a uniform current magnitude $|j_x| = 2v$ for all states.  Adopting natural units $v=1$, the normalized four-component electron spinors are

$$
\boxed{
\Psi_{e\pm} = \frac{e^{iqy \pm ikx}}{\sqrt{\cos\alpha}}
\begin{pmatrix} e^{\mp i\alpha/2} \\ \pm e^{\pm i\alpha/2} \\ 0 \\ 0 \end{pmatrix}
}
$$

with $\Psi_{e-}$ the incident wave and $\Psi_{e+}$ the reflected wave.

### Hole States

For hole states $(u = 0)$ the lower block of the DBdG equation gives

$$
(E_F - v\,\mathbf{p}\cdot\boldsymbol{\sigma})v = \varepsilon v \quad \Longrightarrow \quad v\,\mathbf{p}\cdot\boldsymbol{\sigma}\,v = (E_F - \varepsilon)v .
$$

Compared with the electron equation $v\,\mathbf{p}\cdot\boldsymbol{\sigma}\,u = (E_F + \varepsilon)u$, the only difference is the sign in front of $\varepsilon$: the hole propagates at energy $E_F - \varepsilon$ rather than $E_F + \varepsilon$. The same substitution procedure yields the dispersion relation

$$
k_x^2 + q^2 = \frac{(E_F - \varepsilon)^2}{\hbar^2 v^2},
$$

and, introducing the hole propagation angle $\alpha'$ through

$$
\sin\alpha' = \frac{\hbar v q}{\varepsilon - E_F}, \qquad k' = \frac{\varepsilon - E_F}{\hbar v} \cos\alpha',
$$

with $\alpha' \in (-\pi/2, \pi/2)$ as before.  The crucial point is that the denominator $\varepsilon - E_F$ is an **algebraic quantity**.  When $\varepsilon < E_F$ (retro-reflection regime) the denominator is negative, so $\alpha'$ carries the opposite sign from $\alpha$ for the same transverse momentum $q$; when $\varepsilon > E_F$ (specular regime) the denominator is positive and $\alpha'$ has the same sign as $\alpha$.  The longitudinal wave number $k' = (\varepsilon-E_F)\cos\alpha'/\hbar v$ inherits the same sign as $\varepsilon-E_F$, so $k'$ is negative in the retro regime and positive in the specular regime.

the eigen spinors are

$$
\Psi_{h\pm} = e^{iqy \pm ik'x} \frac{1}{\sqrt{\cos\alpha'}} \begin{pmatrix} 0 \\ 0 \\ e^{\mp i\alpha'/2} \\ \mp e^{\pm i\alpha'/2} \end{pmatrix}.
$$

The critical observation is the sign of $(E_F - \varepsilon)$. When $\varepsilon < E_F$, the hole energy $E_F - \varepsilon$ lies **above** the Dirac point; the hole state therefore sits on the **conduction-band side** of the spectrum, where its group velocity points opposite to its wave vector (retro-reflection). When $\varepsilon > E_F$, the hole energy lies **below** the Dirac point; the state sits on the **valence-band side**, where the group velocity points parallel to the wave vector (specular reflection). The relative orientation of group velocity and wave vector is opposite in the two cases, and this single fact controls the reflection geometry.

## 5. The Critical Angle

The angle $\alpha'$ is real only when $|\sin\alpha'| \leq 1$, which defines a **critical angle**

$$
\alpha_c = \arcsin\!\left(\frac{|E_F - \varepsilon|}{E_F + \varepsilon}\right).
$$

For $|\alpha| < \alpha_c$, Andreev reflection is kinematically allowed and four scattering states coexist in the normal region: $\Psi_{e-}$ (incident electron), $\Psi_{e+}$ (normal reflection), $\Psi_{h-}$ (incident hole), and $\Psi_{h+}$ (Andreev-reflected hole). For $|\alpha| > \alpha_c$, the hole cannot propagate and Andreev reflection is suppressed; only normal reflection survives.

## 6. Superconducting Region and the Heavily Doped Limit

In the superconducting region $(x < 0)$ the potential is $U = -U_0$ and the pairing potential is $\Delta = \Delta_0 e^{i\phi}$. The DBdG equation reads

$$
\begin{pmatrix}
\hbar v\mathbf{k}\cdot\boldsymbol{\sigma} - U_0 - E_F & \Delta_0 e^{i\phi} \\
\Delta_0 e^{-i\phi} & U_0 + E_F - \hbar v\mathbf{k}\cdot\boldsymbol{\sigma}
\end{pmatrix}
\begin{pmatrix} u \\ v \end{pmatrix}
= \varepsilon \begin{pmatrix} u \\ v \end{pmatrix}.
$$

It is convenient to define the superconducting Fermi energy $E_{S0} = U_0 + E_F$ and the normal-state kinetic energy measured from that Fermi level,

$$
\xi_k = \hbar v |k| - E_{S0}.
$$

### Deriving the Superconducting Dispersion

Write the superconducting DBdG Hamiltonian in compact block form.  With $h = \hbar v\,\mathbf{k}\cdot\boldsymbol{\sigma}$ and $E_{S0} = U_0 + E_F$,

$$
\mathcal{H} =
\begin{pmatrix}
h - E_{S0} & \Delta_0 e^{i\phi} \,\mathbb{1}_2 \\
\Delta_0 e^{-i\phi} \,\mathbb{1}_2 & E_{S0} - h
\end{pmatrix}
\equiv
\begin{pmatrix}
h - E_{S0} & \Delta \\
\Delta^\dagger & E_{S0} - h
\end{pmatrix},
$$

where $\Delta = \Delta_0 e^{i\phi}\mathbb{1}_2$ is proportional to the identity in sublattice space because the proximity-induced s-wave pairing does not mix A and B sites.

#### Step 1: Square the matrix

$$
\mathcal{H}^2 =
\begin{pmatrix}
(h-E_{S0})^2 + |\Delta|^2 & [h,\Delta] \\
[\Delta^\dagger, h] & (E_{S0}-h)^2 + |\Delta|^2
\end{pmatrix}.
$$

Because $\Delta$ is a scalar multiple of the identity, it commutes with everything: $[h,\Delta] = 0$.  The off-diagonal blocks vanish.

#### Step 2: Diagonalize $h$ in sublattice space

The kinetic block is $h = \hbar v\,\mathbf{k}\cdot\boldsymbol{\sigma} = \hbar v|k|\,\hat{\mathbf{n}}\cdot\boldsymbol{\sigma}$ with $\hat{\mathbf{n}} = \mathbf{k}/|k|$.  Using the Pauli anticommutator $\{\sigma_i,\sigma_j\} = 2\delta_{ij}$,

$$
h^2 = (\hbar v|k|)^2 (\hat{\mathbf{n}}\cdot\boldsymbol{\sigma})^2 = (\hbar v|k|)^2 \,\mathbb{1}_2 .
$$

Thus $h$ has eigenvalues $\pm \hbar v|k|$.  The corresponding eigen spinors are the **chiral states** $\chi_{\pm}$ satisfying $(\hat{\mathbf{n}}\cdot\boldsymbol{\sigma})\chi_{\pm} = \pm\chi_{\pm}$.  In this chiral basis $h$ is diagonal:

$$
h \;\to\; \mathrm{diag}\bigl(+\hbar v|k|,\; -\hbar v|k|\bigr).
$$

#### Step 3: Evaluate the diagonal blocks in the chiral basis

With $h$ diagonal, each $2\times 2$ block of $\mathcal{H}^2$ becomes diagonal too.  The upper-left block is

$$
(h-E_{S0})^2 + \Delta_0^2
\;\to\;
\mathrm{diag}\Bigl[(\hbar v|k|-E_{S0})^2 + \Delta_0^2,\; (-\hbar v|k|-E_{S0})^2 + \Delta_0^2\Bigr].
$$

The lower-right block gives the same two eigenvalues.  The four eigenvalues of $\mathcal{H}^2$ are therefore

$$
\varepsilon^2 = (\pm\hbar v|k| - E_{S0})^2 + \Delta_0^2,
\qquad \text{(each doubly degenerate)}.
$$

#### Step 4: Heavy-doping (Andreev) limit

In the heavily doped superconductor $E_{S0} \gg \hbar v|k|, \Delta_0, \varepsilon$.  Two of the four roots correspond to energies far from the Fermi level:

$$
\varepsilon \approx \pm(E_{S0} + \hbar v|k|) \quad \text{(high-energy, frozen modes)}.
$$

The remaining two roots live near the Fermi surface.  Defining the normal-state kinetic energy

$$
\xi_k = \hbar v|k| - E_{S0},
$$

these low-energy modes satisfy

$$
\boxed{\varepsilon^2 = \xi_k^2 + \Delta_0^2 = (\hbar v|k| - E_{S0})^2 + \Delta_0^2}.
$$

This is the familiar BCS gapped spectrum, with the crucial difference that $\xi_k$ is linear in $|k|$ rather than quadratic.  The heavy-doping limit has projected the four-component Dirac–Bogoliubov problem onto the single pair of Nambu states that couple to the subgap excitations in the normal region.

This is the familiar gapped spectrum of a BCS superconductor, except that the normal-state dispersion $\xi_k$ is linear in $|k|$ rather than quadratic.

### Subgap States and Exponential Decay

For excitation energies below the gap, $|\varepsilon| < \Delta_0$, the dispersion relation gives

$$
(\hbar v|k| - E_{S0})^2 = \varepsilon^2 - \Delta_0^2 < 0.
$$

The right-hand side is negative, so $\hbar v|k| - E_{S0}$ must be purely imaginary. Writing

$$
\hbar v|k| - E_{S0} = \pm i\sqrt{\Delta_0^2 - \varepsilon^2},
$$

the wave number acquires an imaginary part

$$
\text{Im}(|k|) = \frac{\sqrt{\Delta_0^2 - \varepsilon^2}}{\hbar v} \equiv \kappa.
$$

The wave function therefore decays exponentially into the superconductor as $e^{-\kappa|x|}$. There are no propagating single-particle modes in the subgap regime; all incident probability current from the normal side must be reflected.

### The Heavily Doped Limit

When the superconducting electrode is heavily doped, $U_0 \gg E_F, \varepsilon, \Delta_0$, the superconducting Fermi energy $E_{S0}$ is very large. The decay constant can be written in a compact form by parameterizing the energy as $\varepsilon = \Delta_0 \cos\beta$ with $\beta \in (0, \pi)$. Then

$$
\kappa = \frac{\sqrt{\Delta_0^2 - \varepsilon^2}}{\hbar v} = \frac{\Delta_0 \sin\beta}{\hbar v}.
$$

This expression enters the boundary-condition matching through the ratios of decaying exponentials at $x = 0$.

## 7. Boundary Matching

### Superconducting States in the Heavily Doped Limit

In the superconducting region ($x < 0$) the subgap solutions decay exponentially as $x \to -\infty$.  In the heavily doped limit $U_0 \gg E_F, \varepsilon, \Delta_0$ there are exactly two such decaying modes, distinguished by the sign of the large real part of the longitudinal wave number ($\pm k_0$ with $k_0 \approx E_{S0}/\hbar v$).  Their four-component spinors at $x = 0$ are

$$
\Psi_{S+}(0) = \begin{pmatrix} e^{-i\beta} \\ e^{-i\beta} \\ e^{-i\phi} \\ e^{-i\phi} \end{pmatrix},
\qquad
\Psi_{S-}(0) = \begin{pmatrix} e^{i\beta} \\ -e^{i\beta} \\ e^{-i\phi} \\ -e^{-i\phi} \end{pmatrix}.
$$

The derivation proceeds from the DBdG equation in the superconductor by noting that the kinetic term $\hbar v k_x \sigma_x$ dominates and must be balanced against the large potential $E_{S0}$.  For the $+k_0$ branch the electron and hole spinors both lie in the $\sigma_x = +1$ eigenspace $(1,1)^T$; for the $-k_0$ branch they lie in the $\sigma_x = -1$ eigenspace $(1,-1)^T$.  Solving the remaining $2 \times 2$ electron-hole block to first order in $\Delta_0/E_{S0}$ yields the ratios $v/u = e^{-i(\phi-\beta)}$ for $\Psi_{S+}$ and $v/u = e^{-i(\phi+\beta)}$ for $\Psi_{S-}$.  The common phase $e^{-i\beta}$ in the upper two components of $\Psi_{S+}$ (and $e^{i\beta}$ in $\Psi_{S-}$) is a convenient choice of overall gauge.

### The Scattering State in the Normal Region

An electron is incident from the normal side ($x > 0$) toward the interface.  The scattering state is a superposition of the incident electron, a normally reflected electron, and an Andreev-reflected hole:

$$
\Psi_N(x,y) = \Psi_{e-}(x,y) + r\,\Psi_{e+}(x,y) + r_A\,\Psi_{h+}(x,y).
$$

The amplitudes $r$ (normal reflection) and $r_A$ (Andreev reflection) are the quantities we seek.  Evaluated at the interface ($x = 0$), the three normal-region spinors are

$$
\Psi_{e-}(0) = \frac{1}{\sqrt{\cos\alpha}}
\begin{pmatrix} e^{i\alpha/2} \\ -e^{-i\alpha/2} \\ 0 \\ 0 \end{pmatrix},
\quad
\Psi_{e+}(0) = \frac{1}{\sqrt{\cos\alpha}}
\begin{pmatrix} e^{-i\alpha/2} \\ e^{i\alpha/2} \\ 0 \\ 0 \end{pmatrix},
\quad
\Psi_{h+}(0) = \frac{1}{\sqrt{\cos\alpha'}}
\begin{pmatrix} 0 \\ 0 \\ e^{-i\alpha'/2} \\ -e^{i\alpha'/2} \end{pmatrix}.
$$

### Continuity at the Interface

Demanding continuity of the full four-component wave function at $x = 0$ gives

$$
\Psi_{e-}(0) + r\,\Psi_{e+}(0) + r_A\,\Psi_{h+}(0) = a\,\Psi_{S+}(0) + b\,\Psi_{S-}(0).
$$

Writing this out component by component:

**Component 1** (A sublattice, electron):
$$
\frac{e^{i\alpha/2} + r\,e^{-i\alpha/2}}{\sqrt{\cos\alpha}} = a\,e^{-i\beta} + b\,e^{i\beta}. \tag{1}
$$

**Component 2** (B sublattice, electron):
$$
\frac{-e^{-i\alpha/2} + r\,e^{i\alpha/2}}{\sqrt{\cos\alpha}} = a\,e^{-i\beta} - b\,e^{i\beta}. \tag{2}
$$

**Component 3** (A sublattice, hole):
$$
r_A\,\frac{e^{-i\alpha'/2}}{\sqrt{\cos\alpha'}} = (a+b)\,e^{-i\phi}. \tag{3}
$$

**Component 4** (B sublattice, hole):
$$
-r_A\,\frac{e^{i\alpha'/2}}{\sqrt{\cos\alpha'}} = (a-b)\,e^{-i\phi}. \tag{4}
$$

### Solving for the Superconducting Amplitudes

Equations (3) and (4) involve only the hole sector and can be solved immediately.  Adding and subtracting them gives

$$
a = -\,\frac{i\,r_A\,e^{i\phi}\sin(\alpha'/2)}{\sqrt{\cos\alpha'}},
\qquad
b = \frac{r_A\,e^{i\phi}\cos(\alpha'/2)}{\sqrt{\cos\alpha'}}.
$$

### Solving for the Reflection Amplitudes

Insert these expressions for $a$ and $b$ into equations (1) and (2).  Adding (1) and (2) eliminates $b$:

$$
\frac{i\sin(\alpha/2) + r\cos(\alpha/2)}{\sqrt{\cos\alpha}}
= -\,\frac{i\,r_A\,e^{i\phi}\sin(\alpha'/2)\,e^{-i\beta}}{\sqrt{\cos\alpha'}}. \tag{5}
$$

Subtracting (2) from (1) eliminates $a$:

$$
\frac{\cos(\alpha/2) - i r\sin(\alpha/2)}{\sqrt{\cos\alpha}}
= \frac{r_A\,e^{i\phi}\cos(\alpha'/2)\,e^{i\beta}}{\sqrt{\cos\alpha'}}. \tag{6}
$$

Equations (5) and (6) are two linear equations for the two unknowns $r$ and $r_A$.  It is convenient to eliminate $r_A$ first.  Multiply (5) by $\cos(\alpha'/2)\,e^{i\beta}$ and (6) by $i\sin(\alpha'/2)\,e^{-i\beta}$, then add the results.  After simplifying the trigonometric products with the identities

$$
\sin\frac{\alpha'}{2}\cos\frac{\alpha}{2} = \tfrac{1}{2}\Bigl[\sin\tfrac{\alpha'+\alpha}{2} + \sin\tfrac{\alpha'-\alpha}{2}\Bigr],
\quad
\cos\frac{\alpha'}{2}\sin\frac{\alpha}{2} = \tfrac{1}{2}\Bigl[\sin\tfrac{\alpha'+\alpha}{2} - \sin\tfrac{\alpha'-\alpha}{2}\Bigr],
$$

and similarly for the cosine products, one finds that the left-hand side combines into a single denominator

$$
X = \cos\beta\,\cos\frac{\alpha'-\alpha}{2} + i\sin\beta\,\cos\frac{\alpha'+\alpha}{2},
$$

while the right-hand side yields the Andreev amplitude

$$
r_A = e^{-i\phi}\,X^{-1}\sqrt{\cos\alpha\cos\alpha'} \qquad (|\alpha| < \alpha_c).
$$

Once $r_A$ is known, $r$ follows by substituting back into either (5) or (6).  The result is

$$
r = X^{-1}\Bigl[-\cos\beta\,\sin\tfrac{\alpha'+\alpha}{2} + i\sin\beta\,\sin\tfrac{\alpha'-\alpha}{2}\Bigr].
$$

### Unitarity

For subgap energies $|\varepsilon| < \Delta_0$ the parameter $\beta = \arccos(\varepsilon/\Delta_0)$ is real, and one may verify directly that

$$
|r|^2 + |r_A|^2 = \frac{\cos^2\beta\,\sin^2\frac{\alpha'+\alpha}{2} + \sin^2\beta\,\sin^2\frac{\alpha'-\alpha}{2} + \cos\alpha\cos\alpha'}{|X|^2} = 1.
$$

The equality follows from the trigonometric identity

$$
|X|^2 = \tfrac{1}{2}\bigl[1 + \cos\alpha\cos\alpha' + \sin\alpha\sin\alpha'\cos(2\beta)\bigr],
$$

combined with the half-angle formulas for the sine squares in the numerator.  Since no propagating modes exist in the superconductor below the gap, all probability current must be reflected; the reflection matrix is therefore unitary, with $|r|^2$ the probability for normal reflection and $|r_A|^2$ the probability for Andreev reflection.

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
