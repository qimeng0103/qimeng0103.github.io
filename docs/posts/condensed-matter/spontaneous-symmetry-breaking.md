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

**Two Levels of Abstraction for Functionals**

Before stating the rule, let's clarify the dual nature of functional derivatives. A functional derivative involves **two distinct levels of abstraction**:

1. **The functional level**: $F[\phi]$ is a map from the space of functions to numbers. The functional derivative $\frac{\delta F}{\delta \phi(x)}$ tells us how $F$ responds to changes in $\phi$ at point $x$.

2. **The function level**: Once we evaluate $\frac{\delta F}{\delta \phi(x)}$, we obtain a **new function of position $x$**. For each $x$, this gives a number telling us the sensitivity at that point.

**Key distinction**: $\frac{\delta F}{\delta \phi(x)}$ is itself a function of $x$. When we write $\frac{\delta F}{\delta \phi}$ without the $(x)$, we mean the functional derivative operator or the resulting function evaluated at all points.

**The Lagrangian Density $\mathcal{L}$ — A Different Object**

It's crucial to understand what $\mathcal{L}$ is:
- $\mathcal{L}(\phi(x), \nabla\phi(x), x)$ takes a **position $x$** and field values at that point, and returns a number
- It is **not** a functional—it's an ordinary function of its arguments $(\phi, \nabla\phi, x)$
- For a local theory: $F[\phi] = \int dx \, \mathcal{L}(\phi(x), \nabla\phi(x), x)$

When we write $\frac{\partial \mathcal{L}}{\partial \phi}$, we treat $\mathcal{L}$ as a function of the variable $\phi$ (at fixed $x$), not as a functional of the entire field configuration.

**The Equality**

For a spatially uniform field $\phi(x) = \phi_0$ (constant), the following equality holds:

$$
\left.\frac{\delta F[\phi]}{\delta \phi(x)}\right|_{\phi(x)=\phi_0} = \left.\frac{\partial \mathcal{L}}{\partial \phi}\right|_{\phi=\phi_0}
$$

**Understanding the Left-Hand Side (Functional Derivative)**

The functional derivative $\frac{\delta F}{\delta \phi(x)}$ is computed as follows:
1. Start with $F[\phi] = \int dy \, \mathcal{L}(\phi(y), \nabla\phi(y), y)$
2. Compute $\frac{\delta F}{\delta \phi(x)}$ using the formula for local functionals
3. This yields a **function of $x$**: $\frac{\delta F}{\delta \phi(x)} = \frac{\partial \mathcal{L}}{\partial \phi}(x) - \nabla \cdot \left(\frac{\partial \mathcal{L}}{\partial(\nabla\phi)}(x)\right)$
4. Now substitute the uniform configuration $\phi(x) = \phi_0$ (constant for all $x$)
5. The result is a **constant number** (same value for all $x$)

**Understanding the Right-Hand Side (Ordinary Derivative)**

The partial derivative $\frac{\partial \mathcal{L}}{\partial \phi}$ is computed as follows:
1. Take the Lagrangian density function $\mathcal{L}(\phi, \nabla\phi, x)$
2. Treat $\phi$ as an independent variable (not a field), holding $\nabla\phi$ and $x$ fixed
3. Compute the ordinary partial derivative with respect to this variable
4. Evaluate at the point where the field value is $\phi_0$ and field gradient is $\nabla\phi = 0$
5. The result is a number

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

If $F[f] = G[H[f]]$ where $G$ is an ordinary differentiable function and $H$ is a functional:

$$
\frac{\delta F}{\delta f(x)} = G'(H[f]) \cdot \frac{\delta H}{\delta f(x)}
$$

where $G'(H) = \frac{dG}{dH}$ is the ordinary derivative of $G$ with respect to its argument.

**Complete Proof:**

**Step 1: Set up the variation**

Consider a variation of $f$ at point $x_0$:
$$
f(y) \rightarrow f(y) + \epsilon \delta(y - x_0)
$$

**Step 2: Compute the change in $H$**

By definition of the functional derivative:
$$
\delta H = H[f + \epsilon \delta_{x_0}] - H[f] = \epsilon \frac{\delta H}{\delta f(x_0)} + O(\epsilon^2)
$$

**Step 3: Compute the change in $F = G(H)$**

Since $G$ is an ordinary function, we use its Taylor expansion:
$$
\delta F = G(H + \delta H) - G(H) = G'(H) \cdot \delta H + O((\delta H)^2)
$$

**Step 4: Substitute $\delta H$**

$$
\delta F = G'(H[f]) \cdot \left(\epsilon \frac{\delta H}{\delta f(x_0)}\right) + O(\epsilon^2)
$$

**Step 5: Apply the functional derivative definition**

$$
\frac{\delta F}{\delta f(x_0)} = \lim_{\epsilon \to 0} \frac{\delta F}{\epsilon} = G'(H[f]) \cdot \frac{\delta H}{\delta f(x_0)}
$$

Since $x_0$ is arbitrary, this proves the chain rule for all $x$.

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

**Definition and Physical Picture**

**Spontaneous symmetry breaking** occurs when the ground state of a system has less symmetry than the equations of motion (Hamiltonian or Lagrangian) that govern it.

The symmetry is "spontaneous" for three interconnected reasons:

1. **The equations retain the full symmetry**: The Hamiltonian $H$ (or Lagrangian $\mathcal{L}$) is invariant under the symmetry transformation $U$, i.e., $[H, U] = 0$.

2. **No external symmetry-breaking field is applied**: The symmetry is broken dynamically by the system itself, not by an external perturbation.

3. **The system "chooses" a specific ground state from a degenerate set**: The ground state is not unique—all symmetry-related states have the same energy. The physical system falls into one specific state, breaking the symmetry.

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

The ground state field value $\phi_0$ is found by minimizing the potential $V(\phi)$.

**Physical Picture of Symmetry Breaking**

For a complex scalar field with $U(1)$ symmetry $\phi \rightarrow e^{i\alpha}\phi$:
- If the ground state has $\phi_0 = 0$, the symmetry is preserved (the origin is invariant under rotations)
- If the ground state has $\phi_0 = v e^{i\theta_0} \neq 0$, the symmetry is broken (rotating the phase changes the specific state)

