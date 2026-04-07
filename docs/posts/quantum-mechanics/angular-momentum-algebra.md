---
title: "Angular Momentum Algebra and Its Applications"
description: "Comprehensive treatment of angular momentum theory: algebraic structure, spin systems, Clebsch-Gordan coefficients, central force fields, and identical particle systems"
date: 2026-04-04
tags: ["quantum mechanics", "angular momentum", "spin", "Clebsch-Gordan coefficients", "central force field", "identical particles"]
category: "quantum-mechanics"
math: true
---

# Angular Momentum Algebra and Its Applications

This article presents a systematic treatment of angular momentum theory in quantum mechanics. We begin with the fundamental algebraic structure—commutation relations and ladder operators—then develop the matrix representations and explicit wave function formalism (spherical harmonics) for orbital angular momentum. Building on this foundation, we explore the addition of angular momenta and the resulting Clebsch-Gordan theory. The middle sections develop the deeper group-theoretic perspective (rotation groups SO(3) and SU(2)), including SU(3) flavor and color symmetries. The article concludes with applications to atomic physics coupling schemes and central force fields, including the hidden SO(4) symmetry of the hydrogen atom.

The logical progression follows: **Algebraic Structure** → **Representation Theory** → **Wave Function Realization** → **Angular Momentum Addition** → **Group Theory** → **Atomic Physics Applications** → **Central Force Fields**.

---

## Part I: Fundamental Commutation Relations and Algebraic Structure

### 1.1 Definition of Angular Momentum Operators

In quantum mechanics, angular momentum is defined through operators satisfying specific commutation relations. We begin with **orbital angular momentum** because it has a concrete expression in terms of position and momentum operators, allowing us to verify the commutation relations explicitly:

$$\mathbf{L} = \mathbf{r} \times \mathbf{p}$$

In component form:

$$L_x = yp_z - zp_y, \quad L_y = zp_x - xp_z, \quad L_z = xp_y - yp_x$$

**Fundamental Commutation Relations**

The canonical commutation relations $[x_i, p_j] = i\hbar\delta_{ij}$ lead to:

$$\boxed{[L_i, L_j] = i\hbar\varepsilon_{ijk}L_k}$$

or explicitly:

$$[L_x, L_y] = i\hbar L_z, \quad [L_y, L_z] = i\hbar L_x, \quad [L_z, L_x] = i\hbar L_y$$

**Proof for $[L_x, L_y]$**

$$L_x = yp_z - zp_y, \quad L_y = zp_x - xp_z$$

$$[L_x, L_y] = [yp_z - zp_y, zp_x - xp_z]$$

Expanding:
$$= [yp_z, zp_x] - [yp_z, xp_z] - [zp_y, zp_x] + [zp_y, xp_z]$$

Since $y$ commutes with $z$, $p_x$, and $p_z$:
$$[yp_z, zp_x] = y[p_z, z]p_x = y(-i\hbar)p_x = -i\hbar yp_x$$

Since $y$ and $p_z$ commute with $x$ and $p_z$:
$$[yp_z, xp_z] = 0$$

Since $z$ and $p_y$ commute with $z$ and $p_x$:
$$[zp_y, zp_x] = 0$$

For the last term:
$$[zp_y, xp_z] = x[z, p_z]p_y = x(i\hbar)p_y = i\hbar xp_y$$

Combining:
$$[L_x, L_y] = -i\hbar yp_x + i\hbar xp_y = i\hbar(xp_y - yp_x) = i\hbar L_z$$

### 1.2 The General Angular Momentum Algebra

The commutation relations define an abstract angular momentum algebra. We define a general angular momentum operator $\mathbf{J}$ satisfying:

$$\boxed{[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k}$$

This applies to:
- **Orbital angular momentum**: $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ (integer eigenvalues)
- **Spin angular momentum**: Intrinsic angular momentum (integer or half-integer)
- **Total angular momentum**: $\mathbf{J} = \mathbf{L} + \mathbf{S}$ (combined systems)

**Important Properties**

The total angular momentum squared:
$$J^2 = J_x^2 + J_y^2 + J_z^2$$

commutes with all components:

$$\boxed{[J^2, J_i] = 0}$$

**Proof for $[J^2, J_z]$**

$$[J^2, J_z] = [J_x^2 + J_y^2 + J_z^2, J_z] = [J_x^2, J_z] + [J_y^2, J_z]$$

Using $[AB, C] = A[B, C] + [A, C]B$:
$$[J_x^2, J_z] = J_x[J_x, J_z] + [J_x, J_z]J_x = J_x(-i\hbar J_y) + (-i\hbar J_y)J_x = -i\hbar(J_xJ_y + J_yJ_x)$$

$$[J_y^2, J_z] = J_y[J_y, J_z] + [J_y, J_z]J_y = J_y(i\hbar J_x) + (i\hbar J_x)J_y = i\hbar(J_yJ_x + J_xJ_y)$$

Adding:
$$[J^2, J_z] = -i\hbar(J_xJ_y + J_yJ_x) + i\hbar(J_yJ_x + J_xJ_y) = 0$$

### 1.3 Simultaneous Eigenstates

Since $[J^2, J_z] = 0$, these operators have simultaneous eigenstates. We denote:

$$J^2|j, m\rangle = \hbar^2 j(j+1)|j, m\rangle$$
$$J_z|j, m\rangle = \hbar m|j, m\rangle$$

where $j$ is the total angular momentum quantum number and $m$ is the magnetic quantum number.

---

## Part II: Ladder Operators and Eigenvalue Spectrum

### 2.1 Definition of Raising and Lowering Operators

Define the ladder (or step) operators:

$$\boxed{J_+ = J_x + iJ_y, \quad J_- = J_x - iJ_y}$$

**Inverse Relations**

$$J_x = \frac{J_+ + J_-}{2}, \quad J_y = \frac{J_+ - J_-}{2i}$$

### 2.2 Commutation Relations of Ladder Operators

**With $J_z$:**

$$[J_z, J_+] = [J_z, J_x + iJ_y] = [J_z, J_x] + i[J_z, J_y] = i\hbar J_y + i(-i\hbar J_x) = \hbar(J_x + iJ_y) = \hbar J_+$$

$$\boxed{[J_z, J_+] = \hbar J_+}$$

Similarly:
$$\boxed{[J_z, J_-] = -\hbar J_-}$$

**With $J^2$:**

Since $[J^2, J_x] = [J^2, J_y] = 0$:
$$\boxed{[J^2, J_\pm] = 0}$$

### 2.3 Action of Ladder Operators on Eigenstates

Consider $J_z(J_+|j, m\rangle)$:

$$J_z(J_+|j, m\rangle) = (J_+J_z + [J_z, J_+])|j, m\rangle = J_+J_z|j, m\rangle + \hbar J_+|j, m\rangle$$

$$= J_+(\hbar m)|j, m\rangle + \hbar J_+|j, m\rangle = \hbar(m+1)(J_+|j, m\rangle)$$

This shows that $J_+|j, m\rangle$ is an eigenstate of $J_z$ with eigenvalue $\hbar(m+1)$. Therefore:

$$\boxed{J_+|j, m\rangle \propto |j, m+1\rangle}$$

Similarly:
$$\boxed{J_-|j, m\rangle \propto |j, m-1\rangle}$$

This justifies the names "raising" (creation) and "lowering" (annihilation) operators.

### 2.4 Determining the Eigenvalue Spectrum

**Step 1: Constraint from Positivity**

Since $J_x^2$ and $J_y^2$ are positive operators:

$$J^2 - J_z^2 = J_x^2 + J_y^2 \geq 0$$

This gives:
$$j(j+1) \geq m^2$$

This constrains $m$ for a given $j$, but does not yet determine the allowed values.

**Step 2: Finding the Maximum $m$**

Since $m^2 \leq j(j+1)$, the eigenvalue $m$ is bounded. There must exist a maximum value $m_{\max}$ such that:

$$J_+|j, m_{\max}\rangle = 0$$

Otherwise, repeated application of $J_+$ would produce arbitrarily large $m$, violating the bound. To find the value of $m_{\max}$, we use the operator identity:

$$J_-J_+ = J_x^2 + J_y^2 + i[J_x, J_y] = J^2 - J_z^2 - \hbar J_z$$

Applying this operator to $|j, m_{\max}\rangle$, we note that since $J_+|j, m_{\max}\rangle = 0$, we have:

$$J_-J_+|j, m_{\max}\rangle = J_-(J_+|j, m_{\max}\rangle) = J_- \cdot 0 = 0$$

Therefore:

$$(J^2 - J_z^2 - \hbar J_z)|j, m_{\max}\rangle = 0$$

$$\hbar^2 j(j+1) - \hbar^2 m_{\max}^2 - \hbar^2 m_{\max} = 0$$

$$j(j+1) = m_{\max}(m_{\max} + 1)$$

This quadratic equation has solutions $m_{\max} = j$ or $m_{\max} = -j - 1$. 

First, note that $j(j+1) \geq 0$ is required because $m^2 \geq 0$ and $m^2 \leq j(j+1)$. This means either $j \geq 0$ or $j \leq -1$. If $j \leq -1$, we can define $j' = -j-1 \geq 0$, which gives the same eigenvalue $j'(j'+1) = j(j+1)$. Thus, **we can always take $j \geq 0$ without loss of generality**.

With $j \geq 0$, compare the two solutions:
- $m_{\max} = j \geq 0$
- $m_{\max} = -j-1 < 0$

Since $m_{\max}$ must be the **maximum** eigenvalue of $J_z$, it cannot be negative while another valid solution ($j$) is non-negative. Therefore:

$$\boxed{m_{\max} = j}$$

**Step 3: Finding the Minimum $m$**

Similarly, there must exist a minimum value $m_{\min}$ such that:

$$J_-|j, m_{\min}\rangle = 0$$

Using $J_+J_- = J^2 - J_z^2 + \hbar J_z$:

$$J_+J_-|j, m_{\min}\rangle = (J^2 - J_z^2 + \hbar J_z)|j, m_{\min}\rangle = 0$$

$$\hbar^2 j(j+1) - \hbar^2 m_{\min}^2 + \hbar^2 m_{\min} = 0$$

$$j(j+1) = m_{\min}(m_{\min} - 1)$$

This quadratic has solutions $m_{\min} = j + 1$ or $m_{\min} = -j$. Since $j \geq 0$, we have $j + 1 > j = m_{\max}$, which would make $m_{\min} > m_{\max}$—a contradiction. Therefore:

$$\boxed{m_{\min} = -j}$$

Therefore, for a given $j$, the allowed values of $m$ range from $-j$ to $+j$ in integer steps, giving $2j + 1$ states.

**Step 4: Quantization Condition**

Starting from $m = -j$ and applying $J_+$ repeatedly must eventually reach $m = j$. After $n$ applications:

$$m = -j + n = j$$

Therefore:
$$2j = n$$

$$\boxed{j = 0, \frac{1}{2}, 1, \frac{3}{2}, 2, ...}$$

Angular momentum is quantized in integer or half-integer units.

### 2.5 Normalization Constants

To find the proportionality constants, assume:

$$J_+|j, m\rangle = C_+|j, m+1\rangle$$

Using $J_-J_+ = J^2 - J_z^2 - \hbar J_z$, we take the inner product of $J_+|j, m\rangle$ with itself. Recall that $\langle j,m|J_-$ is the Hermitian conjugate of $J_+|j,m\rangle$:

$$(J_+|j, m\rangle)^\dagger = \langle j, m|J_+^\dagger = \langle j, m|J_-$$

Therefore:

$$\langle j, m|J_-J_+|j, m\rangle = (J_+|j, m\rangle)^\dagger (J_+|j, m\rangle) = |C_+|^2\langle j, m+1|j, m+1\rangle = |C_+|^2$$

$$= \langle j, m|(J^2 - J_z^2 - \hbar J_z)|j, m\rangle = \hbar^2[j(j+1) - m^2 - m]$$

$$= \hbar^2(j - m)(j + m + 1)$$

Choosing the phase convention (Condon-Shortley):

$$\boxed{J_+|j, m\rangle = \hbar\sqrt{(j-m)(j+m+1)}|j, m+1\rangle}$$

Similarly:
$$\boxed{J_-|j, m\rangle = \hbar\sqrt{(j+m)(j-m+1)}|j, m-1\rangle}$$

**The Condon-Shortley Convention**

This convention chooses all matrix elements of $J_+$ and $J_-$ to be real and positive, ensuring that CG coefficients are real numbers and results from different textbooks and software are directly comparable.

---

## Part III: Spin Systems and Matrix Representations

### 3.1 Matrix Elements of Angular Momentum Operators

For a given $j$, the $2j+1$ states $|j, m\rangle$ with $m = -j, -j+1, ..., j$ form a basis for a $(2j+1)$-dimensional representation.

**$J_z$ Matrix:**

$$(J_z)_{m'm} = \langle j, m'|J_z|j, m\rangle = \hbar m \delta_{m'm}$$

This is diagonal:
$$J_z = \hbar\begin{pmatrix} j & 0 & \cdots & 0 \\ 0 & j-1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & -j \end{pmatrix}$$

**$J_+$ and $J_-$ Matrices:**

$$(J_+)_{m',m} = \hbar\sqrt{(j-m)(j+m+1)}\delta_{m',m+1}$$

$$(J_-)_{m',m} = \hbar\sqrt{(j+m)(j-m+1)}\delta_{m',m-1}$$

**$J_x$ and $J_y$ Matrices:**

$$J_x = \frac{J_+ + J_-}{2}, \quad J_y = \frac{J_+ - J_-}{2i}$$

### 3.2 Spin-1/2 System (j = 1/2)

For $j = 1/2$, there are two states: $|1/2, 1/2\rangle \equiv |\uparrow\rangle$ and $|1/2, -1/2\rangle \equiv |\downarrow\rangle$.

**Matrix Elements:**

$$J_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \frac{\hbar}{2}\sigma_z$$

$$J_+ = \hbar\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$$

$$J_- = \hbar\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$$

$$J_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \frac{\hbar}{2}\sigma_x$$

$$J_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \frac{\hbar}{2}\sigma_y$$

The matrices $\sigma_i$ are the **Pauli matrices**:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Properties of Pauli Matrices**

$$\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = I$$

$$[\sigma_i, \sigma_j] = 2i\varepsilon_{ijk}\sigma_k$$

$$\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$$

$$\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$$

**Spin Operators in Terms of Pauli Matrices**

$$\mathbf{S} = \frac{\hbar}{2}\boldsymbol{\sigma}$$

### 3.3 Spin-1 System (j = 1)

For $j = 1$, the basis is $|1, 1\rangle$, $|1, 0\rangle$, $|1, -1\rangle$.

$$S_z = \hbar\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}$$

$$S_+ = \hbar\begin{pmatrix} 0 & \sqrt{2} & 0 \\ 0 & 0 & \sqrt{2} \\ 0 & 0 & 0 \end{pmatrix}, \quad S_- = \hbar\begin{pmatrix} 0 & 0 & 0 \\ \sqrt{2} & 0 & 0 \\ 0 & \sqrt{2} & 0 \end{pmatrix}$$

$$S_x = \frac{\hbar}{\sqrt{2}}\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \quad S_y = \frac{\hbar}{\sqrt{2}}\begin{pmatrix} 0 & -i & 0 \\ i & 0 & -i \\ 0 & i & 0 \end{pmatrix}$$

### 3.4 Higher Spin Systems

**Spin-3/2 System**

For $j = 3/2$, the matrices are $4 \times 4$. The basis states are $|3/2, 3/2\rangle$, $|3/2, 1/2\rangle$, $|3/2, -1/2\rangle$, $|3/2, -3/2\rangle$.

$$S_z = \frac{\hbar}{2}\begin{pmatrix} 3 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -3 \end{pmatrix}$$

$$S_+ = \hbar\begin{pmatrix} 0 & \sqrt{3} & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & \sqrt{3} \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

The off-diagonal matrix elements follow the general formula $\hbar\sqrt{(j-m)(j+m+1)}$.

---

## Part IV: Addition of Angular Momenta and Clebsch-Gordan Coefficients

Having established the algebraic structure of angular momentum and explored its matrix representations, we now turn to the problem of combining multiple angular momenta. This is essential for systems with multiple particles or for coupling orbital and spin angular momenta. The key mathematical tool for this is the **Clebsch-Gordan decomposition**, which expresses the tensor product of two angular momentum representations as a direct sum of irreducible representations.

### 4.1 Tensor Product Space

Consider two independent angular momenta $\mathbf{J}_1$ and $\mathbf{J}_2$ with:

$$[J_{1i}, J_{2j}] = 0$$

The uncoupled basis is:
$$|j_1, m_1; j_2, m_2\rangle = |j_1, m_1\rangle \otimes |j_2, m_2\rangle$$

with $(2j_1+1)(2j_2+1)$ states.

### 4.2 Total Angular Momentum

Define the total angular momentum:

$$\mathbf{J} = \mathbf{J}_1 + \mathbf{J}_2$$

**Commutation Verification**

$$[J_i, J_j] = [J_{1i} + J_{2i}, J_{1j} + J_{2j}]$$

$$= [J_{1i}, J_{1j}] + [J_{1i}, J_{2j}] + [J_{2i}, J_{1j}] + [J_{2i}, J_{2j}]$$

$$= i\hbar\varepsilon_{ijk}J_{1k} + 0 + 0 + i\hbar\varepsilon_{ijk}J_{2k} = i\hbar\varepsilon_{ijk}(J_{1k} + J_{2k})$$

$$= i\hbar\varepsilon_{ijk}J_k$$

### 4.3 Clebsch-Gordan Expansion

The total angular momentum $J^2$ and $J_z$ have eigenstates:

$$|j, m\rangle = \sum_{m_1, m_2} \langle j_1, m_1; j_2, m_2|j, m\rangle |j_1, m_1; j_2, m_2\rangle$$

where $\langle j_1, m_1; j_2, m_2|j, m\rangle$ are the **Clebsch-Gordan (CG) coefficients**.

**Selection Rule**: $m = m_1 + m_2$

### 4.4 Determining Allowed Values of Total $j$

**Constraint**: $m = m_1 + m_2$ since $J_z = J_{1z} + J_{2z}$.

**Maximum $j$:** When $m_1 = j_1$ and $m_2 = j_2$, we get $m = j_1 + j_2$. This is the maximum possible, so:

$$j_{\max} = j_1 + j_2$$

**Counting States:** The uncoupled basis has $(2j_1+1)(2j_2+1)$ states. The coupled basis must have the same number:

$$\sum_{j=j_{\min}}^{j_{\max}}(2j+1) = (2j_1+1)(2j_2+1)$$

Using $\sum_{j=0}^{n}(2j+1) = (n+1)^2$:

$$\sum_{j=j_{\min}}^{j_1+j_2}(2j+1) = (j_1+j_2+1)^2 - j_{\min}^2$$

Setting equal to $(2j_1+1)(2j_2+1)$:

$$(j_1+j_2+1)^2 - j_{\min}^2 = (2j_1+1)(2j_2+1)$$

Solving for $j_{\min}$:

$$\boxed{j_{\min} = |j_1 - j_2|}$$

**Triangle Rule:**
$$\boxed{j = |j_1 - j_2|, |j_1 - j_2| + 1, ..., j_1 + j_2}$$

**Important Distinction from Classical Vector Addition:**

While this looks similar to classical vector addition ($|\mathbf{J}_1 - \mathbf{J}_2| \leq J \leq J_1 + J_2$), there is a crucial difference:

**Classically:** The magnitude of the resultant vector can take *any continuous value* within the range.

**Quantum Mechanically:** The total angular momentum quantum number $j$ is **quantized**—it can only take values differing by integers. If $j_1$ and $j_2$ are both integers or both half-integers, $j$ takes integer values. If one is integer and the other half-integer, $j$ takes half-integer values.

**Example:** For $j_1 = 2$ and $j_2 = 1$:
- Classical: $1 \leq J \leq 3$ (any real number)
- Quantum: $j \in \{1, 2, 3\}$ (only these three discrete values)

The "triangle rule" name comes from the geometric picture where the three angular momentum vectors form a triangle, but remember that in quantum mechanics, the lengths of these vectors are quantized as $\sqrt{j(j+1)}\hbar$, not arbitrary values.

### 4.5 General CG Coefficient Derivation from Matrix Elements

**Setting Up the Problem:**

We want to express the coupled basis states $|j, m\rangle$ in terms of the uncoupled basis $|j_1, m_1; j_2, m_2\rangle$:

$$|j, m\rangle = \sum_{m_1, m_2} C^{j, m}_{j_1, m_1; j_2, m_2} |j_1, m_1; j_2, m_2\rangle$$

where $C^{j, m}_{j_1, m_1; j_2, m_2} = \langle j_1, m_1; j_2, m_2|j, m\rangle$ are the CG coefficients.

**Key Constraint: $m = m_1 + m_2$**

Since $J_z = J_{1z} + J_{2z}$, we have:
$$J_z|j, m\rangle = \hbar m |j, m\rangle$$

Acting on the expansion:
$$\sum_{m_1, m_2} C^{j, m}_{j_1, m_1; j_2, m_2} (\hbar m_1 + \hbar m_2)|j_1, m_1; j_2, m_2\rangle = \hbar m \sum_{m_1, m_2} C^{j, m}_{j_1, m_1; j_2, m_2}|j_1, m_1; j_2, m_2\rangle$$

This requires:
$$\boxed{(m_1 + m_2)C^{j, m}_{j_1, m_1; j_2, m_2} = m C^{j, m}_{j_1, m_1; j_2, m_2}}$$

Therefore, $C^{j, m}_{j_1, m_1; j_2, m_2} = 0$ unless $m = m_1 + m_2$. This reduces the double sum to a single sum over $m_1$ (with $m_2 = m - m_1$).

**Step 1: Constructing the Highest Weight State**

**What is "Highest Weight"?**

In representation theory, a **weight** is the eigenvalue of a state under the action of the Cartan subalgebra—the maximal set of mutually commuting elements in the Lie algebra. 

For angular momentum, we check which operators commute with $J_z$:
- $[J_z, J_+] = \hbar J_+ \neq 0$
- $[J_z, J_-] = -\hbar J_- \neq 0$  
- $[J_z, J^2] = 0$

Only $J^2$ commutes with $J_z$, but $J^2$ is a Casimir operator (a combination of generators, not an independent element of the Lie algebra). Therefore, the Cartan subalgebra is one-dimensional, generated by $J_z$ alone: $\text{span}\{J_z\}$.

The eigenvalue $m$ of $J_z$ is called the **weight**. The **highest weight state** $|j, m=j\rangle$ is the state with maximum $m$ value for a given $j$, satisfying:
$$J_+|j, j\rangle = 0$$

**Why Start from Highest Weight?**

1. **Uniqueness:** For the maximum $m = j_1 + j_2$, there is only ONE uncoupled state: $|j_1, j_1; j_2, j_2\rangle$. This means the CG coefficient must be unity (up to a phase, which we take to be 1):

$$|j = j_1 + j_2, m = j_1 + j_2\rangle = |j_1, j_1; j_2, j_2\rangle$$

So:
$$\boxed{C^{j_1+j_2, j_1+j_2}_{j_1, j_1; j_2, j_2} = 1}$$

2. **Systematic Construction:** Once we have the highest weight state, we can generate ALL other states in the multiplet by repeatedly applying the lowering operator $J_-$. This is much easier than trying to construct states from the middle of the multiplet.

**Step 2: Applying the Lowering Operator - Mathematical Induction**

Apply $J_- = J_{1-} + J_{2-}$ to both sides. Using:
$$J_-|j, m\rangle = \hbar\sqrt{(j+m)(j-m+1)}|j, m-1\rangle$$

**Example: From $|j_1+j_2, j_1+j_2\rangle$ to $|j_1+j_2, j_1+j_2-1\rangle$**

Left side:
$$J_-|j_1+j_2, j_1+j_2\rangle = \hbar\sqrt{2(j_1+j_2)}|j_1+j_2, j_1+j_2-1\rangle$$

Right side:
$$(J_{1-} + J_{2-})|j_1, j_1; j_2, j_2\rangle = \hbar\sqrt{2j_1}|j_1, j_1-1; j_2, j_2\rangle + \hbar\sqrt{2j_2}|j_1, j_1; j_2, j_2-1\rangle$$

Therefore:
$$|j_1+j_2, j_1+j_2-1\rangle = \sqrt{\frac{j_1}{j_1+j_2}}|j_1, j_1-1; j_2, j_2\rangle + \sqrt{\frac{j_2}{j_1+j_2}}|j_1, j_1; j_2, j_2-1\rangle$$

By successively applying $J_-$, we can construct all states in the $j = j_1 + j_2$ multiplet.

**Step 3: Finding Lower $j$ States by Orthogonality**

**Why Fix $m$ and Vary $j$?**

To find states with lower total angular momentum $j$, we use a crucial observation: **States with different $j$ but the same $m$ are orthogonal.** This is because $J^2$ is Hermitian, and eigenstates of a Hermitian operator with different eigenvalues are orthogonal.

By fixing $m = j_1 + j_2 - 1$ (the second-highest possible $m$ value), we can find ALL states with this $m$ value, regardless of their $j$:
- The $j = j_1 + j_2$ state (already constructed in Step 2)
- The $j = j_1 + j_2 - 1$ state (to be found by orthogonality)

**The Strategy:**

1. For $m = j_1 + j_2 - 1$, the uncoupled basis states are:
   - $|j_1, j_1-1; j_2, j_2\rangle$ 
   - $|j_1, j_1; j_2, j_2-1\rangle$

2. We already know one linear combination (the $j = j_1+j_2$ state from Step 2):
   $$|j_1+j_2, j_1+j_2-1\rangle = \sqrt{\frac{j_1}{j_1+j_2}}|j_1, j_1-1; j_2, j_2\rangle + \sqrt{\frac{j_2}{j_1+j_2}}|j_1, j_1; j_2, j_2-1\rangle$$

3. The orthogonal combination (normalized) gives the highest weight state for $j = j_1 + j_2 - 1$:

$$|j_1+j_2-1, j_1+j_2-1\rangle = \sqrt{\frac{j_2}{j_1+j_2}}|j_1, j_1-1; j_2, j_2\rangle - \sqrt{\frac{j_1}{j_1+j_2}}|j_1, j_1; j_2, j_2-1\rangle$$

Verify orthogonality:
$$\langle j_1+j_2, j_1+j_2-1|j_1+j_2-1, j_1+j_2-1\rangle = \sqrt{\frac{j_2}{j_1+j_2}}\sqrt{\frac{j_1}{j_1+j_2}} - \sqrt{\frac{j_1}{j_1+j_2}}\sqrt{\frac{j_2}{j_1+j_2}} = 0 \quad \checkmark$$

**Step 4: General Recursion Relation**

For arbitrary $j$, we derive a recursion relation that connects CG coefficients with different $m$ values. Acting with $J_+ = J_{1+} + J_{2+}$ on $|j, m\rangle$:

**Left side (coupled basis):**
$$J_+|j, m\rangle = \hbar\sqrt{(j-m)(j+m+1)}|j, m+1\rangle$$

Expanding $|j, m+1\rangle$ in the uncoupled basis:
$$|j, m+1\rangle = \sum_{m_1'} C^{j, m+1}_{j_1, m_1'; j_2, m+1-m_1'} |j_1, m_1'; j_2, m+1-m_1'\rangle$$

**Right side (acting on uncoupled expansion):**
$$\begin{aligned} J_+|j, m\rangle &= \sum_{m_1} C^{j, m}_{j_1, m_1; j_2, m_2} (J_{1+} + J_{2+})|j_1, m_1; j_2, m_2\rangle \\ &= \sum_{m_1} C^{j, m}_{j_1, m_1; j_2, m_2} \Big[\hbar\sqrt{(j_1-m_1)(j_1+m_1+1)}|j_1, m_1+1; j_2, m_2\rangle \\ &\quad + \hbar\sqrt{(j_2-m_2)(j_2+m_2+1)}|j_1, m_1; j_2, m_2+1\rangle\Big] \end{aligned}$$

**Equating Coefficients:**

To match terms with $|j_1, m_1; j_2, m_2\rangle$ on both sides, we need to perform a **dummy variable substitution** on the right side:

- In the first term: let $m_1 \to m_1 - 1$ (so $m_1+1 \to m_1$)
- In the second term: let $m_1 \to m_1$ (which means $m_2 \to m_2 - 1$ since $m_2 = m - m_1$)

This gives:
$$\sqrt{(j-m)(j+m+1)}C^{j, m+1}_{j_1, m_1; j_2, m_2} = \sqrt{(j_1-m_1+1)(j_1+m_1)}C^{j, m}_{j_1, m_1-1; j_2, m_2} + \sqrt{(j_2-m_2+1)(j_2+m_2)}C^{j, m}_{j_1, m_1; j_2, m_2-1}$$

This recursion, combined with the normalization condition $\sum_{m_1}|C^{j, m}_{j_1, m_1; j_2, m_2}|^2 = 1$, uniquely determines all CG coefficients.

**Explicit Formula (Racah Formula):**

The general closed-form expression is:

$$
\begin{aligned}
\langle j_1, m_1; j_2, m_2|j, m\rangle &= \delta_{m, m_1+m_2} \sqrt{\frac{(2j+1)(j_1+j_2-j)!(j+j_1-j_2)!(j+j_2-j_1)!}{(j_1+j_2+j+1)!}} \\
&\quad \times \sqrt{(j_1+m_1)!(j_1-m_1)!(j_2+m_2)!(j_2-m_2)!(j+m)!(j-m)!} \\
&\quad \times \sum_k \frac{(-1)^k}{k!(j_1+j_2-j-k)!(j_1-m_1-k)!(j_2+m_2-k)!(j-j_2+m_1+k)!(j-j_1-m_2+k)!}
\end{aligned}
$$

where the sum is over all integers $k$ that keep all factorial arguments non-negative.

---

### 4.6 Two Spin-1/2 System: Detailed CG Coefficient Calculation

Now let's apply the general method to the specific case of two spin-1/2 particles ($j_1 = j_2 = 1/2$):

$$j = |1/2 - 1/2|, ..., 1/2 + 1/2 = 0, 1$$

**Notation Clarification:**

We use a compact notation for uncoupled basis states:
- $|\uparrow\uparrow\rangle \equiv |1/2, 1/2; 1/2, 1/2\rangle$ (both spins up)
- $|\uparrow\downarrow\rangle \equiv |1/2, 1/2; 1/2, -1/2\rangle$ (first spin up, second down)
- $|\downarrow\uparrow\rangle \equiv |1/2, -1/2; 1/2, 1/2\rangle$ (first spin down, second up)
- $|\downarrow\downarrow\rangle \equiv |1/2, -1/2; 1/2, -1/2\rangle$ (both spins down)

Here the first arrow refers to particle 1 (with $j_1 = 1/2$) and the second arrow refers to particle 2 (with $j_2 = 1/2$).

**Triplet States ($j = 1$):**

For $|1, 1\rangle$: Only $m_1 = m_2 = 1/2$ contributes.

$$|1, 1\rangle = |\uparrow\uparrow\rangle = |1/2, 1/2; 1/2, 1/2\rangle$$

Apply $J_- = J_{1-} + J_{2-}$ to get $|1, 0\rangle$:

$$J_-|1, 1\rangle = \hbar\sqrt{(1+1)(1-1+1)}|1, 0\rangle = \hbar\sqrt{2}|1, 0\rangle$$

$$J_-|\uparrow\uparrow\rangle = (J_{1-} + J_{2-})|\uparrow\uparrow\rangle = \hbar|\downarrow\uparrow\rangle + \hbar|\uparrow\downarrow\rangle$$

Therefore:
$$|1, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)$$

Apply $J_-$ again to get $|1, -1\rangle$:

$$J_-|1, 0\rangle = \hbar\sqrt{2}|1, -1\rangle$$

$$J_-\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) = \frac{1}{\sqrt{2}}(\hbar|\downarrow\downarrow\rangle + \hbar|\downarrow\downarrow\rangle) = \hbar\sqrt{2}|\downarrow\downarrow\rangle$$

Therefore:
$$|1, -1\rangle = |\downarrow\downarrow\rangle$$

**Singlet State ($j = 0$):**

For $|0, 0\rangle$: Must be orthogonal to $|1, 0\rangle$ and have $m = 0$.

$$|0, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$

Verification: Apply $J^2 = (\mathbf{S}_1 + \mathbf{S}_2)^2$:

$$J^2 = S_1^2 + S_2^2 + 2\mathbf{S}_1 \cdot \mathbf{S}_2$$

$$= \frac{3\hbar^2}{4} + \frac{3\hbar^2}{4} + 2\mathbf{S}_1 \cdot \mathbf{S}_2 = \frac{3\hbar^2}{2} + 2\mathbf{S}_1 \cdot \mathbf{S}_2$$

For the singlet state:
$$\mathbf{S}_1 \cdot \mathbf{S}_2 = \frac{1}{2}(S_{1+}S_{2-} + S_{1-}S_{2+}) + S_{1z}S_{2z}$$

$$S_{1z}S_{2z}|0,0\rangle = \frac{\hbar^2}{4}\frac{1}{\sqrt{2}}(-|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) = -\frac{\hbar^2}{4}|0,0\rangle$$

$$S_{1+}S_{2-}|0,0\rangle = \hbar^2\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - 0) = \frac{\hbar^2}{\sqrt{2}}|\uparrow\downarrow\rangle$$

$$S_{1-}S_{2+}|0,0\rangle = \hbar^2\frac{1}{\sqrt{2}}(0 - |\downarrow\uparrow\rangle) = -\frac{\hbar^2}{\sqrt{2}}|\downarrow\uparrow\rangle$$

$$\mathbf{S}_1 \cdot \mathbf{S}_2|0,0\rangle = \frac{1}{2}(\frac{\hbar^2}{\sqrt{2}}|\uparrow\downarrow\rangle - \frac{\hbar^2}{\sqrt{2}}|\downarrow\uparrow\rangle) - \frac{\hbar^2}{4}|0,0\rangle = \frac{\hbar^2}{2}|0,0\rangle - \frac{\hbar^2}{4}|0,0\rangle = \frac{\hbar^2}{4}|0,0\rangle$$

Therefore:
$$J^2|0,0\rangle = \left(\frac{3\hbar^2}{2} + \frac{\hbar^2}{2}\right)|0,0\rangle = 2\hbar^2|0,0\rangle = \hbar^2 \cdot 0(0+1)|0,0\rangle$$

This confirms $|0,0\rangle$ has $j = 0$.

**Summary Table of CG Coefficients:**

| Coupled State | Uncoupled State | CG Coefficient |
|:-------------:|:---------------:|:--------------:|
| $\vert j=1, m=1\rangle$ | $\vert \uparrow\uparrow\rangle$ | $1$ |
| $\vert j=1, m=0\rangle$ | $\frac{1}{\sqrt{2}}(\vert \uparrow\downarrow\rangle + \vert \downarrow\uparrow\rangle)$ | $\frac{1}{\sqrt{2}}$ |
| $\vert j=1, m=-1\rangle$ | $\vert \downarrow\downarrow\rangle$ | $1$ |
| $\vert j=0, m=0\rangle$ | $\frac{1}{\sqrt{2}}(\vert \uparrow\downarrow\rangle - \vert \downarrow\uparrow\rangle)$ | $\frac{1}{\sqrt{2}}$ |

**Triplet States (Symmetric, $S=1$):**
$$|1,1\rangle = |\uparrow\uparrow\rangle$$
$$|1,0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)$$
$$|1,-1\rangle = |\downarrow\downarrow\rangle$$

