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

**Step 1: Evaluate at uniform field $\phi(x) = \phi_0$**

When we substitute the constant field $\phi_0$:
- The partial derivative $\frac{\partial \mathcal{L}}{\partial \phi}$ is evaluated at $(\phi, \nabla\phi) = (\phi_0, 0)$
- Since $\nabla\phi = 0$ everywhere, the derivative term becomes a **constant number** (independent of $x$)

**Step 2: The gradient term vanishes**

The second term involves $\frac{\partial \mathcal{L}}{\partial(\nabla\phi)}(x)$. For a uniform field:
- $\nabla\phi(x) = 0$ (constant field has no spatial variation)
- Therefore $\frac{\partial \mathcal{L}}{\partial(\nabla\phi)}$ is evaluated at zero field gradient
- The divergence of a constant (or zero) is zero: $\nabla_x \cdot [\text{constant}] = 0$

**Step 3: The equality**

Combining these results:

$$
\left.\frac{\delta F}{\delta \phi(x)}\right|_{\phi(x)=\phi_0} = \frac{\partial \mathcal{L}}{\partial \phi}(\phi_0, 0) - 0 = \frac{\partial \mathcal{L}}{\partial \phi}(\phi_0, 0)
$$

The right-hand side $\left.\frac{\partial \mathcal{L}}{\partial \phi}\right|_{\phi=\phi_0}$ means:
1. Take the function $\mathcal{L}(\phi, \nabla\phi)$ 
2. Compute its partial derivative with respect to the variable $\phi$
3. Evaluate at the point where the field value is $\phi_0$ and field gradient is $0$

This gives exactly $\frac{\partial \mathcal{L}}{\partial \phi}(\phi_0, 0)$, proving the equality.

**Clarifying the Notation Confusion**

| Symbol | Meaning | Evaluated at uniform field |
|--------|---------|---------------------------|
| $\frac{\delta F}{\delta \phi(x)}$ | Functional derivative (function of $x$) | Becomes constant: $\frac{\partial \mathcal{L}}{\partial \phi}(\phi_0, 0)$ |
| $\frac{\partial \mathcal{L}}{\partial \phi}$ | Partial derivative of density (function of $\phi, \nabla\phi$) | Evaluated to number: $\frac{\partial \mathcal{L}}{\partial \phi}(\phi_0, 0)$ |

Both sides yield the same **numerical value** after evaluation, but they reach it through different paths:
- LHS: Take functional derivative first (getting a function), then substitute uniform field
- RHS: Take partial derivative of density, then evaluate at the point $(\phi_0, 0)$

**Key Takeaway:**

This equality is why physicists often mix notation—but it **only holds for uniform configurations**! For non-uniform fields, the gradient term $\nabla \cdot \frac{\partial \mathcal{L}}{\partial(\nabla\phi)}$ contributes, and the functional derivative differs from the ordinary partial derivative.

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

Imagine a perfectly symmetrical pencil balanced on its tip. Let's write down the physics explicitly.

**The Lagrangian**

For a rigid rod of mass $m$ and length $l$, pivoted at one end (on a horizontal table), the Lagrangian in spherical coordinates $(\theta, \phi)$ is:

$$
L = \frac{1}{2}I\dot{\theta}^2 + \frac{1}{2}I\sin^2\theta \, \dot{\phi}^2 + mgl\cos\theta
$$

where:
- $I = \frac{1}{3}ml^2$ is the moment of inertia about the pivot
- $\theta$ is the polar angle measured from the **vertical upward direction** ($\theta = 0$ is balanced upright on its tip)
- $\phi$ is the azimuthal angle in the horizontal plane (specifies which way the pencil falls)
- The potential $V = -mgl\cos\theta$ comes from gravity (center of mass height is $h = \frac{l}{2}\cos\theta$)

**Note:** We use $+mgl\cos\theta$ in $L = T - V$, so $V = -mgl\cos\theta$ means the Lagrangian contains $+mgl\cos\theta$.

**Symmetry Analysis**

Notice that $L$ does **not** depend on $\phi$ explicitly:

$$
\frac{\partial L}{\partial \phi} = 0
$$

This means $L$ is invariant under rotations about the vertical axis:

$$
\phi \rightarrow \phi + \alpha \quad \text{(for any constant } \alpha\text{)}
$$

By Noether's theorem, the conjugate momentum $p_\phi = \partial L/\partial\dot{\phi} = I\sin^2\theta \, \dot{\phi}$ is conserved.

**The Equilibrium States**

The potential $V(\theta) = -mgl\cos\theta$ has:
- **Maximum** at $\theta = 0$ ($\cos\theta = 1$, upright position, unstable equilibrium)
- **Minimum** at $\theta = \pi/2$ ($\cos\theta = 0$, rod lying horizontally on the table, stable equilibrium)

*Physical interpretation:*
- $\theta = 0$: Pencil balanced upright on its tip (unstable, maximum potential energy)
- $\theta = \pi/2$: Pencil has fallen and lies flat on the table (stable, minimum potential energy)

For the **fallen state** at $\theta = \pi/2$:
- The rod lies in a specific direction in the $xy$-plane: $(\theta = \pi/2, \phi = \phi_0)$
- The value of $\phi_0$ is arbitrary—any horizontal direction (north, east, south, west...) is equivalent
- But the pencil must pick **one specific** $\phi_0$ when it falls

**Symmetry Breaking**

The **Hamiltonian** $H = \frac{p_\theta^2}{2I} + \frac{p_\phi^2}{2I\sin^2\theta} - mgl\cos\theta$ is invariant under $\phi \rightarrow \phi + \alpha$.

However, the **ground state** $|\theta = \pi/2, \phi = \phi_0\rangle$ is **not** invariant:

$$
e^{i\alpha p_\phi/\hbar}|\theta = \pi/2, \phi = \phi_0\rangle = |\theta = \pi/2, \phi = \phi_0 + \alpha\rangle \neq |\theta = \pi/2, \phi = \phi_0\rangle
$$

The ground state is transformed into a **different** ground state (pointing in a different direction). This is spontaneous symmetry breaking.

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

**Important Distinction: Field Operator vs. Vacuum Expectation Value**

In quantum field theory, $\phi(x)$ is an **operator** that acts on the quantum state. The **vacuum expectation value (VEV)** is:

$$
\langle\phi\rangle \equiv \langle 0|\phi(x)|0\rangle
$$

where $|0\rangle$ is the ground state (vacuum).

**Key differences:**

| Quantity | Type | Description |
|----------|------|-------------|
| $\phi(x)$ | Field operator | Acts on states; has fluctuations; $\phi(x)\vert 0\rangle \neq 0$ even if $\langle\phi\rangle = 0$ |
| $\langle\phi\rangle$ | Number (c-number) | Classical background value; determines symmetry breaking |

**Why VEV $\neq$ 0 Implies Symmetry Breaking**

Under a symmetry transformation $U$:
- The field transforms: $\phi \rightarrow U\phi U^{-1}$
- The vacuum transforms: $|0\rangle \rightarrow U|0\rangle$

