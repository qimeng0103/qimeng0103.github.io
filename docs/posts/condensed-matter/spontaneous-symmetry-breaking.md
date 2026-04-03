# Spontaneous Symmetry Breaking: From Functional Calculus to Goldstone Modes

📅 **Date:** 2026-04-03 | 🏷️ **Tags:** Condensed Matter Physics, Field Theory, Symmetry Breaking | 📂 **Category:** Condensed Matter Notes

---

## Introduction

Spontaneous symmetry breaking is one of the most profound concepts in modern physics. While symmetries typically simplify physical problems, the spontaneous breaking of continuous symmetries leads to rich phenomenology—including phonons in solids, magnons in magnets, and the Higgs mechanism in particle physics.

This article provides a comprehensive treatment, with particular attention to the mathematical machinery of functional calculus. We carefully distinguish between ordinary differentiation and functional variation, explaining why the latter is essential for field theory.

---

## Part I: Functional Calculus

### 1.1 Functions vs. Functionals: The Fundamental Distinction

**Ordinary Functions**

A function maps numbers to numbers:

$$
f: \mathbb{R} \rightarrow \mathbb{R}, \quad x \mapsto f(x)
$$

The derivative measures how the output changes when the input changes:

$$
\frac{df}{dx} = \lim_{\epsilon \rightarrow 0} \frac{f(x + \epsilon) - f(x)}{\epsilon}
$$

Here $\epsilon$ is a small **number**.

**Functionals**

A **functional** maps an entire function to a number:

$$
F: \mathcal{F} \rightarrow \mathbb{R}, \quad f(\cdot) \mapsto F[f]
$$

**Key Examples:**

1. **Action in classical mechanics:**
   $$
   S[q] = \int_0^T dt \, L(q(t), \dot{q}(t))
   $$
   The input is the entire path $q(t)$; the output is a single number $S$.

2. **Average value:**
   $$
   I[f] = \int_{-\infty}^{+\infty} dx \, x^2 f(x)
   $$

3. **Energy functional** (kinetic + potential energy):
   $$
   E[\psi] = \int d^3r \left[\frac{\hbar^2}{2m}\vert\nabla\psi\vert^2 + V(r)\vert\psi\vert^2\right]
   $$
   
   **Note:** After integration by parts, the kinetic term becomes:
   $$-\int d^3r \, \frac{\hbar^2}{2m}\psi^*\nabla^2\psi$$

### 1.2 The Problem: How to Differentiate a Functional?

**The Challenge**

For a functional $F[f]$, how do we define "$dF/df$"? The issue is that $f$ is not a single variable but a function defined at infinitely many points.

**Two Perspectives:**

**Perspective A: Multivariable Calculus View**

Think of $f(x)$ as an infinite collection of independent variables $\{f_x\}$, one for each position $x$. Then:

$$
F[f] = F(f_{x_1}, f_{x_2}, f_{x_3}, \ldots)
$$

The partial derivative with respect to one variable is:

$$
\frac{\partial F}{\partial f_y} = \lim_{\epsilon \rightarrow 0} \frac{F(\ldots, f_y + \epsilon, \ldots) - F(\ldots, f_y, \ldots)}{\epsilon}
$$

**Perspective B: Function Space View**

Think of $f$ as a vector in an infinite-dimensional function space. We want the directional derivative in the direction of a "test function" $\eta(x)$:

$$
\left.\frac{d}{d\epsilon}F[f + \epsilon\eta]\right|_{\epsilon=0}
$$

**The Resolution: Point-by-Point Variation**

To measure sensitivity at a **specific point** $x_0$, we choose a variation that only changes $f$ at that point. This is achieved using the **Dirac delta function**:

$$
\eta(x) = \delta(x - x_0)
$$

**Why the Delta Function?**

The delta function $\delta(x - x_0)$ has the key property:

$$
\int dx \, g(x) \delta(x - x_0) = g(x_0)
$$

When we add $\epsilon \delta(x - x_0)$ to $f(x)$, we change $f$ only in an infinitesimal neighborhood of $x_0$, leaving it unchanged everywhere else.

### 1.3 Definition of the Functional Derivative

**Formal Definition:**

The functional derivative of $F$ at point $x_0$ is:

$$
\frac{\delta F[f]}{\delta f(x_0)} \equiv \lim_{\epsilon \rightarrow 0} \frac{F[f + \epsilon \delta_{x_0}] - F[f]}{\epsilon}
$$

where $\delta_{x_0}(x) = \delta(x - x_0)$.

**Key Properties:**

| Property | Ordinary Derivative | Functional Derivative |
|----------|---------------------|----------------------|
| Input | Number $x$ | Function $f(x)$ |
| Output | Number $df/dx$ | Function of position: $\frac{\delta F}{\delta f(x_0)}$ |
| Variation | $\epsilon$ (number) | $\epsilon \cdot \delta(x-x_0)$ (distribution) |
| Notation | $d/dx$ or $\partial/\partial x_i$ | $\delta/\delta f(x)$ |

**Important Clarification: Function vs. Function Value**

The functional derivative $\frac{\delta F}{\delta f(x_0)}$ is itself a **function of $x_0$**. However, physicists often write $\frac{\delta F}{\delta f}$ or $\frac{\delta F}{\delta \phi}$ without the explicit $(x_0)$, which can cause confusion between:
- The function $\frac{\delta F}{\delta f(x)}$ for all $x$
- The value $\frac{\delta F}{\delta f(x_0)}$ at a specific point $x_0$

### 1.4 Worked Example: Computing a Functional Derivative