The field "chooses" a specific phase angle $\theta_0$, breaking the continuous $U(1)$ symmetry.

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

**Substituting into the Lagrangian — Complete Calculation**

We substitute $\phi = v + \frac{1}{\sqrt{2}}(h + i\pi)$ into $\mathcal{L}$ and expand to quadratic order in $h$ and $\pi$.

**Step 1: Compute $\vert\phi\vert^2$**

$$
\vert\phi\vert^2 = \phi^*\phi = \left(v + \frac{h}{\sqrt{2}} - i\frac{\pi}{\sqrt{2}}\right)\left(v + \frac{h}{\sqrt{2}} + i\frac{\pi}{\sqrt{2}}\right)
$$

$$
= \left(v + \frac{h}{\sqrt{2}}\right)^2 + \left(\frac{\pi}{\sqrt{2}}\right)^2 = v^2 + \sqrt{2}vh + \frac{h^2}{2} + \frac{\pi^2}{2}
$$

**Step 2: Expand the potential to quadratic order**

Let $\rho = \vert\phi\vert^2 = v^2 + \sqrt{2}vh + \frac{h^2+\pi^2}{2}$. The potential is $V(\rho) = -\alpha\rho + \gamma\rho^2$.

First, compute $\rho^2$ keeping terms up to quadratic order in $h$ and $\pi$:

$$
\rho^2 = \left(v^2 + \sqrt{2}vh + \frac{h^2+\pi^2}{2}\right)^2 = v^4 + 2\sqrt{2}v^3h + v^2(2h^2 + \pi^2) + O(h^3, h^2\pi, \ldots)
$$

Now substitute into $V$:

$$
V = -\alpha\left(v^2 + \sqrt{2}vh + \frac{h^2+\pi^2}{2}\right) + \gamma\left(v^4 + 2\sqrt{2}v^3h + v^2(2h^2 + \pi^2)\right)
$$

**Step 3: Group terms by order**

Constant term:
$$V_0 = -\alpha v^2 + \gamma v^4 = V_{min}$$

Linear terms in $h$:
$$V_1 = \sqrt{2}vh(-\alpha + 2\gamma v^2)$$

Using the minimum condition $\alpha = 2\gamma v^2$:
$$V_1 = \sqrt{2}vh(-2\gamma v^2 + 2\gamma v^2) = 0$$

The linear terms vanish as expected (we expanded around the minimum).

Quadratic terms:
$$V_2 = -\alpha\frac{h^2+\pi^2}{2} + \gamma v^2(2h^2 + \pi^2)$$

Using $\alpha = 2\gamma v^2$:
$$V_2 = -\gamma v^2(h^2+\pi^2) + \gamma v^2(2h^2 + \pi^2) = \gamma v^2 h^2 + 0 \cdot \pi^2$$

**Step 4: Final result**

With $m_h^2 = 2\gamma v^2 \cdot 2 = 4\gamma v^2 = 2\alpha$:

$$
V = V_{min} + \frac{1}{2}m_h^2 h^2 + 0 \cdot \pi^2 + O(h^3, h^2\pi, \ldots)
$$

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

**Example: The Generator for $U(1)$ Symmetry**

Consider a complex scalar field with $U(1)$ phase symmetry. An infinitesimal phase rotation is:

$$
\phi \rightarrow \phi e^{i\epsilon} \approx \phi(1 + i\epsilon) = \phi + i\epsilon\phi
$$

Comparing with $\phi \rightarrow \phi + \epsilon \eta$, the **generator** is:

$$
\eta(x) = i\phi(x)
$$

For a real scalar field with two components $\phi = (\phi_1, \phi_2)$, the $SO(2)$ rotation generator is:

$$
\eta = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} \phi_1 \\ \phi_2 \end{pmatrix} = \begin{pmatrix} -\phi_2 \\ \phi_1 \end{pmatrix}
$$

This represents an infinitesimal rotation in the $(\phi_1, \phi_2)$ plane.

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

**Step 5: Local Theory Simplification — Detailed Derivation of $M(y,x)$**

For a local theory, the potential has the form:

$$
V[\phi] = \int dy \, \mathcal{V}(\phi(y), \nabla\phi(y))
$$

**Computing the first functional derivative:**

Using the Euler-Lagrange structure:

$$
\frac{\delta V}{\delta \phi(x)} = \frac{\partial \mathcal{V}}{\partial \phi}(x) - \nabla_x \cdot \frac{\partial \mathcal{V}}{\partial(\nabla\phi)}(x)
$$

**Computing the second functional derivative:**

Now take $\frac{\delta}{\delta \phi(y)}$ of the above:

$$
M(y,x) = \frac{\delta^2 V}{\delta \phi(y)\delta \phi(x)} = \frac{\delta}{\delta \phi(y)}\left[\frac{\partial \mathcal{V}}{\partial \phi}(x) - \nabla_x \cdot \frac{\partial \mathcal{V}}{\partial(\nabla\phi)}(x)\right]
$$

The key identity is:

$$
\frac{\delta}{\delta \phi(y)}\left(\frac{\partial \mathcal{V}}{\partial \phi}(x)\right) = \frac{\partial^2 \mathcal{V}}{\partial \phi^2}(x) \delta(x-y)
$$

This is because $\frac{\partial \mathcal{V}}{\partial \phi}(x)$ depends on $\phi$ only at point $x$.

For the gradient term, after integration by parts twice:

$$
\frac{\delta}{\delta \phi(y)}\left(-\nabla_x \cdot \frac{\partial \mathcal{V}}{\partial(\nabla\phi)}(x)\right) = -\nabla_x \cdot \left[\frac{\partial^2 \mathcal{V}}{\partial(\nabla\phi)\partial\phi}(x)\delta(x-y)\right] - \nabla_x^2\left[\frac{\partial^2 \mathcal{V}}{\partial(\nabla\phi)^2}(x)\delta(x-y)\right]
$$

**Simplification for uniform background:**

