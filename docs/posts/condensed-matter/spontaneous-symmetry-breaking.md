# Spontaneous Symmetry Breaking: From Functional Calculus to Goldstone Modes

📅 **Date:** 2026-04-02 | 🏷️ **Tags:** Condensed Matter Physics, Field Theory, Symmetry Breaking | 📂 **Category:** Condensed Matter Notes

---

## Introduction

Spontaneous symmetry breaking is one of the most profound concepts in modern physics, appearing across condensed matter, particle physics, and cosmology. While symmetries typically simplify physical problems, the spontaneous breaking of continuous symmetries leads to rich phenomenology—including phonons in solids, magnons in magnets, and the Higgs mechanism in particle physics.

This article provides a comprehensive treatment of spontaneous symmetry breaking, with particular attention to the mathematical machinery of functional calculus. We carefully distinguish between ordinary differentiation and functional variation, explaining why the latter is essential for deriving the equations of motion in field theory and condensed matter physics.

---

## Part I: Functional Calculus—Variation vs. Differentiation

### 1.1 The Fundamental Distinction

**Ordinary Differentiation**

In ordinary calculus, we consider functions $f: \mathbb{R} \rightarrow \mathbb{R}$ that map numbers to numbers. The derivative measures how the output changes when the input changes:

$$
\frac{df}{dx} = \lim_{\epsilon \rightarrow 0} \frac{f(x + \epsilon) - f(x)}{\epsilon}
$$

Here, the variation $\epsilon$ is a number. For a function of multiple variables, we have partial derivatives $\partial f/\partial x_i$.

**Functional Differentiation**

A **functional** is a mapping from a space of functions to the real (or complex) numbers. Symbolically:

$$
F: \mathcal{F} \rightarrow \mathbb{R}
$$

where $\mathcal{F}$ is some space of functions (e.g., continuous, differentiable, square-integrable functions). A functional takes an entire function as input and returns a single number.

**Key Examples:**

1. **Action in classical mechanics:**
   $$
   S[q] = \int_0^T dt \, L(q(t), \dot{q}(t))
   $$
   The action $S$ is a functional of the path $q(t)$.

2. **Average value:**
   $$
   I[f] = \int_{-\infty}^{+\infty} dx \, x^2 f(x)
   $$
   
3. **Energy functional:**
   $$
   E[\psi] = \int d^3r \left[\frac{\hbar^2}{2m}|\nabla\psi|^2 + V(r)|\psi|^2\right]
   $$

### 1.2 Defining the Functional Derivative

**The Core Problem**

How do we define "small changes" when the argument is itself a function? We cannot simply add a number $\epsilon$ to a function $f(x)$. Instead, we consider:

$$
f(x) \rightarrow f(x) + \epsilon \, \eta(x)
$$

where $\eta(x)$ is an arbitrary test function and $\epsilon$ is a small parameter. However, this changes $f$ at all points simultaneously. To measure the sensitivity at a specific point $x_0$, we use the **Dirac delta function**.

**The Definition**

The functional derivative $\delta F/\delta f(x_0)$ measures how the functional $F[f]$ changes when we perturb the function $f$ only at the point $x_0$:

$$
f(x) \rightarrow f(x) + \epsilon \, \delta(x - x_0)
$$

**Formal Definition:**

$$
\frac{\delta F[f]}{\delta f(x_0)} = \lim_{\epsilon \rightarrow 0} \frac{F[f + \epsilon \delta_{x_0}] - F[f]}{\epsilon}
$$

where $\delta_{x_0}(x) = \delta(x - x_0)$.

**Key Difference from Ordinary Derivatives:**

| Aspect | Ordinary Derivative | Functional Derivative |
|--------|---------------------|----------------------|
| Input | Number $x \in \mathbb{R}$ | Function $f(x)$ |
| Output | Number $df/dx$ | Function $\delta F/\delta f(x_0)$ of $x_0$ |
| Variation | $\epsilon$ (number) | $\epsilon \cdot \delta(x-x_0)$ (distribution) |
| Notation | $d/dx$ or $\partial/\partial x_i$ | $\delta/\delta f(x)$ |

### 1.3 Explicit Calculation: A Simple Example

**Problem:** Calculate the functional derivative of:

$$
I[f] = \int_{-\infty}^{+\infty} dx \, x^2 f(x)
$$

**Step-by-Step Solution:**

1. **Introduce the variation:**
   $$
   f(x) \rightarrow f(x) + \epsilon \delta(x - x_0)
   $$