**Singlet State (Antisymmetric, $S=0$):**
$$|0,0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$

### 4.7 Orbital-Spin Coupling ($j = l \pm 1/2$)

**Is $j$ the Coupling of $l$ and $s$? Yes!**

For a single particle (like an electron), the total angular momentum $\mathbf{j}$ is indeed the vector sum of orbital angular momentum $\mathbf{l}$ and spin angular momentum $\mathbf{s}$:

$$\mathbf{j} = \mathbf{l} + \mathbf{s}$$

This is a special case of the general angular momentum addition with $j_1 = l$ (integer) and $j_2 = s = 1/2$ (half-integer).

**Understanding $m_j$:**

The quantum number $m_j$ is the **magnetic quantum number of the total angular momentum**, specifically the eigenvalue of $j_z$ (the z-component of total angular momentum):

$$j_z |j, m_j\rangle = \hbar m_j |j, m_j\rangle$$

For a single particle, the z-component of total angular momentum is the sum of orbital and spin z-components:
$$j_z = l_z + s_z$$

Therefore, the eigenvalues add:
$$m_j = m_l + m_s$$

where:
- $m_l = -l, -l+1, ..., l$ is the magnetic quantum number for orbital angular momentum
- $m_s = \pm 1/2$ is the magnetic quantum number for spin (spin up/down along z-axis)

**Allowed Values of $j$:**

Applying the triangle rule with $j_1 = l$ and $j_2 = 1/2$:
- $j_{\max} = l + 1/2$
- $j_{\min} = |l - 1/2| = l - 1/2$ (for $l \geq 1$)

For $l = 0$ (s-orbital), the triangle rule gives $j_{\min} = |0 - 1/2| = 1/2$, so only $j = 1/2$ is possible.

**States with $j = l + 1/2$:**

$$|j = l + 1/2, m_j\rangle = \sqrt{\frac{l + m_j + 1/2}{2l + 1}}|l, m_j - 1/2; 1/2, 1/2\rangle + \sqrt{\frac{l - m_j + 1/2}{2l + 1}}|l, m_j + 1/2; 1/2, -1/2\rangle$$

**States with $j = l - 1/2$:**

$$|j = l - 1/2, m_j\rangle = -\sqrt{\frac{l - m_j + 1/2}{2l + 1}}|l, m_j - 1/2; 1/2, 1/2\rangle + \sqrt{\frac{l + m_j + 1/2}{2l + 1}}|l, m_j + 1/2; 1/2, -1/2\rangle$$

### 4.9 Coupling Three Angular Momenta

**The Problem: Non-commutativity of Intermediate Coupling**

When coupling three angular momenta $\mathbf{J} = \mathbf{J}_1 + \mathbf{J}_2 + \mathbf{J}_3$, we face a fundamental question: **in what order do we couple them?** Unlike classical vector addition, the quantum mechanical coupling order matters because the intermediate angular momentum operators do not commute.

**Two Coupling Schemes:**

**Scheme 1 ($j_{12}$ coupling):** First couple $\mathbf{J}_1$ and $\mathbf{J}_2$ to get $\mathbf{J}_{12}$, then couple with $\mathbf{J}_3$:
$$\mathbf{J}_{12} = \mathbf{J}_1 + \mathbf{J}_2, \quad \mathbf{J} = \mathbf{J}_{12} + \mathbf{J}_3$$

The basis states are labeled as $|(j_1 j_2)j_{12}, j_3; j, m\rangle$. This notation means:
- First $j_1$ and $j_2$ are coupled to intermediate $j_{12}$
- Then $j_{12}$ is coupled with $j_3$ to give total $j$
- The state has magnetic quantum number $m$

**Note on notation:** This compact notation focuses on the $j$ quantum numbers. The intermediate $m_{12}$ values are implicitly summed over in the CG expansion—the basis state is a superposition over all $m_1, m_2$ such that $m_1 + m_2 = m_{12}$ and $m_{12} + m_3 = m$.

The allowed values are:
- $j_{12} \in \{|j_1 - j_2|, ..., j_1 + j_2\}$
- $j \in \{|j_{12} - j_3|, ..., j_{12} + j_3\}$

**Scheme 2 ($j_{23}$ coupling):** First couple $\mathbf{J}_2$ and $\mathbf{J}_3$ to get $\mathbf{J}_{23}$, then couple with $\mathbf{J}_1$:
$$\mathbf{J}_{23} = \mathbf{J}_2 + \mathbf{J}_3, \quad \mathbf{J} = \mathbf{J}_1 + \mathbf{J}_{23}$$

The basis states are labeled as $|j_1, (j_2 j_3)j_{23}; j, m\rangle$, where:
- $j_{23} \in \{|j_2 - j_3|, ..., j_2 + j_3\}$
- $j \in \{|j_1 - j_{23}|, ..., j_1 + j_{23}\}$

**Why These Bases Are Different:**

The operators $\mathbf{J}_{12}^2$ and $\mathbf{J}_{23}^2$ do not commute. To see this, expand:
$$\mathbf{J}_{12}^2 = (\mathbf{J}_1 + \mathbf{J}_2)^2 = J_1^2 + J_2^2 + 2\mathbf{J}_1 \cdot \mathbf{J}_2$$
$$\mathbf{J}_{23}^2 = (\mathbf{J}_2 + \mathbf{J}_3)^2 = J_2^2 + J_3^2 + 2\mathbf{J}_2 \cdot \mathbf{J}_3$$

The cross term contains $\mathbf{J}_1 \cdot \mathbf{J}_2$ versus $\mathbf{J}_2 \cdot \mathbf{J}_3$. Since $[J_{1i}, J_{2j}] = 0$ but $[J_{2i}, J_{2j}] = i\hbar\varepsilon_{ijk}J_{2k}$, these operators do not commute.

**Key consequence:** When two Hermitian operators do not commute, they cannot be simultaneously diagonalized. This means:
- A state with definite $j_{12}$ does NOT have definite $j_{23}$
- The two coupling schemes define different orthonormal bases
- Both bases span the same $(2j_1+1)(2j_2+1)(2j_3+1)$-dimensional Hilbert space

### 4.10 Wigner 3j Symbols: Symmetric Notation for CG Coefficients

**From CG to 3j**

The CG coefficient $\langle j_1, m_1; j_2, m_2 | j_3, m_3 \rangle$ couples $j_1$ and $j_2$ to give $j_3$ with $m_3 = m_1 + m_2$. The **Wigner 3j symbol** rewrites this as a symmetric quantity where all three angular momenta appear on equal footing:

$$\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} = \frac{(-1)^{j_1 - j_2 - m_3}}{\sqrt{2j_3 + 1}} \langle j_1, m_1; j_2, m_2 | j_3, -m_3 \rangle$$

**Why $-m_3$ instead of $m_3$?** The CG coefficient requires $m_1 + m_2 = m_3$. The 3j symbol uses $-m_3$ so that the selection rule becomes:
$$m_1 + m_2 + m_3 = 0$$
This treats all three magnetic quantum numbers symmetrically—none is singled out as the "result."

**Application: Angular Correlations in Nuclear $\gamma$-Decay**

Consider an excited nucleus with spin $j_i$ that emits a photon (angular momentum 1) and decays to a state with spin $j_f$. We want to compute the angular distribution of the emitted photon relative to the nuclear spin quantization axis.

**Step 0: The Wigner-Eckart Theorem — General Form**

Before diving into the nuclear decay calculation, let's establish the general Wigner-Eckart theorem. This is one of the most powerful results in angular momentum theory.

**Background:** In quantum mechanics, we often need to calculate matrix elements of tensor operators between angular momentum eigenstates. These matrix elements depend on:
- The "physics" (transition strength, coupling constants)
- The "geometry" (how the states and operator are oriented in space)

The Wigner-Eckart theorem states that these dependencies **factorize**.

**Irreducible Tensor Operators**

An **irreducible tensor operator** $T^{(k)}$ of rank $k$ is a set of $2k+1$ operators $\{T^{(k)}_q : q = -k, -k+1, ..., k\}$ that transform under rotations in the same way as the angular momentum eigenstates $\{|k, q\rangle : q = -k, -k+1, ..., k\}$.

**Connection to State Transformation:**

Under a rotation $R$, an angular momentum eigenstate transforms as:
$$R |k, q\rangle = \sum_{q'} D^{(k)}_{q'q}(R) |k, q'\rangle$$

where $D^{(k)}(R)$ is the Wigner D-matrix. The state "mixes" with other $m$ values according to the D-matrix elements.