At $\phi(x) = \phi_0$ (constant):
- The mixed derivative term vanishes: $\frac{\partial^2 \mathcal{V}}{\partial(\nabla\phi)\partial\phi} = 0$ (the Lagrangian density typically has no such coupling)
- For the second derivative term: $\nabla_x^2[\cdots\delta(x-y)] = [\nabla_x^2\cdots]\delta(x-y)$

Therefore:

$$
M(y,x) = \left[\frac{\partial^2 \mathcal{V}}{\partial \phi^2} - \nabla^2\frac{\partial^2 \mathcal{V}}{\partial(\nabla\phi)^2}\right]_{\phi_0} \delta(y-x)
$$

For a uniform background $\phi(x) = \phi_0$, the spatial derivatives of the background vanish, giving:

$$
M(y,x) = \frac{\partial^2 \mathcal{V}}{\partial \phi^2}\bigg|_{\phi_0} \delta(y-x) = m^2 \delta(y-x)
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

**Historical Origin and Soft Modes:**

The concept was introduced by Landau in the 1930s to describe phase transitions. The key insight is that near a phase transition, there's typically a "soft mode" that becomes unstable, and the order parameter characterizes the new state that emerges.

**What is a Soft Mode?**

A **soft mode** is a collective excitation whose restoring force (or effective "spring constant") decreases as the system approaches a phase transition. In the language of field theory:

- The excitation energy is $\omega(k)$ for wavevector $k$
- Near the phase transition at $T = T_c$, the gap vanishes: $\omega(0) \rightarrow 0$
- The mode becomes **unstable** when the curvature of the free energy at the symmetric point changes sign

**Physical Picture:**

Consider a potential $V(M) = \frac{1}{2}\alpha(T)M^2 + \frac{1}{4}\gamma M^4$ where $\alpha(T) = \alpha_0(T-T_c)$:
- For $T > T_c$: $\alpha > 0$, the potential has a single minimum at $M = 0$
- For $T < T_c$: $\alpha < 0$, the potential develops a double-well structure

The "soft mode" corresponds to oscillations around $M = 0$. As $T \rightarrow T_c^+$:
- The curvature $\frac{\partial^2 V}{\partial M^2}|_{M=0} = \alpha \rightarrow 0$
- The oscillation frequency $\omega \propto \sqrt{\alpha} \rightarrow 0$
- The mode becomes "soft" (easy to excite) and eventually unstable

This soft mode instability drives the system to develop a non-zero order parameter $M \neq 0$ below $T_c$.

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

**Why This Form? — Detailed Justification**

Landau's expansion $F(M) = F_0 + \frac{1}{2}\alpha(T) M^2 + \frac{1}{4}\gamma M^4$ is justified by three key principles:

**1. Symmetry Constraints**

The free energy must respect the symmetries of the underlying Hamiltonian. For an Ising ferromagnet with spin-up/spin-down ($M \leftrightarrow -M$) symmetry:
- $F(M) = F(-M)$ requires only even powers of $M$
- Terms like $M^3$ or $M^5$ are forbidden by symmetry
- The lowest-order even terms are $M^2$ and $M^4$

**2. Analyticity Assumption**

Landau assumed $F(M)$ is an analytic function of $M$ near the transition. This means $F(M)$ can be expanded as a Taylor series:

$$
F(M) = F_0 + a_1 M + a_2 M^2 + a_3 M^3 + a_4 M^4 + \ldots
$$

- The linear term $a_1 = 0$ (we expand around the minimum)
- Symmetry eliminates odd terms: $a_3 = a_5 = \ldots = 0$
- We're left with: $F(M) = F_0 + a_2 M^2 + a_4 M^4 + \ldots$

**3. Physical Justification for Truncation**

Why keep only up to $M^4$?

- **Near the critical temperature**: $M$ is small (it vanishes at $T_c$)
- **Scaling argument**: If $M \sim (T_c - T)^{1/2}$, then $M^4 \sim (T_c - T)^2$ is the leading correction
- **Stability requirement**: The $M^4$ term with $\gamma > 0$ ensures the free energy is bounded below as $M \rightarrow \infty$
- **Higher-order terms** ($M^6$, etc.) contribute at $O((T_c-T)^3)$ and are negligible close to $T_c$

**Why must $\alpha(T)$ change sign?**

- For $T > T_c$: The disordered phase $M = 0$ must be the minimum $\Rightarrow \alpha > 0$
- For $T < T_c$: The disordered phase becomes unstable, ordered phases appear $\Rightarrow \alpha < 0$
- The simplest form: $\alpha(T) = \alpha_0(T - T_c)$ with $\alpha_0 > 0$

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

For readers who want to deepen their understanding of functional calculus, this appendix provides detailed examples from quantum field theory and superconductivity. Section B.1 illustrates functional variation in Quantum Electrodynamics (QED), while Section B.4 presents a complete derivation of the Ginzburg-Landau theory of superconductivity, including the two GL equations, characteristic length scales, type I/II classification, and the Abrikosov vortex solution.

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

**Step 3:** Vary the Maxwell term by direct substitution.

The Maxwell action is $S_{\text{Maxwell}} = -\frac{1}{4}\int d^4x \, F_{\mu\nu}F^{\mu\nu}$. We substitute $A_\nu \rightarrow A_\nu + \delta A_\nu$ and expand to first order.

First, the field strength with varied potential:

$$
F_{\mu\nu}[A + \delta A] = \partial_\mu(A_\nu + \delta A_\nu) - \partial_\nu(A_\mu + \delta A_\mu) = F_{\mu\nu} + \delta F_{\mu\nu}
$$

where $\delta F_{\mu\nu} = \partial_\mu(\delta A_\nu) - \partial_\nu(\delta A_\mu)$.

Now compute $F_{\mu\nu}F^{\mu\nu}$ with the varied potential:

$$
F_{\mu\nu}F^{\mu\nu}[A + \delta A] = (F_{\mu\nu} + \delta F_{\mu\nu})(F^{\mu\nu} + \delta F^{\mu\nu})
$$

