# From Mott Scattering to the Rosenbluth Formula: Electron-Proton Elastic Scattering

---

## 1. Introduction: Why Protons Are Not Point Charges

The scattering of electrons by atomic nuclei was Rutherford's original tool for discovering the compact, positively charged core of the atom. In the non-relativistic limit, the differential cross section for a pointlike target is the famous Rutherford formula:

$$
\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{4E^2\sin^4(\theta/2)}
$$

where $E$ is the incident electron energy and $\theta$ the scattering angle. When the electron's kinetic energy becomes comparable to its rest mass, the formula generalizes to the Mott cross section, which incorporates relativistic spin effects via the replacement $\sin^4(\theta/2) \to \sin^4(\theta/2) \cdot (1 - v^2\sin^2(\theta/2))$.

But the proton is not a point charge. Deep inelastic scattering experiments revealed that the proton possesses internal structure—quarks and gluons bound by the strong interaction. Even in elastic scattering, where the proton remains intact, its finite size and magnetic moment modify the cross section in a manner that cannot be captured by a single coupling constant. The electromagnetic vertex of the proton must be described by *form factors*—functions of the momentum transfer that encode the spatial distribution of charge and magnetization within the proton.

The goal of this note is to derive the Rosenbluth formula, which expresses the electron-proton elastic scattering cross section in terms of two Sachs form factors, $G_E(Q^2)$ and $G_M(Q^2)$. These form factors are among the most precisely measured quantities in hadron physics and provide direct access to the proton's charge and magnetic radii.

---

## 2. Kinematics

Consider the elastic scattering process $e^-(k) + p(p) \to e^-(k') + p(p')$. The four-momenta satisfy:

$$
k + p = k' + p', \quad q \equiv k - k' = p' - p
$$

The Mandelstam variable $t = q^2$ is negative for physical scattering. It is conventional to work with the positive quantity $Q^2 \equiv -q^2 > 0$.

### On-Shell Conditions

For elastic scattering, all external particles are on their mass shells:

$$
k^2 = k'^2 = m_e^2, \quad p^2 = p'^2 = m_p^2
$$

From $p' = p + q$, squaring gives:

$$
m_p^2 = m_p^2 + 2p\cdot q + q^2 \quad \Longrightarrow \quad p\cdot q = -\frac{q^2}{2} = \frac{Q^2}{2}
$$

Similarly, from $k' = k - q$:

$$
m_e^2 = m_e^2 - 2k\cdot q + q^2 \quad \Longrightarrow \quad k\cdot q = \frac{q^2}{2} = -\frac{Q^2}{2}
$$

### Laboratory Frame

In the laboratory frame, the proton is initially at rest: $p = (m_p, \vec{0})$. The incident and scattered electron momenta are:

$$
k = (E, 0, 0, E), \quad k' = (E', E'\sin\theta, 0, E'\cos\theta)
$$

where we have taken the high-energy limit $E \gg m_e$ so that the electron is effectively massless. Energy-momentum conservation yields the relation between $E'$ and $E$:

$$
q^2 = (k - k')^2 = -2k\cdot k' = -2EE'(1 - \cos\theta) = -4EE'\sin^2\frac{\theta}{2}
$$

and from $p\cdot q = Q^2/2$:

$$
m_p(E - E') = \frac{Q^2}{2} = 2EE'\sin^2\frac{\theta}{2}
$$

Solving for $E'$:

$$
E' = \frac{E}{1 + \dfrac{2E}{m_p}\sin^2\dfrac{\theta}{2}}
$$

This relation is exact in the limit $m_e \to 0$ and will be essential for reducing the cross section to the Rosenbluth form.

---

## 3. The Electromagnetic Vertex and Form Factors

### The Most General Lorentz-Covariant Vertex

For a pointlike Dirac particle of charge $e$, the electromagnetic vertex is simply $-ie\gamma^\mu$. For the proton, which is a composite object, the vertex must respect Lorentz covariance, gauge invariance, and hermiticity. The most general form consistent with these constraints is:

$$
\Gamma^\mu = \gamma^\mu F_1(q^2) + \frac{i\sigma^{\mu\nu}q_\nu}{2m_p}F_2(q^2)
$$

where $F_1(q^2)$ and $F_2(q^2)$ are the **Dirac** and **Pauli form factors**, respectively. At zero momentum transfer:

- $F_1(0) = 1$ ensures that the proton carries one unit of electric charge.
- $F_2(0) = \kappa_p \approx 1.79$ is the anomalous magnetic moment in units of the nuclear magneton.

The tensor $\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu, \gamma^\nu]$ couples the photon to the proton's magnetic dipole moment. The factors $F_1$ and $F_2$ are functions of $q^2$ because the photon resolves the internal structure of the proton; at higher $Q^2$, the photon wavelength becomes shorter and probes smaller distance scales within the proton.

### Sachs Form Factors

It is often more intuitive to work with linear combinations of $F_1$ and $F_2$ known as the **Sachs form factors**:

$$
G_E(Q^2) = F_1(q^2) - \tau F_2(q^2), \quad G_M(Q^2) = F_1(q^2) + F_2(q^2)
$$

where $\tau \equiv Q^2/(4m_p^2) = -q^2/(4m_p^2)$. The electric form factor $G_E$ reduces to the Fourier transform of the proton's charge density in the non-relativistic limit, while $G_M$ encodes the magnetic moment distribution. The Rosenbluth formula takes its simplest form when expressed in terms of $G_E$ and $G_M$.

### Gordon Decomposition

A useful identity, valid for on-shell spinors, is the Gordon decomposition:

$$
\bar{u}(p')\gamma^\mu u(p) = \bar{u}(p')\left[\frac{p^\mu + p'^\mu}{2m_p} + \frac{i\sigma^{\mu\nu}(p' - p)_\nu}{2m_p}\right]u(p)
$$

This shows that the Dirac current can be split into a convection part (proportional to the average momentum) and a spin part (proportional to the magnetic moment). While this decomposition is invaluable for physical interpretation, we will use the original form of $\Gamma^\mu$ for the trace calculations below, as it leads directly to the Sachs form factors.

---

## 4. The Scattering Amplitude

To lowest order in the electromagnetic coupling, the scattering process proceeds through the exchange of a single virtual photon. The invariant matrix element is:

$$
\mathcal{M} = (-ie)^2 \bar{u}(k')\gamma^\mu u(k) \frac{-ig_{\mu\nu}}{q^2} \bar{u}(p')\Gamma^\nu u(p)
$$

or more compactly:

$$
\mathcal{M} = \frac{e^2}{q^2} j_e^\mu \cdot j_{p,\mu}
$$

with the electron current $j_e^\mu = \bar{u}(k')\gamma^\mu u(k)$ and the proton current $j_p^\mu = \bar{u}(p')\Gamma^\mu u(p)$. The factor $1/q^2$ is the photon propagator; the spacelike momentum transfer $q^2 = -Q^2 < 0$ ensures that the interaction is mediated by a virtual photon.

The cross section requires $|\mathcal{M}|^2$, averaged over initial spins and summed over final spins. For unpolarized scattering:

$$
\overline{|\mathcal{M}|^2} = \frac{e^4}{q^4} L^{\mu\nu} W_{\mu\nu}
$$

where the leptonic and hadronic tensors are defined by:

$$
L^{\mu\nu} = \frac{1}{2}\sum_{\text{e-spins}} \bar{u}(k')\gamma^\mu u(k) \bar{u}(k)\gamma^\nu u(k') = \frac{1}{2}\operatorname{Tr}\left[(\slashed{k}' + m_e)\gamma^\mu(\slashed{k} + m_e)\gamma^\nu\right]
$$

$$
W_{\mu\nu} = \frac{1}{2}\sum_{\text{p-spins}} \bar{u}(p')\Gamma_\mu u(p) \bar{u}(p)\Gamma_\nu u(p') = \frac{1}{2}\operatorname{Tr}\left[(\slashed{p}' + m_p)\Gamma_\mu(\slashed{p} + m_p)\Gamma_\nu\right]
$$

The remainder of this note is devoted to the evaluation of these two tensors and their contraction.

---

## 5. The Leptonic Tensor

The leptonic tensor is evaluated using standard trace technology. Expanding the product:

$$
L^{\mu\nu} = \frac{1}{2}\operatorname{Tr}\left[\slashed{k}'\gamma^\mu\slashed{k}\gamma^\nu + m_e\slashed{k}'\gamma^\mu\gamma^\nu + m_e\gamma^\mu\slashed{k}\gamma^\nu + m_e^2\gamma^\mu\gamma^\nu\right]
$$

The traces of products with an odd number of gamma matrices vanish in four dimensions. Thus:

$$
\operatorname{Tr}[\slashed{k}'\gamma^\mu\gamma^\nu] = k'_\alpha \operatorname{Tr}[\gamma^\alpha\gamma^\mu\gamma^\nu] = 0, \quad \operatorname{Tr}[\gamma^\mu\slashed{k}\gamma^\nu] = 0
$$

For the trace of four gamma matrices, we use the identity:

$$
\operatorname{Tr}[\gamma^\alpha\gamma^\beta\gamma^\mu\gamma^\nu] = 4\left(g^{\alpha\beta}g^{\mu\nu} - g^{\alpha\mu}g^{\beta\nu} + g^{\alpha\nu}g^{\beta\mu}\right)
$$

Applying this to the first term:

$$
\frac{1}{2}\operatorname{Tr}[\slashed{k}'\gamma^\mu\slashed{k}\gamma^\nu] = \frac{1}{2} \cdot 4\left(k'^\mu k^\nu - g^{\mu\nu}k\cdot k' + k'^\nu k^\mu\right) = 2\left(k'^\mu k^\nu + k'^\nu k^\mu - g^{\mu\nu}k\cdot k'\right)
$$

For the mass term:

$$
\frac{m_e^2}{2}\operatorname{Tr}[\gamma^\mu\gamma^\nu] = \frac{m_e^2}{2} \cdot 4g^{\mu\nu} = 2m_e^2 g^{\mu\nu}
$$

Collecting all contributions:

$$
L^{\mu\nu} = 2\left(k'^\mu k^\nu + k'^\nu k^\mu - g^{\mu\nu}k\cdot k' + m_e^2 g^{\mu\nu}\right)
$$

In the high-energy limit $E \gg m_e$, the electron mass can be neglected, and the leptonic tensor simplifies to:

$$
L^{\mu\nu} \approx 2\left(k'^\mu k^\nu + k'^\nu k^\mu - g^{\mu\nu}k\cdot k'\right)
$$

This is the standard result for massless electrons and will be used in the contraction below.

---

## 6. The Hadronic Tensor

The hadronic tensor is the heart of the calculation. Its structure is constrained by two fundamental requirements: **Lorentz covariance** and **electromagnetic current conservation**. The latter, expressed as $q^\mu W_{\mu\nu} = q^\nu W_{\mu\nu} = 0$, follows from gauge invariance and holds for any target, elastic or inelastic.

### Parameterization by Symmetry

The most general symmetric rank-2 tensor that can be constructed from $p_\mu$ and $q_\mu$ and satisfies current conservation is:

$$
W_{\mu\nu} = W_1\left(-g_{\mu\nu} + \frac{q_\mu q_\nu}{q^2}\right) + \frac{W_2}{m_p^2}\left(p_\mu - \frac{p\cdot q}{q^2}q_\mu\right)\left(p_\nu - \frac{p\cdot q}{q^2}q_\nu\right)
$$

where $W_1$ and $W_2$ are scalar functions of $q^2$ (or equivalently $Q^2$). For elastic scattering, the on-shell condition $p' = p + q$ implies $2p\cdot q + q^2 = 0$, so $p\cdot q = -q^2/2 = Q^2/2$. The parameterization simplifies to:

$$
W_{\mu\nu} = W_1\left(-g_{\mu\nu} + \frac{q_\mu q_\nu}{q^2}\right) + \frac{W_2}{4m_p^2}(2p_\mu + q_\mu)(2p_\nu + q_\nu)
$$

The task is now to determine $W_1$ and $W_2$ from the explicit trace formula.

### Direct Trace Evaluation

Inserting $\Gamma_\mu = \gamma_\mu F_1 + \frac{i\sigma_{\mu\rho}q^\rho}{2m_p}F_2$ into the trace definition, we expand $W_{\mu\nu}$ into three structures:

$$
W_{\mu\nu} = F_1^2 \cdot T^{(1)}_{\mu\nu} + F_1F_2 \cdot T^{(12)}_{\mu\nu} + F_2^2 \cdot T^{(2)}_{\mu\nu}
$$

**The $F_1^2$ term** is identical to the Dirac point-particle case:

$$
T^{(1)}_{\mu\nu} = \frac{1}{2}\operatorname{Tr}\left[(\slashed{p}' + m_p)\gamma_\mu(\slashed{p} + m_p)\gamma_\nu\right]
$$

Evaluating the trace as in the leptonic case:

$$
\frac{1}{2}\operatorname{Tr}[\slashed{p}'\gamma_\mu\slashed{p}\gamma_\nu] = 2\left(p'_\mu p_\nu + p'_\nu p_\mu - g_{\mu\nu}p\cdot p'\right)
$$

$$
\frac{m_p^2}{2}\operatorname{Tr}[\gamma_\mu\gamma_\nu] = 2m_p^2 g_{\mu\nu}
$$

The odd terms vanish, giving:

$$
T^{(1)}_{\mu\nu} = 2\left(p'_\mu p_\nu + p'_\nu p_\mu + g_{\mu\nu}(m_p^2 - p\cdot p')\right)
$$

Using $p' = p + q$ and $p\cdot p' = m_p^2 + p\cdot q = m_p^2 - q^2/2$:

$$
T^{(1)}_{\mu\nu} = 2\left(2p_\mu p_\nu + p_\mu q_\nu + p_\nu q_\mu + g_{\mu\nu}\frac{q^2}{2}\right)
$$

**The $F_1F_2$ cross term** involves a single $\sigma$ matrix. Using $\sigma_{\nu\rho} = \frac{i}{2}[\gamma_\nu, \gamma_\rho]$:

$$
T^{(12)}_{\mu\nu} = \frac{1}{2}\operatorname{Tr}\left[(\slashed{p}' + m_p)\gamma_\mu(\slashed{p} + m_p)\frac{i\sigma_{\nu\rho}q^\rho}{2m_p}\right] + (\mu \leftrightarrow \nu)
$$

The factor of $i\sigma_{\nu\rho}q^\rho/(2m_p)$ can be rewritten as $-[\gamma_\nu, \slashed{q}]/(4m_p)$. Expanding the commutator and evaluating the trace with the standard identities yields:

$$
T^{(12)}_{\mu\nu} = -\frac{1}{m_p}\left(p_\mu q_\nu + p_\nu q_\mu + q^2 g_{\mu\nu}\right)
$$

**The $F_2^2$ term** involves two $\sigma$ matrices. The product $\sigma_{\mu\rho}\sigma_{\nu\sigma}$ can be reduced using:

$$
\sigma_{\mu\rho}\sigma_{\nu\sigma} = -\frac{1}{4}\left[\gamma_\mu, \gamma_\rho\right]\left[\gamma_\nu, \gamma_\sigma\right]
$$

Taking the trace and contracting with $q^\rho q^\sigma$ gives:

$$
T^{(2)}_{\mu\nu} = \frac{1}{2m_p^2}\left(q_\mu q_\nu - q^2 g_{\mu\nu}\right)(p\cdot q + m_p^2) = \frac{1}{2m_p^2}\left(q_\mu q_\nu - q^2 g_{\mu\nu}\right)\left(m_p^2 - \frac{q^2}{2}\right)
$$

### Assembling the Full Hadronic Tensor

Combining the three contributions with their respective coefficients:

$$
W_{\mu\nu} = 2F_1^2\left(2p_\mu p_\nu + p_\mu q_\nu + p_\nu q_\mu + g_{\mu\nu}\frac{q^2}{2}\right) - \frac{F_1F_2}{m_p}\left(p_\mu q_\nu + p_\nu q_\mu + q^2 g_{\mu\nu}\right) + \frac{F_2^2}{2m_p^2}\left(q_\mu q_\nu - q^2 g_{\mu\nu}\right)\left(m_p^2 - \frac{q^2}{2}\right)
$$

This expression must match the general parameterization. To determine $W_1$ and $W_2$, we compare the coefficients of the independent tensor structures $g_{\mu\nu}$, $p_\mu p_\nu$, $p_\mu q_\nu + p_\nu q_\mu$, and $q_\mu q_\nu$ on both sides. After straightforward but lengthy algebra, one finds:

$$
W_1 = -\frac{q^2}{4m_p^2}(F_1 + F_2)^2 = \tau G_M^2
$$

$$
W_2 = \frac{(F_1 - \tau F_2)^2 + \tau(F_1 + F_2)^2}{1 + \tau} = \frac{G_E^2 + \tau G_M^2}{1 + \tau}
$$

where $\tau = -q^2/(4m_p^2) = Q^2/(4m_p^2)$.

A direct verification is provided by the limit $F_2 = 0$, $F_1 = 1$, which describes a pointlike Dirac proton. In this limit $G_E = G_M = 1$, and the hadronic tensor reduces to:

$$
W_{\mu\nu}^{(F_2=0)} = 2\left(2p_\mu p_\nu + p_\mu q_\nu + p_\nu q_\mu + g_{\mu\nu}\frac{q^2}{2}\right)
$$

Substituting $W_1 = \tau$ and $W_2 = 1$ into the parameterization gives exactly the same expression, confirming the consistency of the result.

---

## 7. Tensor Contraction

With $L^{\mu\nu}$ and $W_{\mu\nu}$ in hand, we evaluate the contraction $L^{\mu\nu}W_{\mu\nu}$. It is convenient to work in the massless electron limit and expand the contraction in terms of the parameterization coefficients $W_1$ and $W_2$.

### Contraction with the Parameterized Form

Inserting $L^{\mu\nu} = 2(k'^\mu k^\nu + k'^\nu k^\mu - g^{\mu\nu}k\cdot k')$ and the parameterized $W_{\mu\nu}$, we exploit a key simplification: for massless electrons, the leptonic tensor is transverse to the photon momentum $q$:

$$
q_\mu L^{\mu\nu} = q_\nu L^{\mu\nu} = 0
$$

This is the statement of electromagnetic current conservation (Ward identity) for the electron vertex. The proof is immediate:

$$
q_\mu L^{\mu\nu} = 2\left[(q\cdot k')k^\nu + (q\cdot k)k'^\nu - q^\nu(k\cdot k')\right]
$$

For massless electrons on shell, $q\cdot k' = (k-k')\cdot k' = k\cdot k'$ and $q\cdot k = (k-k')\cdot k = -k\cdot k'$ (using $k^2 = k'^2 = 0$). Thus:

$$
q_\mu L^{\mu\nu} = 2\left[(k\cdot k')k^\nu + (-k\cdot k')k'^\nu - q^\nu(k\cdot k')\right] = 2(k\cdot k')(k - k' - q)^\nu = 0
$$

since $q = k - k'$. Therefore, any term in $W_{\mu\nu}$ proportional to $q_\mu$ or $q_\nu$ gives zero upon contraction with $L^{\mu\nu}$.

**Contribution from $W_1$:**

$$
L^{\mu\nu} \cdot W_1\left(-g_{\mu\nu} + \frac{q_\mu q_\nu}{q^2}\right) = -W_1 L^\mu_\mu + \frac{W_1}{q^2} L^{\mu\nu}q_\mu q_\nu = -W_1 L^\mu_\mu
$$

Computing the trace $L^\mu_\mu = g_{\mu\nu}L^{\mu\nu}$:

$$
L^\mu_\mu = 2\left(k'\cdot k + k\cdot k' - 4k\cdot k'\right) = -4k\cdot k'
$$

Thus the $W_1$ contribution is:

$$
L^{\mu\nu}W_{\mu\nu}^{(1)} = 4W_1 k\cdot k'
$$

**Contribution from $W_2$:**

The $W_2$ term contains $(2p_\mu + q_\mu)(2p_\nu + q_\nu)$. Since $q_\mu L^{\mu\nu} = 0$, the cross terms and the pure $q$ term vanish:

$$
L^{\mu\nu}(2p_\mu + q_\mu)(2p_\nu + q_\nu) = 4p_\mu p_\nu L^{\mu\nu}
$$

Computing $p_\mu p_\nu L^{\mu\nu}$:

$$
p_\mu p_\nu L^{\mu\nu} = 2\left[2(p\cdot k)(p\cdot k') - m_p^2(k\cdot k')\right]
$$

In the lab frame, $p = (m_p, \vec{0})$, so $p\cdot k = m_p E$ and $p\cdot k' = m_p E'$. Using $k\cdot k' = EE'(1-\cos\theta) = 2EE'\sin^2(\theta/2)$:

$$
p_\mu p_\nu L^{\mu\nu} = 2m_p^2 EE'\left[2 - 2\sin^2\frac{\theta}{2}\right] = 4m_p^2 EE'\cos^2\frac{\theta}{2}
$$

Thus the $W_2$ contribution is:

$$
L^{\mu\nu}W_{\mu\nu}^{(2)} = \frac{W_2}{m_p^2} \cdot 4m_p^2 EE'\cos^2\frac{\theta}{2} = 4W_2 EE'\cos^2\frac{\theta}{2}
$$

**Total contraction:**

Combining both contributions and using $k\cdot k' = 2EE'\sin^2(\theta/2)$:

$$
L^{\mu\nu}W_{\mu\nu} = 4W_1 \cdot 2EE'\sin^2\frac{\theta}{2} + 4W_2 EE'\cos^2\frac{\theta}{2} = 4EE'\left[2W_1\sin^2\frac{\theta}{2} + W_2\cos^2\frac{\theta}{2}\right]
$$

Substituting $W_1 = \tau G_M^2$ and $W_2 = \frac{G_E^2 + \tau G_M^2}{1+\tau}$:

$$
L^{\mu\nu}W_{\mu\nu} = 4EE'\left[2\tau G_M^2\sin^2\frac{\theta}{2} + \frac{G_E^2 + \tau G_M^2}{1+\tau}\cos^2\frac{\theta}{2}\right]
$$

This is the spin-averaged amplitude squared, from which the differential cross section follows by standard phase-space integration.

---

## 8. Phase Space and the Differential Cross Section

The unpolarized differential cross section for a $2 \to 2$ process is:

$$
d\sigma = \frac{1}{4\sqrt{(k\cdot p)^2 - m_e^2 m_p^2}} \overline{|\mathcal{M}|^2} \, d\Phi_2
$$

In the lab frame with $m_e \approx 0$, the flux factor reduces to:

$$
4\sqrt{(k\cdot p)^2} = 4m_p E
$$

The two-body phase space in the lab frame is:

$$
d\Phi_2 = \frac{E'}{(4\pi)^2 m_p} d\Omega = \frac{E'}{16\pi^2 m_p} d\Omega
$$

where $d\Omega = d\cos\theta \, d\phi$ is the solid angle element for the scattered electron. Using azimuthal symmetry ($\int d\phi = 2\pi$ for the unpolarized cross section):

$$
\frac{d\sigma}{d\Omega} = \frac{1}{4m_p E} \cdot \frac{e^4}{q^4} \cdot L^{\mu\nu}W_{\mu\nu} \cdot \frac{E'}{16\pi^2 m_p} \cdot 2\pi
$$

Simplifying with $e^2 = 4\pi\alpha$ and $q^2 = -4EE'\sin^2(\theta/2)$:

$$
\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{4E^2\sin^4(\theta/2)} \frac{E'}{E} \left[\frac{G_E^2 + \tau G_M^2}{1+\tau}\cos^2\frac{\theta}{2} + 2\tau G_M^2\sin^2\frac{\theta}{2}\right]
$$

This is the **Rosenbluth formula**. It is the relativistic generalization of the Rutherford and Mott formulas for a composite, magnetizable target.

---

## 9. Physical Discussion

### The Pointlike Limit

For a structureless Dirac particle, $G_E = G_M = 1$ independent of $Q^2$. The Rosenbluth formula then reduces to:

$$
\frac{d\sigma}{d\Omega}\bigg|_{\text{point}} = \frac{\alpha^2}{4E^2\sin^4(\theta/2)} \frac{E'}{E} \cos^2\frac{\theta}{2}
$$

which is the **Mott cross section** for Coulomb scattering of a relativistic spin-$1/2$ particle. The factor $\cos^2(\theta/2)$ is the helicity-flip suppression characteristic of magnetic scattering.

### Separation of Form Factors

The Rosenbluth formula expresses the cross section as a linear combination of $G_E^2$ and $G_M^2$ at fixed $Q^2$:

$$
\frac{d\sigma}{d\Omega} = A(Q^2, \theta) G_M^2(Q^2) + B(Q^2, \theta) G_E^2(Q^2)
$$

By measuring the differential cross section at the same $Q^2$ but different scattering angles $\theta$ (the so-called Rosenbluth separation), one can extract both form factors independently. This was the dominant experimental technique for proton form factor measurements for several decades.

At low $Q^2$, the electric term dominates at forward angles ($\theta \to 0$), where $\cos^2(\theta/2) \approx 1$ and $\sin^2(\theta/2) \approx 0$:

$$
\frac{d\sigma}{d\Omega}\bigg|_{\theta \to 0} \approx \frac{\alpha^2}{4E^2\sin^4(\theta/2)} \frac{E'}{E} G_E^2(Q^2)
$$

At backward angles ($\theta \to \pi$), the magnetic term dominates:

$$
\frac{d\sigma}{d\Omega}\bigg|_{\theta \to \pi} \approx \frac{\alpha^2}{4E^2} \frac{E'}{E} \cdot 2\tau G_M^2(Q^2)
$$

### Charge and Magnetic Radii

The slope of $G_E$ at $Q^2 = 0$ determines the proton's charge radius:

$$
\langle r_E^2 \rangle = -6 \left.\frac{dG_E(Q^2)}{dQ^2}\right|_{Q^2 = 0}
$$

Similarly, the magnetic radius is extracted from $G_M$. Precise measurements of these slopes have been central to the so-called "proton radius puzzle," where spectroscopic determinations of the charge radius disagreed with scattering extractions at the $4\%$ level—a discrepancy that took nearly a decade to resolve.

### Beyond Rosenbluth

The Rosenbluth separation becomes increasingly difficult at high $Q^2$ because the $G_E^2$ term is suppressed by $\tau = Q^2/(4m_p^2)$ relative to the $G_M^2$ term. For $Q^2 \gg m_p^2$, the cross section is dominated by magnetic scattering, and $G_E$ becomes hard to extract. Polarization transfer measurements, where the recoil proton's polarization is detected, provide a more direct separation of $G_E$ and $G_M$ at high $Q^2$ and have largely superseded the Rosenbluth method in modern experiments.

---

## References

- *An Introduction to Quantum Field Theory*, Ch. 6: Electron-Proton Scattering and the Rosenbluth Formula