If the vacuum is **symmetric** (invariant):

$$
U|0\rangle = |0\rangle \quad \Rightarrow \quad \langle\phi\rangle = \langle 0|U^{-1}\phi U|0\rangle = \langle 0|\phi|0\rangle
$$

This is consistent with any $\langle\phi\rangle$ **only if** $\langle\phi\rangle = 0$ (or transforms as a singlet).

For our complex scalar field with $U(1)$ symmetry $\phi \rightarrow e^{i\alpha}\phi$:

$$
\text{If } \langle\phi\rangle = v \neq 0: \quad \langle\phi\rangle \rightarrow e^{i\alpha}v \neq v
$$

The VEV is **not invariant** even though the Hamiltonian is. This is spontaneous symmetry breaking.

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

**The Pinning Mechanism: A Detailed Picture**

**Domain Wall Energy:**

A domain wall is a transition region where magnetization rotates from one direction to another. The wall has an **energy per unit area** $\sigma_w$ (wall tension) because spins in the wall are not aligned with the easy axis, costing anisotropy energy.

**Defects as Pinning Centers:**

Real crystals have imperfections:
- **Vacancies:** Missing atoms disrupt the exchange interaction
- **Dislocations:** Line defects where the crystal lattice is distorted
- **Impurity atoms:** Foreign atoms with different magnetic moments
- **Grain boundaries:** Interfaces between crystal regions with different orientations

**Why Domain Walls Get Trapped:**

Near a defect, the magnetic properties change:
1. **Exchange interaction** $J$ is weakened or altered
2. **Anisotropy energy** $K$ (energy cost of deviating from easy axis) changes
3. The domain wall **energy density** $\sigma_w(\mathbf{r})$ becomes position-dependent

A domain wall is attracted to locations where $\sigma_w$ is **minimized**—typically near defects where the magnetic order is already disrupted. This creates a **pinning potential** $V_{pin}(x)$ for the wall.

**The Pinning Potential:**

Imagine a domain wall at position $x$. The pinning potential might look like:

$$
V_{pin}(x) = -V_0 \sum_i \exp\left(-\frac{(x - x_i)^2}{2\xi^2}\right)
$$

where $x_i$ are defect positions and $\xi$ is the defect interaction range.

**Metastable State:** A state that is locally stable (small perturbations return to it) but not globally stable (there exists a lower energy state). A domain configuration is metastable because moving a domain wall costs energy—it must overcome the pinning potential barrier.

**Hysteresis and the Barkhausen Effect**

**The Role of External Magnetic Field:**

When an external field $H$ is applied along, say, the $+z$ direction:
- Domains with $M_z > 0$ have lower energy: $E = -\mathbf{M} \cdot \mathbf{H} = -MH\cos\theta$
- Domains with $M_z < 0$ have higher energy
- The field creates a **pressure** on domain walls to expand the favorable domains

**Force on a Domain Wall:**

The magnetic field exerts a **pressure** (force per unit area) on the wall:

$$
P = 2MH
$$

This pressure tries to push the wall in the direction that expands the lower-energy domain.

**De-pinning Process:**

1. **Weak field:** $P < \text{max}|\nabla V_{pin}|$ — wall stays trapped (pinned)
2. **Critical field:** $P \approx \text{max}|\nabla V_{pin}|$ — wall is at the threshold
3. **Above critical:** Wall breaks free and moves rapidly to the next pinning site

**Discontinuous Jumps (Barkhausen Effect):**

As the external field is slowly varied:
1. Domain walls remain pinned for a range of field values
2. Suddenly, at a threshold field, a wall breaks free and moves rapidly
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

## Appendix B: Advanced Functional Variation Examples

For readers who want to deepen their understanding of functional calculus, here are several advanced examples from quantum field theory and condensed matter physics.

### B.1 Quantum Electrodynamics (QED)

**The QED Action**

The QED action couples the Dirac field $\psi$ to the electromagnetic field $A_\mu$:

$$
S[\bar{\psi}, \psi, A_\mu] = \int d^4x \left[\bar{\psi}(i\gamma^\mu D_\mu - m)\psi - \frac{1}{4}F_{\mu\nu}F^{\mu\nu}\right]
$$

where:
- $D_\mu = \partial_\mu + ieA_\mu$ is the covariant derivative
- $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is the field strength
- $\gamma^\mu$ are Dirac matrices

**Step-by-Step Variation with respect to $\bar{\psi}$**

**Step 1:** Identify the relevant part of the action:

$$
S_{\text{Dirac}} = \int d^4x \, \bar{\psi}(x)(i\gamma^\mu D_\mu - m)\psi(x)
$$

**Step 2:** Introduce a variation:

$$
\bar{\psi}(x) \rightarrow \bar{\psi}(x) + \delta\bar{\psi}(x)
$$

**Step 3:** Compute the change in the action:

$$
\delta S = S[\bar{\psi} + \delta\bar{\psi}] - S[\bar{\psi}] = \int d^4x \, \delta\bar{\psi}(x)(i\gamma^\mu D_\mu - m)\psi(x)
$$

**Step 4:** Apply the functional derivative definition:

By definition, $\delta S = \int d^4x \, \frac{\delta S}{\delta\bar{\psi}(x)}\delta\bar{\psi}(x)$.

Comparing with our result:

$$
\frac{\delta S}{\delta \bar{\psi}(x)} = (i\gamma^\mu D_\mu - m)\psi(x)
$$

**Step 5:** Stationary condition:

Setting $\frac{\delta S}{\delta\bar{\psi}} = 0$ gives the **Dirac equation in an electromagnetic field**:

$$
(i\gamma^\mu D_\mu - m)\psi = 0
$$

Expanding $D_\mu = \partial_\mu + ieA_\mu$:

$$
(i\gamma^\mu\partial_\mu - e\gamma^\mu A_\mu - m)\psi = 0
$$

This describes a relativistic spin-1/2 particle interacting with the electromagnetic field.

---

**Step-by-Step Variation with respect to $A_\nu$**

**Step 1:** Split the action into fermion and gauge parts:

$$
S = \underbrace{\int d^4x \, \bar{\psi}(i\gamma^\mu\partial_\mu - m)\psi}_{S_{\text{free}}} + \underbrace{\int d^4x \, e\bar{\psi}\gamma^\mu A_\mu\psi}_{S_{\text{int}}} - \underbrace{\int d^4x \, \frac{1}{4}F_{\mu\nu}F^{\mu\nu}}_{S_{\text{Maxwell}}}
$$

**Step 2:** Vary $A_\nu \rightarrow A_\nu + \delta A_\nu$.

For the interaction term:

$$
\delta S_{\text{int}} = \int d^4x \, e\bar{\psi}\gamma^\mu\psi \, \delta A_\mu(x) = \int d^4x \, j^\mu(x)\delta A_\mu(x)
$$

where $j^\mu = e\bar{\psi}\gamma^\mu\psi$.

**Step 3:** Vary the Maxwell term.

First, note that $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, so:

$$
\delta F_{\mu\nu} = \partial_\mu(\delta A_\nu) - \partial_\nu(\delta A_\mu)
$$