$$
= F_{\mu\nu}F^{\mu\nu} + F_{\mu\nu}\delta F^{\mu\nu} + \delta F_{\mu\nu}F^{\mu\nu} + O((\delta A)^2)
$$

$$
= F_{\mu\nu}F^{\mu\nu} + 2F^{\mu\nu}\delta F_{\mu\nu} + O((\delta A)^2)
$$

To first order in $\delta A$:

$$
\delta(F_{\mu\nu}F^{\mu\nu}) = 2F^{\mu\nu}\delta F_{\mu\nu} = 2F^{\mu\nu}(\partial_\mu\delta A_\nu - \partial_\nu\delta A_\mu) = 4F^{\mu\nu}\partial_\mu\delta A_\nu
$$

(using antisymmetry $F^{\mu\nu} = -F^{\nu\mu}$ in the last step)

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

### B.4 Ginzburg-Landau Theory of Superconductivity — Complete Derivation

#### B.4.1 The GL Free Energy Functional

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

#### B.4.2 Gauge Invariance

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

#### B.4.3 First GL Equation: Variation with respect to $\psi^*$

**Setup**

We vary $\psi^*(\mathbf{r}) \rightarrow \psi^*(\mathbf{r}) + \delta\psi^*(\mathbf{r})$ while keeping $\psi$ and $\mathbf{A}$ fixed. The variation of the free energy must vanish at the minimum. We use the **direct substitution method**: substitute $\psi^* \rightarrow \psi^* + \delta\psi^*$ into the Lagrangian density and expand to first order in $\delta\psi^*$.

**Step 1: Direct substitution into potential terms**

For $\alpha|\psi|^2 = \alpha\psi^*\psi$, substitute $\psi^* \rightarrow \psi^* + \delta\psi^*$:

$$
\alpha(\psi^* + \delta\psi^*)\psi = \alpha\psi^*\psi + \alpha\psi\,\delta\psi^*
$$

The variation (first-order term) is:

$$
\delta(\alpha|\psi|^2) = \alpha\psi\,\delta\psi^*
$$

For $\frac{\beta}{2}|\psi|^4 = \frac{\beta}{2}(\psi^*\psi)^2$, substitute $\psi^* \rightarrow \psi^* + \delta\psi^*$:

$$
\frac{\beta}{2}[(\psi^* + \delta\psi^*)\psi]^2 = \frac{\beta}{2}(\psi^*\psi)^2 + \beta(\psi^*\psi)(\psi\,\delta\psi^*) + O((\delta\psi^*)^2)
$$

The variation to first order is:

$$
\delta\left(\frac{\beta}{2}|\psi|^4\right) = \beta|\psi|^2\psi\,\delta\psi^*
$$

**Step 2: Direct substitution into the kinetic term**

Define the **covariant derivative**:

$$
\mathbf{D} \equiv -i\hbar\nabla - \frac{e^*}{c}\mathbf{A}
$$

The kinetic term is $\mathcal{T} = \frac{1}{2m^*}|\mathbf{D}\psi|^2$. We substitute $\psi \rightarrow \psi + \delta\psi$ and $\psi^* \rightarrow \psi^* + \delta\psi^*$, then expand to first order.

First, note that $|\mathbf{D}\psi|^2 = (\mathbf{D}\psi)^* \cdot (\mathbf{D}\psi)$. When we vary $\psi$:

$$
\mathbf{D}(\psi + \delta\psi) = \mathbf{D}\psi + \mathbf{D}\delta\psi
$$

Now substitute into the kinetic term:

$$
|\mathbf{D}(\psi + \delta\psi)|^2 = (\mathbf{D}\psi + \mathbf{D}\delta\psi)^* \cdot (\mathbf{D}\psi + \mathbf{D}\delta\psi)
$$

$$
= (\mathbf{D}\psi)^* \cdot (\mathbf{D}\psi) + (\mathbf{D}\delta\psi)^* \cdot (\mathbf{D}\psi) + (\mathbf{D}\psi)^* \cdot (\mathbf{D}\delta\psi) + O((\delta\psi)^2)
$$

The variation (first-order terms) is:

$$
\delta(|\mathbf{D}\psi|^2) = (\mathbf{D}\delta\psi)^* \cdot (\mathbf{D}\psi) + (\mathbf{D}\psi)^* \cdot (\mathbf{D}\delta\psi)
$$

Similarly, varying $\psi^* \rightarrow \psi^* + \delta\psi^*$ while keeping $\psi$ fixed:

$$
\delta(|\mathbf{D}\psi|^2) = (\mathbf{D}\delta\psi^*) \cdot (\mathbf{D}\psi) = [(i\hbar\nabla - \frac{e^*}{c}\mathbf{A})\delta\psi^*] \cdot (\mathbf{D}\psi)
$$

where we used $(\mathbf{D}\psi)^* = (i\hbar\nabla - \frac{e^*}{c}\mathbf{A})\psi^*$. Therefore:

$$
\delta\mathcal{T} = \frac{1}{2m^*}[(i\hbar\nabla - \frac{e^*}{c}\mathbf{A})\delta\psi^*] \cdot (\mathbf{D}\psi)
$$

**Step 3: Integration by parts**

We need to evaluate the integral:

$$
\int d^3r \, \delta\mathcal{T} = \frac{1}{2m^*}\int d^3r \, [(i\hbar\nabla - \frac{e^*}{c}\mathbf{A})\delta\psi^*] \cdot (\mathbf{D}\psi)
$$

Writing out the components with $D_j = -i\hbar\partial_j - \frac{e^*}{c}A_j$:

$$
= \frac{1}{2m^*}\int d^3r \sum_j (i\hbar\partial_j - \frac{e^*}{c}A_j)\delta\psi^* \cdot D_j\psi
$$

Integrate by parts (assuming boundary terms vanish):

$$
= -\frac{1}{2m^*}\int d^3r \sum_j \delta\psi^* \cdot (i\hbar\partial_j - \frac{e^*}{c}A_j)D_j\psi
$$

$$
= \frac{1}{2m^*}\int d^3r \, \delta\psi^* \cdot \mathbf{D}^2\psi
$$