2. **Compute the perturbed functional:**
   $$
   I[f + \epsilon \delta_{x_0}] = \int dx \, x^2 [f(x) + \epsilon \delta(x - x_0)]
   $$
   $$
   = \int dx \, x^2 f(x) + \epsilon \int dx \, x^2 \delta(x - x_0)
   $$

3. **Evaluate the delta function integral:**
   Using $\int dx \, g(x) \delta(x - x_0) = g(x_0)$:
   $$
   I[f + \epsilon \delta_{x_0}] = I[f] + \epsilon \, x_0^2
   $$

4. **Take the limit:**
   $$
   \frac{\delta I}{\delta f(x_0)} = \lim_{\epsilon \rightarrow 0} \frac{\epsilon \, x_0^2}{\epsilon} = x_0^2
   $$

**Result:**

$$
\frac{\delta I}{\delta f(x)} = x^2
$$

This tells us that the functional $I[f]$ is most sensitive to changes in $f$ at points where $x^2$ is large.

### 1.4 Deriving the Euler-Lagrange Equations

**The Action Principle**

In classical mechanics, we extremize the action functional:

$$
S[q] = \int_0^T dt \, L(q(t), \dot{q}(t))
$$

The condition for an extremum is that the functional derivative vanishes:

$$
\frac{\delta S}{\delta q(t)} = 0 \quad \text{for all } t
$$

**Step-by-Step Derivation:**

1. **Introduce variation:**
   $$
   q(t) \rightarrow q(t) + \epsilon \delta(t - t')
   $$
   The time derivative also changes:
   $$
   \dot{q}(t) \rightarrow \dot{q}(t) + \epsilon \frac{d}{dt}\delta(t - t') = \dot{q}(t) + \epsilon \dot{\delta}(t - t')
   $$

2. **Expand the Lagrangian to first order:**
   Using Taylor expansion:
   $$
   L(q + \epsilon \delta, \dot{q} + \epsilon \dot{\delta}) = L(q, \dot{q}) + \epsilon \frac{\partial L}{\partial q} \delta(t-t') + \epsilon \frac{\partial L}{\partial \dot{q}} \dot{\delta}(t-t')
   $$

3. **Compute the functional derivative:**
   $$
   \frac{\delta S}{\delta q(t')} = \lim_{\epsilon \rightarrow 0} \frac{1}{\epsilon} \int_0^T dt \left[\epsilon \frac{\partial L}{\partial q} \delta(t-t') + \epsilon \frac{\partial L}{\partial \dot{q}} \dot{\delta}(t-t')\right]
   $$
   $$
   = \int_0^T dt \left[\frac{\partial L}{\partial q} \delta(t-t') + \frac{\partial L}{\partial \dot{q}} \dot{\delta}(t-t')\right]
   $$

4. **Integrate the second term by parts:**
   $$
   \int_0^T dt \frac{\partial L}{\partial \dot{q}} \dot{\delta}(t-t') = \left[\frac{\partial L}{\partial \dot{q}} \delta(t-t')\right]_0^T - \int_0^T dt \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right) \delta(t-t')
   $$
   
   The boundary term vanishes because $\delta(t-t') = 0$ at $t = 0$ and $t = T$ (assuming $t'$ is inside the interval).

5. **Evaluate the remaining integrals:**
   $$
   \frac{\delta S}{\delta q(t')} = \frac{\partial L}{\partial q(t')} - \frac{d}{dt'}\left(\frac{\partial L}{\partial \dot{q}(t')}\right)
   $$

**Result—the Euler-Lagrange Equation:**

Setting $\delta S/\delta q(t) = 0$:

$$
\frac{\partial L}{\partial q} - \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right) = 0
$$

This derivation explicitly shows how the functional derivative with respect to $q(t)$ produces the familiar Euler-Lagrange equation at each time $t$.

### 1.5 Rules for Functional Differentiation

**Chain Rule for Functionals:**

If $F[f] = G[H[f]]$ where $G$ is an ordinary function and $H$ is a functional:

$$
\frac{\delta F}{\delta f(x)} = \frac{dG}{dH} \cdot \frac{\delta H}{\delta f(x)}
$$

**Product Rule:**

If $F[f] = A[f] \cdot B[f]$:

$$
\frac{\delta F}{\delta f(x)} = \frac{\delta A}{\delta f(x)} B + A \frac{\delta B}{\delta f(x)}
$$