Then:

$$
\delta(F_{\mu\nu}F^{\mu\nu}) = 2F^{\mu\nu}\delta F_{\mu\nu} = 2F^{\mu\nu}(\partial_\mu\delta A_\nu - \partial_\nu\delta A_\mu) = 4F^{\mu\nu}\partial_\mu\delta A_\nu
$$

(using antisymmetry $F^{\mu\nu} = -F^{\nu\mu}$)

**Step 4:** Integrate by parts:

$$
\delta S_{\text{Maxwell}} = -\frac{1}{4}\int d^4x \, 4F^{\mu\nu}\partial_\mu\delta A_\nu = \int d^4x \, (\partial_\mu F^{\mu\nu})\delta A_\nu
$$

(assuming boundary terms vanish).

**Step 5:** Combine results:

$$
\delta S = \int d^4x \, \left[j^\nu(x) + \partial_\mu F^{\mu\nu}(x)\right]\delta A_\nu(x)
$$

Therefore:

$$
\frac{\delta S}{\delta A_\nu(x)} = j^\nu(x) + \partial_\mu F^{\mu\nu}(x) = e\bar{\psi}\gamma^\nu\psi + \partial_\mu F^{\mu\nu}
$$

**Step 6:** Stationary condition gives Maxwell's equations:

$$
\partial_\mu F^{\mu\nu} = -j^\nu = -e\bar{\psi}\gamma^\nu\psi
$$