where $\mathbf{D}^2 = \left(-i\hbar\nabla - \frac{e^*}{c}\mathbf{A}\right)^2$ and we used $(i\hbar\partial_j - \frac{e^*}{c}A_j) = -D_j$.

**Step 4: Collect all terms**

The total variation of the free energy is:

$$
\delta F = \int d^3r \, \delta\psi^*\left[\alpha\psi + \beta|\psi|^2\psi + \frac{1}{2m^*}\mathbf{D}^2\psi\right]
$$

Since $\delta\psi^*$ is arbitrary, the integrand must vanish:

$$
\alpha\psi + \beta|\psi|^2\psi + \frac{1}{2m^*}\left(-i\hbar\nabla - \frac{e^*}{c}\mathbf{A}\right)^2\psi = 0
$$

This is the **first Ginzburg-Landau equation** — a non-linear Schrödinger equation for Cooper pairs.

#### B.4.4 Second GL Equation: Variation with respect to $\mathbf{A}$

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

**Step 2: Magnetic field term variation by direct substitution**

Start with $\mathbf{B} = \nabla \times \mathbf{A}$. Under the variation $\mathbf{A} \rightarrow \mathbf{A} + \delta\mathbf{A}$:

$$
\mathbf{B}[\mathbf{A} + \delta\mathbf{A}] = \nabla \times (\mathbf{A} + \delta\mathbf{A}) = \underbrace{\nabla \times \mathbf{A}}_{\mathbf{B}} + \underbrace{\nabla \times \delta\mathbf{A}}_{\delta\mathbf{B}} = \mathbf{B} + \delta\mathbf{B}
$$

Now compute $\mathbf{B}^2$ with the varied vector potential:

$$
\mathbf{B}^2[\mathbf{A} + \delta\mathbf{A}] = (\mathbf{B} + \delta\mathbf{B})^2 = \mathbf{B}^2 + 2\mathbf{B} \cdot \delta\mathbf{B} + (\delta\mathbf{B})^2
$$

To first order in $\delta\mathbf{A}$:

$$
\delta(\mathbf{B}^2) = \mathbf{B}^2[\mathbf{A} + \delta\mathbf{A}] - \mathbf{B}^2[\mathbf{A}] = 2\mathbf{B} \cdot \delta\mathbf{B} = 2\mathbf{B} \cdot (\nabla \times \delta\mathbf{A})
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

#### B.4.5 Physical Consequences: Characteristic Lengths

**Coherence Length $\xi$**

In zero magnetic field ($\mathbf{A} = 0$), far from boundaries, the first GL equation reduces to:

$$
-\frac{\hbar^2}{2m^*}\nabla^2\psi + \alpha\psi + \beta|\psi|^2\psi = 0
$$

This is a non-linear Schrödinger equation. To find the characteristic length scale over which $\psi$ varies, we **linearize** the equation around the bulk equilibrium value.

**Step 1: Setup and Linearization Procedure**

Near $T_c$, we write the order parameter as:

$$
\psi(\mathbf{r}) = \psi_\infty + \delta\psi(\mathbf{r})
$$

where:
- $\psi_\infty$ is the uniform bulk value with $|\psi_\infty|^2 = -\alpha/\beta$ (from minimizing the homogeneous free energy)
- $\delta\psi(\mathbf{r})$ is a small spatially-varying perturbation

The linearization procedure involves:
1. Substitute $\psi = \psi_\infty + \delta\psi$ into the GL equation
2. Expand to first order in $\delta\psi$ (dropping higher-order terms)
3. Use the fact that $\psi_\infty$ satisfies the bulk equilibrium condition

**Step 2: Detailed Expansion of the Potential Term**

The potential term $\alpha\psi + \beta|\psi|^2\psi$ expands as:

$$
\alpha(\psi_\infty + \delta\psi) + \beta(\psi_\infty + \delta\psi)(\psi_\infty^* + \delta\psi^*)(\psi_\infty + \delta\psi)
$$

Expanding the product:

$$
= \alpha\psi_\infty + \alpha\delta\psi + \beta|\psi_\infty|^2\psi_\infty + \beta(2|\psi_\infty|^2\delta\psi + \psi_\infty^2\delta\psi^*) + O((\delta\psi)^2)
$$

The **zeroth-order terms** cancel because $\psi_\infty$ satisfies the bulk condition:

$$
\alpha\psi_\infty + \beta|\psi_\infty|^2\psi_\infty = \psi_\infty(\alpha + \beta|\psi_\infty|^2) = \psi_\infty(\alpha - \alpha) = 0
$$

Keeping only **linear terms** and assuming $\delta\psi$ is real for simplicity (the phase fluctuations decouple):

$$
\alpha\delta\psi + 2\beta|\psi_\infty|^2\delta\psi = \alpha\delta\psi - 2\alpha\delta\psi = -\alpha\delta\psi
$$

where we used $|\psi_\infty|^2 = -\alpha/\beta$.

**Step 3: The Linearized GL Equation**

Substituting back into the GL equation:

$$
-\frac{\hbar^2}{2m^*}\nabla^2\delta\psi - \alpha\delta\psi = 0
$$

Rearranging (and using $-\alpha = |\alpha|$ since $\alpha < 0$ below $T_c$):

$$
\nabla^2\delta\psi - \frac{2m^*|\alpha|}{\hbar^2}\delta\psi = 0
$$

This is the **linearized Ginzburg-Landau equation** — a Helmholtz equation that describes how small perturbations to the order parameter relax back to the bulk value.

**Step 4: Solving for the Coherence Length**

Consider a 1D geometry with a perturbation at the boundary ($x = 0$). The equation becomes:

$$
\frac{d^2\delta\psi}{dx^2} = \frac{2m^*|\alpha|}{\hbar^2}\delta\psi
$$

This is a second-order linear ODE with constant coefficients. The characteristic equation is:

$$
r^2 = \frac{2m^*|\alpha|}{\hbar^2} \quad \Rightarrow \quad r = \pm\frac{1}{\xi}
$$

where we define the **coherence length**:

$$
\xi = \sqrt{\frac{\hbar^2}{2m^*|\alpha|}} = \sqrt{\frac{\hbar^2}{2m^*\alpha_0|T_c - T|}}
$$

The general solution is:

$$
\delta\psi(x) = A e^{-x/\xi} + B e^{x/\xi}
$$

**Step 5: Applying Boundary Conditions**

For a physically acceptable solution in a semi-infinite superconductor ($x > 0$):
- At $x = 0$: $\delta\psi(0) = \delta\psi_0$ (given perturbation)
- As $x \rightarrow \infty$: $\delta\psi \rightarrow 0$ (returns to bulk value)

The second condition requires $B = 0$ (otherwise the solution diverges). With $A = \delta\psi_0$:

$$
\delta\psi(x) = \delta\psi_0 \, e^{-x/\xi}
$$

**Physical Interpretation:** The coherence length $\xi$ characterizes the **exponential healing length** over which the superconducting order parameter recovers from a perturbation. It represents the "stiffness" or rigidity of the superconducting state—spatial variations in $\psi$ are suppressed over distances larger than $\xi$. The **coherence length diverges as $T \rightarrow T_c$** (as $|T_c - T|^{-1/2}$) because the restoring force (proportional to $|\alpha| \propto |T_c - T|$) vanishes at the phase transition, making the order parameter increasingly susceptible to spatial fluctuations.

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

#### B.4.6 Type I vs Type II Superconductors

**The GL Parameter**

The ratio of the two characteristic length scales defines the **Ginzburg-Landau parameter**:

$$
\kappa = \frac{\lambda}{\xi} = \frac{m^*c}{\hbar e^*}\sqrt{\frac{\beta}{2\pi}}
$$

Remarkably, $\kappa$ is **temperature-independent** within GL theory (both $\lambda$ and $\xi$ diverge as $|T_c - T|^{-1/2}$ with the same critical exponent), making it a fundamental material property that determines the superconductor type.

**Thermodynamic Critical Field $H_c$ — Detailed Definition**

The **thermodynamic critical field** $H_c$ is defined as the magnetic field at which the **magnetic energy density equals the superconducting condensation energy density**. To derive this:

1. The condensation energy density (difference between normal and superconducting free energy densities) is:
   $$
   f_n - f_s = \frac{\alpha^2}{2\beta}
   $$
   
2. The magnetic energy density associated with a field $H$ is:
   $$
   f_{mag} = \frac{H^2}{8\pi}
   $$

Equating these gives:

$$
\frac{H_c^2}{8\pi} = \frac{\alpha^2}{2\beta} = f_n - f_s
$$

**Physical interpretation:** $H_c$ represents the thermodynamic field at which the energy cost of expelling magnetic flux equals the energy gain from superconducting condensation. In a **type I** superconductor (neglecting geometric effects), this is the field at which the first-order transition to the normal state occurs.

**Interface Energy $\sigma_{ns}$ — Physical Meaning and Detailed Derivation**

The **interface energy** (also called surface tension) $\sigma_{ns}$ is the **excess free energy per unit area** associated with a boundary between normal and superconducting regions. Physically, it answers the question: *How much energy does it cost to create a unit area of normal-superconducting interface?*

To understand this, consider a planar interface at $x = 0$:
- For $x < 0$: Normal metal ($\psi = 0$, magnetic field $H$ penetrates)
- For $x > 0$: Superconductor ($\psi \rightarrow \psi_\infty$, field expelled)

At such an interface, two competing physical effects occur over different length scales:

**Effect 1: Order Parameter Suppression (over distance $\sim \xi$)**

The superconducting order parameter cannot change discontinuously from $\psi = 0$ to $\psi = \psi_\infty$. Instead, it rises smoothly over a distance $\sim \xi$. This spatial variation has two consequences:
- **Kinetic energy cost**: The gradient term $\frac{1}{2m^*}|\nabla\psi|^2$ contributes positive energy
- **Reduced condensation energy**: Near the interface, $|\psi| < |\psi_\infty|$, so the system doesn't gain the full condensation energy

The energy cost per unit area is approximately:

$$
\sigma_\psi \sim \xi \cdot \frac{H_c^2}{8\pi}
$$

**Effect 2: Magnetic Field Penetration (over distance $\sim \lambda$)**

The magnetic field cannot be expelled discontinuously at the interface. Instead, it penetrates into the superconductor over a distance $\sim \lambda$ (the Meissner effect with exponential decay). This partial penetration:
- **Reduces the magnetic energy cost**: The system doesn't have to fully expel the field in the penetration layer
- Provides an **energy gain** relative to complete flux expulsion

The energy gain per unit area is approximately:

$$
\sigma_B \sim \lambda \cdot \frac{H_c^2}{8\pi}
$$

**Net Interface Energy and Its Sign**

The total interface energy is the sum of these competing contributions:

$$
\sigma_{ns} = \sigma_\psi - \sigma_B \approx \frac{H_c^2}{8\pi}(\xi - \lambda)
$$

The **sign** of $\sigma_{ns}$ determines the behavior of the superconductor:

| Sign | Condition | Physical Meaning | Behavior |
|------|-----------|------------------|----------|
| **Positive** ($\sigma_{ns} > 0$) | $\xi > \lambda$ ($\kappa < 1/\sqrt{2}$) | It **costs energy** to create an interface | System minimizes interfaces → **Meissner state** with complete flux expulsion |
| **Negative** ($\sigma_{ns} < 0$) | $\xi < \lambda$ ($\kappa > 1/\sqrt{2}$) | System **gains energy** by creating interfaces | Favors many interfaces → **Vortex state** with flux penetration |

**Physical Interpretation of the Two Regimes:**

- **Type I ($\sigma_{ns} > 0$)**: Creating normal-superconducting boundaries is energetically unfavorable. The system expels all magnetic flux until $H_c$ is reached, then undergoes a first-order phase transition to the normal state.

- **Type II ($\sigma_{ns} < 0$)**: The system can lower its free energy by creating normal regions (vortex cores) within the superconductor. Magnetic flux penetrates in discrete quanta, each surrounded by a superconducting region.