**Important Identity:**

The functional derivative of the function itself:

$$
\frac{\delta f(x)}{\delta f(y)} = \delta(x - y)
$$

This is analogous to $\partial x_i / \partial x_j = \delta_{ij}$ in ordinary calculus.

---

## Part II: Spontaneous Symmetry Breaking

### 2.1 Symmetries in Physics

**Discrete vs. Continuous Symmetries**

Symmetries play a central role in physics by constraining the form of physical laws and predicting conserved quantities (via Noether's theorem).

**Discrete symmetries** have a finite number of elements:
- Permutation symmetry (bosons vs. fermions)
- Parity ($\mathbf{r} \rightarrow -\mathbf{r}$)
- Time reversal ($t \rightarrow -t$)

**Continuous symmetries** have infinitely many elements parameterized by continuous variables:
- Rotational symmetry (parameterized by angles)
- Translational symmetry (parameterized by displacement)
- Phase symmetry $U(1)$: $\psi \rightarrow e^{i\theta}\psi$ (parameterized by phase angle $\theta$)

### 2.2 The Phenomenon of Spontaneous Symmetry Breaking

**Definition**

**Spontaneous symmetry breaking** occurs when the ground state of a system has less symmetry than the Hamiltonian or Lagrangian that governs it. The symmetry is "spontaneously" broken without any external field or explicit symmetry-breaking term in the equations.

**Mechanical Analogy: The Pencil**

Consider a perfectly symmetrical pencil balanced on its tip. The Hamiltonian is rotationally symmetric about the vertical axis. However, the pencil cannot remain balanced—it must fall in some direction. Once it falls, the ground state (the fallen pencil) has a specific orientation, breaking the rotational symmetry.

The key insight is that any direction is equally likely, but the system must choose one. The resulting ground state breaks the symmetry, even though the underlying laws remain symmetric.

### 2.3 The Complex Scalar Field Model

**The Lagrangian**

Consider a relativistic complex scalar field $\phi$ with Lagrangian density:

$$
\mathcal{L} = (\partial_\mu \phi^*)(\partial^\mu \phi) - V(\phi)
$$

where the potential is:

$$
V(\phi) = -\alpha |\phi|^2 + \gamma |\phi|^4
$$

with $\alpha > 0$ and $\gamma > 0$.

**Symmetry Analysis**

This Lagrangian has a global $U(1)$ symmetry:

$$
\phi \rightarrow \phi e^{i\theta}
$$

where $\theta$ is a constant (independent of spacetime position). Since $\phi^* \rightarrow \phi^* e^{-i\theta}$, the combination $|\phi|^2 = \phi^*\phi$ is invariant.

**Finding the Ground State**

To find the ground state, we minimize the potential $V(\phi)$. Writing $\phi = \phi_1 + i\phi_2$:

$$
V = -\alpha(\phi_1^2 + \phi_2^2) + \gamma(\phi_1^2 + \phi_2^2)^2
$$

The minima occur where:

$$
\frac{\partial V}{\partial \phi_1} = \frac{\partial V}{\partial \phi_2} = 0
$$

Computing:

$$
\frac{\partial V}{\partial \phi_1} = -2\alpha\phi_1 + 4\gamma(\phi_1^2 + \phi_2^2)\phi_1 = 2\phi_1[-\alpha + 2\gamma(\phi_1^2 + \phi_2^2)] = 0
$$

Similarly for $\phi_2$. The solutions are:

1. $\phi_1 = \phi_2 = 0$ (local maximum, not minimum)
2. $|\phi|^2 = \phi_1^2 + \phi_2^2 = \frac{\alpha}{2\gamma} \equiv v^2$ (circle of minima)

**The "Mexican Hat" Potential**

The potential has the shape of a Mexican hat:
- A local maximum at $\phi = 0$
- A circle of minima at radius $v = \sqrt{\alpha/(2\gamma)}$ in the complex $\phi$ plane

The ground state energy is:

$$
V_{min} = -\alpha v^2 + \gamma v^4 = -\frac{\alpha^2}{4\gamma} < 0
$$

**Spontaneous Symmetry Breaking**

The system must choose one point on the circle of minima. We can parameterize the choice as:

$$
\phi_0 = v e^{i\theta_0}
$$

for some arbitrary phase $\theta_0$. This choice breaks the $U(1)$ symmetry because $\phi_0$ is not invariant under $\phi \rightarrow \phi e^{i\theta}$ (unless $\theta = 0$).

**Expanding Around the Minimum**

To study excitations, we write:

$$
\phi(x) = [v + \eta(x)] e^{i\theta(x)}
$$

or equivalently:

$$
\phi(x) = v + \frac{1}{\sqrt{2}}[h(x) + i\pi(x)]
$$

where $h$ (the Higgs field) represents radial fluctuations and $\pi$ (the Goldstone mode) represents phase fluctuations.

Substituting into the Lagrangian and expanding to quadratic order:

$$
\mathcal{L} \approx \frac{1}{2}(\partial_\mu h)(\partial^\mu h) - \frac{1}{2}m_h^2 h^2 + \frac{1}{2}(\partial_\mu \pi)(\partial^\mu \pi)
$$

where $m_h^2 = 4\gamma v^2 = 2\alpha$.

**Key Observations:**

1. The $h$ field has mass $m_h$—it costs energy to change the amplitude.
2. The $\pi$ field has **no mass term**—it is a massless Goldstone boson.

### 2.4 Goldstone's Theorem

**Statement of the Theorem**

**Goldstone's Theorem:** When a continuous global symmetry is spontaneously broken, there exists a massless bosonic excitation (a Goldstone mode) for each generator of the broken symmetry.

**Proof Sketch:**

Consider a theory with Lagrangian $\mathcal{L} = T - V(\phi)$ where $\phi$ may be a complex field. Assume the theory has a continuous symmetry:

$$
V(\phi) = V(\phi + \epsilon \delta\phi)
$$

for infinitesimal $\epsilon$ and generator $\delta\phi$.

**Step 1: Symmetry Condition**

Expand $V(\phi + \epsilon \delta\phi)$ to first order:

$$
V(\phi + \epsilon \delta\phi) = V(\phi) + \epsilon \frac{\delta V}{\delta \phi} \delta\phi = V(\phi)
$$

This requires:

$$
\frac{\delta V}{\delta \phi} \delta\phi = 0
$$

**Step 2: Broken Symmetry**

Now assume the symmetry is spontaneously broken. The field $\phi$ acquires an expectation value $\phi_0$ that minimizes $V$:

$$
\left.\frac{\delta V}{\delta \phi}\right|_{\phi=\phi_0} = 0
$$

But $\phi_0$ is not invariant under the symmetry transformation (otherwise the symmetry would not be broken).

**Step 3: Mass Matrix**

Expand $V$ around $\phi_0$:

$$
V(\phi_0 + \chi) = V(\phi_0) + \frac{1}{2}\chi^2 \left.\frac{\partial^2 V}{\partial \phi^2}\right|_{\phi_0} + \ldots
$$

The second derivative defines the mass matrix:

$$
m^2 = \left.\frac{\partial^2 V}{\partial \phi^2}\right|_{\phi_0}
$$

**Step 4: Key Identity**

Differentiate the symmetry condition $\frac{\delta V}{\delta \phi} \delta\phi = 0$ with respect to $\phi$:

$$
\frac{\partial^2 V}{\partial \phi^2} \delta\phi + \frac{\partial \delta\phi}{\partial \phi} \frac{\delta V}{\delta \phi} = 0
$$

Evaluate at $\phi = \phi_0$ where $\frac{\delta V}{\delta \phi} = 0$:

$$
\left.\frac{\partial^2 V}{\partial \phi^2}\right|_{\phi_0} \delta\phi_0 = 0
$$

Since $\delta\phi_0 \neq 0$ (the symmetry is broken), we have:

$$
m^2 \delta\phi_0 = 0
$$

This means the mass matrix has a zero eigenvalue with eigenvector $\delta\phi_0$.

**Conclusion:** There is a massless mode associated with the broken symmetry generator $\delta\phi$.

### 2.5 Physical Examples of Goldstone Modes

**1. Phonons in Solids**

A crystal spontaneously breaks continuous translational symmetry. The atoms sit at fixed lattice positions, selecting specific locations even though the Hamiltonian is translationally invariant.

The Goldstone modes are **phonons**—collective vibrations of the lattice. They are gapless (acoustic phonons have $\omega \rightarrow 0$ as $\mathbf{k} \rightarrow 0$) because uniform translation of the entire crystal costs no energy.

**2. Magnons in Ferromagnets**

In a ferromagnet, spins align along a specific direction, breaking rotational symmetry. The order parameter is the magnetization $\mathbf{M}$.

The Goldstone modes are **magnons** (spin waves)—collective excitations where spins precess around the magnetization direction. In the long-wavelength limit, magnons have $\omega \propto k^2$ (quadratic dispersion).

**3. Superconductivity and the Phase Mode**

In a superconductor, the complex order parameter $\psi = |\psi|e^{i\theta}$ acquires a non-zero value. The amplitude $|\psi|$ is fixed, but the phase $\theta$ can vary.

The Goldstone mode associated with broken $U(1)$ charge symmetry would be a massless phase mode. However, in a charged superconductor, the Coulomb interaction gaps out this mode (Anderson-Higgs mechanism), giving rise to the superconducting gap.

---

## Part III: Order Parameters and Phase Transitions

### 3.1 The Order Parameter Concept

**Definition**

An **order parameter** is a quantity that:
1. Is zero in the high-symmetry (disordered) phase
2. Is non-zero in the low-symmetry (ordered) phase
3. Tracks the broken symmetry

**Examples:**

| System | Order Parameter | Broken Symmetry |
|--------|----------------|-----------------|
| Ferromagnet | Magnetization $\mathbf{M}$ | Rotational |
| Crystal | Displacement $\mathbf{u}$ | Translational |
| Superconductor | Pair field $\langle\psi_\uparrow\psi_\downarrow\rangle$ | $U(1)$ phase |
| Superfluid | $\langle\hat{\psi}\rangle$ | $U(1)$ phase |
| Nematic liquid crystal | Director $\mathbf{n}$ | Rotational |

### 3.2 Landau Theory of Phase Transitions

**Landau Free Energy**

Near a continuous phase transition, the free energy can be expanded in powers of the order parameter $M$ (e.g., magnetization):

$$
F(M) = F_0 + \frac{1}{2}\alpha(T) M^2 + \frac{1}{4}\gamma M^4
$$

where $\alpha(T) = \alpha_0(T - T_c)$ changes sign at the critical temperature $T_c$, and $\gamma > 0$ ensures stability.

**Minimization:**

$$
\frac{\partial F}{\partial M} = \alpha M + \gamma M^3 = 0
$$

Solutions:
- $M = 0$ (high temperature, $T > T_c$)
- $M = \pm\sqrt{-\alpha/\gamma} = \pm\sqrt{\alpha_0(T_c - T)/\gamma}$ (low temperature, $T < T_c$)

**Critical Behavior:**

Near $T_c$, the order parameter vanishes as:

$$
M \propto (T_c - T)^{\beta}
$$

with mean-field critical exponent $\beta = 1/2$.

### 3.3 Domain Formation and Hysteresis

**Domain Walls**

In real materials, the system does not uniformly choose one symmetry-broken state. Instead, it forms **domains**—regions where the order parameter points in different directions. Domain walls separate regions with different orientations.

In iron, typical domain sizes are $\sim 300$ lattice spacings. The existence of domains means that macroscopic samples may have zero net magnetization even below $T_c$.

**Hysteresis**

Applying an external magnetic field aligns the domains. When the field is removed, domains remain aligned due to pinning at defects—this is **hysteresis**. The magnetization curve $M(H)$ shows history-dependent behavior, with discontinuous jumps (Barkhausen effect) as domain walls de-pin from defects.

---

## Summary

| Concept | Key Formula/Result |
|---------|-------------------|
| **Functional Derivative** | $\frac{\delta F}{\delta f(x_0)} = \lim_{\epsilon \rightarrow 0} \frac{F[f + \epsilon\delta_{x_0}] - F[f]}{\epsilon}$ |
| **Difference from Ordinary Derivative** | Functional derivative is a function of position; ordinary derivative is a number |
| **Goldstone Theorem** | Spontaneous breaking of continuous symmetry $\Rightarrow$ massless Goldstone mode |
| **Mexican Hat Potential** | $V = -\alpha|\phi|^2 + \gamma|\phi|^4$ with minima at $|\phi|^2 = \alpha/(2\gamma)$ |
| **Order Parameter** | Non-zero in ordered phase, zero in disordered phase |
| **Critical Exponent** | $M \propto (T_c - T)^\beta$ with $\beta = 1/2$ (mean field) |

Spontaneous symmetry breaking demonstrates that the ground state of a system need not share the symmetries of the governing Hamiltonian. This seemingly simple observation has profound consequences, from the existence of phonons and magnons to the mechanism of superconductivity and the Higgs mechanism in particle physics.