Similarly, for operators, we use the **active transformation** (operators change, states fixed):
$$T^{(k)}_q \to R T^{(k)}_q R^{-1} = \sum_{q'} D^{(k)}_{q'q}(R) T^{(k)}_{q'}$$

The same D-matrix appears because both the states $|k,q\rangle$ and the operators $T^{(k)}_q$ carry angular momentum $k$ and transform identically under rotations.

**Example: Rotation about the z-axis**

For a rotation by angle $\phi$ about the $z$-axis, the Wigner D-matrix is diagonal:
$$D^{(k)}_{q'q}(R_z(\phi)) = e^{-iq\phi} \delta_{q'q}$$

Therefore:
$$R_z(\phi) |k, q\rangle = e^{-iq\phi} |k, q\rangle$$

and for operators:
$$R_z(\phi) T^{(k)}_q R_z^{-1}(\phi) = e^{-iq\phi} T^{(k)}_q$$

This confirms that both states and operators acquire the same phase factor $e^{-iq\phi}$ under $z$-rotations.

**Commutation relations with angular momentum:**
$$[J_z, T^{(k)}_q] = \hbar q \, T^{(k)}_q$$
$$[J_\pm, T^{(k)}_q] = \hbar \sqrt{k(k+1) - q(q\pm 1)} \, T^{(k)}_{q\pm 1}$$

These are the operator analogs of:
- $J_z |k,q\rangle = \hbar q |k,q\rangle$
- $J_\pm |k,q\rangle = \hbar \sqrt{k(k+1) - q(q\pm 1)} |k,q\pm 1\rangle$

**Theorem (Wigner-Eckart):** For an irreducible tensor operator $T^{(k)}_q$ of rank $k$ (component $q$), the matrix element between angular momentum states factorizes as:

$$\langle j' m' | T^{(k)}_q | j m \rangle = \frac{\langle j m; k q | j' m' \rangle}{\sqrt{2j'+1}} \langle j' || T^{(k)} || j \rangle$$

where:
- $\langle j m; k q | j' m' \rangle$ is the **Clebsch-Gordan coefficient**
- $\langle j' || T^{(k)} || j \rangle$ is the **reduced matrix element** (independent of $m, m', q$)
- The factor $1/\sqrt{2j'+1}$ is a **conventional normalization**

**Why this factor?** Different textbooks use different conventions for the reduced matrix element. The Racah convention includes $1/\sqrt{2j'+1}$, which ensures that when we convert to 3j symbols, the dimensional factors cancel cleanly. Specifically, using the 3j symbol definition:
$$\begin{pmatrix} j & k & j' \\ m & q & -m' \end{pmatrix} = \frac{(-1)^{j-k+m'}}{\sqrt{2j'+1}} \langle j m; k q | j' m' \rangle$$

The $\sqrt{2j'+1}$ in the Wigner-Eckart theorem combines with the $\sqrt{2j'+1}$ in the 3j symbol definition to give simple orthogonality relations.

**Step 1: The Transition Amplitude**

The photon emission is described by an operator $\hat{O}$ that carries angular momentum $L=1$ (and projection $m_\gamma$). The transition amplitude is:

$$\mathcal{M}_{m_i \to m_f, m_\gamma} = \langle j_f m_f; 1 m_\gamma | \hat{O} | j_i m_i \rangle$$

where $|j_i m_i\rangle$ is the initial nuclear state, $|j_f m_f\rangle$ is the final nuclear state, and the photon state carries angular momentum $|1 m_\gamma\rangle$ with $m_\gamma = -1, 0, +1$.

**Step 2: Factorizing the Matrix Element — E1 Transition**

The transition amplitude $\mathcal{M} = \langle j_f m_f | \hat{O} | j_i m_i \rangle$ describes the photon emission process. Here $\hat{O}$ is the photon emission operator.

**Electric Dipole (E1) Operator:**

For electric dipole (E1) transitions, the operator takes the form:

$$\hat{O}_{E1} = e \sum_{p=1}^{Z} \mathbf{r}_p \cdot \boldsymbol{\varepsilon}^* e^{-i\mathbf{k}\cdot\mathbf{r}_p}$$

where:
- $e$ is the proton charge
- $\mathbf{r}_p$ is the position of the $p$-th proton in the nucleus (neutrons don't contribute to electric transitions)
- $Z$ is the proton number
- $\boldsymbol{\varepsilon}$ is the photon polarization vector
- $\mathbf{k}$ is the photon wave vector

**Long-wavelength approximation:** For nuclear $\gamma$-decay, the photon wavelength $\lambda = 2\pi/k$ is much larger than the nuclear size ($R \sim 5$ fm). Since $kR \ll 1$, we can set $e^{-i\mathbf{k}\cdot\mathbf{r}} \approx 1$ in the interaction operator, simplifying the E1 operator to depend only on the nuclear position coordinates.

**Spherical Components:**

To apply angular momentum theory, we need the **spherical components** of vectors. Given a vector $\mathbf{V} = (V_x, V_y, V_z)$, its spherical components are:

$$V_{+1} = -\frac{1}{\sqrt{2}}(V_x + iV_y)$$
$$V_0 = V_z$$
$$V_{-1} = \frac{1}{\sqrt{2}}(V_x - iV_y)$$

**Why this form?** Under rotations about the $z$-axis by angle $\phi$:
- $V_{\pm 1} \to e^{\pm i\phi} V_{\pm 1}$ (transforms like $e^{\pm i\phi}$, i.e., $m = \pm 1$)
- $V_0 \to V_0$ (invariant, $m = 0$)

These are the eigenfunctions of $L_z$ (the generator of rotations about $z$) with eigenvalues $\pm\hbar$ and $0$.

The E1 operator in spherical components becomes:
$$\hat{O}_{E1} = e \sum_{q=-1}^{+1} (-1)^q \hat{R}_q \, \varepsilon^*_{-q}$$

where:
$$\hat{R}_q = \sum_{p=1}^{Z} \hat{r}_{p,q}$$
is the total nuclear position operator in spherical component $q$, and $\hat{r}_{p,q}$ is the $q$-th spherical component of the $p$-th proton's position operator.

**Irreducible Tensor Property:**

Define the total nuclear position operator in spherical basis:
$$\hat{\mathbf{R}} = \{\hat{R}_{+1}, \hat{R}_0, \hat{R}_{-1}\}$$

These components satisfy the commutation relations of a rank-1 irreducible tensor operator:
$$[J_z, \hat{R}_q] = \hbar q \, \hat{R}_q$$
$$[J_\pm, \hat{R}_q] = \hbar \sqrt{2 - q(q\pm 1)} \, \hat{R}_{q\pm 1}$$

Therefore, $\hat{\mathbf{R}}$ is a **rank-1 irreducible tensor operator**.

**Connection to Wigner-Eckart:**

In the Wigner-Eckart theorem applied to E1 transitions:
- The operator is $\hat{R}_q$ with $k = 1$ (rank)
- The component $q$ is determined by the photon polarization: $q = m_\gamma$
- The matrix element $\langle j_f m_f | \hat{R}_{m_\gamma} | j_i m_i \rangle$ factorizes via the CG coefficient $\langle j_i m_i; 1 m_\gamma | j_f m_f \rangle$

**Multipolarity, Parity, and Selection Rules:**

Electromagnetic transitions are classified by **multipolarity** $L$ (angular momentum carried by photon) and **type** (E=electric, M=magnetic):

| Type | Notation | Parity Change of Nuclear States | Relative Strength |
|------|----------|--------------------------------|-------------------|
| Electric | $EL$ | $\pi_i \pi_f = (-1)^L$ | $\sim (kR)^{2L}$ |
| Magnetic | $ML$ | $\pi_i \pi_f = (-1)^{L+1}$ | $\sim (kR)^{2L}$ |

**Parity Change Explained:**

The "parity change" refers to the product of initial and final nuclear state parities $\pi_i \cdot \pi_f$:
- If $\pi_i \pi_f = +1$: no parity change (even)
- If $\pi_i \pi_f = -1$: parity changes (odd)

For E1 ($L=1$): parity must change ($\pi_i \pi_f = -1$).

**Why this selection rule?** The E1 operator is proportional to $\mathbf{r}$ (position), which is a **polar vector**. Under parity inversion ($\mathbf{r} \to -\mathbf{r}$), the E1 operator changes sign (odd parity). For the matrix element $\langle f | \hat{O}_{E1} | i \rangle$ to be non-zero, the integrand must have even parity:
$$\pi_f \cdot (-1) \cdot \pi_i = +1 \implies \pi_i \pi_f = -1$$

**Transition Probability Scaling:**

Why do higher multipoles have smaller transition probabilities? The key is the ratio of photon wavelength to nuclear size.

**Physical picture:** For nuclear $\gamma$-rays, photon wavelength $\lambda = 2\pi/k$ is much larger than the nuclear size $R \sim 5$ fm. Thus $kR \ll 1$, and each additional factor of $kR$ strongly suppresses the transition.

**Origin of the scaling (Weisskopf estimate):**

The decay rate $\Gamma$ follows from Fermi's Golden Rule:
$$\Gamma = \frac{2\pi}{\hbar} |\mathcal{M}|^2 \rho(E_f)$$

For electric $L$-pole transitions, the **Weisskopf estimate** gives:
$$\Gamma_{EL} \sim \frac{e^2}{\hbar c} \cdot c k \cdot (kR)^{2L}$$

**Where does $(kR)^{2L}$ come from?**

This factor arises from comparing the nuclear size $R$ to the photon wavelength $\lambda \sim 1/k$:

**1. Matrix element $|\mathcal{M}|$:**
The $EL$ transition operator involves matrix elements of the form $\langle f | \hat{O}_{EL} | i \rangle$. For electric multipoles:
- E1: Operator $\propto \mathbf{r}$ → matrix element $\sim R$
- E2: Operator $\propto \mathbf{r}(\mathbf{k}\cdot\mathbf{r})$ → matrix element $\sim R \cdot (kR) = kR^2$
- E$L$: Operator involves $L$ powers of $\mathbf{r}$, with $(L-1)$ of them coming from expanding $e^{-i\mathbf{k}\cdot\mathbf{r}}$ → matrix element $\sim R \cdot (kR)^{L-1} = k^{L-1}R^L$

**2. Photon density of states $\rho(E)$:**
In 3D, $\rho(E) \propto k^2$ (phase space factor).

**3. Photon field normalization:**
The quantized photon field contributes $1/\sqrt{\omega} \propto 1/\sqrt{k}$, giving $|\mathcal{M}|^2 \propto 1/k$.

**Combining for E$L$:**
$$\Gamma_{EL} \propto \underbrace{\frac{1}{k}}_{\text{field norm}} \cdot \underbrace{k^2}_{\text{phase space}} \cdot \underbrace{(k^{L-1}R^L)^2}_{\text{matrix element}^2} = k \cdot k^{2L-2} R^{2L} = c k (kR)^{2L}$$

where we insert the factor $c$ for dimensional correctness ($[ck] = T^{-1}$).

**Key insight:** Each increase in multipolarity by 1 adds a factor of $(kR)^2$ suppression because:
- One additional $\mathbf{r}$ in the operator → factor of $R$ in matrix element
- One additional $\mathbf{k}\cdot\mathbf{r}$ from expansion → factor of $kR$ in matrix element
- Together: $(kR)^2$ in the transition probability $|\mathcal{M}|^2$

For relative comparison at the same photon energy:
$$\frac{\Gamma_{E(L+1)}}{\Gamma_{EL}} \sim (kR)^2 \ll 1$$

**Typical numbers:**
- Photon energy: $E_\gamma \sim 0.1 - 10$ MeV
- Wave number: $k = E_\gamma/\hbar c \sim 10^{-3} - 10^{-1}$ fm$^{-1}$
- Nuclear radius: $R \sim 5$ fm
- Ratio: $kR \sim 0.005 - 0.5$ (typically $\sim 0.1$)

**Resulting hierarchy:**

Using $kR \sim 0.1$ for typical nuclear $\gamma$-rays:

| Multipole | Relative Rate | Typical Lifetime |
|-----------|---------------|------------------|
| E1 | 1 (baseline) | $10^{-15} - 10^{-12}$ s (fast) |
| M1 | $\sim 0.1 - 1$ | $10^{-14} - 10^{-11}$ s |
| E2 | $\sim 10^{-2} - 10^{-4}$ | $10^{-11} - 10^{-8}$ s |
| E3/M2 | $\sim 10^{-4} - 10^{-6}$ | $10^{-7} - 10^{-3}$ s (slow, isomeric) |

M1 has the same $kR$ scaling as E1 but is typically weaker due to spin-flip nature ($\mu \sim e\hbar/m$ vs $er$).

**When is E1 Forbidden? Selection Rules:**

E1 transitions require:
1. **Angular momentum:** $|j_i - j_f| \leq 1 \leq j_i + j_f$ (triangle rule with $L=1$)
2. **Parity:** $\pi_i \neq \pi_f$ (parity must change)

**Nuclear Physics Notation:**
- $^{A}X$: Nucleus with mass number $A$ and element $X$
- $nl_j$: Single-particle orbital ($n$=principal quantum number, $l$=orbital angular momentum with $s,p,d,f,...$ for $l=0,1,2,3,...$, $j$=total angular momentum)
- $J^\pi_n$: Nuclear state with total angular momentum $J$, parity $\pi$ ($+$=even, $-$=odd), and excitation index $n$ ($n=1$=ground state, $n=2$=first excited, etc.)

**Example 1: E1 Allowed — Oxygen-17**

$^{17}$O: $1d_{5/2} \to 2p_{3/2}$ 

A proton transitions from $d$-shell to $p$-shell:
- Initial: $j_i = 5/2$ ($d_{5/2}$ orbital), Final: $j_f = 3/2$ ($p_{3/2}$ orbital)
- Angular momentum: $|5/2 - 3/2| = 1 \leq 1 \leq 4$ ✓
- Parity: $l_i = 2$ (even) $\to$ $l_f = 1$ (odd), changes ✓
- **Result:** E1 allowed

**Example 2: E1 Forbidden by Parity — Oxygen-17**

$^{17}$O: $1d_{5/2} \to 1d_{3/2}$ 

A proton stays in $d$-shell, only $j$ changes:
- Angular momentum: $|5/2 - 3/2| = 1 \leq 1 \leq 4$ ✓
- Parity: $l_i = l_f = 2$ (both even), does NOT change ✗
- **Result:** E1 forbidden; proceeds via M1 or E2

**Example 3: E1 Forbidden by Angular Momentum — Oxygen-16**

$^{16}$O: $0^+_2 \to 0^+_1$ (excited state $\to$ ground state)

Both states have $J = 0$:
- Angular momentum: $J_i = 0$, $J_f = 0$; cannot satisfy $0 = 0 + 1$ ✗
- E1 requires photon with $L = 1$, but no angular momentum to spare
- **Result:** E1 forbidden; proceeds via E2

**Note:** $0^+ \to 0^+$ transitions cannot emit single photons (photon always has $L \geq 1$). They decay via internal conversion or two-photon emission.

**Conclusion:** E1 dominates **only when both angular momentum and parity selection rules are satisfied**. When either is violated, the transition must proceed via higher multipolarity (E2, M1, etc.) and is much slower.

**Applying Wigner-Eckart:**

$$\mathcal{M} = \text{(Geometric factor)} \times \text{(Physical factor)}$$

The **geometric factor** is the CG coefficient for angular momentum coupling:
$$\text{Geometric factor} = \langle j_i m_i; 1 m_\gamma | j_f m_f \rangle$$

This describes how the initial nuclear angular momentum $(j_i, m_i)$ combines with the photon's angular momentum $(1, m_\gamma)$ to produce the final nuclear state $(j_f, m_f)$. This factor contains all the dependence on the orientations (the $m$ values).

The **physical factor** is the reduced matrix element:
$$\text{Physical factor} = \frac{\langle j_f || \hat{O} || j_i \rangle}{\sqrt{2j_f+1}}$$

This contains the intrinsic transition strength (how likely the transition is) but does NOT depend on $m_i, m_f,$ or $m_\gamma$.

**Normalization Convention Note:** The factor $\sqrt{2j_f+1}$ in the denominator is a convention (the Racah convention). When we compute $|\mathcal{M}|^2$, this gives a factor of $2j_f+1$ in the denominator. This precisely cancels the $2j_f+1$ factor that appears when we convert CG coefficients to 3j symbols (Step 4), leaving a clean formula. Different conventions (e.g., Edmonds) omit this factor, leading to different-looking but equivalent final results.

**Step 3: Computing the Angular Distribution**

The probability of a specific transition is $P = |\mathcal{M}|^2$:
$$P(m_i \to m_f, m_\gamma) = C \times |\langle j_i m_i; 1 m_\gamma | j_f m_f \rangle|^2$$

where $C = |\langle j_f || \hat{O} || j_i \rangle|^2 / (2j_f+1)$ is a constant.

**The Photon Angular Dependence and Polarization:**

The photon is emitted with angular momentum projection $m_\gamma$ relative to the nuclear spin quantization axis. The probability of finding this photon at angle $(\theta, \phi)$ relative to the spin axis is given by $|Y_1^{m_\gamma}(\theta, \phi)|^2$.

**Where does this come from?** 

The photon wavefunction in the far-field (radiation zone) is a spherical wave with angular dependence given by vector spherical harmonics. For an E1 transition:
- The photon carries away one unit of angular momentum ($L=1$)
- The angular distribution is determined by the angular momentum eigenstate $|1, m_\gamma\rangle$
- In position representation, this eigenstate is proportional to the spherical harmonic $Y_1^{m_\gamma}(\theta, \phi)$

The spherical harmonics $Y_L^m(\theta, \phi)$ are the angular momentum eigenfunctions:
$$\langle \theta, \phi | L, m \rangle = Y_L^m(\theta, \phi)$$

For $L=1$:
$$Y_1^{\pm 1}(\theta, \phi) = \mp \sqrt{\frac{3}{8\pi}} \sin\theta \, e^{\pm i\phi}$$
$$Y_1^0(\theta, \phi) = \sqrt{\frac{3}{4\pi}} \cos\theta$$

The intensity (probability density) is $|Y_1^{m_\gamma}|^2$:
- $|Y_1^{\pm 1}|^2 \propto \sin^2\theta$ (emission perpendicular to spin axis)
- $|Y_1^0|^2 \propto \cos^2\theta$ (emission along spin axis)

**Polarization and Angular Momentum Projection:**

The polarization of the emitted photon depends on $m_\gamma$:

**$m_\gamma = \pm 1$: Circular Polarization**

The photon polarization vector for $m_\gamma = \pm 1$ is:
$$\boldsymbol{\varepsilon}_{\pm 1} = \mp \frac{1}{\sqrt{2}}(\hat{x} \pm i\hat{y})$$

These are the **circular polarization vectors** (helicity $\pm 1$):
- $\boldsymbol{\varepsilon}_{+1}$: Right-circular polarization (photon spin aligned with propagation)
- $\boldsymbol{\varepsilon}_{-1}$: Left-circular polarization (photon spin anti-aligned with propagation)

When $m_\gamma = \pm 1$, the photon's intrinsic angular momentum (spin) has projection $\pm\hbar$ along the quantization axis. This corresponds to circular polarization because the electric field vector rotates in a circle in the plane perpendicular to the propagation direction.

**$m_\gamma = 0$: Linear Polarization**

The photon polarization vector for $m_\gamma = 0$ is:
$$\boldsymbol{\varepsilon}_0 = \hat{z}$$

This is **linear polarization** along the $z$-axis (quantization axis). When the photon propagates in the $x$-$y$ plane (perpendicular to the spin axis), the electric field oscillates along $\hat{z}$, which is a linear polarization.

Alternatively, when propagating along $z$, $m_\gamma = 0$ corresponds to linear polarization in the $x$-$y$ plane (superposition of $\pm 1$ states with definite relative phase).

**Physical Picture:**
- **$m_\gamma = \pm 1$**: Photon spin is aligned with the nuclear spin axis; emitted preferentially perpendicular to the axis ($\sin^2\theta$); circularly polarized
- **$m_\gamma = 0$**: Photon has no angular momentum along the spin axis; emitted preferentially along the axis ($\cos^2\theta$); linearly polarized

Therefore, the joint probability of the specific transition AND photon emission at angle $\theta$ is:
$$P(m_i \to m_f, m_\gamma; \theta) = C \times |\langle j_i m_i; 1 m_\gamma | j_f m_f \rangle|^2 \times |Y_1^{m_\gamma}(\theta)|^2$$

where we use $\phi=0$ by symmetry around the spin axis.

To get the total angular distribution for a given initial state $m_i$, we sum over all possible final states $m_f$ and photon polarizations $m_\gamma$:

$$W_{m_i}(\theta) = \sum_{m_f, m_\gamma} P(m_i \to m_f, m_\gamma; \theta)$$

**Step 4: Converting to 3j Symbols**

Using the definition of the 3j symbol:
$$\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} = \frac{(-1)^{j_1 - j_2 - m_3}}{\sqrt{2j_3 + 1}} \langle j_1, m_1; j_2, m_2 | j_3, -m_3 \rangle$$

We identify $j_1 = j_i, m_1 = m_i, j_2 = 1, m_2 = m_\gamma, j_3 = j_f, -m_3 = m_f$ (so $m_3 = -m_f$). Therefore:
$$\langle j_i m_i; 1 m_\gamma | j_f m_f \rangle = (-1)^{j_i - 1 + m_f} \sqrt{2j_f+1} \begin{pmatrix} j_i & 1 & j_f \\ m_i & m_\gamma & -m_f \end{pmatrix}$$

Taking the modulus squared (the phase factor has unit modulus $|(-1)^{j_i-1+m_f}|^2 = 1$):
$$|\langle j_i m_i; 1 m_\gamma | j_f m_f \rangle|^2 = (2j_f+1) \left|\begin{pmatrix} j_i & 1 & j_f \\ m_i & m_\gamma & -m_f \end{pmatrix}\right|^2$$

Substituting into $W_{m_i}(\theta)$:
$$W_{m_i}(\theta) = \frac{|\langle j_f || \hat{O} || j_i \rangle|^2}{2j_f+1} \times (2j_f+1) \sum_{m_f, m_\gamma} \left|\begin{pmatrix} j_i & 1 & j_f \\ m_i & m_\gamma & -m_f \end{pmatrix}\right|^2 |Y_1^{m_\gamma}(\theta, 0)|^2$$

$$W_{m_i}(\theta) = |\langle j_f || \hat{O} || j_i \rangle|^2 \sum_{m_f, m_\gamma} \left|\begin{pmatrix} j_i & 1 & j_f \\ m_i & m_\gamma & -m_f \end{pmatrix}\right|^2 |Y_1^{m_\gamma}(\theta, 0)|^2$$

**Step 5: Averaging Over Initial States**

If the initial nuclei are unoriented (random $m_i$), we average over $m_i$:

$$W(\theta) = \frac{1}{2j_i+1} \sum_{m_i} W_{m_i}(\theta) = \frac{|\langle j_f || \hat{O} || j_i \rangle|^2}{2j_i+1} \sum_{m_i, m_f, m_\gamma} \left|\begin{pmatrix} j_i & 1 & j_f \\ m_i & m_\gamma & -m_f \end{pmatrix}\right|^2 |Y_1^{m_\gamma}(\theta, 0)|^2$$

**Why use 3j symbols?**

1. **Symmetric treatment:** The CG coefficient $\langle j_i m_i; 1 m_\gamma | j_f m_f \rangle$ treats $j_f$ as the "result" of coupling $j_i$ and 1. But physically, all three angular momenta (initial, photon, final) are on equal footing. The 3j symbol treats them equally: even permutations of columns leave it unchanged, while odd permutations multiply by $(-1)^{j_1+j_2+j_3}$.

2. **Selection rule visibility:** The conservation of $J_z$ ($m_f = m_i + m_\gamma$, or equivalently $m_i + m_\gamma + (-m_f) = 0$) is immediately apparent from the sum-to-zero condition in the 3j symbol.

3. **Computational efficiency:** The sum over $m_i$ and $m_f$ can be performed using the orthogonality relation of 3j symbols.

**Demonstration: Closed-Form Angular Distribution**

The 3j symbol orthogonality relation states:
$$\sum_{m_1, m_2} \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} \begin{pmatrix} j_1 & j_2 & j_3' \\ m_1 & m_2 & m_3' \end{pmatrix} = \frac{\delta_{j_3 j_3'} \delta_{m_3 m_3'}}{2j_3 + 1}$$

This sums over the first two magnetic quantum numbers ($m_1, m_2$), leaving the third fixed. To apply this to our problem, we need the initial and final nuclear magnetic quantum numbers ($m_i, m_f$) in the first two positions.

**Step 1: Rearrange the 3j Symbol**

Our starting point is:
$$W(\theta) \propto \sum_{m_i, m_f} \left|\begin{pmatrix} j_i & 1 & j_f \\ m_i & m_\gamma & -m_f \end{pmatrix}\right|^2 |Y_1^{m_\gamma}(\theta)|^2$$

The orthogonality relation sums over the first two magnetic quantum numbers, but here $m_i$ and $m_f$ are in positions 1 and 3. We need to swap columns to bring $m_i$ and $-m_f$ into the first two positions.

Swapping columns 2 and 3 introduces a phase factor $(-1)^{j_i+j_f+1}$:
$$\begin{pmatrix} j_i & j_f & 1 \\ m_i & -m_f & m_\gamma \end{pmatrix} = (-1)^{j_i+j_f+1} \begin{pmatrix} j_i & 1 & j_f \\ m_i & m_\gamma & -m_f \end{pmatrix}$$

Since we square the 3j symbol, the phase factor vanishes:
$$\left|\begin{pmatrix} j_i & 1 & j_f \\ m_i & m_\gamma & -m_f \end{pmatrix}\right|^2 = \left|\begin{pmatrix} j_i & j_f & 1 \\ m_i & -m_f & m_\gamma \end{pmatrix}\right|^2$$

Now $m_i$ and $-m_f$ occupy the first two positions, ready for orthogonality summation.

**Step 2: Apply Orthogonality**

With $j_1 = j_i$, $j_2 = j_f$, $j_3 = 1$, and $m_3 = m_\gamma$:
$$\sum_{m_i, m_f} \left|\begin{pmatrix} j_i & j_f & 1 \\ m_i & -m_f & m_\gamma \end{pmatrix}\right|^2 = \frac{1}{2(1)+1} = \frac{1}{3}$$

**Step 3: Evaluate the Angular Distribution**

The sum over magnetic quantum numbers becomes:
$$W(\theta) = \frac{|\langle j_f || \hat{O} || j_i \rangle|^2}{(2j_i+1)} \sum_{m_\gamma} \left[\sum_{m_i, m_f} \left|\begin{pmatrix} j_i & j_f & 1 \\ m_i & -m_f & m_\gamma \end{pmatrix}\right|^2\right] |Y_1^{m_\gamma}(\theta)|^2$$

$$= \frac{|\langle j_f || \hat{O} || j_i \rangle|^2}{(2j_i+1)} \cdot \frac{1}{3} \sum_{m_\gamma=-1}^{1} |Y_1^{m_\gamma}(\theta)|^2$$

Using the spherical harmonic addition theorem: $\sum_{m=-1}^{1} |Y_1^m(\theta, \phi)|^2 = \frac{3}{4\pi}$ (independent of angles):

$$W(\theta) = \frac{|\langle j_f || \hat{O} || j_i \rangle|^2}{4\pi(2j_i+1)}$$

**Result:** The angular distribution is **independent of $\theta$**:
$$\boxed{W(\theta) = \text{constant}}$$

For unoriented nuclei (randomly oriented initial spins), the gamma emission is **isotropic** (uniform in all directions). The 3j symbol orthogonality provides this closed-form result directly, avoiding tedious summation over all magnetic sub-states.

---

## Part V: Symmetry and Group Theory in Physics

Angular momentum theory is deeply rooted in group representation theory. This part explains the mathematical structures underlying symmetries and their physical interpretations.

### 5.1 Representations and Irreducibility

**Definition**

A **representation** of a group $G$ is a homomorphism $D: G \to \text{GL}(V)$, where $V$ is the Hilbert space and $D(g)$ is the operator implementing symmetry transformation $g$.

**Irreducible Representations as Classification**

An **irreducible representation** cannot be decomposed into smaller invariant subspaces. These are the fundamental building blocks:

| Label | Dimension | Physical System |
|-------|-----------|-----------------|
| $D^{(0)}$ | 1 | Spin-0 particle |
| $D^{(1/2)}$ | 2 | Spin-1/2 particle |
| $D^{(1)}$ | 3 | Spin-1 particle |
| $D^{(j)}$ | $2j+1$ | Spin-$j$ particle |

Each physical system with definite total angular momentum $j$ occupies ONE irreducible representation. The quantum number $m = -j, ..., j$ labels states within that representation.

**Key Point:** Different irreducible representations are orthogonal. A spin-1/2 system never "mixes" with spin-1 under rotation—they are distinct sectors.

**Tensor Product: Building Composite Systems**

When two systems combine, their representations multiply:

$$D^{(j_1)} \otimes D^{(j_2)} = \bigoplus_{j=|j_1-j_2|}^{j_1+j_2} D^{(j)}$$

**Example:** Two spin-1/2 particles
- Product space: 4-dimensional
- Decomposes into: $D^{(1)}$ (triplet, 3D) $\oplus$ $D^{(0)}$ (singlet, 1D)

**Physical Interpretation:** The composite system's Hilbert space contains TWO independent sectors. A state in the triplet sector remains there under rotation; a state in the singlet sector remains there. The decomposition reveals what total angular momentum values ($j=1$ or $j=0$) are possible for the composite system.

**Types of Representations**

**1. Faithful Representation**

A representation is **faithful** if different group elements always map to different operators:
$$g_1 \neq g_2 \implies D(g_1) \neq D(g_2)$$

**Example:** SU(2) on spin-1/2 is faithful. Consider two different SU(2) elements:
$$U_1 = e^{-i\theta_1 \sigma_z/2}, \quad U_2 = e^{-i\theta_2 \sigma_z/2}$$
If $\theta_1 \neq \theta_2$ (mod $4\pi$), then $D(U_1) \neq D(U_2)$ as $2 \times 2$ matrices. The representation is injective.

**Counter-example:** The trivial representation $D(g) = 1$ for all $g$ is NOT faithful—all group elements map to the same number 1.

**2. Projective Representation**

In quantum mechanics, states are rays: $|\psi\rangle$ and $e^{i\phi}|\psi\rangle$ represent the same physical state. A **projective representation** satisfies:
$$D(g_1)D(g_2) = e^{i\omega(g_1,g_2)} D(g_1g_2)$$

The product is only required up to a phase factor.

**Example:** Half-integer spin representations of SO(3) are projective. For spin-1/2:
- SO(3) rotation $R_z(2\pi) = I$ (identity)
- But the quantum operator is $D^{(1/2)}(R_z(2\pi)) = -I$

So $D(I) = I$ but $D(R_z(2\pi)) = -I$, even though $R_z(2\pi) = I$ in SO(3). This is NOT a true representation of SO(3), but it IS a projective representation because $-I$ differs from $I$ only by a phase ($-1 = e^{i\pi}$).

**3. Fundamental Representation**

The **fundamental representation** is the defining representation of the group—the smallest one used to define the group itself.

**Example 1 (SU(2)):** SU(2) is defined as $2 \times 2$ unitary matrices with $\det = 1$. The fundamental representation is these matrices acting on $\mathbb{C}^2$ (2-component spinors):
$$\psi = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix} \xrightarrow{U} U\psi$$

**Example 2 (SU(3)):** SU(3) is defined as $3 \times 3$ unitary matrices with $\det = 1$. The fundamental representation acts on $\mathbb{C}^3$ (quark triplet: up, down, strange).

**4. Adjoint Representation**

The **adjoint representation** is a representation where the group acts on its own Lie algebra (the space of generators).

**Understanding the Adjoint Representation:**

A Lie group $G$ has generators $\{T_a\}$ forming a vector space $\mathfrak{g}$ (the Lie algebra). For SU(2), the generators are $\{J_x, J_y, J_z\}$—a 3D vector space.

A group element $g \in G$ acts on a generator $T \in \mathfrak{g}$ by conjugation:
$$T \xrightarrow{g} g T g^{-1}$$

This defines the adjoint representation: $D_{\text{adj}}(g) T = g T g^{-1}$

**Why it is a representation:** Check that $D(g_1g_2) = D(g_1)D(g_2)$:
$$D_{\text{adj}}(g_1g_2)T = (g_1g_2)T(g_1g_2)^{-1} = g_1(g_2 T g_2^{-1})g_1^{-1} = D_{\text{adj}}(g_1)[D_{\text{adj}}(g_2)T]$$

**Example (SU(2)):** The adjoint representation has dimension 3 (equal to the number of generators $J_x, J_y, J_z$). For a rotation $R_z(\theta)$ about the $z$-axis:
$$J_x \to \cos\theta \, J_x + \sin\theta \, J_y$$
$$J_y \to -\sin\theta \, J_x + \cos\theta \, J_y$$
$$J_z \to J_z$$

In matrix form (basis $\{J_x, J_y, J_z\}$):
$$D_{\text{adj}}(R_z(\theta)) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

This is just the standard $3 \times 3$ rotation matrix! For SU(2), the adjoint representation is the spin-1 (vector) representation.

**Summary of Dimensions:**
- SU(2): Fundamental = 2D (spin-1/2), Adjoint = 3D (spin-1)
- SU(3): Fundamental = 3D (quark), Adjoint = 8D (gluon)

---

**Properties of Representations**

**Character**

The **character** of a representation is the trace:
$$\chi_j(g) = \text{Tr}[D^{(j)}(g)]$$

Characters are powerful because they depend only on the **conjugacy class** of $g$ (elements related by $g' = hgh^{-1}$ have the same character). For rotations, this means $\chi_j$ depends only on the rotation angle $\theta$, not the axis.

**Example (Spin-1/2):**
For rotation by angle $\theta$ about any axis:
$$D^{(1/2)}(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}$$
$$\chi_{1/2}(\theta) = e^{-i\theta/2} + e^{i\theta/2} = 2\cos(\theta/2)$$

**Orthogonality Relation and Haar Measure**

Characters of different irreducible representations are orthogonal:
$$\int_G dg \, \chi_j^*(g)\chi_{j'}(g) = \delta_{jj'}$$

**Why the Haar measure?**

The **Haar measure** $dg$ is the unique measure on the group that is invariant under group multiplication:
$$\int_G f(g)dg = \int_G f(hg)dg = \int_G f(gh)dg$$

For SO(3), the Haar measure is:
$$dg = \frac{1}{2}\sin^2\frac{\theta}{2} \frac{d\theta}{2\pi} \frac{d\Omega}{4\pi}$$

where $d\Omega$ is the solid angle for the rotation axis. The $\sin^2(\theta/2)$ factor accounts for the Jacobian when parameterizing rotations.

**Example: Decomposing Tensor Products**

To find how many times $D^{(j)}$ appears in $D^{(j_1)} \otimes D^{(j_2)}$:
$$n_j = \int_0^{2\pi} \frac{d\theta}{\pi} \sin^2\frac{\theta}{2} \, \chi_{j_1}(\theta)\chi_{j_2}(\theta)\chi_j^*(\theta)$$

For $j_1 = j_2 = 1/2$:
- $\chi_{1/2}(\theta) = 2\cos(\theta/2)$
- $\chi_0(\theta) = 1$ (singlet)
- $\chi_1(\theta) = 1 + 2\cos\theta$ (triplet)

Checking $n_0$ (singlet):
$$n_0 \propto \int \sin^2\frac{\theta}{2} \cdot 4\cos^2\frac{\theta}{2} \cdot 1 \, d\theta$$
$$= \int_0^{2\pi} \sin^2\theta \, d\theta = \pi$$

Checking $n_1$ (triplet):
$$n_1 \propto \int \sin^2\frac{\theta}{2} \cdot 4\cos^2\frac{\theta}{2} \cdot (1 + 2\cos\theta) \, d\theta$$
Using $\sin^2(\theta/2)\cos^2(\theta/2) = \frac{1}{4}\sin^2\theta$:
$$= \int_0^{2\pi} \sin^2\theta (1 + 2\cos\theta) d\theta = \pi$$

So $n_0 = n_1 = 1$, confirming $\frac{1}{2} \otimes \frac{1}{2} = 0 \oplus 1$.

**Summary:**
- **Irreducible representation** = fundamental classification label ($j$)
- **Multiplet** = set of states within one representation (degenerate under symmetry)
- **Tensor product decomposition** = finding which $j$ values appear when systems combine

### 5.2 Lie Algebras: Why the Identity?

**The Tangent Space Insight**

A Lie group is a continuous manifold. The **Lie algebra** is the tangent space at the identity element.

**Why focus on the identity?**

Because any group element near the identity can be written as:
$$g(\theta) = I - i\theta T + O(\theta^2)$$

The generator $T$ (the derivative at $\theta=0$) determines the behavior of the entire group through exponentiation:
$$g(\theta) = e^{-i\theta T}$$

**Key theorem:** The local structure of a Lie group (near identity) completely determines its global structure. The commutation relations of generators:
$$[T_a, T_b] = i\sum_c f_{abc} T_c$$
capture all essential group properties.

**Generators and Exponentiation**

The generator $J_z$ is extracted from the rotation operator by differentiation at the identity:
$$J_z = i\hbar \frac{d R_z(\theta)}{d \theta}\bigg|_{\theta=0}$$

This derivative extracts the "tangent vector" to the group manifold at the identity—the Lie algebra element. Finite rotations are built by exponentiation:
$$R_z(\theta) = e^{-i\theta J_z/\hbar}$$

The commutation relations $[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k$ reflect the geometric structure of rotations: performing two rotations in different order differs by a third rotation.

### 5.3 SU(2) vs. SO(3): Double Cover and Projective Representations

**Same Algebra, Different Groups**

SU(2) and SO(3) have **identical Lie algebras** but different global topology:

| Property | SO(3) | SU(2) |
|----------|-------|-------|
| Group elements | 3×3 real orthogonal matrices | 2×2 complex unitary matrices with $\det = 1$ |
| Topology | 3D ball with antipodal surface points identified | 3-sphere $S^3$ (no identifications) |
| Fundamental group | $\pi_1 = \mathbb{Z}_2$ (has non-contractible loops) | $\pi_1 = \{e\}$ (simply connected) |
| Periodicity | $R(2\pi) = I$ | $U(2\pi) = -I$, $U(4\pi) = I$ |

**Topology Explained:**

- **SO(3):** Can be visualized as a ball of radius $\pi$. A rotation by angle $\theta$ about axis $\mathbf{n}$ is point $\theta\mathbf{n}$. Opposite points on the surface ($\pi\mathbf{n}$ and $-\pi\mathbf{n}$) represent the same rotation—this is **antipodal identification**.

- **SU(2):** Is a 3-sphere. Each point corresponds to a unique matrix $U = a_0 I + i\mathbf{a} \cdot \boldsymbol{\sigma}$ with $a_0^2 + |\mathbf{a}|^2 = 1$. No identifications needed.

**The Double Cover:**

$$
\text{SU(2)}/\mathbb{Z}_2 \cong \text{SO(3)}
$$

The map: For $U = e^{-i\theta \mathbf{n}\cdot\boldsymbol{\sigma}/2} \in$ SU(2), the corresponding SO(3) element rotates by angle $\theta$ about axis $\mathbf{n}$. Both $U$ and $-U$ map to the same SO(3) rotation.

**Example:** For rotation about $z$-axis:
- SU(2): $U(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}$
- SO(3): $R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$

Note: $U(2\pi) = -I$ but $R_z(2\pi) = I$.

**Projective Representations:**

In quantum mechanics, $|\psi\rangle$ and $e^{i\phi}|\psi\rangle$ represent the same physical state. A **projective representation** satisfies:
$$D(g_1)D(g_2) = e^{i\omega(g_1,g_2)} D(g_1 g_2)$$

where $\omega(g_1, g_2)$ is a phase factor (cocycle).

**Key Result:**
- **Integer $j$:** $U(2\pi) = +I$ — this is a true representation of SO(3)
- **Half-integer $j$:** $U(2\pi) = -I$ — this is only a projective representation of SO(3)

For half-integer spin, a $2\pi$ rotation produces a phase factor $-1$. Since $|\psi\rangle$ and $-|\psi\rangle$ are the same quantum state, this is acceptable for SO(3).

**Lifting Representations:**

Every representation of SO(3) "lifts" to SU(2): given $D_{\text{SO(3)}}$, we can construct $D_{\text{SU(2)}}(U) = D_{\text{SO(3)}}(R)$ where $R$ is the rotation corresponding to $U$.

Conversely, a representation of SU(2) descends to SO(3) **only if** $D(-U) = D(U)$. This holds for integer $j$ but fails for half-integer $j$ (where $D(-U) = -D(U)$).

**Why SU(2) is fundamental:**
- SU(2) is simply connected—no "holes" in its topology
- Every representation of SO(3) comes from a representation of SU(2)
- But SU(2) has additional representations (half-integer $j$) with no SO(3) counterpart
- These "extra" representations describe fermions (electrons, quarks, etc.)

**SO(4) and SU(2) × SU(2): The Hydrogen Connection**

The SO(4) symmetry of hydrogen (section 7.4) is deeply connected to SU(2). The six generators of SO(4) can be organized into two sets of three:
$$\mathbf{M} = \frac{1}{2}(\mathbf{L} + \mathbf{K}), \quad \mathbf{N} = \frac{1}{2}(\mathbf{L} - \mathbf{K})$$

These satisfy:
$$[M_i, M_j] = i\hbar \varepsilon_{ijk} M_k, \quad [N_i, N_j] = i\hbar \varepsilon_{ijk} N_k, \quad [M_i, N_j] = 0$$

This is the algebra of **SU(2) × SU(2)**—two independent SU(2) algebras that commute. Therefore:
$$\text{SO(4)} \cong \text{SU(2)} \times \text{SU(2)}$$

**Physical Significance:**
- Each SU(2) factor contributes a quantum number ($m$ and $n$ in the text)
- For hydrogen, the constraint $\mathbf{L} \cdot \mathbf{K} = 0$ forces $m = n$
- The principal quantum number is $n = 2m + 1$ (in the text's convention)
- This explains why the hydrogen spectrum depends only on $n$: both SU(2) factors contribute equally.

### 5.4 SU(3) Flavor vs. SU(3) Color: Two Different Symmetries

**Global vs. Local (Gauge) Symmetry**

| Property | Flavor SU(3) | Color SU(3) |
|----------|-------------|-------------|
| Type | **Global** symmetry | **Local** gauge symmetry |
| Transformation | Same at all spacetime points | Different at each point: $U(x)$ |
| Connection | No gauge field | Requires gluon field $A_\mu^a(x)$ |
| Approximate? | Yes (broken by quark mass differences) | Exact |
| Physical role | Classifies hadrons | Generates strong interaction |

**Local Symmetry (Gauge Principle):** For a symmetry to hold independently at every spacetime point, a compensating field (the gauge field) must exist. For SU(3) color, this field is the **gluon**, and the symmetry requires quarks interact via gluon exchange.

**The Color Singlet Rule**

All observable hadrons must be **color singlets** (invariant under SU(3) color transformations). This explains:

1. **Mesons:** Quark + antiquark
   $$\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$$
   The singlet $\mathbf{1}$ is the physical meson.

2. **Baryons:** Three quarks
   $$\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$$
   The singlet $\mathbf{1}$ is the physical baryon.

**Why the color singlet?** Only color-singlet states have finite energy. Color-charged states (octet, decuplet, etc.) have infinite energy due to confinement—they cannot exist as isolated particles.

**The Baryon Color Wavefunction:**

For three quarks with colors $c_1, c_2, c_3 \in \{r, g, b\}$:

$$|\text{color singlet}\rangle = \frac{1}{\sqrt{6}} \varepsilon_{c_1 c_2 c_3} |c_1 c_2 c_3\rangle$$

Explicitly:
$$= \frac{1}{\sqrt{6}}(|rgb\rangle - |rbg\rangle + |gbr\rangle - |grb\rangle + |brg\rangle - |bgr\rangle)$$

This is the **Levi-Civita symbol** $\varepsilon_{c_1 c_2 c_3}$, which is totally antisymmetric. When you apply any SU(3) color transformation, the state remains unchanged (singlet property).

### 5.5 SU(3): Weight Diagrams and Young Tableaux

**Purpose: Why SU(3) is More Complex than SU(2)**

SU(2) has rank 1 (one Cartan generator $J_z$), so representations are labeled by a single quantum number $j$, and states within a representation by $m$. The tensor product decomposition for SU(2) is simple: $j_1 \otimes j_2 = |j_1-j_2| \oplus \cdots \oplus (j_1+j_2)$.

SU(3) has rank 2 (two Cartan generators). This means:
1. Representations need **two** labels $(p,q)$ to specify them
2. States within a representation need **two** quantum numbers $(i_3, y)$ to label them
3. The tensor product decomposition is more complex—we need systematic methods

**Two Tools for SU(3): Weight Diagrams and Young Tableaux**

| Tool | What It Shows | Best For |
|:----:|:-------------:|:--------:|
| **Weight diagrams** | States as points in $(i_3, y)$ space | Visualizing representations, understanding particle multiplets |
| **Young tableaux** | Symmetry patterns of tensor indices | Computing tensor products systematically |

**The SU(3) Weight Space**

SU(3) has rank 2, so weights are 2D vectors $(i_3, y)$ where:
- $i_3$ = isospin projection (horizontal axis)
- $y$ = hypercharge (vertical axis)

**The Root Diagram (Adjoint Representation)**

The 6 roots form a hexagon in weight space. Each root corresponds to a raising/lowering operator:

<img src="/images/angular-momentum/su3_root_diagram.png" width="500px" alt="SU(3) Root Diagram">

*The SU(3) root diagram. The six outer points are the root vectors ($I_\pm, U_\pm, V_\pm$) corresponding to ladder operators. The origin contains the two Cartan generators $(I_3, Y)$.*

**The Fundamental Representation $\mathbf{3}$ (Quarks):**

<img src="/images/angular-momentum/su3_fundamental_triplet.png" width="450px" alt="SU(3) Quark Triplet">

*The quark triplet in weight space. The $u$ and $d$ quarks form an isospin doublet, while $s$ is an isosinglet with different hypercharge.*

**The Octet $\mathbf{8}$ (Baryons):**

<img src="/images/angular-momentum/su3_octet_baryons.png" width="550px" alt="SU(3) Baryon Octet">

*The baryon octet forms a hexagon in weight space. Note that the center contains two states ($\Sigma^0$ and $\Lambda$) at the same position—this is a 2D representation of an 8D space.*

**The Decuplet $\mathbf{10}$ (Spin-3/2 Baryons):**

<img src="/images/angular-momentum/su3_decuplet_baryons.png" width="600px" alt="SU(3) Baryon Decuplet">

*The baryon decuplet forms a triangular pattern. The $\Delta$ resonances form a quartet, $\Sigma^*$ a triplet, $\Xi^*$ a doublet, and $\Omega^-$ is a singlet.*

**All Representations Comparison:**

<img src="/images/angular-momentum/su3_all_representations.png" width="700px" alt="SU(3) All Representations">

*Comparison of SU(3) representations. Notice how the dimension increases with the complexity of the shape.*

**Reading Weight Diagrams:**
- **Points** are states (particles), labeled by $(I_3, Y)$ quantum numbers
- **Lines** connect states differing by one root (ladder operators move along these lines)
- **Multiplicity** at a point indicates degeneracy (e.g., center of octet has $\Sigma^0$ and $\Lambda$)
- The **outer boundary** is determined by the highest weight state

**Cartan Subalgebra and Quantum Numbers**

The Cartan subalgebra consists of mutually commuting generators. Its eigenvalues label states:

- **SU(2):** One Cartan generator $J_z$ → one quantum number $m$
- **SU(3):** Two Cartan generators $I_3$ (isospin) and $Y$ (hypercharge) → two quantum numbers $(i_3, y)$

**Weights: State Labels within a Representation**

In a representation, weights are the eigenvalues of Cartan generators:
$$H_i |\Lambda\rangle = \Lambda_i |\Lambda\rangle$$

**Example (SU(3) octet baryons):**
| Baryon | $I_3$ | $Y$ | Weight $(i_3, y)$ |
|--------|-------|-----|-------------------|
| $p$ | +1/2 | 1 | $(+1/2, 1)$ |
| $n$ | -1/2 | 1 | $(-1/2, 1)$ |
| $\Lambda$ | 0 | 0 | $(0, 0)$ |
| $\Sigma^+$ | +1 | 0 | $(+1, 0)$ |

**Roots: How Generators Move Between States**

Roots are weights of the **adjoint representation** (generators themselves). They tell us how ladder operators change quantum numbers:
- SU(2): $J_\pm$ changes $m$ by $\pm 1$ → root vectors $\pm 1$
- SU(3): Ladder operators move between states in the $(i_3, y)$ plane

**Highest Weight Theorem:**
Each irreducible representation has a unique highest weight state. All other states are reached by applying lowering operators. This is why SU(3) representations are labeled by $(p,q)$—these integers specify the highest weight.

**Young Tableaux: Systematic Tensor Product Decomposition**

While weight diagrams visualize representations, **Young tableaux** provide a systematic way to compute tensor products. They represent the symmetry pattern of tensor indices.

**Basic Rules:**
- Each box represents a tensor index
- A row of $n$ boxes = totally symmetric combination of $n$ indices
- A column of $n$ boxes = totally antisymmetric combination of $n$ indices
- For SU($N$), columns can have at most $N$ boxes (more would vanish by antisymmetry)

**SU(3) Representations as Young Tableaux:**

| Dimension | Label | Young Tableau | Symmetry |
|:---------:|:-----:|:-------------:|:--------:|
| 1 | $\mathbf{1}$ | <img src="/images/angular-momentum/young_singlet.png" width="20px"> | Trivial |
| 3 | $\mathbf{3}$ | <img src="/images/angular-momentum/young_3.png" width="25px"> | Single box |
| $\bar{3}$ | $\bar{\mathbf{3}}$ | <img src="/images/angular-momentum/young_3bar.png" width="25px"> | Single column, 2 boxes |
| 6 | $\mathbf{6}$ | <img src="/images/angular-momentum/young_6.png" width="45px"> | Two symmetric boxes |
| 8 | $\mathbf{8}$ | <img src="/images/angular-momentum/young_8.png" width="45px"> | Mixed symmetry |
| 10 | $\mathbf{10}$ | <img src="/images/angular-momentum/young_10.png" width="70px"> | Three symmetric boxes |

**Computing Tensor Products with Young Tableaux:**

The product $\mathbf{3} \otimes \mathbf{3} = \mathbf{6} \oplus \bar{\mathbf{3}}$ is computed by:
1. Start with the first tableau: <img src="/images/angular-momentum/young_3.png" width="25px">
2. Add boxes from the second tableau in all allowed positions
3. Enforce: no two added boxes in same column (antisymmetry constraint)
4. Discard any column with 3 boxes (vanishes in SU(3))

**Example: Meson Octet from $\mathbf{3} \otimes \bar{\mathbf{3}}$**

$$\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$$

This is the quark-antiquark combination giving mesons. The singlet is a scalar meson; the octet contains the pions, kaons, and eta meson.

**Example: Baryon Decuplet from $\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3}$**

$$\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$$

Three quarks combine to give the decuplet (spin-3/2 baryons), two octets (spin-1/2 baryons), and a singlet (forbidden by spin-statistics for three identical fermions).

**Key Insight:** Young tableaux encode the permutation symmetry of identical particles. For multi-quark systems, the color, flavor, and spin wavefunctions must combine to give overall antisymmetry (for fermions).

### 5.6 Isospin: SU(2) in Nuclear Physics

**Nucleons as an SU(2) Doublet**

Proton and neutron are nearly identical under strong interactions:
$$|p\rangle = |I=1/2, I_3=+1/2\rangle, \quad |n\rangle = |I=1/2, I_3=-1/2\rangle$$

This is **not** real spin—it's an internal symmetry (flavor symmetry) with identical SU(2) algebra.

**Physical Consequences:**
- Mirror nuclei (e.g., $^3$He and $^3$H) have similar energy levels
- Isospin conservation in strong interactions constrains reaction cross sections
- The neutron-proton mass difference ($\sim 1.3$ MeV) is electromagnetic, not strong interaction

**Gell-Mann–Nishijima Formula:**
$$Q = I_3 + \frac{B+S}{2}$$
relates charge $Q$, isospin projection $I_3$, baryon number $B$, and strangeness $S$.

**Application:**
Given any three of the four quantum numbers, the fourth is determined. Strong interactions conserve $I_3$, $B$, and $S$, so charge is automatically conserved.

---

## Part VI: Atomic Physics: Coupling Schemes

**Term Symbols and Multi-Electron Atoms**

Atomic states are labeled by term symbols $^{2S+1}L_J$:
- $S$ = total spin
- $L$ = total orbital angular momentum (S, P, D, F for $L=0,1,2,3$)
- $J$ = total angular momentum

**LS vs. jj Coupling: Two Ways to Couple**

| Scheme | Order of Coupling | Applies To |
|--------|-------------------|------------|
| **LS** (Russell-Saunders) | $\mathbf{L} = \sum \mathbf{l}_i$, then $\mathbf{J} = \mathbf{L} + \mathbf{S}$ | Light atoms (weak spin-orbit) |
| **jj** | $\mathbf{j}_i = \mathbf{l}_i + \mathbf{s}_i$, then $\mathbf{J} = \sum \mathbf{j}_i$ | Heavy atoms (strong spin-orbit) |

Both are group-theoretically valid; the choice depends on which interaction dominates.

**Hund's Rules:** From group theory, the ground state maximizes symmetry:
1. Maximum $S$ (symmetric spin state)
2. Maximum $L$ for that $S$
3. $J$ depends on shell filling (minimum for $<$ half, maximum for $>$ half)

---

## Part VII: Spherical Harmonics and Central Potentials

The algebraic machinery developed so far finds immediate application in the physics of central force fields, where the potential depends only on the radial coordinate $V(r)$. Angular momentum plays a central role because the spherical symmetry of such systems guarantees that $[H, L^2] = [H, L_z] = 0$, allowing simultaneous eigenstates of energy and angular momentum. This leads to the separation of the Schrödinger equation into radial and angular parts.

### 7.1 Separation of Variables in Spherical Coordinates

For a particle in a central potential $V(r)$, the Hamiltonian is:

$$H = -\frac{\hbar^2}{2\mu}\nabla^2 + V(r)$$

In spherical coordinates:

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2}\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$$

The angular part is related to $L^2$:

$$L^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$$

Therefore:
$$H = -\frac{\hbar^2}{2\mu}\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{L^2}{2\mu r^2} + V(r)$$

### 7.2 Simultaneous Eigenfunctions and Spherical Harmonics

Since $[H, L^2] = [H, L_z] = [L^2, L_z] = 0$, we have simultaneous eigenfunctions:

$$\psi(r, \theta, \phi) = R_{nl}(r)Y_l^m(\theta, \phi)$$

where:
- $Y_l^m(\theta, \phi)$ are the **spherical harmonics** (eigenfunctions of $L^2$ and $L_z$)
- $L^2 Y_l^m = \hbar^2 l(l+1) Y_l^m$
- $L_z Y_l^m = \hbar m Y_l^m$ with $m = -l, -l+1, ..., l$

**Spherical Harmonics: The "Standard Basis" for Orbital Angular Momentum**

Spherical harmonics $Y_l^m(\theta, \phi)$ are the position-space representation of the angular momentum eigenstates $|l, m\rangle$. They form a complete orthonormal set on the unit sphere:

$$\int_0^{2\pi} d\phi \int_0^{\pi} d\theta \sin\theta \, [Y_l^m(\theta, \phi)]^* Y_{l'}^{m'}(\theta, \phi) = \delta_{ll'}\delta_{mm'}$$

**Explicit Form:**

$$Y_l^m(\theta, \phi) = (-1)^m \sqrt{\frac{(2l+1)(l-m)!}{4\pi(l+m)!}} P_l^m(\cos\theta) e^{im\phi}$$

where $P_l^m$ are the associated Legendre polynomials.

**First Few Spherical Harmonics:**

| $l$ | $m$ | $Y_l^m(\theta, \phi)$ | Name |
|:---:|:---:|:---------------------:|:----:|
| 0 | 0 | $\sqrt{\frac{1}{4\pi}}$ | s-wave |
| 1 | 0 | $\sqrt{\frac{3}{4\pi}}\cos\theta$ | p$_z$ |
| 1 | $\pm 1$ | $\mp\sqrt{\frac{3}{8\pi}}\sin\theta e^{\pm i\phi}$ | p$_{\pm}$ |
| 2 | 0 | $\sqrt{\frac{5}{16\pi}}(3\cos^2\theta - 1)$ | d$_{z^2}$ |

**Visualization:**

<img src="/images/angular-momentum/spherical_harmonics_overview.png" width="700px" alt="Spherical harmonics probability density">

*Angular probability density $|Y_l^m|^2$ for s, p, and d states. The radial distance from the origin represents the probability density in that direction (x-z plane cross-section).*

**What is Being Shown:**

The figure displays **$|Y_l^m(\theta, \phi)|^2$**, the angular probability density. This is the physical quantity that describes where the particle can be found—the quantum analog of the classical orbital shape.

**Key Features:**
- **$|Y_0^0|^2$**: Spherical (s-state)
- **$|Y_1^0|^2$**: Dumbbell along $z$-axis (p$_z$)  
- **$|Y_1^{\pm 1}|^2$**: Torus in $xy$-plane; the x-z cross-section shows a "dumbbell" edge-on view
- **$|Y_2^0|^2$**: Two lobes along $z$-axis with equatorial ring (d$_{z^2}$)
- **$|Y_2^{\pm 2}|^2$**: More pronounced torus than $l=1$

**Complex vs. Real Spherical Harmonics**

| Type | Form | Eigenstate of | Used in |
|:----:|:----:|:-------------:|:-------:|
| Complex $Y_l^m$ | Eigenfunctions of $L_z$ | $L_z$ | Physics (angular momentum) |
| Real orbitals | Linear combinations of $Y_l^{\pm m}$ | $L^2$ only | Chemistry (bonding) |

**Important Distinction:**

The figure displays $|Y_l^m|^2$, which is the **probability density** for finding the electron at a given angular position. This is NOT the same as the "real orbitals" (p$_x$, p$_y$, etc.) used in chemistry.

| Quantity | What It Is | Physical Meaning |
|:--------:|:----------:|:----------------:|
| $|Y_l^m|^2$ | Modulus squared of spherical harmonic | Probability density as function of angle |
| Real orbitals (p$_x$, p$_y$) | Linear combinations: $Y_l^{\pm m} \pm Y_l^{\mp m}$ | Standing waves with definite nodal planes |

**Key Point:** The labels like "p$_z$" and "d$_{z^2}$" in the figure indicate which real orbital has the SAME probability density pattern as $|Y_l^m|^2$. But mathematically:
- p$_z$ orbital $\propto Y_1^0$ (real, proportional to $\cos\theta$)
- p$_x$ orbital $\propto Y_1^{-1} - Y_1^{+1}$ (real combination)
- p$_y$ orbital $\propto Y_1^{-1} + Y_1^{+1}$ (real combination, with $i$ factors)

Real orbitals are used in chemistry because they create standing waves along specific axes, useful for understanding chemical bonding along bond directions.

### 7.3 Angular Momentum in Central Force Fields: Key Theorems

**Theorem 1: Degeneracy with respect to magnetic quantum number $m$**

For a particle in a central force field $V(r)$, the energy eigenvalues are independent of the magnetic quantum number $m$.

**Proof:**

The Hamiltonian is:
$$H = \frac{\mathbf{p}^2}{2\mu} + V(r)$$

We need to show $[H, L_z] = 0$.

$$[L_z, \mathbf{p}^2] = [(xp_y - yp_x), (p_x^2 + p_y^2 + p_z^2)]$$

$$= [xp_y, p_x^2] - [yp_x, p_y^2]$$

Using $[x, p_x^2] = 2i\hbar p_x$:

$$[xp_y, p_x^2] = x[p_y, p_x^2] + [x, p_x^2]p_y = 2i\hbar p_x p_y$$

Similarly:
$$[yp_x, p_y^2] = y[p_x, p_y^2] + [y, p_y^2]p_x = 2i\hbar p_y p_x$$

Therefore:
$$[L_z, \mathbf{p}^2] = 2i\hbar p_x p_y - 2i\hbar p_y p_x = 0$$

Also $[L_z, V(r)] = 0$ since $V(r)$ depends only on $r = \sqrt{x^2+y^2+z^2}$, which is rotationally invariant.

Thus $[H, L_z] = 0$, proving that energy is independent of $m$. The degeneracy is $2l+1$.

**Theorem 2: Radial Equation and Behavior Near Origin**

Substituting $\psi = R_{nl}(r)Y_l^m(\theta,\phi)$ into the Schrödinger equation gives the **radial equation**:

$$\left[-\frac{\hbar^2}{2\mu}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{d}{dr}\right) + \frac{\hbar^2 l(l+1)}{2\mu r^2} + V(r)\right]R_{nl}(r) = E R_{nl}(r)$$

Define $u_{nl}(r) = r R_{nl}(r)$ to obtain:

$$\left[-\frac{\hbar^2}{2\mu}\frac{d^2}{dr^2} + V_{\text{eff}}(r)\right]u_{nl}(r) = E u_{nl}(r)$$

with the **effective potential**:
$$\boxed{V_{\text{eff}}(r) = V(r) + \frac{\hbar^2 l(l+1)}{2\mu r^2}}$$

The second term is the **centrifugal barrier**. For $r \to 0$, assuming $V(r)$ is less singular than $1/r^2$, the centrifugal term dominates. The equation becomes:

$$\frac{d^2u}{dr^2} - \frac{l(l+1)}{r^2}u = 0$$

Trying $u \propto r^s$ gives the indicial equation $s(s-1) = l(l+1)$, with solutions $s = l+1$ or $s = -l$. 

**Why $s = -l$ is Unphysical:**

For $s = -l$, we have $u \propto r^{-l}$ and thus $R = u/r \propto r^{-l-1}$. The normalization integral for the radial wavefunction is:
$$\int_0^\infty |R_{nl}(r)|^2 r^2 dr = \int_0^\infty |u_{nl}(r)|^2 dr$$

Near $r = 0$, the $s = -l$ solution gives:
$$\int_0^{\epsilon} |u|^2 dr \propto \int_0^{\epsilon} r^{-2l} dr$$

For $l \geq 1$, this integral diverges at the origin since $-2l \leq -2 < -1$. 

For $l = 0$, we have $R \propto r^{-1}$. While the probability integral $\int_0^\epsilon |R|^2 r^2 dr = \int_0^\epsilon dr$ appears finite, the wavefunction $R \propto 1/r$ is singular at the origin. More importantly, the kinetic energy expectation value:
$$\langle T \rangle \propto \int_0^\epsilon \left|\frac{d}{dr}(rR)\right|^2 dr = \int_0^\epsilon \left|\frac{d}{dr}(1)\right|^2 dr$$
diverges because the derivative of a constant is zero... actually, let us be more careful. With $u = rR = $ constant, we have $u' = 0$ for $r > 0$, but the discontinuity at $r=0$ gives a delta function contribution. The correct calculation shows the kinetic energy is infinite. Therefore, the $s = -l$ solution must be discarded on physical grounds.

The regular solution is:
$$\boxed{u_{nl}(r) \propto r^{l+1} \quad \Rightarrow \quad R_{nl}(r) = \frac{u_{nl}}{r} \propto r^l}$$

**Behavior Summary:**
- **s-waves ($l=0$)**: $R_{n0}(0) \neq 0$, finite probability at origin
- **p-waves ($l=1$)**: $R_{n1} \propto r$, linear suppression
- **d-waves ($l=2$)**: $R_{n2} \propto r^2$, quadratic suppression

Higher angular momentum states are increasingly excluded from the nucleus by the centrifugal barrier.

### 7.4 The Hidden Symmetry of the Hydrogen Atom: SO(4) and the Runge-Lenz Vector

The Coulomb potential $V(r) = -e^2/r$ possesses a **hidden symmetry** that goes beyond the obvious rotational symmetry. This additional symmetry explains the "accidental" degeneracy of hydrogen energy levels: states with the same principal quantum number $n$ but different orbital angular momentum $l$ are degenerate, even though $[H, L^2] \neq 0$ for a generic central potential.

#### 7.4.1 The Quantum Runge-Lenz Vector

In quantum mechanics, the Runge-Lenz vector operator is defined as:

$$\boxed{\hat{\mathbf{A}} = \frac{1}{2}(\hat{\mathbf{p}} \times \hat{\mathbf{L}} - \hat{\mathbf{L}} \times \hat{\mathbf{p}}) - \mu k \frac{\hat{\mathbf{r}}}{r}}$$

The symmetric ordering is required because $\hat{\mathbf{p}}$ and $\hat{\mathbf{L}}$ do not commute. Using $\hat{\mathbf{L}} \times \hat{\mathbf{p}} = -\hat{\mathbf{p}} \times \hat{\mathbf{L}} + 2i\hbar\hat{\mathbf{p}}$:

$$\hat{\mathbf{A}} = \hat{\mathbf{p}} \times \hat{\mathbf{L}} - i\hbar\hat{\mathbf{p}} - \mu k \frac{\hat{\mathbf{r}}}{r}$$

Or equivalently:
$$\hat{\mathbf{A}} = \frac{1}{\mu}\hat{\mathbf{p}} \times \hat{\mathbf{L}} - \frac{k\hat{\mathbf{r}}}{r} - \frac{i\hbar}{\mu}\hat{\mathbf{p}}$$

**Commutation with Hamiltonian:**

For the hydrogen Hamiltonian:
$$\hat{H} = \frac{\hat{\mathbf{p}}^2}{2\mu} - \frac{k}{r}$$

One can show that:
$$[\hat{H}, \hat{\mathbf{A}}] = 0$$

This means $\hat{\mathbf{A}}$ is a conserved quantity, generating a symmetry of the system.

#### 7.4.2 The Rescaled Runge-Lenz Vector and SO(4) Algebra

To reveal the algebraic structure, define the **rescaled Runge-Lenz vector**:

$$\boxed{\hat{\mathbf{K}} = \sqrt{-\frac{\mu}{2E}} \hat{\mathbf{A}}}$$

(For bound states, $E < 0$, so the square root is real.)

The operators $\hat{\mathbf{L}}$ and $\hat{\mathbf{K}}$ satisfy the following commutation relations:

**Angular Momentum Algebra (as expected):**
$$[L_i, L_j] = i\hbar \varepsilon_{ijk} L_k$$

**Cross Relations between $\mathbf{L}$ and $\mathbf{K}$:**

$$\boxed{[L_i, K_j] = i\hbar \varepsilon_{ijk} K_k}$$

**Proof of the Cross Commutation Relation:**

We need to show that $\mathbf{K}$ transforms as a vector under rotations generated by $\mathbf{L}$. First, note that $[L_i, r_j] = i\hbar \varepsilon_{ijk} r_k$ and $[L_i, p_j] = i\hbar \varepsilon_{ijk} p_k$. This means both $\mathbf{r}$ and $\mathbf{p}$ are vector operators.

Since $\mathbf{L} = \mathbf{r} \times \mathbf{p}$, we have:
$$[L_i, L_j] = i\hbar \varepsilon_{ijk} L_k$$

Now consider $[L_i, A_j]$ where $\mathbf{A} = \mathbf{p} \times \mathbf{L} - i\hbar\mathbf{p} - \mu k \mathbf{r}/r$. Since $\mathbf{p}$, $\mathbf{L}$, and $\mathbf{r}$ are all vector operators, their cross products also transform as vectors. Specifically:

- $[L_i, p_j] = i\hbar \varepsilon_{ijk} p_k$ (vector)
- $[L_i, L_j] = i\hbar \varepsilon_{ijk} L_k$ (vector)
- $[L_i, r_j/r] = i\hbar \varepsilon_{ijk} r_k/r$ (scalar $r$ commutes with $L_i$)

Therefore, each term in $\mathbf{A}$ transforms as a vector:
$$[L_i, A_j] = i\hbar \varepsilon_{ijk} A_k$$

Since $\mathbf{K}$ is proportional to $\mathbf{A}$ (with a factor that commutes with $\mathbf{L}$ because $[\mathbf{L}, H] = 0$ and thus $[\mathbf{L}, E] = 0$ for eigenstates):

$$[L_i, K_j] = i\hbar \varepsilon_{ijk} K_k \quad \checkmark$$

This confirms that $\mathbf{K}$ is a vector operator under rotations.

**The Key Commutation Relation: $[K_i, K_j]$**

$$\boxed{[K_i, K_j] = i\hbar \varepsilon_{ijk} L_k}$$

**Proof:**

This is the most involved calculation. Using $\hat{\mathbf{K}} = \sqrt{-\mu/(2E)}\hat{\mathbf{A}}$ and the definition of $\hat{\mathbf{A}}$:

$$[A_i, A_j] = -2i\hbar H \varepsilon_{ijk} L_k$$

Therefore:
$$[K_i, K_j] = -\frac{\mu}{2E} [A_i, A_j] = -\frac{\mu}{2E} (-2i\hbar H \varepsilon_{ijk} L_k) = i\hbar \varepsilon_{ijk} L_k$$

where we used $H = E$ (on energy eigenstates) in the last step.

**Sketch of the Calculation:**

Computing $[A_i, A_j]$ involves lengthy but straightforward commutator algebra using:
- $[r_i, p_j] = i\hbar \delta_{ij}$
- $[r_i, p^2] = 2i\hbar p_i$  
- $[p_i, r] = -i\hbar r_i/r$

The key result is:
$$[A_i, A_j] = -2i\hbar H \varepsilon_{ijk} L_k$$

On an energy eigenspace ($H = E$), this becomes:
$$[A_i, A_j] = -2i\hbar E \varepsilon_{ijk} L_k$$

The scaling factor $\sqrt{-\mu/(2E)}$ in $\mathbf{K} = \sqrt{-\mu/(2E)}\mathbf{A}$ is chosen to normalize this to the standard angular momentum commutator form.

#### 7.4.3 Casimir Operators

**Definition:** A **Casimir operator** is an operator that commutes with all generators of a Lie algebra. For the angular momentum algebra so(3), the Casimir operator is:

$$\boxed{\mathbf{L}^2 = L_x^2 + L_y^2 + L_z^2}$$

This commutes with all components:
$$[\mathbf{L}^2, L_i] = 0$$

The eigenvalue of $\mathbf{L}^2$ labels the irreducible representations: $\mathbf{L}^2 |l,m\rangle = \hbar^2 l(l+1) |l,m\rangle$.

**SO(4) Casimir Operators:**

The algebra generated by $\mathbf{L}$ and $\mathbf{K}$ is isomorphic to so(4), the Lie algebra of rotations in 4 dimensions. Define:

$$\mathbf{M} = \frac{1}{2}(\mathbf{L} + \mathbf{K}), \quad \mathbf{N} = \frac{1}{2}(\mathbf{L} - \mathbf{K})$$

These satisfy two independent so(3) algebras:
$$[M_i, M_j] = i\hbar \varepsilon_{ijk} M_k, \quad [N_i, N_j] = i\hbar \varepsilon_{ijk} N_k, \quad [M_i, N_j] = 0$$

The Casimir operators of so(4) are:

$$\boxed{C_1 = \mathbf{M}^2 + \mathbf{N}^2 = \frac{1}{2}(\mathbf{L}^2 + \mathbf{K}^2)}$$
$$\boxed{C_2 = \mathbf{M}^2 - \mathbf{N}^2 = \mathbf{L} \cdot \mathbf{K} = 0}$$

The second Casimir vanishes because $\mathbf{L} \cdot \mathbf{A} = 0$ (orthogonality of angular momentum and Runge-Lenz vector), which implies $\mathbf{L} \cdot \mathbf{K} = 0$.

**Eigenvalues:**
For representations labeled by $(m, n)$ where $m, n$ are the quantum numbers for $\mathbf{M}^2$ and $\mathbf{N}^2$:
$$\mathbf{M}^2 = \hbar^2 m(m+1), \quad \mathbf{N}^2 = \hbar^2 n(n+1)$$

Since $C_2 = 0$, we have $m = n$, and:
$$C_1 = \hbar^2 [m(m+1) + n(n+1)] = 2\hbar^2 n(n+1)$$

#### 7.4.4 The Accidental Degeneracy Explained

**Energy Formula from SO(4):**

Using the identity:
$$\mathbf{A}^2 = \mu^2 k^2 + 2\mu H(\mathbf{L}^2 + \hbar^2)$$

(This includes a quantum correction $\hbar^2$ not present classically.)

Therefore:
$$\mathbf{K}^2 = -\frac{\mu}{2E} \mathbf{A}^2 = -\frac{\mu}{2E}[\mu^2 k^2 + 2\mu E(\mathbf{L}^2 + \hbar^2)]$$

The first Casimir:
$$C_1 = \frac{1}{2}(\mathbf{L}^2 + \mathbf{K}^2) = \frac{1}{2}\mathbf{L}^2 - \frac{\mu^3 k^2}{4E} - \frac{\mu}{2}(\mathbf{L}^2 + \hbar^2)$$

$$= -\frac{\mu^3 k^2}{4E} - \frac{\mu\hbar^2}{2}$$

Setting $C_1 = 2\hbar^2 n(n+1)$ (with $n = m$ from $C_2 = 0$):

$$2\hbar^2 n(n+1) = -\frac{\mu^3 k^2}{4E} - \frac{\mu\hbar^2}{2}$$

Solving for $E$:

$$-\frac{\mu^3 k^2}{4E} = 2\hbar^2 n(n+1) + \frac{\mu\hbar^2}{2} = \hbar^2(2n^2 + 2n + \frac{1}{2})$$

Actually, the standard convention uses the principal quantum number $n = 0, 1, 2, ...$ where the irreducible representation is labeled by $(j, j)$ with $j = (n-1)/2$. Then:

$$C_1 = 2\hbar^2 \cdot \frac{n-1}{2} \cdot \frac{n+1}{2} = \frac{\hbar^2(n^2-1)}{2}$$

Equating:
$$\frac{\hbar^2(n^2-1)}{2} = -\frac{\mu^3 k^2}{4E} - \frac{\mu\hbar^2}{2}$$

$$\frac{\hbar^2 n^2}{2} = -\frac{\mu^3 k^2}{4E}$$

$$\boxed{E_n = -\frac{\mu k^2}{2\hbar^2 n^2} = -\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2 n^2} = -\frac{13.6 \text{ eV}}{n^2}}$$

**Why is this degeneracy "accidental"?**

The energy depends **only on $n$**, not on $l$. For a given $n$:
- The allowed values of $l$ are $l = 0, 1, ..., n-1$
- For each $l$, there are $2l+1$ values of $m$
- The total degeneracy is $\sum_{l=0}^{n-1}(2l+1) = n^2$

In a generic central potential, the energy would depend on both $n$ and $l$ (e.g., in alkali atoms, the penetrating $s$-orbitals have lower energy due to core penetration). The Coulomb potential is special because its SO(4) symmetry makes $[H, \mathbf{K}] = 0$, and since $\mathbf{K}^2$ depends only on $n$, all states with the same $n$ are degenerate regardless of $l$.

**Summary of the Symmetry Structure:**

| Symmetry | Generators | Casimir | Degeneracy |
|----------|------------|---------|------------|
| SO(3) rotational | $\mathbf{L}$ | $\mathbf{L}^2$ | $2l+1$ (magnetic) |
| SO(4) hidden | $\mathbf{L}$, $\mathbf{K}$ | $C_1 = \frac{1}{2}(\mathbf{L}^2 + \mathbf{K}^2)$ | $n^2$ (full hydrogen) |

The larger SO(4) symmetry explains why hydrogen has more degeneracy than required by rotational symmetry alone. This "accidental" degeneracy is actually a signature of the hidden dynamical symmetry of the $1/r$ potential.