**Why $\kappa = 1/\sqrt{2}$ is the Universal Threshold**

Abrikosov's exact calculation (1957) gives:

$$
\sigma_{ns} = \frac{H_c^2}{8\pi} \cdot \xi \cdot \frac{4}{3}(\sqrt{2} - \kappa) \cdot f(\kappa)
$$

where $f(\kappa)$ is a positive function of $\kappa$. The crucial observation is that:

1. The factor $(\sqrt{2} - \kappa)$ determines the **sign** of $\sigma_{ns}$
2. All other factors are always positive

Therefore, the interface energy changes sign exactly when:

$$
\kappa = \kappa_c = \frac{1}{\sqrt{2}} \approx 0.707
$$

This is the **universal critical value** (independent of material details) that separates:

| Type | Condition | Interface Energy | Behavior |
|------|-----------|------------------|----------|
| **Type I** | $\kappa < 1/\sqrt{2}$ | $\sigma_{ns} > 0$ | Complete flux expulsion (Meissner state) |
| **Type II** | $\kappa > 1/\sqrt{2}$ | $\sigma_{ns} < 0$ | Flux penetration via vortices (mixed state) |

**Critical Fields for Type II Superconductors**

For Type II superconductors, there are two critical fields:
- $H_{c1}$: Lower critical field — first vortex enters the sample
- $H_{c2}$: Upper critical field — superconductivity is completely destroyed

These are given by:

$$
H_{c2} = \frac{\Phi_0}{2\pi\xi^2} = \sqrt{2}\kappa H_c, \quad H_{c1} \approx \frac{\Phi_0}{4\pi\lambda^2}\ln\kappa = \frac{H_c}{\sqrt{2}\kappa}\ln\kappa
$$

where $\Phi_0 = hc/e^* = hc/2e$ is the flux quantum.

For $\kappa \gg 1$, the interval $H_{c1} < H < H_{c2}$ is very wide, allowing extensive applications of type II superconductors (e.g., Nb-Ti, Nb₃Sn) in high-field magnets.

#### B.4.7 The Abrikosov Vortex Solution

**Introduction: What is a Vortex?**

In a type II superconductor ($\kappa > 1/\sqrt{2}$), when the applied magnetic field exceeds $H_{c1}$, magnetic flux penetrates the superconductor in the form of **vortices** (also called flux lines or fluxons). Each vortex consists of:
1. A **normal core** (radius $\sim \xi$) where $\psi \approx 0$
2. **Circulating supercurrents** that screen the magnetic field over a distance $\sim \lambda$

A vortex carries exactly **one quantum of magnetic flux**:

$$
\Phi_0 = \frac{hc}{e^*} = \frac{hc}{2e} \approx 2.07 \times 10^{-15} \, \text{Wb}
$$

**Vortex Ansatz and Variable Separation**

For a single straight vortex along the $z$-axis, we use cylindrical coordinates $(r, \theta, z)$. Due to cylindrical symmetry:

1. The order parameter has the form of a **vortex ansatz**:
   $$
   \psi(r, \theta) = f(r)e^{in\theta}
   $$
   where:
   - $n$ is the winding number (vorticity), a positive integer
   - $f(r)$ is a real radial function (the amplitude profile)
   - The phase factor $e^{in\theta}$ ensures that $\psi$ winds $n$ times around the origin

2. The vector potential is purely azimuthal:
   $$
   \mathbf{A} = A_\theta(r)\hat{\mathbf{\theta}}
   $$

**Boundary Conditions — Detailed Specification**

For the order parameter amplitude $f(r)$:

| Limit | Condition | Physical Reason |
|-------|-----------|-----------------|
| $r \rightarrow 0$ | $f(r) \rightarrow 0$ | Normal state at core center (suppressed superconductivity) |
| $r \rightarrow \infty$ | $f(r) \rightarrow \psi_\infty = \sqrt{-\alpha/\beta}$ | Recovers bulk superconducting value far from core |
| $r \rightarrow 0$ | $f(r) \sim r^n$ (regular behavior) | Finite energy requires regular solution at origin |

For the vector potential $A_\theta(r)$:

| Limit | Condition | Physical Reason |
|-------|-----------|-----------------|
| $r \rightarrow 0$ | $A_\theta \rightarrow 0$ | Regular at origin (no singularities) |
| $r \rightarrow \infty$ | $B(r) = \frac{1}{r}\frac{d}{dr}(rA_\theta) \rightarrow 0$ | Magnetic field screened far from vortex |
| $r \rightarrow \infty$ | $\oint \mathbf{A} \cdot d\mathbf{l} = 2\pi r A_\theta \rightarrow \frac{n\Phi_0}{2\pi}$ | Flux quantization condition |

**Deriving the Coupled Differential Equations — Step by Step**

**Step 1: The Covariant Derivative in Cylindrical Coordinates**

The covariant derivative is $\mathbf{D} = -i\hbar\nabla - \frac{e^*}{c}\mathbf{A}$. Acting on $\psi = f(r)e^{in\theta}$:

$$
\mathbf{D}\psi = -i\hbar\left(\frac{df}{dr}\hat{\mathbf{r}} + \frac{in f}{r}\hat{\mathbf{\theta}}\right)e^{in\theta} - \frac{e^*}{c}A_\theta f e^{in\theta}\hat{\mathbf{\theta}}
$$

$$
= -i\hbar\frac{df}{dr}e^{in\theta}\hat{\mathbf{r}} + \hbar\left(\frac{n}{r} - \frac{e^*A_\theta}{\hbar c}\right)f e^{in\theta}\hat{\mathbf{\theta}}
$$

The **kinetic term** involves $\mathbf{D}^2\psi$:

$$
\mathbf{D}^2\psi = -\hbar^2\left[\frac{1}{r}\frac{d}{dr}\left(r\frac{df}{dr}\right) - \left(\frac{n}{r} - \frac{e^*A_\theta}{\hbar c}\right)^2 f\right]e^{in\theta}
$$

**Step 2: First GL Equation for $f(r)$**