**Problem:** Find the functional derivative of:

$$
I[f] = \int_{-\infty}^{+\infty} dx \, x^2 f(x)
$$

**Solution:**

**Step 1:** Introduce a point-variation at $x_0$:

$$
f(x) \rightarrow f(x) + \epsilon \delta(x - x_0)
$$

**Step 2:** Compute the perturbed functional:

$$
I[f + \epsilon \delta_{x_0}] = \int dx \, x^2 [f(x) + \epsilon \delta(x - x_0)]
$$

$$
= \underbrace{\int dx \, x^2 f(x)}_{I[f]} + \epsilon \int dx \, x^2 \delta(x - x_0)
$$

**Step 3:** Evaluate using the delta function property:

$$
\int dx \, x^2 \delta(x - x_0) = x_0^2
$$

Therefore:

$$
I[f + \epsilon \delta_{x_0}] = I[f] + \epsilon \, x_0^2
$$

**Step 4:** Take the limit:

$$
\frac{\delta I}{\delta f(x_0)} = \lim_{\epsilon \rightarrow 0} \frac{\epsilon \, x_0^2}{\epsilon} = x_0^2
$$

**Result:**

$$
\frac{\delta I}{\delta f(x)} = x^2
$$

**Physical Interpretation:** The functional $I[f]$ is most sensitive to changes in $f$ at points where $x^2$ is large. This makes intuitive sense: $I[f]$ is a weighted average of $f$ with weight $x^2$, so changing $f$ where the weight is large has a bigger effect on the integral.

### 1.5 Deriving the Euler-Lagrange Equations

**The Action Principle**

In classical mechanics, the action is a functional of the path $q(t)$:

$$
S[q] = \int_0^T dt \, L(q(t), \dot{q}(t))
$$

where $L(q, \dot{q})$ is the Lagrangian **function** (not functional—it depends only on values at a single time).

The condition for an extremum is that the functional derivative vanishes at all times:

$$
\frac{\delta S}{\delta q(t')} = 0 \quad \text{for all } t' \in (0, T)
$$

**Step-by-Step Derivation:**

**Step 1:** Introduce a point-variation at time $t'$:

$$
q(t) \rightarrow q(t) + \epsilon \delta(t - t')
$$

where we assume $t' \in (0, T)$ (interior point, not at the boundaries).

The time derivative also changes:

$$
\dot{q}(t) \rightarrow \dot{q}(t) + \epsilon \frac{d}{dt}\delta(t - t')
$$

**Step 2:** Taylor expansion of $L$ (ordinary multivariable Taylor expansion, since $L$ is a function of two variables $q$ and $\dot{q}$):

$$
L(q + \epsilon\delta, \dot{q} + \epsilon\dot{\delta}) = L(q, \dot{q}) + \epsilon \frac{\partial L}{\partial q} \delta(t-t') + \epsilon \frac{\partial L}{\partial \dot{q}} \dot{\delta}(t-t') + O(\epsilon^2)
$$

**Note:** Here $\frac{\partial L}{\partial q}$ and $\frac{\partial L}{\partial \dot{q}}$ are ordinary partial derivatives because $L$ is evaluated at a specific time $t$ with specific values $q(t)$ and $\dot{q}(t)$.

**Step 3:** Compute the variation of the action:

$$
\delta S = S[q + \epsilon\delta_{t'}] - S[q]
$$

$$
= \epsilon \int_0^T dt \left[\frac{\partial L}{\partial q} \delta(t-t') + \frac{\partial L}{\partial \dot{q}} \dot{\delta}(t-t')\right]
$$

**Step 4:** Integrate the second term by parts:

$$
\int_0^T dt \frac{\partial L}{\partial \dot{q}} \dot{\delta}(t-t') = \left[\frac{\partial L}{\partial \dot{q}} \delta(t-t')\right]_0^T - \int_0^T dt \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right) \delta(t-t')
$$

The boundary term vanishes because $\delta(t-t') = 0$ at $t = 0$ and $t = T$ (since $t' \in (0, T)$ is strictly inside).

**Step 5:** Use the delta function to evaluate at $t = t'$:

$$
\frac{\delta S}{\delta q(t')} = \lim_{\epsilon \to 0} \frac{\delta S}{\epsilon} = \frac{\partial L}{\partial q}(t') - \frac{d}{dt'}\left(\frac{\partial L}{\partial \dot{q}}\right)(t')
$$

**Result—the Euler-Lagrange Equation:**

Setting $\frac{\delta S}{\delta q(t)} = 0$:

$$
\frac{\partial L}{\partial q} - \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}}\right) = 0
$$

**Important:** This is an ordinary differential equation at each time $t$, derived from a functional extremization over all paths.

### 1.6 The Critical Distinction: $\frac{\delta}{\delta\phi}$ vs $\frac{\partial}{\partial\phi}$

**The Core Confusion**

In field theory, we encounter both:
- $\frac{\delta F}{\delta \phi(x)}$ — functional derivative
- $\frac{\partial \mathcal{L}}{\partial \phi}$ — ordinary partial derivative

When to use which?

**Rule 1: Look at What You're Differentiating**

| Object | Depends on | Derivative Type | Example |
|--------|-----------|-----------------|---------|
| Action $S[\phi]$ | Entire function $\phi(x)$ | Functional | $\frac{\delta S}{\delta \phi(x)}$ |
| Lagrangian density $\mathcal{L}$ | Value $\phi(x)$ at single point | Ordinary partial | $\frac{\partial \mathcal{L}}{\partial \phi}$ |
| Potential $V(\phi)$ (uniform field) | Single number $\phi$ | Ordinary | $\frac{\partial V}{\partial \phi}$ |

**Rule 2: Local vs. Non-Local Functionals**

A **local functional** has the form:

$$
F[\phi] = \int dx \, \mathcal{L}(\phi(x), \nabla\phi(x), x)
$$

where $\mathcal{L}$ (the **Lagrangian density**) depends only on the field and its derivatives at the same point $x$.

For local functionals, the functional derivative is related to ordinary partial derivatives by:

$$
\frac{\delta F}{\delta \phi(x)} = \frac{\partial \mathcal{L}}{\partial \phi}(x) - \nabla \cdot \left(\frac{\partial \mathcal{L}}{\partial(\nabla\phi)}(x)\right)
$$

**Key Point:** The density $\mathcal{L}$ uses ordinary partial derivatives; the functional $F$ uses functional derivatives.

**Example Where They Differ:**

Consider $F[\phi] = \int dx \, \frac{1}{2}(\nabla\phi)^2$.
- The density is $\mathcal{L} = \frac{1}{2}(\nabla\phi)^2$
- Ordinary partial: $\frac{\partial \mathcal{L}}{\partial \phi} = 0$ (no explicit $\phi$ dependence)
- Functional derivative: $\frac{\delta F}{\delta \phi(x)} = -\nabla^2\phi(x)$

These are completely different! The functional derivative captures spatial variation.

### 1.7 Rule 3: Uniform Field Configurations - Detailed Analysis

**The Equality**

For a spatially uniform field $\phi(x) = \phi_0$ (constant), the following equality holds:

$$
\left.\frac{\delta F[\phi]}{\delta \phi(x)}\right|_{\phi(x)=\phi_0} = \left.\frac{\partial \mathcal{L}}{\partial \phi}\right|_{\phi=\phi_0}
$$

**Understanding the Left-Hand Side (Functional Derivative)**

The left-hand side is evaluated by:
1. Compute the functional derivative $\frac{\delta F}{\delta \phi(x)}$ as a function of $x$ (which involves $\phi(x)$ and its derivatives)
2. Substitute the uniform configuration $\phi(x) = \phi_0$ (constant)
3. The result is a number (constant, independent of $x$)

**Understanding the Right-Hand Side (Ordinary Derivative)**

The right-hand side is evaluated by:
1. Take the Lagrangian density $\mathcal{L}(\phi, \nabla\phi)$
2. Treat $\phi$ as a variable and compute $\frac{\partial \mathcal{L}}{\partial \phi}$
3. Set $\nabla\phi = 0$ (uniform field) and $\phi = \phi_0$
4. The result is a number

**Detailed Proof:**

For a local functional:

$$
F[\phi] = \int dy \, \mathcal{L}(\phi(y), \nabla\phi(y))
$$

The functional derivative is:

$$
\frac{\delta F}{\delta \phi(x)} = \frac{\partial \mathcal{L}}{\partial \phi}(x) - \nabla_x \cdot \frac{\partial \mathcal{L}}{\partial(\nabla\phi)}(x)
$$

Now substitute $\phi(x) = \phi_0$ (constant):
- $\frac{\partial \mathcal{L}}{\partial \phi}(x) = \frac{\partial \mathcal{L}}{\partial \phi}(\phi_0, 0)$ (just a number)
- $\nabla\phi(x) = 0$, so the second term vanishes

Therefore:

$$
\left.\frac{\delta F}{\delta \phi(x)}\right|_{\phi(x)=\phi_0} = \frac{\partial \mathcal{L}}{\partial \phi}(\phi_0, 0) = \left.\frac{\partial \mathcal{L}}{\partial \phi}\right|_{\phi=\phi_0}
$$

**Why This is Confusing**

The notation makes it look like we're comparing:
- A function evaluated at a point: $\frac{\delta F}{\delta \phi(x)}|_{\phi(x)=\phi_0}$
- A function of a variable: $\frac{\partial \mathcal{L}}{\partial \phi}|_{\phi=\phi_0}$

But after substitution, both are just **numbers**. The equality holds because for a uniform field, spatial derivatives vanish, and the functional derivative reduces to the ordinary derivative of the density.

**Key Takeaway:**

This equality is why physicists often mix notation—but it **only holds for uniform configurations**! For non-uniform fields, the functional derivative contains additional terms from spatial derivatives.

### 1.8 Worked Example: $\phi^4$ Theory

**The Model**

Consider a real scalar field with potential:

$$
V(\phi) = \frac{1}{2}m^2\phi^2 + \frac{1}{4}\lambda\phi^4
$$

The total energy functional is:

$$
E[\phi] = \int d^dx \left[\frac{1}{2}(\nabla\phi)^2 + V(\phi(x))\right]
$$

**Finding the Ground State**

The ground state minimizes $E[\phi]$. We compute the functional derivative:

**Step 1:** Vary the field:

$$
\phi(x) \rightarrow \phi(x) + \delta\phi(x)
$$

**Step 2:** Compute $\delta E$ to first order:

$$
\delta E = \int d^dx \left[(\nabla\phi)\cdot(\nabla\delta\phi) + V'(\phi)\delta\phi\right]
$$

$$
= \int d^dx \left[-\nabla^2\phi + V'(\phi)\right]\delta\phi \quad \text{(integration by parts)}
$$

**Step 3:** Set $\delta E = 0$ for arbitrary $\delta\phi(x)$:

$$
-\nabla^2\phi(x) + V'(\phi(x)) = 0
$$

This is the Euler-Lagrange equation. For the ground state, we look for uniform solutions $\phi(x) = \phi_0$:

$$
V'(\phi_0) = m^2\phi_0 + \lambda\phi_0^3 = 0
$$

Solutions: $\phi_0 = 0$ or $\phi_0 = \pm\sqrt{-m^2/\lambda}$ (if $m^2 < 0$).

**Why Uniform Field for Ground State?**

The kinetic term $\frac{1}{2}(\nabla\phi)^2$ is always non-negative. Any spatial variation increases the energy. Therefore, the lowest energy configuration has $\nabla\phi = 0$, i.e., uniform field.

### 1.9 Rules for Functional Differentiation

**Chain Rule for Functionals:**

If $F[f] = G[H[f]]$ where $G$ is an ordinary function and $H$ is a functional:

$$
\frac{\delta F}{\delta f(x)} = \frac{dG}{dH} \cdot \frac{\delta H}{\delta f(x)}
$$

**Proof:** By direct computation using the definition.

**Product Rule:**

If $F[f] = A[f] \cdot B[f]$:

$$
\frac{\delta F}{\delta f(x)} = \frac{\delta A}{\delta f(x)} B + A \frac{\delta B}{\delta f(x)}
$$

**Important Identity:**

$$
\frac{\delta f(x)}{\delta f(y)} = \delta(x - y)
$$

**Proof:** Vary $f$ at point $y$: $f(x) \rightarrow f(x) + \epsilon\delta(x-y)$. Then:

$$
\frac{\delta f(x)}{\delta f(y)} = \lim_{\epsilon\to 0} \frac{\epsilon\delta(x-y)}{\epsilon} = \delta(x-y)
$$

This is the functional analog of $\partial x_i/\partial x_j = \delta_{ij}$.

---

## Part II: Spontaneous Symmetry Breaking

### 2.1 Symmetries in Physics

**Discrete vs. Continuous Symmetries**

**Discrete symmetries** have a finite number of elements:
- Parity: $\mathbf{r} \rightarrow -\mathbf{r}$
- Time reversal: $t \rightarrow -t$

**Continuous symmetries** have infinitely many elements parameterized by continuous variables:
- Translation: $\mathbf{r} \rightarrow \mathbf{r} + \mathbf{a}$ (parameterized by displacement $\mathbf{a}$)
- Rotation: parameterized by angles
- Phase rotation $U(1)$: $\psi \rightarrow e^{i\theta}\psi$ (parameterized by phase angle $\theta$)

**Noether's Theorem:** Every continuous symmetry implies a conserved quantity.

### 2.2 What is Spontaneous Symmetry Breaking?

**Definition**

**Spontaneous symmetry breaking** occurs when the ground state of a system has less symmetry than the equations of motion (Hamiltonian or Lagrangian) that govern it.

The symmetry is "spontaneous" because:
1. The equations remain symmetric
2. No external symmetry-breaking field is applied
3. The system "chooses" a specific ground state that breaks the symmetry

**Analogy: The Balanced Pencil**

Imagine a perfectly symmetrical pencil balanced on its tip:
- The **Hamiltonian** (gravity + rigid body dynamics) is rotationally symmetric about the vertical axis
- The balanced state (unstable) respects this symmetry
- However, the pencil must fall in some direction
- The **fallen state** (ground state) points in a specific direction, breaking the rotational symmetry

Mathematically, if the pencil falls along the $x$-axis, the ground state has $\langle\phi\rangle = \phi_0 \hat{x}$ where $\phi$ is the orientation angle. The Hamiltonian is invariant under $\phi \rightarrow \phi + \delta\phi$, but the ground state is not.

**Key Insight:** Any fall direction is equally likely (symmetric), but the system must pick one (symmetry breaking).

### 2.3 The Complex Scalar Field Model

**The Lagrangian Density**

Consider a relativistic complex scalar field $\phi(x)$ with:

$$
\mathcal{L} = (\partial_\mu \phi^*)(\partial^\mu \phi) - V(\phi)
$$

where the potential is:

$$
V(\phi) = -\alpha \vert\phi\vert^2 + \gamma \vert\phi\vert^4
$$

with $\alpha > 0$ and $\gamma > 0$.

**Symmetry Analysis**

This Lagrangian has a global $U(1)$ symmetry:

$$
\phi \rightarrow \phi e^{i\theta}
$$

where $\theta$ is a constant (independent of spacetime). Since $\vert\phi\vert^2 = \phi^*\phi$ is invariant under this transformation, the potential $V$ and kinetic term are unchanged.

**Finding the Ground State: Why Minimize $V$?**

In quantum field theory, the ground state (vacuum) is the state of lowest energy. For a static, uniform field configuration:
- Kinetic energy $(\partial_\mu\phi)^2 = 0$ (no spatial or temporal variation)
- Total energy density = $V(\phi)$

Therefore, the ground state field value $\phi_0$ minimizes $V(\phi)$.

**Mathematical Minimization**

Write $\phi = \phi_1 + i\phi_2$ in terms of real components. Then:

$$
V = -\alpha(\phi_1^2 + \phi_2^2) + \gamma(\phi_1^2 + \phi_2^2)^2
$$

Find critical points:

$$
\frac{\partial V}{\partial \phi_1} = -2\alpha\phi_1 + 4\gamma(\phi_1^2 + \phi_2^2)\phi_1 = 2\phi_1[-\alpha + 2\gamma(\phi_1^2 + \phi_2^2)] = 0
$$

Similarly for $\phi_2$.

Solutions:
1. $\phi_1 = \phi_2 = 0$ (local **maximum**, since $V(0) = 0$ and $V < 0$ nearby)
2. $\vert\phi\vert^2 = \phi_1^2 + \phi_2^2 = \frac{\alpha}{2\gamma} \equiv v^2$ (circle of **minima**)

The ground state energy is:

$$
V_{min} = -\alpha v^2 + \gamma v^4 = -\frac{\alpha^2}{4\gamma} < 0
$$

**The "Mexican Hat" Potential**

Plotting $V$ as a function of $(\phi_1, \phi_2)$:
- A local maximum at the origin $(0, 0)$
- A circular valley (minimum) at radius $v = \sqrt{\alpha/(2\gamma)}$
- The shape resembles a Mexican hat or wine bottle

**Symmetry Breaking**

The system must choose one point on the circle of minima. Parameterize the choice as:

$$
\phi_0 = v e^{i\theta_0}
$$

for some arbitrary phase angle $\theta_0$.

This choice **breaks** the $U(1)$ symmetry because $\phi_0$ is not invariant under $\phi \rightarrow \phi e^{i\theta}$ (unless $\theta = 0$).

All choices $\theta_0 \in [0, 2\pi)$ are equally valid ground states, related by the symmetry transformation. They are called **degenerate vacua**.

### 2.4 Excitations Around the Ground State

**Why Study Excitations?**

The ground state $\phi_0$ is static. To understand the dynamics (particles, collective modes), we study small fluctuations around $\phi_0$.

**Parametrizing Fluctuations**

Write the field as:

$$
\phi(x) = [v + \eta(x)] e^{i\theta(x)}
$$

where:
- $v$ is the vacuum expectation value
- $\eta(x)$ is the amplitude fluctuation (radial direction)
- $\theta(x)$ is the phase fluctuation (angular direction)

Equivalently, in Cartesian form:

$$
\phi(x) = v + \frac{1}{\sqrt{2}}[h(x) + i\pi(x)]
$$

where $h$ and $\pi$ are real fields. This form is obtained by expanding:

$$
\phi = (v + \eta)e^{i\theta} = (v + \eta)(\cos\theta + i\sin\theta) \approx (v + \eta)(1 + i\theta) \approx v + \eta + iv\theta
$$

So $h = \sqrt{2}\eta$ (amplitude) and $\pi = \sqrt{2}v\theta$ (phase).

**Substituting into the Lagrangian**

We substitute $\phi = v + \frac{1}{\sqrt{2}}(h + i\pi)$ into $\mathcal{L}$ and expand to quadratic order in $h$ and $\pi$.

First, compute $\vert\phi\vert^2$:

$$
\vert\phi\vert^2 = \left(v + \frac{h}{\sqrt{2}}\right)^2 + \left(\frac{\pi}{\sqrt{2}}\right)^2 = v^2 + \sqrt{2}vh + \frac{h^2}{2} + \frac{\pi^2}{2}
$$

Then expand $V(\vert\phi\vert^2)$ to quadratic order:

$$
V = -\alpha\vert\phi\vert^2 + \gamma\vert\phi\vert^4 = -\alpha(v^2 + \sqrt{2}vh + \frac{h^2+\pi^2}{2}) + \gamma(v^2 + \sqrt{2}vh + \ldots)^2
$$

Using $\alpha = 2\gamma v^2$ (from the minimum condition), the linear terms cancel, and we get:

$$
V \approx V_{min} + \frac{1}{2}m_h^2 h^2 + 0 \cdot \pi^2 + \ldots
$$

where $m_h^2 = 4\gamma v^2 = 2\alpha$.

**The Key Result**

The quadratic Lagrangian is:

$$
\mathcal{L}_{quad} = \frac{1}{2}(\partial_\mu h)(\partial^\mu h) - \frac{1}{2}m_h^2 h^2 + \frac{1}{2}(\partial_\mu \pi)(\partial^\mu \pi)
$$

**Physical Interpretation:**

1. **The $h$ field** has mass $m_h$ and satisfies the Klein-Gordon equation:
   $$(\partial^2 + m_h^2)h = 0$$
   Mass means it costs energy $\Delta E = m_h$ to create a quantum of the $h$ field. This is the **Higgs boson**.

2. **The $\pi$ field** has **no mass term** ($m_\pi = 0$). It satisfies:
   $$\partial^2 \pi = 0$$
   This is a **massless** excitation—the **Goldstone boson**.

**Why "Massless" Means "Costs No Energy at Long Wavelengths"**

For a massive field, the energy of a plane wave $e^{i\mathbf{k}\cdot\mathbf{x}}$ is:

$$
E = \sqrt{\mathbf{k}^2 + m^2}
$$

As $\mathbf{k} \rightarrow 0$:
- Massive: $E \rightarrow m \neq 0$ (finite energy gap)
- Massless: $E \rightarrow 0$ (gapless)

For the phase mode $\pi$: a uniform rotation $\theta = $ constant costs **zero energy** because all points on the Mexican hat minimum have the same energy. This is the Goldstone mode.

### 2.5 Goldstone's Theorem

**Statement**

**Goldstone's Theorem:** When a continuous global symmetry is spontaneously broken, there exists a massless bosonic excitation (Goldstone mode) for each broken symmetry generator.

**Proof**

**Setup:**
- Let the theory have a continuous symmetry with generator $\eta$ (a fixed function or direction in field space)
- The symmetry transformation is: $\phi(x) \rightarrow \phi(x) + \epsilon \eta(x)$
- The potential $V[\phi]$ is invariant: $V[\phi + \epsilon\eta] = V[\phi]$

**Step 1: Symmetry Condition**

Expand $V[\phi + \epsilon\eta]$ to first order in $\epsilon$:

$$
V[\phi + \epsilon\eta] = V[\phi] + \epsilon \int dx \, \frac{\delta V}{\delta \phi(x)} \eta(x) + O(\epsilon^2)
$$

Invariance requires that the coefficient of $\epsilon$ vanish:

$$
\int dx \, \frac{\delta V}{\delta \phi(x)} \eta(x) = 0 \quad \text{for all } \phi
$$

**Step 2: Take the Functional Derivative of the Identity**

The above equation is an identity—it holds for all field configurations $\phi(x)$. We can take the functional derivative of both sides with respect to $\phi(y)$:

$$
\frac{\delta}{\delta \phi(y)} \int dx \, \frac{\delta V}{\delta \phi(x)} \eta(x) = 0
$$

**Key Point:** The functional derivative $\frac{\delta}{\delta \phi(y)}$ commutes with the integral $\int dx$ because $x$ and $y$ are independent variables (different points in space).

**Step 3: Apply the Product Rule**

Using the product rule for functional derivatives:

$$
\frac{\delta}{\delta \phi(y)} \left(\frac{\delta V}{\delta \phi(x)} \eta(x)\right) = \frac{\delta^2 V}{\delta \phi(y)\delta \phi(x)} \eta(x) + \frac{\delta V}{\delta \phi(x)} \frac{\delta \eta(x)}{\delta \phi(y)}
$$

Since $\eta(x)$ is a fixed generator (independent of $\phi$), we have $\frac{\delta \eta(x)}{\delta \phi(y)} = 0$.

Therefore:

$$
\int dx \, \frac{\delta^2 V}{\delta \phi(y)\delta \phi(x)} \eta(x) = 0
$$

**Step 4: Evaluate at the Minimum**

At the symmetry-broken minimum $\phi_0$, we have $\frac{\delta V}{\delta \phi}|_{\phi_0} = 0$. Define the **mass kernel**:

$$
M(y,x) = \frac{\delta^2 V}{\delta \phi(y)\delta \phi(x)}\bigg|_{\phi_0}
$$

Then the equation becomes:

$$
\int dx \, M(y,x) \eta(x) = 0
$$

**Step 5: Local Theory Simplification**

For a local theory, the potential has the form:

$$
V[\phi] = \int dy \, \mathcal{V}(\phi(y), \nabla\phi(y))
$$

The second functional derivative gives (after integration by parts):

$$
M(y,x) = \left[\frac{\partial^2 \mathcal{V}}{\partial \phi^2} - \nabla^2\frac{\partial^2 \mathcal{V}}{\partial(\nabla\phi)^2}\right]_{\phi_0} \delta(y-x)
$$

For a uniform background $\phi(x) = \phi_0$, spatial derivatives vanish, and this simplifies to:

$$
M(y,x) = m^2 \delta(y-x)
$$

where $m^2 = \frac{\partial^2 \mathcal{V}}{\partial \phi^2}|_{\phi_0}$ is the mass squared.

**Step 6: The Massless Mode**

Substituting the diagonal form into the integral equation:

$$
\int dx \, m^2 \delta(y-x) \eta(x) = m^2 \eta(y) = 0
$$

Since the symmetry is broken, the generator $\eta(y) \neq 0$ (the ground state is not invariant under the transformation). Therefore:

$$
m^2 = 0
$$

**Conclusion:** The mass matrix has a zero eigenvalue with eigenvector $\eta$. This is the Goldstone mode.

**Why $\eta \neq 0$ for Broken Symmetry?**

If $\eta = 0$, then the ground state $\phi_0$ would be invariant under the symmetry transformation ($\phi_0 \rightarrow \phi_0 + \epsilon \cdot 0 = \phi_0$). This is the **unbroken** case. For **broken** symmetry, $\phi_0$ changes under the transformation, so $\eta \neq 0$.

### 2.6 Physical Examples of Goldstone Modes

**2.6.1 Phonons in Solids (Broken Translation Symmetry)**

A crystal spontaneously breaks continuous translational symmetry—the atoms sit at fixed lattice positions rather than being uniformly distributed.

- **Order parameter:** The displacement field $\mathbf{u}(\mathbf{r})$ from lattice positions
- **Broken symmetry:** Continuous translation $\mathbf{r} \rightarrow \mathbf{r} + \mathbf{a}$
- **Goldstone mode:** **Phonons** (lattice vibrations)

**Why gapless?** A uniform translation of the entire crystal (all atoms move together by the same amount) costs **zero energy** because the Hamiltonian is translationally invariant. This corresponds to the $\mathbf{k} = 0$ phonon mode with $\omega \rightarrow 0$.

**2.6.2 Magnons in Ferromagnets (Broken Rotation Symmetry)**

In a ferromagnet below the Curie temperature, spins align along a specific direction (e.g., the $z$-axis).

- **Order parameter:** Magnetization $\mathbf{M}$ (average spin direction)
- **Broken symmetry:** Spin rotation symmetry
- **Goldstone mode:** **Magnons** (spin waves)

**Magnetization Basics:**
- Each atom has a magnetic moment (spin) like a tiny bar magnet
- In a ferromagnet, these moments align parallel to each other
- The macroscopic magnetization $\mathbf{M}$ is the vector sum of all atomic moments

**Why spin precession?** In a magnon, spins tilt away from the $z$-axis and precess around it (like a spinning top precessing in a gravitational field). Neighboring spins precess with a phase shift, creating a wave pattern.

**Dispersion:** Magnons have $\omega \propto k^2$ at long wavelengths (quadratic dispersion, unlike phonons which are linear).

**2.6.3 Superconductivity and the Anderson-Higgs Mechanism**

In a superconductor, electrons form Cooper pairs. The order parameter is the pair wavefunction:

$$
\psi(\mathbf{r}) = \langle \hat{\psi}_\uparrow(\mathbf{r})\hat{\psi}_\downarrow(\mathbf{r})\rangle = \vert\psi\vert e^{i\theta(\mathbf{r})}
$$

- **Broken symmetry:** $U(1)$ phase symmetry (charge conservation)
- **Expected Goldstone mode:** Phase fluctuations $\theta(\mathbf{r})$

**The Anderson-Higgs Mechanism:**

In a **neutral** superfluid, the phase mode is indeed gapless (Goldstone mode).

However, in a **charged** superconductor:
- The phase $\theta$ is coupled to the electromagnetic field
- The photon acquires mass inside the superconductor (Meissner effect)
- This "gives mass to" (or "gaps out") the would-be Goldstone mode

**"Gap Out" = "Give Mass" Explanation:**

In particle/condensed matter physics:
- **Massless mode:** Energy $E = \hbar\omega \propto k$ vanishes as momentum $k \rightarrow 0$
- **Massive mode (gapped):** Energy $E \rightarrow \Delta > 0$ as $k \rightarrow 0$

The gap $\Delta$ is like a mass: you need a minimum energy $\Delta$ to excite the mode. In a charged superconductor, the Coulomb interaction turns the massless phase mode into a massive plasmon mode with energy gap $\omega_p$ (plasma frequency).

---

## Part III: Order Parameters and Phase Transitions

### 3.1 The Order Parameter Concept

**What is an Order Parameter?**

An **order parameter** is a quantity that:
1. Is **zero** in the high-temperature, high-symmetry (disordered) phase
2. Is **non-zero** in the low-temperature, low-symmetry (ordered) phase
3. **Tracks** the broken symmetry

**Historical Origin:**

The concept was introduced by Landau in the 1930s to describe phase transitions. The key insight is that near a phase transition, there's typically a "soft mode" that becomes unstable, and the order parameter characterizes the new state that emerges.

**Why "Ordered = Low Symmetry"?**

This seems counterintuitive! In everyday language, "ordered" usually means "symmetric." But in physics:

- **High symmetry:** Many equivalent configurations (high entropy)
- **Low symmetry:** Specific configuration selected (low entropy)

A crystal is "ordered" (atoms at fixed positions) but has **lower** translational symmetry than a liquid (atoms anywhere).

**How to Identify the Order Parameter:**

1. Find the symmetry of the Hamiltonian
2. Identify a quantity that transforms non-trivially under that symmetry
3. Check that this quantity is zero in the high-temperature phase and non-zero in the low-temperature phase

**Examples Table**

| System | Order Parameter | Broken Symmetry |
|--------|----------------|-----------------|
| Ferromagnet | Magnetization $\mathbf{M} = \langle\sum_i \mathbf{S}_i\rangle/V$ | Rotational |
| Crystal | Displacement $\mathbf{u}(\mathbf{r})$ from lattice | Translational |
| Superconductor | Pair amplitude $\langle\hat{\psi}_\uparrow\hat{\psi}_\downarrow\rangle$ | $U(1)$ phase |
| Superfluid | BEC order parameter $\langle\hat{\psi}\rangle$ | $U(1)$ phase |
| Nematic liquid crystal | Director $\mathbf{n}$ (average molecular orientation) | Rotational |

**Note on Notation:** The angle brackets $\langle\cdots\rangle$ denote thermal or quantum expectation value. For superconductors and superfluids, the order parameter involves expectation values of field operators (Cooper pair or boson annihilation operators, denoted by $\hat{\psi}$ with a hat to indicate they are operators).

### 3.2 Landau Theory of Phase Transitions

**What is a Phase Transition?**

A phase transition is a sharp change in the properties of a system as a parameter (usually temperature) is varied.

- **First-order:** Discontinuous change (e.g., liquid-gas at boiling point)
- **Continuous (second-order):** Gradual change with diverging correlation length (e.g., ferromagnetic transition)

**Free Energy in Thermodynamics**

In thermodynamics, the **Helmholtz free energy** $F$ is defined as:

$$
F = U - TS
$$

where:
- $U$ is the internal energy
- $T$ is the temperature
- $S$ is the entropy

**Physical meaning:** $F$ represents the energy available to do work at constant temperature. Systems naturally evolve to minimize $F$, not just $U$, because increasing entropy also lowers $F$.

**Landau's Brilliant Insight**

Near a continuous phase transition, Landau proposed that the free energy can be expanded as a power series in the order parameter $M$ (e.g., magnetization):

$$
F(M) = F_0 + \frac{1}{2}\alpha(T) M^2 + \frac{1}{4}\gamma M^4
$$

where:
- $\alpha(T) = \alpha_0(T - T_c)$ changes sign at critical temperature $T_c$
- $\gamma > 0$ ensures stability (prevents $F$ from going to $-\infty$)

**Why This Form?**

1. **Symmetry:** For an Ising magnet (up/down symmetry), $F$ must be even in $M$, so only even powers appear
2. **Analyticity:** Landau assumed $F$ is an analytic function of $M$ near the transition
3. **Truncation:** Higher-order terms ($M^6$, etc.) are negligible near the transition

**Finding the Minimum**

To find the equilibrium state, minimize $F$ with respect to $M$:

$$
\frac{\partial F}{\partial M} = \alpha M + \gamma M^3 = 0
$$

Solutions:
- $M = 0$ (high temperature, $T > T_c$, where $\alpha > 0$)
- $M = \pm\sqrt{-\alpha/\gamma} = \pm\sqrt{\alpha_0(T_c-T)/\gamma}$ (low temperature, $T < T_c$)

**Critical Behavior Derivation**

Near $T_c$ from below ($T < T_c$):

$$
M = \sqrt{\frac{\alpha_0(T_c - T)}{\gamma}} = \sqrt{\frac{\alpha_0}{\gamma}} (T_c - T)^{1/2}
$$

So we can write:

$$
M \propto (T_c - T)^{\beta}
$$

with the **critical exponent** $\beta = 1/2$ in mean-field theory.

**Physical Interpretation:**

- At $T = T_c$, the magnetization turns on continuously
- Near $T_c$, $M$ grows slowly as $\sqrt{T_c - T}$
- The exponent $\beta$ characterizes how "sharp" the transition is

**Domains and the Concept of Metastability**

In a real ferromagnet below $T_c$:
- Different regions (**domains**) have magnetization pointing in different directions
- Macroscopically, the net magnetization may be zero (equal numbers of up and down domains)

**Why Domains Form?**

The system globally wants to minimize energy, but:
1. Defects and impurities in the crystal structure create "pinning sites"
2. Domain walls get trapped at these sites
3. The system gets stuck in **metastable states** (local minima of free energy, not global minimum)

**Metastable State:** A state that is locally stable (small perturbations return to it) but not globally stable (there exists a lower energy state). A domain configuration is metastable because moving a domain wall costs energy (it must overcome the pinning potential).

**Hysteresis and the Barkhausen Effect**

When an external magnetic field $H$ is applied:
- The field exerts a force on domain walls
- At weak fields, walls stay pinned
- At a critical field, a wall "de-pins" and moves rapidly

**Discontinuous Jumps (Barkhausen Effect):**

As the external field is slowly varied:
1. Domain walls remain pinned for a range of field values
2. Suddenly, at a threshold field, a wall breaks free and moves
3. This causes a sudden, discontinuous change (jump) in the total magnetization
4. These jumps produce tiny voltage pulses in a pickup coil—the **Barkhausen noise**

**Hysteresis:**

The magnetization curve $M(H)$ shows **hysteresis**—the path depends on history:
- When increasing $H$, de-pinning occurs at certain threshold fields
- When decreasing $H$, different domains de-pin at different fields
- The result is a loop in the $M$-$H$ curve

**Key Features of Hysteresis:**
- **Remanence:** $M \neq 0$ when $H = 0$ (magnetization persists after field removal)
- **Coercivity:** The field needed to reduce $M$ to zero
- **Saturation:** At high fields, all domains align and $M$ saturates

**Summary Table**

| Concept | Explanation |
|---------|-------------|
| **Metastable state** | Local free energy minimum, not global |
| **Domain wall pinning** | Defects trap domain walls |
| **Barkhausen effect** | Sudden jumps in magnetization as walls de-pin |
| **Hysteresis** | Path-dependent magnetization due to pinning |

---

## Summary and Key Takeaways

### Functional Calculus

| Concept | Formula/Key Point |
|---------|-------------------|
| Functional derivative | $\frac{\delta F}{\delta f(x_0)} = \lim_{\epsilon\to 0}\frac{F[f+\epsilon\delta_{x_0}]-F[f]}{\epsilon}$ |
| Use $\delta/\delta\phi(x)$ when | The object depends on the entire function $\phi(x)$ |
| Use $\partial/\partial\phi$ when | The object depends on $\phi$ at a single point (density) |
| For uniform fields | $\frac{\delta F}{\delta\phi(x)}\big\vert_{\text{uniform}} = \frac{\partial\mathcal{L}}{\partial\phi}$ (numerical equality) |
| Important identity | $\frac{\delta f(x)}{\delta f(y)} = \delta(x-y)$ |

### Spontaneous Symmetry Breaking

| Concept | Explanation |
|---------|-------------|
| **Definition** | Ground state has less symmetry than Hamiltonian |
| **Goldstone Theorem** | Broken continuous symmetry $\Rightarrow$ massless mode |
| **Mexican Hat Potential** | $V = -\alpha\vert\phi\vert^2 + \gamma\vert\phi\vert^4$ with circular minimum |
| **Order Parameter** | Non-zero in ordered phase, zero in disordered phase; identifies the broken symmetry |
| **Landau Theory** | Free energy expansion near $T_c$: $F = F_0 + \frac{1}{2}\alpha(T-T_c)M^2 + \frac{1}{4}\gamma M^4$ |
| **Critical Exponent** | $M \propto (T_c-T)^{\beta}$ with $\beta = 1/2$ (mean field) |
| **Higgs vs Goldstone** | Amplitude mode ($h$) is massive; Phase mode ($\pi$) is massless (unless gapped by Anderson-Higgs) |

### Physical Realizations

| System | Broken Symmetry | Goldstone Mode |
|--------|----------------|----------------|
| Crystal | Translation | Phonons (gapless) |
| Ferromagnet | Rotation | Magnons (gapless) |
| Superfluid | $U(1)$ phase | Phonon (gapless) |
| Superconductor | $U(1)$ phase | Gapped (Anderson-Higgs mechanism) |

The interplay between symmetry, functional methods, and collective excitations forms the foundation of modern condensed matter physics.