This is $\partial_\mu F^{\mu\nu} = -j^\nu$, which in 3-vector notation gives:
- $\nabla \cdot \mathbf{E} = \rho$ (Gauss's law)
- $\nabla \times \mathbf{B} - \partial_t\mathbf{E} = \mathbf{j}$ (Ampère-Maxwell law)

### B.2 Quantum Chromodynamics (QCD) — Non-Abelian Gauge Theory

**The QCD Action**

QCD describes quarks interacting via gluons. The gluon field $A_\mu^a$ carries a color index $a = 1, ..., 8$ (for SU(3) gauge group):

$$
S = \int d^4x \left[\bar{\psi}_i(i\gamma^\mu D_\mu^{ij} - m\delta^{ij})\psi_j - \frac{1}{4}F_{\mu\nu}^a F^{\mu\nu}_a\right]
$$

**Key difference from QED:** The covariant derivative and field strength are **non-commuting** (non-Abelian):

$$
D_\mu^{ij} = \partial_\mu\delta^{ij} + igA_\mu^a (T^a)^{ij}
$$

$$
F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c
$$

where $T^a$ are Gell-Mann matrices (generators of SU(3)) and $f^{abc}$ are structure constants.

**The Challenge:** The field strength contains **quadratic terms** $A_\mu^b A_\nu^c$, leading to **three-gluon and four-gluon self-interactions** that have no analogue in QED.

**Step-by-Step Variation — Yang-Mills Equations**

**Step 1:** Write the QCD action separating matter and gauge parts:

$$
S = \int d^4x \, \bar{\psi}_i(i\gamma^\mu D_\mu^{ij} - m\delta^{ij})\psi_j - \frac{1}{4}\int d^4x \, F_{\mu\nu}^a F^{\mu\nu}_a
$$

**Step 2:** Variation of the matter term with respect to $A_\nu^b$.

The covariant derivative is $D_\mu^{ij} = \partial_\mu\delta^{ij} + igA_\mu^a (T^a)^{ij}$. Varying:

$$
\delta D_\mu^{ij} = ig\delta A_\mu^a (T^a)^{ij}
$$

So the variation of the matter action is:

$$
\delta S_{\text{matter}} = \int d^4x \, \bar{\psi}_i(i\gamma^\mu)(ig\delta A_\mu^a T^a)^{ij}\psi_j = -\int d^4x \, g\bar{\psi}_i\gamma^\mu(T^a)^{ij}\psi_j \delta A_\mu^a
$$

Define the **color current**:

$$
j^{\mu,a} = g\bar{\psi}\gamma^\mu T^a\psi
$$

**Step 3:** Variation of the gauge field term.

This is more complex than QED because $F_{\mu\nu}^a$ contains quadratic terms:

$$
F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c
$$

The variation is:

$$
\delta F_{\mu\nu}^a = \partial_\mu(\delta A_\nu^a) - \partial_\nu(\delta A_\mu^a) + gf^{abc}[\delta A_\mu^b A_\nu^c + A_\mu^b \delta A_\nu^c]
$$

**Step 4:** Compute $\delta(F_{\mu\nu}^a F^{\mu\nu}_a) = 2F^{\mu\nu}_a \delta F_{\mu\nu}^a$.

After careful algebra and integration by parts (see textbooks for detailed steps):

$$
\delta S_{\text{gauge}} = \int d^4x \, (D_\mu F^{\mu\nu})_a \delta A_\nu^a
$$

where $(D_\mu F^{\mu\nu})_a = \partial_\mu F^{\mu\nu}_a + gf_{abc}A_\mu^b F^{\mu\nu}_c$ is the **covariant divergence**.

**Step 5:** Combine variations:

$$
\frac{\delta S}{\delta A_\nu^b(x)} = -j^{\nu,b}(x) + (D_\mu F^{\mu\nu})_b(x) = 0
$$

This gives the **Yang-Mills equations**:

$$
(D_\mu F^{\mu\nu})^a = g\bar{\psi}\gamma^\nu T^a\psi = j^{\nu,a}
$$

**Physical Significance:**
- Unlike QED ($\partial_\mu F^{\mu\nu} = j^\nu$), the left side has covariant derivative
- This reflects that gluons themselves carry color charge (they contribute to the current)
- The non-linear terms lead to **asymptotic freedom** (weak at high energy) and **confinement** (strong at low energy)

### B.3 Electroweak Theory (Spontaneously Broken Gauge Theory)

**The Higgs Mechanism**

The electroweak Lagrangian combines QED-like and weak interactions. The key is the Higgs doublet $\Phi$:

$$
\mathcal{L}_{\text{Higgs}} = (D_\mu\Phi)^\dagger(D^\mu\Phi) - V(\Phi)
$$

with the "Mexican hat" potential:

$$
V(\Phi) = -\mu^2|\Phi|^2 + \lambda|\Phi|^4
$$

**Spontaneous Symmetry Breaking:**

The minimum of $V$ is at $|\Phi| = v/\sqrt{2} = \sqrt{\mu^2/(2\lambda)}$. Choose the vacuum:

$$
\langle\Phi\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ v \end{pmatrix}
$$

**Step-by-Step Expansion and Mass Generation**

**Step 1:** Parameterize fluctuations around the vacuum:

$$
\Phi(x) = \frac{1}{\sqrt{2}}\begin{pmatrix} \phi_1(x) + i\phi_2(x) \\ v + h(x) + i\phi_3(x) \end{pmatrix} = \frac{1}{\sqrt{2}}\exp\left(i\frac{\phi_a\tau^a}{v}\right)\begin{pmatrix} 0 \\ v + h \end{pmatrix}
$$

where $\tau^a$ are Pauli matrices and $\phi_1, \phi_2, \phi_3$ are Goldstone fields.

**Step 2:** The covariant derivative in electroweak theory is:

$$
D_\mu = \partial_\mu - ig\frac{\tau^a}{2}W_\mu^a - ig'\frac{Y}{2}B_\mu
$$

where:
- $W_\mu^a$ ($a = 1,2,3$) are SU(2)$_L$ gauge fields
- $B_\mu$ is U(1)$_Y$ gauge field
- $g$ and $g'$ are respective couplings
- $Y = 1$ is the hypercharge of the Higgs doublet

**Step 3:** Compute the kinetic term $(D_\mu\Phi)^\dagger(D^\mu\Phi)$.

Focus on the vacuum contribution (constant $v$):

$$
D_\mu\langle\Phi\rangle = -\frac{igv}{2\sqrt{2}}\begin{pmatrix} W_\mu^1 - iW_\mu^2 \\ -W_\mu^3 + \frac{g'}{g}B_\mu \end{pmatrix}
$$

Therefore:

$$
|D_\mu\langle\Phi\rangle|^2 = \frac{g^2v^2}{4}W_\mu^+ W^{-\mu} + \frac{g^2v^2}{8\cos^2\theta_W}Z_\mu Z^\mu + 0 \cdot A_\mu A^\mu
$$

where we've defined:
- $W_\mu^\pm = (W_\mu^1 \mp iW_\mu^2)/\sqrt{2}$ (charged weak bosons)
- $Z_\mu = \cos\theta_W W_\mu^3 - \sin\theta_W B_\mu$ (neutral weak boson)
- $A_\mu = \sin\theta_W W_\mu^3 + \cos\theta_W B_\mu$ (photon)
- $\tan\theta_W = g'/g$ (Weinberg angle)

**Step 4: Read off the masses**

Comparing with the Proca Lagrangian $\mathcal{L} = \frac{1}{2}M^2 A_\mu A^\mu$:

$$
M_W = \frac{gv}{2}, \quad M_Z = \frac{gv}{2\cos\theta_W} = \frac{M_W}{\cos\theta_W}
$$

The photon $A_\mu$ remains massless (unbroken U(1)$_{\text{em}}$).

**Step 5: Goldstone boson "eating"**

The three fields $\phi_1, \phi_2, \phi_3$ mix with the gauge fields. They become the **longitudinal polarizations** of the massive $W^\pm$ and $Z$ bosons. This is the **Higgs mechanism** — gauge bosons acquire mass by "eating" Goldstone bosons.

**Functional Variation after SSB:**

After shifting $\Phi \rightarrow \langle\Phi\rangle + \text{fluctuations}$, the functional derivatives give:
- **Massive $W^\pm$ and $Z$ bosons** (3 polarizations each)
- **Massless photon** (2 polarizations) — the unbroken U(1)$_{\text{em}}$
- **Massive Higgs boson** $h$ with $M_h = \sqrt{2\mu^2}$
- Three "eaten" Goldstone bosons ($\phi_1, \phi_2, \phi_3$) become the longitudinal polarizations of $W$ and $Z$

### B.4 Density Functional Theory (DFT) — Condensed Matter

**The Universal Density Functional**

In DFT, the ground state energy is a functional of the electron density $n(\mathbf{r})$:

$$
E[n] = T_s[n] + \int d^3r \, n(\mathbf{r})V_{ext}(\mathbf{r}) + E_H[n] + E_{xc}[n]
$$

where:
- $T_s[n]$: Kinetic energy of non-interacting electrons
- $V_{ext}$: External potential (ion cores)
- $E_H[n] = \frac{e^2}{2}\int d^3r d^3r' \frac{n(\mathbf{r})n(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}$: Hartree (classical electrostatic) energy
- $E_{xc}[n]$: Exchange-correlation energy (quantum effects beyond mean-field)

**The Hohenberg-Kohn Theorem and Constrained Minimization**

The ground state density $n_0(\mathbf{r})$ minimizes $E[n]$ subject to the constraint:

$$
\int d^3r \, n(\mathbf{r}) = N \quad \text{(fixed particle number)}
$$

**Mathematical Problem:** Minimize $E[n]$ subject to $C[n] = \int n(\mathbf{r})d^3r - N = 0$.

---

### Supplement: Lagrange Multipliers in Constrained Variational Problems

**When to Use Lagrange Multipliers**

When optimizing a functional subject to **equality constraints**, we introduce a Lagrange multiplier. For a finite-dimensional example:

Minimize $f(x,y) = x^2 + y^2$ subject to $g(x,y) = x + y - 1 = 0$.

Construct the Lagrangian:

$$
\mathcal{L}(x,y,\lambda) = f(x,y) - \lambda g(x,y) = x^2 + y^2 - \lambda(x + y - 1)
$$

The stationary conditions $\partial\mathcal{L}/\partial x = \partial\mathcal{L}/\partial y = \partial\mathcal{L}/\partial\lambda = 0$ yield the constrained minimum. The multiplier $\lambda$ represents the sensitivity of the optimal value to the constraint constant.

---

**Application to DFT**

For the density constraint, construct:

$$
\mathcal{F}[n, \mu] = E[n] - \mu\left(\int d^3r \, n(\mathbf{r}) - N\right)
$$

where $\mu$ is the Lagrange multiplier (the chemical potential).

**Step 1: Vary with respect to $n(\mathbf{r})$**

Setting $\delta\mathcal{F}/\delta n = 0$:

$$
\frac{\delta E}{\delta n(\mathbf{r})} = \mu
$$

**Step 2: Compute functional derivatives**

For the external potential term:

$$
\frac{\delta}{\delta n(\mathbf{r})}\int d^3r' \, n(\mathbf{r}')V_{ext}(\mathbf{r}') = V_{ext}(\mathbf{r})
$$

using $\frac{\delta n(\mathbf{r}')}{\delta n(\mathbf{r})} = \delta(\mathbf{r} - \mathbf{r}')$.

For the Hartree energy:

$$
\frac{\delta E_H}{\delta n(\mathbf{r})} = e^2\int d^3r' \frac{n(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|} \equiv V_H(\mathbf{r})
$$

For the exchange-correlation energy:

$$
\frac{\delta E_{xc}}{\delta n(\mathbf{r})} \equiv V_{xc}(\mathbf{r})
$$

**Step 3: The Kohn-Sham Construction**

The kinetic energy term $T_s[n]$ requires special treatment. Introduce auxiliary non-interacting orbitals $\phi_i$ such that:

$$
n(\mathbf{r}) = \sum_{i=1}^N |\phi_i(\mathbf{r})|^2
$$

The non-interacting kinetic energy is:

$$
T_s = -\frac{\hbar^2}{2m}\sum_{i=1}^N \int d^3r \, \phi_i^*\nabla^2\phi_i
$$

Minimizing $E$ with respect to the orbitals subject to orthonormality constraints yields the **Kohn-Sham equation**:

$$
\left(-\frac{\hbar^2}{2m}\nabla^2 + V_{eff}(\mathbf{r})\right)\phi_i(\mathbf{r}) = \epsilon_i\phi_i(\mathbf{r})
$$

with effective potential:

$$
V_{eff}(\mathbf{r}) = V_{ext}(\mathbf{r}) + V_H(\mathbf{r}) + V_{xc}(\mathbf{r}) = V_{ext} + e^2\int d^3r' \frac{n(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|} + \frac{\delta E_{xc}}{\delta n}
$$

**Step 4: Physical interpretation of $\mu$**

The chemical potential satisfies:

$$
\mu = \frac{\delta E}{\delta n(\mathbf{r})}\bigg|_{n=n_0}
$$

For a finite system at $T=0$: $\mu = \epsilon_N$ (highest occupied Kohn-Sham eigenvalue).

**Self-Consistency:** The equations must be solved iteratively since $V_{eff}$ depends on $n$, which depends on the orbitals $\phi_i$.

---

**Summary: Lagrange Multipliers in Physics**

| Situation | Constraint | Multiplier |
|-----------|-----------|------------|
| DFT | $\int n = N$ | Chemical potential $\mu$ |
| Statistical mechanics | $\langle H \rangle = E$ | Inverse temperature $\beta$ |
| QED/QCD | $\partial_\mu A^\mu = 0$ | Gauge-fixing parameter |
| Quantum mechanics | $\int \vert\psi\vert^2 = 1$ | Energy eigenvalue $E$ |

The Lagrange multiplier enforces constraints through the variational principle without restricting the function space a priori.

### B.4 General Relativity — The Einstein-Hilbert Action

**The Einstein-Hilbert Action**

General relativity can be formulated as a **functional of the metric tensor** $g_{\mu\nu}(x)$. The Einstein-Hilbert action is:

$$
S[g_{\mu\nu}] = \frac{c^4}{16\pi G}\int d^4x \, \sqrt{-g} \, R + S_{\text{matter}}[g_{\mu\nu}, \psi]
$$

where:
- $g = \det(g_{\mu\nu})$ is the metric determinant
- $R = g^{\mu\nu}R_{\mu\nu}$ is the Ricci scalar (curvature)
- $G$ is Newton's gravitational constant
- $S_{\text{matter}}$ describes matter fields $\psi$ coupled to gravity

**The Ricci Tensor and Christoffel Symbols**

The Ricci tensor is built from the Christoffel symbols:

$$
\Gamma^\lambda_{\mu\nu} = \frac{1}{2}g^{\lambda\sigma}(\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu})
$$

$$
R_{\mu\nu} = \partial_\lambda\Gamma^\lambda_{\mu\nu} - \partial_\nu\Gamma^\lambda_{\mu\lambda} + \Gamma^\lambda_{\lambda\rho}\Gamma^\rho_{\mu\nu} - \Gamma^\lambda_{\mu\rho}\Gamma^\rho_{\lambda\nu}
$$

**Step-by-Step Variation of the Einstein-Hilbert Action**

**Step 1: Setup the variation**

Vary the metric: $g_{\mu\nu} \rightarrow g_{\mu\nu} + \delta g_{\mu\nu}$, or equivalently $g^{\mu\nu} \rightarrow g^{\mu\nu} + \delta g^{\mu\nu}$.

Note: $\delta g^{\mu\nu} = -g^{\mu\alpha}g^{\nu\beta}\delta g_{\alpha\beta}$ (using $g^{\mu\alpha}g_{\alpha\nu} = \delta^\mu_\nu$).

**Step 2: Variation of $\sqrt{-g}$**

Using $\delta g = g g^{\mu\nu}\delta g_{\mu\nu} = -g g_{\mu\nu}\delta g^{\mu\nu}$:

$$
\delta(\sqrt{-g}) = \frac{1}{2\sqrt{-g}}(-g)g^{\mu\nu}\delta g_{\mu\nu} = -\frac{1}{2}\sqrt{-g}g_{\mu\nu}\delta g^{\mu\nu}
$$

**Step 3: Variation of the Ricci scalar $R = g^{\mu\nu}R_{\mu\nu}$**

$$
\delta R = R_{\mu\nu}\delta g^{\mu\nu} + g^{\mu\nu}\delta R_{\mu\nu}
$$

**Step 4: The Palatini Identity for $\delta R_{\mu\nu}$**

This is the key step. The Ricci tensor is:

$$
R_{\mu\nu} = \partial_\lambda\Gamma^\lambda_{\mu\nu} - \partial_\nu\Gamma^\lambda_{\mu\lambda} + \Gamma^\lambda_{\lambda\rho}\Gamma^\rho_{\mu\nu} - \Gamma^\lambda_{\mu\rho}\Gamma^\rho_{\lambda\nu}
$$

The variation $\delta R_{\mu\nu}$ can be written as a **total derivative** plus Christoffel terms. After calculation (see Carroll's "Spacetime and Geometry" for details):

$$
\delta R_{\mu\nu} = \nabla_\lambda(\delta\Gamma^\lambda_{\mu\nu}) - \nabla_\nu(\delta\Gamma^\lambda_{\mu\lambda})
$$

This is the **Palatini identity**.

Therefore:

$$
g^{\mu\nu}\delta R_{\mu\nu} = \nabla_\lambda(g^{\mu\nu}\delta\Gamma^\lambda_{\mu\nu} - g^{\mu\lambda}\delta\Gamma^\rho_{\mu\rho}) \equiv \nabla_\lambda V^\lambda
$$

This is a total covariant divergence.

**Step 5: Putting it together**

$$
\delta(\sqrt{-g}R) = \delta(\sqrt{-g})R + \sqrt{-g}\delta R
$$

$$
= -\frac{1}{2}\sqrt{-g}g_{\mu\nu}R\delta g^{\mu\nu} + \sqrt{-g}R_{\mu\nu}\delta g^{\mu\nu} + \sqrt{-g}g^{\mu\nu}\delta R_{\mu\nu}
$$

$$
= \sqrt{-g}\left(R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R\right)\delta g^{\mu\nu} + \sqrt{-g}\nabla_\lambda V^\lambda
$$

**Step 6: Integration by parts / Boundary terms**

The last term $\sqrt{-g}\nabla_\lambda V^\lambda = \partial_\lambda(\sqrt{-g}V^\lambda)$ is a total divergence. When integrated over spacetime with suitable boundary conditions (variations vanish at boundaries), this term vanishes.

**Result:**

$$
\delta S_{EH} = \frac{c^4}{16\pi G}\int d^4x \, \sqrt{-g}\left(R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R\right)\delta g^{\mu\nu}
$$

**Step 7: The Energy-Momentum Tensor**

The matter action variation defines the **energy-momentum tensor**:

$$
\delta S_{\text{matter}} = -\frac{1}{2}\int d^4x \, \sqrt{-g} \, T_{\mu\nu}\delta g^{\mu\nu}
$$

Or equivalently:

$$
T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta S_{\text{matter}}}{\delta g^{\mu\nu}}
$$

**Examples:**
- For a scalar field: $T_{\mu\nu} = \partial_\mu\phi\partial_\nu\phi - \frac{1}{2}g_{\mu\nu}(\partial\phi)^2$
- For electromagnetic field: $T_{\mu\nu} = F_{\mu\alpha}F_\nu^{\alpha} - \frac{1}{4}g_{\mu\nu}F^2$
- For perfect fluid: $T_{\mu\nu} = (\rho + p)u_\mu u_\nu + pg_{\mu\nu}$

**Step 8: The Einstein Field Equations**

Setting the total variation $\delta S = \delta S_{EH} + \delta S_{\text{matter}} = 0$:

$$
\frac{c^4}{16\pi G}\left(R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R\right) - \frac{1}{2}T_{\mu\nu} = 0
$$

Rearranging:

$$
R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4}T_{\mu\nu}
$$

Or in the more familiar trace-reversed form (taking the trace $g^{\mu\nu}g_{\mu\nu} = 4$):

$$
R_{\mu\nu} = \frac{8\pi G}{c^4}\left(T_{\mu\nu} - \frac{1}{2}g_{\mu\nu}T\right)
$$

**Physical Interpretation:**

- **Left side:** Geometric quantities describing spacetime curvature
- **Right side:** Matter energy-momentum content
- The equation states: **"Matter tells spacetime how to curve; curved spacetime tells matter how to move"**

**The Challenge of Quantum Gravity:**

Unlike other field theories, the Einstein-Hilbert action is **non-renormalizable** in 4D. The coupling constant $G$ has dimensions of length², leading to divergences that cannot be absorbed by counterterms. This is a key motivation for:
- String theory (spacetime is not fundamental)
- Loop quantum gravity (discrete spacetime structure)
- Asymptotic safety (RG fixed point at high energy)

### B.5 Ginzburg-Landau Theory of Superconductivity — Complete Derivation

#### B.5.1 The GL Free Energy Functional

**Physical Motivation**

The Ginzburg-Landau theory (1950) is a phenomenological description of superconductors near the critical temperature $T_c$. It predates the microscopic BCS theory (1957) and introduces a **complex order parameter** $\psi(\mathbf{r})$ that can be interpreted as the wavefunction of Cooper pairs.

**Key assumptions:**
1. The superconducting state is characterized by a complex order parameter $\psi(\mathbf{r})$
2. Near $T_c$, $|\psi|$ is small, so we can expand the free energy in powers of $|\psi|$
3. The system interacts with the electromagnetic field via minimal coupling

**The Free Energy Functional**

$$
F[\psi, \psi^*, \mathbf{A}] = \int d^3r \left[\alpha|\psi|^2 + \frac{\beta}{2}|\psi|^4 + \frac{1}{2m^*}\left|\left(-i\hbar\nabla - \frac{e^*}{c}\mathbf{A}\right)\psi\right|^2 + \frac{\mathbf{B}^2}{8\pi}\right]
$$

where:
- $\alpha = \alpha_0(T - T_c)$ changes sign at $T_c$ (linear temperature dependence)
- $\beta > 0$ ensures stability (quartic term prevents $|\psi| \rightarrow \infty$)
- $m^* = 2m$ and $e^* = 2e$ are the effective mass and charge of Cooper pairs
- $\mathbf{B} = \nabla \times \mathbf{A}$ is the magnetic field

**Physical interpretation of each term:**

| Term | Physical Meaning |
|------|-----------------|
| $\alpha\vert\psi\vert^2$ | Quadratic term in the Landau expansion; drives the phase transition |
| $\frac{\beta}{2}\vert\psi\vert^4$ | Quartic stabilization term |
| $\frac{1}{2m^*}\vert\mathbf{D}\psi\vert^2$ | Kinetic energy of Cooper pairs (gauge-covariant) |
| $\frac{\mathbf{B}^2}{8\pi}$ | Magnetic field energy (Maxwell term) |

#### B.5.2 Gauge Invariance

**U(1) Gauge Transformation**

The GL functional has a **local U(1) gauge symmetry**:

$$
\psi(\mathbf{r}) \rightarrow \psi'(\mathbf{r}) = \psi(\mathbf{r})e^{i\chi(\mathbf{r})}
$$

$$
\mathbf{A}(\mathbf{r}) \rightarrow \mathbf{A}'(\mathbf{r}) = \mathbf{A}(\mathbf{r}) + \frac{\hbar c}{e^*}\nabla\chi(\mathbf{r})
$$

where $\chi(\mathbf{r})$ is an arbitrary real function.

**Proof of gauge invariance:**

The covariant derivative transforms as:

$$
\mathbf{D}'\psi' = \left(-i\hbar\nabla - \frac{e^*}{c}\mathbf{A}'\right)\psi e^{i\chi}
$$

$$
= e^{i\chi}\left(-i\hbar\nabla + \hbar\nabla\chi - \frac{e^*}{c}\mathbf{A} - \frac{e^*}{c}\cdot\frac{\hbar c}{e^*}\nabla\chi\right)\psi
$$

$$
= e^{i\chi}\left(-i\hbar\nabla - \frac{e^*}{c}\mathbf{A}\right)\psi = e^{i\chi}\mathbf{D}\psi
$$

Therefore:

$$
|\mathbf{D}'\psi'|^2 = |e^{i\chi}\mathbf{D}\psi|^2 = |\mathbf{D}\psi|^2
$$

The kinetic term is gauge invariant. The magnetic field $\mathbf{B} = \nabla \times \mathbf{A}$ is also gauge invariant since $\nabla \times \nabla\chi = 0$.

#### B.5.3 First GL Equation: Variation with respect to $\psi^*$

**Setup**

We vary $\psi^*(\mathbf{r}) \rightarrow \psi^*(\mathbf{r}) + \delta\psi^*(\mathbf{r})$ while keeping $\psi$ and $\mathbf{A}$ fixed. The variation of the free energy must vanish at the minimum:

$$
\delta F = F[\psi + \delta\psi, \psi^* + \delta\psi^*, \mathbf{A}] - F[\psi, \psi^*, \mathbf{A}] = 0
$$

to first order in $\delta\psi^*$.

**Step 1: Potential terms**

For $\alpha|\psi|^2 = \alpha\psi^*\psi$:

$$
\delta(\alpha\psi^*\psi) = \alpha(\delta\psi^*)\psi + \alpha\psi^*\underbrace{(\delta\psi)}_{=0 \text{ (fixed)}} = \alpha\psi \delta\psi^*
$$

For $\frac{\beta}{2}|\psi|^4 = \frac{\beta}{2}(\psi^*\psi)^2$:

$$
\delta\left(\frac{\beta}{2}|\psi|^4\right) = \frac{\beta}{2} \cdot 2(\psi^*\psi) \cdot \delta(\psi^*\psi) = \beta|\psi|^2(\psi \delta\psi^* + \psi^*\underbrace{\delta\psi}_{=0}) = \beta|\psi|^2\psi \delta\psi^*
$$

**Step 2: Kinetic term (detailed calculation)**

Define the **covariant derivative**:

$$
\mathbf{D} \equiv -i\hbar\nabla - \frac{e^*}{c}\mathbf{A}
$$

The kinetic term is:

$$
\mathcal{T} = \frac{1}{2m^*}|\mathbf{D}\psi|^2 = \frac{1}{2m^*}(\mathbf{D}\psi)^* \cdot (\mathbf{D}\psi)
$$

Under variation $\psi^* \rightarrow \psi^* + \delta\psi^*$:

$$
\delta\mathcal{T} = \frac{1}{2m^*}\left[(\mathbf{D}\delta\psi)^* \cdot (\mathbf{D}\psi) + (\mathbf{D}\psi)^* \cdot (\mathbf{D}\underbrace{\delta\psi}_{=0})\right] = \frac{1}{2m^*}(\mathbf{D}\delta\psi)^* \cdot (\mathbf{D}\psi)
$$

**Step 3: Integration by parts**

We need to evaluate:

$$
\int d^3r \, (\mathbf{D}\delta\psi)^* \cdot (\mathbf{D}\psi)
$$

First, write out the components. Let $D_j = -i\hbar\partial_j - \frac{e^*}{c}A_j$ where $j = x, y, z$. Then:

$$
(D_j\delta\psi)^* = (i\hbar\partial_j - \frac{e^*}{c}A_j)\delta\psi^*
$$

since $(-i\hbar\partial_j)^* = i\hbar\partial_j$ and $A_j$ is real.

Therefore:

$$
\int d^3r \, (\mathbf{D}\delta\psi)^* \cdot (\mathbf{D}\psi) = \int d^3r \sum_j (i\hbar\partial_j - \frac{e^*}{c}A_j)\delta\psi^* \cdot D_j\psi
$$

Integrate by parts (assuming boundary terms vanish):

$$
= -\int d^3r \sum_j \delta\psi^* \cdot (i\hbar\partial_j - \frac{e^*}{c}A_j)D_j\psi
$$

$$
= -\int d^3r \, \delta\psi^* \sum_j D_j^2\psi
$$

where we used the fact that $D_j$ acts on everything to its right. Since $D_j^2$ means applying $D_j$ twice:

$$
D_j^2\psi = (-i\hbar\partial_j - \frac{e^*}{c}A_j)(-i\hbar\partial_j - \frac{e^*}{c}A_j)\psi
$$

we have:

$$
\int d^3r \, (\mathbf{D}\delta\psi)^* \cdot (\mathbf{D}\psi) = \int d^3r \, \delta\psi^* \mathbf{D}^2\psi
$$

where $\mathbf{D}^2 = \mathbf{D} \cdot \mathbf{D} = \left(-i\hbar\nabla - \frac{e^*}{c}\mathbf{A}\right)^2$.

**Step 4: Collect all terms**

The total variation is:

$$
\delta F = \int d^3r \, \delta\psi^*\left[\alpha\psi + \beta|\psi|^2\psi + \frac{1}{2m^*}\mathbf{D}^2\psi\right]
$$

Since $\delta\psi^*$ is arbitrary, the integrand must vanish:

$$
\alpha\psi + \beta|\psi|^2\psi + \frac{1}{2m^*}\left(-i\hbar\nabla - \frac{e^*}{c}\mathbf{A}\right)^2\psi = 0
$$

This is the **first Ginzburg-Landau equation** — a non-linear Schrödinger equation for Cooper pairs.

#### B.5.4 Second GL Equation: Variation with respect to $\mathbf{A}$

**Setup**

Now vary $\mathbf{A}(\mathbf{r}) \rightarrow \mathbf{A}(\mathbf{r}) + \delta\mathbf{A}(\mathbf{r})$ while keeping $\psi$ fixed. The free energy change is:

$$
\delta F = \int d^3r \left[\frac{1}{2m^*}\delta(|\mathbf{D}\psi|^2) + \frac{1}{8\pi}\delta(\mathbf{B}^2)\right]
$$

**Step 1: Kinetic term variation**

Expand the kinetic term:

$$
|\mathbf{D}\psi|^2 = (\mathbf{D}\psi)^* \cdot (\mathbf{D}\psi)
$$

$$
= \left[(i\hbar\nabla - \frac{e^*}{c}\mathbf{A})\psi^*\right] \cdot \left[(-i\hbar\nabla - \frac{e^*}{c}\mathbf{A})\psi\right]
$$

$$
= \hbar^2|\nabla\psi|^2 + \frac{i\hbar e^*}{c}\mathbf{A}\cdot(\psi^*\nabla\psi - \psi\nabla\psi^*) + \frac{(e^*)^2}{c^2}|\psi|^2\mathbf{A}^2
$$

Varying with respect to $\mathbf{A}$:

$$
\delta(|\mathbf{D}\psi|^2) = \left[\frac{i\hbar e^*}{c}(\psi^*\nabla\psi - \psi\nabla\psi^*) + \frac{2(e^*)^2}{c^2}|\psi|^2\mathbf{A}\right]\cdot\delta\mathbf{A}
$$

**Step 2: Magnetic field term variation**

With $\mathbf{B} = \nabla \times \mathbf{A}$:

$$
\delta\mathbf{B} = \nabla \times \delta\mathbf{A}
$$

Therefore:

$$
\delta(\mathbf{B}^2) = 2\mathbf{B} \cdot \delta\mathbf{B} = 2\mathbf{B} \cdot (\nabla \times \delta\mathbf{A})
$$

Using the vector identity:

$$
\mathbf{a} \cdot (\nabla \times \mathbf{b}) = \mathbf{b} \cdot (\nabla \times \mathbf{a}) - \nabla \cdot (\mathbf{a} \times \mathbf{b})
$$

we get:

$$
\mathbf{B} \cdot (\nabla \times \delta\mathbf{A}) = (\nabla \times \mathbf{B}) \cdot \delta\mathbf{A} - \nabla \cdot (\mathbf{B} \times \delta\mathbf{A})
$$

The divergence term integrates to a surface term (vanishing at infinity), so:

$$
\int d^3r \, \mathbf{B} \cdot (\nabla \times \delta\mathbf{A}) = \int d^3r \, (\nabla \times \mathbf{B}) \cdot \delta\mathbf{A}
$$

**Step 3: Collect terms and define supercurrent**

The total variation is:

$$
\delta F = \int d^3r \left\{\frac{1}{2m^*}\left[\frac{i\hbar e^*}{c}(\psi^*\nabla\psi - \psi\nabla\psi^*) + \frac{2(e^*)^2}{c^2}|\psi|^2\mathbf{A}\right] + \frac{1}{4\pi}(\nabla \times \mathbf{B})\right\}\cdot\delta\mathbf{A}
$$

Define the **supercurrent density**:

$$
\mathbf{j} = \frac{e^*\hbar}{2im^*}(\psi^*\nabla\psi - \psi\nabla\psi^*) - \frac{(e^*)^2}{m^*c}|\psi|^2\mathbf{A}
$$

The first term is the **paramagnetic current** (from phase gradients), the second is the **diamagnetic current** (screening response).

Setting $\delta F/\delta\mathbf{A} = 0$:

$$
\frac{1}{c}\mathbf{j} + \frac{1}{4\pi}\nabla \times \mathbf{B} = 0
$$

Rearranging:

$$
\nabla \times \mathbf{B} = \frac{4\pi}{c}\mathbf{j}
$$

This is **Ampère's law** with the supercurrent — the **second Ginzburg-Landau equation**.

#### B.5.5 Physical Consequences: Characteristic Lengths

**Coherence Length $\xi$**

In zero magnetic field ($\mathbf{A} = 0$), far from boundaries, the GL equation becomes:

$$
-\frac{\hbar^2}{2m^*}\nabla^2\psi + \alpha\psi + \beta|\psi|^2\psi = 0
$$

Near $T_c$, write $\psi = \psi_\infty + \delta\psi$ where $|\psi_\infty|^2 = -\alpha/\beta$ (bulk value). Linearizing:

$$
-\frac{\hbar^2}{2m^*}\nabla^2\delta\psi + \alpha\delta\psi + 2\beta|\psi_\infty|^2\delta\psi = 0
$$

Using $|\psi_\infty|^2 = -\alpha/\beta$:

$$
-\frac{\hbar^2}{2m^*}\nabla^2\delta\psi - \alpha\delta\psi = 0
$$

This has solutions $\delta\psi \propto e^{-x/\xi}$ with:

$$
\xi = \sqrt{\frac{\hbar^2}{2m^*|\alpha|}} = \sqrt{\frac{\hbar^2}{2m^*\alpha_0|T_c - T|}}
$$

The **coherence length** diverges as $T \rightarrow T_c$.

**Penetration Depth $\lambda$**

Consider a weak magnetic field penetrating from the surface. With $\psi \approx \psi_\infty$ (constant), the supercurrent is:

$$
\mathbf{j} = -\frac{(e^*)^2n_s}{m^*c}\mathbf{A} = -\frac{c}{4\pi\lambda^2}\mathbf{A}
$$

where $n_s = |\psi_\infty|^2$ and:

$$
\lambda = \sqrt{\frac{m^*c^2}{4\pi(e^*)^2n_s}} = \sqrt{\frac{m^*c^2\beta}{4\pi(e^*)^2|\alpha|}}
$$

From Ampère's law $\nabla \times \mathbf{B} = \frac{4\pi}{c}\mathbf{j}$ and $\mathbf{B} = \nabla \times \mathbf{A}$:

$$
\nabla^2\mathbf{B} = \frac{1}{\lambda^2}\mathbf{B}
$$

The solution $\mathbf{B}(x) = \mathbf{B}_0 e^{-x/\lambda}$ shows exponential decay — the **Meissner effect**.

#### B.5.6 Type I vs Type II Superconductors

**The GL Parameter**

The ratio:

$$
\kappa = \frac{\lambda}{\xi} = \frac{m^*c}{\hbar e^*}\sqrt{\frac{\beta}{2\pi}}
$$

is temperature-independent (within GL theory) and determines the superconductor type.

**Interface Energy Analysis**

Consider the energy of a normal-superconducting interface. There are two competing effects:

1. **Positive contribution**: Energy cost of suppressing $|\psi|$ over distance $\xi$ (condensation energy loss)
2. **Negative contribution**: Energy gain from allowing magnetic field penetration over distance $\lambda$ (field energy reduction)

The interface energy is:

$$
\sigma_{ns} \approx \frac{H_c^2}{8\pi}(\xi - \lambda)
$$

where $H_c$ is the thermodynamic critical field.

- **Type I** ($\kappa < 1/\sqrt{2}$): $\xi > \lambda$, $\sigma_{ns} > 0$ — positive surface energy, complete flux expulsion (Meissner state)
- **Type II** ($\kappa > 1/\sqrt{2}$): $\xi < \lambda$, $\sigma_{ns} < 0$ — negative surface energy, flux penetration favored

**Critical Fields**

For Type II superconductors:
- $H_{c1}$: Lower critical field — first vortex enters
- $H_{c2}$: Upper critical field — superconductivity destroyed

$$
H_{c2} = \frac{\Phi_0}{2\pi\xi^2}, \quad H_{c1} \approx \frac{\Phi_0}{4\pi\lambda^2}\ln\kappa
$$

where $\Phi_0 = hc/e^* = hc/2e$ is the flux quantum.

#### B.5.7 The Abrikosov Vortex Solution

**Vortex Ansatz**

For a single vortex along the $z$-axis, use cylindrical coordinates $(r, \theta, z)$. The order parameter has the form:

$$
\psi(r, \theta) = f(r)e^{in\theta}
$$

where $n$ is the winding number (vorticity). By symmetry, $f(r) \rightarrow 0$ as $r \rightarrow 0$ (normal core) and $f(r) \rightarrow \psi_\infty$ as $r \rightarrow \infty$.

**Core Structure**

Near the core ($r \ll \xi$), $f(r) \approx 0$ and the region is normal. The core radius is $\sim \xi$.

**Magnetic Field Distribution**

The magnetic field peaks at the center and decays exponentially:

$$
B(r) \approx \frac{\Phi_0}{2\pi\lambda^2}K_0(r/\lambda)
$$

where $K_0$ is the modified Bessel function. For $r \gg \lambda$: $B(r) \propto e^{-r/\lambda}/\sqrt{r}$.

**Supercurrent Pattern**

The current circulates azimuthally:

$$
j_\theta(r) = \frac{e^*\hbar n}{m^*r}f^2(r) - \frac{(e^*)^2}{m^*c}A_\theta(r)f^2(r)
$$

**Vortex Energy**

The energy per unit length is:

$$
\epsilon = \left(\frac{\Phi_0}{4\pi\lambda}\right)^2\ln\left(\frac{\lambda}{\xi}\right) = \frac{\Phi_0H_{c1}}{4\pi}
$$

for $\kappa \gg 1$.

#### B.5.8 Connection to BCS Theory

**Microscopic Derivation**

Gor'kov (1959) showed that GL theory follows from BCS theory near $T_c$. The key results:

$$
\psi(\mathbf{r}) = \sqrt{\frac{7\zeta(3)n}{8\pi^2T_c^2}}\Delta(\mathbf{r})
$$

where $\Delta(\mathbf{r})$ is the BCS gap parameter, $n$ is the electron density, and $\zeta(3) \approx 1.202$.

The GL coefficients are:

$$
\alpha = -\frac{6\pi^2T_c^2}{7\zeta(3)\epsilon_F}N(0), \quad \beta = \frac{12\pi^2T_c^2}{7\zeta(3)N(0)n}
$$

where $N(0)$ is the density of states at the Fermi level and $\epsilon_F$ is the Fermi energy.

**Characteristic lengths in BCS terms:**

$$
\xi_0 = \frac{\hbar v_F}{\pi\Delta(0)}, \quad \lambda_L(0) = \sqrt{\frac{mc^2}{4\pi n e^2}}
$$

The GL theory bridges the gap between the microscopic BCS theory and macroscopic electrodynamics, providing a powerful framework for describing superconducting phenomena.

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