Substituting into $\alpha\psi + \beta|\psi|^2\psi + \frac{1}{2m^*}\mathbf{D}^2\psi = 0$ and canceling the phase factor $e^{in\theta}$:

$$
-\frac{\hbar^2}{2m^*}\left[\frac{1}{r}\frac{d}{dr}\left(r\frac{df}{dr}\right) - \left(\frac{n}{r} - \frac{e^*A_\theta}{\hbar c}\right)^2 f\right] + \alpha f + \beta f^3 = 0
$$

Expanding the radial derivative and rearranging:

$$
\frac{d^2f}{dr^2} + \frac{1}{r}\frac{df}{dr} - \frac{n^2}{r^2}f\left(1 - \frac{e^*A_\theta r}{n\hbar c}\right)^2 - \frac{2m^*\alpha}{\hbar^2}f + \frac{2m^*\beta}{\hbar^2}f^3 = 0
$$

**Step 3: Second GL Equation for $A_\theta(r)$**

From Ampère's law $\nabla \times \mathbf{B} = \frac{4\pi}{c}\mathbf{j}$ with:
- Magnetic field: $\mathbf{B} = B(r)\hat{\mathbf{z}} = \frac{1}{r}\frac{d}{dr}(rA_\theta)\hat{\mathbf{z}}$
- Current density: $\mathbf{j} = j_\theta(r)\hat{\mathbf{\theta}}$

The radial component of Ampère's law gives:

$$-\frac{dB}{dr} = \frac{4\pi}{c}j_\theta$$

The supercurrent density is derived from:

$$
j_\theta = \frac{e^*\hbar}{m^*}\left(\frac{n}{r} - \frac{e^*A_\theta}{\hbar c}\right)f^2$$

Substituting and rearranging:

$$
\frac{d}{dr}\left[\frac{1}{r}\frac{d}{dr}(rA_\theta)\right] = -\frac{4\pi e^*\hbar}{m^*c}\left(\frac{n}{r} - \frac{e^*A_\theta}{\hbar c}\right)f^2
$$

Or equivalently:

$$
\frac{d^2A_\theta}{dr^2} + \frac{1}{r}\frac{dA_\theta}{dr} - \frac{A_\theta}{r^2} = -\frac{4\pi e^*\hbar n}{m^*c r}f^2\left(1 - \frac{e^*A_\theta r}{n\hbar c}\right)
$$

**Summary: The Complete Coupled Vortex Equations**

Introducing dimensionless variables $\tilde{r} = r/\xi$, $\tilde{f} = f/\psi_\infty$, and expressing $A_\theta$ in appropriate units, the vortex equations become:

$$
\boxed{\begin{aligned}
\frac{d^2f}{dr^2} + \frac{1}{r}\frac{df}{dr} &= \frac{n^2}{r^2}f\left(1 - \frac{r A_\theta}{n \lambda^2 H_{c2}}\right)^2 + \frac{f^3 - f}{\xi^2} \\[8pt]
\frac{d^2A_\theta}{dr^2} + \frac{1}{r}\frac{dA_\theta}{dr} - \frac{A_\theta}{r^2} &= \frac{f^2}{\lambda^2}\left(\frac{n\Phi_0}{2\pi r} - A_\theta\right)
\end{aligned}}
$$

where we use $|\psi_\infty|^2 = -\alpha/\beta$, $\xi^2 = \hbar^2/(2m^*|\alpha|)$, and $\lambda^2 = m^*c^2/(4\pi(e^*)^2|\psi_\infty|^2)$.

**Step 4: Solution Strategy and Asymptotic Analysis**

These coupled non-linear ODEs generally require numerical solution. However, we can obtain analytical insights in limiting cases:

**Case A: Near the Core ($r \ll \xi$)**

In the core region:
- $f \approx 0$ (order parameter suppressed)
- The non-linear term $\beta f^3$ is negligible
- The equation for $f$ simplifies to:

$$
\frac{d^2f}{dr^2} + \frac{1}{r}\frac{df}{dr} - \frac{n^2}{r^2}f \approx 0
$$

This is the **modified Bessel equation of order $n$** (in a different form). The solution regular at $r = 0$ is:

$$
f(r) \propto r^n \quad \text{for } r \ll \xi
$$

For the lowest vorticity ($n = 1$), $f \propto r$, showing linear growth from the center.

**Case B: Far from the Core ($r \gg \lambda$)**

In the outer region:
- $f \approx \psi_\infty$ (order parameter saturated)
- The current vanishes as the field is screened
- The equation for $A_\theta$ gives exponential decay:

$$
B(r) = \frac{1}{r}\frac{d}{dr}(rA_\theta) \approx \frac{\Phi_0}{2\pi\lambda^2}K_0\left(\frac{r}{\lambda}\right)
$$

where $K_0$ is the modified Bessel function of the second kind. For large arguments:

$$
B(r) \propto \frac{e^{-r/\lambda}}{\sqrt{r}} \quad \text{as } r \rightarrow \infty
$$

**Step 5: Vortex Energy and Interaction**

The energy per unit length of a single vortex is:

$$
\epsilon = \left(\frac{\Phi_0}{4\pi\lambda}\right)^2\ln\kappa = \frac{\Phi_0 H_{c1}}{4\pi}
$$

for $\kappa \gg 1$. The logarithmic divergence at large distances is cut off by:
- The London penetration depth $\lambda$ (for isolated vortex)
- Inter-vortex spacing (for vortex lattice)

**Physical Picture: Three Distinct Regions**

| Region | Range | Characteristics |
|--------|-------|-----------------|
| **Core** | $r < \xi$ | Normal state ($\psi \approx 0$), magnetic field maximum, high energy density |
| **Intermediate** | $\xi < r < \lambda$ | $\psi$ rises to bulk value, strong supercurrents, field being screened |
| **Outer** | $r > \lambda$ | Bulk superconductor ($\psi \approx \psi_\infty$), exponentially decaying field and currents |

The vortex represents a topological defect in the superconducting order parameter, stabilized by the quantization of magnetic flux and the energetic preference for type II superconductors to form normal-superconducting interfaces.

#### B.4.8 Connection to BCS Theory

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
