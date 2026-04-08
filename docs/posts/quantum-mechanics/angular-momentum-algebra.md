---
title: "Angular Momentum Algebra and Its Applications"
description: "Comprehensive treatment of angular momentum theory: algebraic structure, spin systems, Clebsch-Gordan coefficients, central force fields, and identical particle systems"
date: 2026-04-04
tags: ["quantum mechanics", "angular momentum", "spin", "Clebsch-Gordan coefficients", "central force field", "identical particles"]
category: "quantum-mechanics"
math: true
---

# Angular Momentum Algebra and Its Applications

This article presents a systematic treatment of angular momentum theory in quantum mechanics. We begin with the fundamental algebraic structure—commutation relations and ladder operators—then develop the matrix representations for spin systems. Building on this foundation, we explore the addition of angular momenta and the resulting Clebsch-Gordan theory. The subsequent sections develop applications to atomic physics coupling schemes and central force fields, including spherical harmonics and the hidden SO(4) symmetry of the hydrogen atom. The article concludes with a deeper group-theoretic perspective on angular momentum (rotation groups SO(3) and SU(2)), including SU(3) flavor and color symmetries.

The logical progression follows: **Algebraic Structure** → **Ladder Operators** → **Spin Systems** → **Angular Momentum Addition** → **Atomic Physics Applications** → **Central Force Fields** → **Group Theory**.

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

## Part V: Atomic Physics: Coupling Schemes

Multi-electron atoms present a fundamental problem: how do the individual angular momenta of electrons combine? Each electron has orbital angular momentum $\mathbf{l}_i$ and spin $\mathbf{s}_i$, and there are $(2l_i+1)(2s_i+1)$ states per electron. For $N$ electrons, the total number of states grows exponentially, but the symmetries of identical fermions and the hierarchy of electromagnetic interactions allow us to organize these into physically meaningful term symbols.

### 5.1 Term Symbols: The Notation

Atomic states are labeled by term symbols $^{2S+1}L_J$:
- **$S$** = total spin quantum number
- **$L$** = total orbital angular momentum quantum number (S=0, P=1, D=2, F=3, G=4...)
- **$J$** = total angular momentum quantum number
- **$2S+1$** = spin multiplicity (singlet, doublet, triplet, etc.)

**Examples:**
- $^2P_{3/2}$: Doublet (S=1/2), P-wave (L=1), J=3/2
- $^3D_2$: Triplet (S=1), D-wave (L=2), J=2
- $^1S_0$: Singlet (S=0), S-wave (L=0), J=0

### 5.2 LS (Russell-Saunders) Coupling

**The Hierarchy of Interactions**

In light atoms (roughly $Z < 30$), the electrostatic repulsion between electrons dominates over spin-orbit coupling. This leads to the LS coupling scheme:

1. **First**: Individual orbital angular momenta couple to total $L$
   $$\mathbf{L} = \sum_{i} \mathbf{l}_i$$
   
2. **Second**: Individual spins couple to total $S$
   $$\mathbf{S} = \sum_{i} \mathbf{s}_i$$
   
3. **Finally**: $\mathbf{L}$ and $\mathbf{S}$ couple via spin-orbit interaction
   $$\mathbf{J} = \mathbf{L} + \mathbf{S}$$

**Why This Order?**

The electrostatic repulsion depends on spatial configuration, which is determined by orbital angular momentum. This is because the electrostatic energy is computed from the Coulomb integral $\langle \psi | \frac{e^2}{|\mathbf{r}_i - \mathbf{r}_j|} | \psi \rangle$, which depends on the spatial wavefunction—and the spatial wavefunction is characterized by orbital angular momentum quantum numbers $l$ and $m_l$.

**Why same $l$ but different $m_l$ have different spatial distributions:**

The magnetic quantum number $m_l$ determines the orientation of the orbital in space. For example:
- $p_z$ ($m_l = 0$): electron density concentrated along the $z$-axis
- $p_x$ ($m_l = \pm 1$ combinations): electron density in the $xy$-plane

Two electrons with the same $l$ but different $m_l$ have their charge distributed differently in space, leading to different average separations $\langle |\mathbf{r}_i - \mathbf{r}_j| \rangle$ and therefore different Coulomb repulsion energies.

**The Exchange Interaction:**

The exchange interaction is a purely quantum mechanical effect arising from the antisymmetry requirement of identical fermions. When electrons have parallel spins (same $m_s$), they can occupy the same spatial region only if their spatial wavefunction is antisymmetric—this keeps them apart and reduces Coulomb repulsion. When spins are antiparallel, the symmetric spatial wavefunction allows them to come closer, increasing repulsion. This energy difference creates an effective "exchange force" that favors parallel spin alignment.

**Mathematical Structure**

The Hamiltonian in LS coupling approximation:
$$H = H_0 + \underbrace{\sum_{i<j} \frac{e^2}{|\mathbf{r}_i - \mathbf{r}_j|}}_{\text{dominant in light atoms}} + \underbrace{H_{\text{SO}}}_{\text{perturbation}}$$

where:
- $H_0$ is the central field approximation (independent electron model)
- The electrostatic repulsion term couples the orbital motions of electrons
- $H_{\text{SO}}$ is the spin-orbit coupling, treated as a perturbation

**Energy splitting hierarchy:**
1. **Configuration**: Electrons in specific shells (e.g., $2p^2$) — largest energy scale
2. **Term**: Same $L$ and $S$ — split by electrostatic repulsion
3. **Level**: Same $L$, $S$, different $J$ — split by spin-orbit coupling

For example, the $2p^2$ configuration splits into terms $^3P$, $^1D$, $^1S$, and the $^3P$ term further splits into levels $^3P_0$, $^3P_1$, $^3P_2$.

### 5.3 Deriving Term Symbols: Detailed Examples

**Goal:** Determine the possible quantum states (terms) for multi-electron atoms and find the ground state configuration using Hund's rules.

**Example 1: Two p-electrons (p² configuration)**

Consider two equivalent p-electrons (same $n$ and $l=1$), as in carbon ($2p^2$) or oxygen ($2p^4$).

For a single p-electron: $l=1$, $s=1/2$, giving $m_l = -1, 0, +1$ and $m_s = \pm 1/2$.

**Step 1: List all microstates**

Two equivalent p-electrons: we must respect the Pauli exclusion principle. The possible $(m_{l1}, m_{s1}; m_{l2}, m_{s2})$ combinations where the total state is antisymmetric.

Actually, a better approach is to use the vector model for $L$ and $S$:
- $l_1 = l_2 = 1$, so $L = |l_1 - l_2|, ..., l_1 + l_2 = 0, 1, 2$ (S, P, D)
- $s_1 = s_2 = 1/2$, so $S = 0$ or $1$ (singlet or triplet)

**Pauli Principle and Symmetry:**

For equivalent electrons (same $n$ and $l$), the total wavefunction must be antisymmetric under exchange. The total wavefunction factors as:
$$\Psi_{\text{total}} = \psi_{\text{space}} \otimes \chi_{\text{spin}}$$

where:
- $\psi_{\text{space}}$ depends on orbital angular momentum $L$
- $\chi_{\text{spin}}$ depends on total spin $S$

**Symmetry of $L$ states under particle exchange:**

The total orbital wavefunction with definite $L$ transforms under particle exchange according to $(-1)^L$:
- **Even $L$ (S, D, ...): symmetric** under exchange $(-1)^L = +1$
- **Odd $L$ (P, F, ...): antisymmetric** under exchange $(-1)^L = -1$

For two p-electrons:
- $L=0$ (S): even → symmetric spatial wavefunction
- $L=1$ (P): odd → antisymmetric spatial wavefunction  
- $L=2$ (D): even → symmetric spatial wavefunction

**Combining with spin symmetry:**

Since $\Psi_{\text{total}}$ must be antisymmetric:
- If $S=1$ (symmetric spin, triplet), spatial part must be **antisymmetric** → only $L=1$ (P) allowed
- If $S=0$ (antisymmetric spin, singlet), spatial part must be **symmetric** → $L=0$ or $L=2$ allowed

Therefore:
- **Triplet states** ($S=1$, symmetric spin): can only combine with $L=1$ (P)
  - $^3P$ with $J = |L-S|, ..., L+S = 0, 1, 2$
  - Terms: $^3P_0$, $^3P_1$, $^3P_2$
  
- **Singlet states** ($S=0$, antisymmetric spin): can combine with $L=0$ or $L=2$
  - $^1S$ with $J=0$: $^1S_0$
  - $^1D$ with $J=2$: $^1D_2$

**Result for p²:** $^3P_{0,1,2}$, $^1D_2$, $^1S_0$

**State Counting:**

Each term $^{2S+1}L_J$ has $(2J+1)$ magnetic sublevels ($m_J = -J, ..., +J$). Counting all states:
- $^3P$: $J = 0, 1, 2$ → $(1 + 3 + 5) = 9$ states
- $^1D$: $J = 2$ → $5$ states  
- $^1S$: $J = 0$ → $1$ state

Total: $9 + 5 + 1 = 15$ microstates.

**Verification:** Two equivalent p-electrons, each with 6 possible states ($m_l = -1, 0, 1$ and $m_s = \pm 1/2$). The number of ways to choose 2 states from 6 is:
$$\binom{6}{2} = \frac{6 \times 5}{2} = 15$$

This confirms we have found all possible states.

**Example 2: Carbon Ground State ($1s^2 2s^2 2p^2$)**

**Why closed shells contribute $L=0$, $S=0$:**

In a filled subshell (e.g., $p^6$, $d^{10}$), all possible $(m_l, m_s)$ combinations are occupied:
- For every electron with $m_l$, there is one with $-m_l$
- For every electron with $m_s = +1/2$, there is one with $m_s = -1/2$

Therefore, the total projections are:
$$M_L = \sum_i m_{l,i} = 0, \quad M_S = \sum_i m_{s,i} = 0$$

A closed shell is spherically symmetric. The only spherically symmetric state has $L=0$ and $S=0$. Thus closed shells don't contribute to the total angular momentum, and we only consider valence electrons ($2p^2$ for carbon).

From above, possible terms: $^3P$, $^1D$, $^1S$.

**Hund's First Rule**: The term with maximum multiplicity (maximum $S$) lies lowest in energy.

**Multiplicity = spin degeneracy = $2S+1$:**

- $S=0$: singlet (1 state) — multiplicity 1
- $S=1$: triplet (3 states) — multiplicity 3  
- $S=2$: quintet (5 states) — multiplicity 5

Higher multiplicity $\Rightarrow$ larger $S$ $\Rightarrow$ more parallel spins.

**Application to carbon:**
- $^3P$ has $S=1$ (triplet, multiplicity 3) — highest $S$
- $^1D$ and $^1S$ have $S=0$ (singlets, multiplicity 1)

Therefore, the ground term is $^3P$.

**Hund's Second Rule**: For a given $S$, the term with maximum $L$ lies lowest.
- Among singlets: $^1D$ ($L=2$) vs $^1S$ ($L=0$)
- So $^1D$ is lower than $^1S$

Energy ordering: $^3P < {}^1D < {}^1S$

**Hund's Third Rule**: The ground level $J$ depends on shell filling:
- Less than half-filled: lowest $J$ is lowest in energy
- More than half-filled: highest $J$ is lowest in energy

For $p^2$ (2 out of 6 possible electrons, less than half), the ground level is $^3P_0$.

**Final answer**: Carbon ground state is $^3P_0$.

**Example 3: Oxygen Ground State ($1s^2 2s^2 2p^4$)**

Four p-electrons in a shell that can hold 6 electrons (2 per orbital × 3 orbitals). 

**Hole picture:** A filled $p^6$ shell has $L=0$, $S=0$. Removing 2 electrons (creating 2 holes) leaves 4 electrons. The term structure of $p^4$ is identical to $p^2$ because holes have the same angular momentum coupling properties as electrons:
- $p^2$ (2 electrons in 6 states) → 15 microstates
- $p^4$ (4 electrons in 6 states) → also 15 microstates (by particle-hole symmetry)

Therefore $p^4$ gives the same terms as $p^2$: $^3P$, $^1D$, $^1S$.

Ground term is still $^3P$ (Hund's first rule, maximum $S$).

**Applying Hund's third rule:**
- $p^4$ is more than half-filled (4 out of 6 > 3)
- For more than half-filled shells, the level with **maximum** $J$ has lowest energy
- For $^3P$: $J = |L-S|, ..., L+S = 0, 1, 2$
- Maximum $J = 2$

**Final answer**: Oxygen ground state is $^3P_2$.

### 5.4 jj Coupling

**When Spin-Orbit Dominates**

In heavy atoms ($Z > 50$), the spin-orbit interaction for each electron becomes stronger than the electrostatic repulsion between electrons. This leads to a different coupling scheme where the order of angular momentum addition is reversed.

**LS vs. jj: Different Coupling Schemes as Different Bases**

Both LS and jj coupling describe the same physical system, but they use different bases (sets of basis states):

| Coupling | First Coupling | Second Coupling | Basis States |
|----------|---------------|-----------------|--------------|
| **LS** | $\mathbf{L} = \sum_i \mathbf{l}_i$ | $\mathbf{S} = \sum_i \mathbf{s}_i$ | $|L, M_L; S, M_S\rangle$ |
| **jj** | $\mathbf{j}_i = \mathbf{l}_i + \mathbf{s}_i$ | $\mathbf{J} = \sum_i \mathbf{j}_i$ | $|j_1, m_{j1}; j_2, m_{j2}; ...\rangle$ |

For a given configuration, both bases span the same Hilbert space, but:
- In LS coupling, $L^2$ and $S^2$ are good quantum numbers (commute with the dominant part of $H$)
- In jj coupling, $j_i^2$ are good quantum numbers

When spin-orbit dominates, the jj basis diagonalizes the Hamiltonian more naturally.

**jj Coupling Scheme:**

Each electron's orbital and spin first couple to form individual total angular momentum:
$$\mathbf{j}_i = \mathbf{l}_i + \mathbf{s}_i$$

giving $j_i = l_i \pm 1/2$ (for $l_i \neq 0$).

Then the individual $j_i$ couple to total $J$:
$$\mathbf{J} = \sum_{i} \mathbf{j}_i$$

**Example: Lead ($6p^2$ configuration)**

For each p-electron:
- $l=1$, $s=1/2$
- $j = l \pm 1/2 = 1/2$ or $3/2$

**jj Coupling for Two Equivalent Electrons:**

For two equivalent electrons with individual angular momentum $j$, a total $J$ state is allowed if $(-1)^{2j-J} = -1$ (antisymmetric).

| Configuration | Allowed $J$ | Forbidden $J$ |
|:-------------:|:-----------:|:-------------:|
| $(1/2)^2$ | $J=0$ | $J=1$ |
| $(3/2)^2$ | $J=0, 2$ | $J=1, 3$ |
| $(1/2)(3/2)$ | $J=1, 2$ (no restriction) | — |

The formula works for all $j$ because $2j$ is always an integer. For non-equivalent electrons (different $j$), there is no Pauli restriction.

**Energy level ordering in jj coupling:**

In jj coupling, the energy ordering depends on:
1. The $j$ values of individual electrons (spin-orbit energy)
2. The residual electrostatic interaction between $j$-coupled electrons

For heavy atoms, larger $j$ typically has lower energy due to spin-orbit coupling ($j = l + 1/2$ lower than $j = l - 1/2$).

The resulting levels are labeled as $(j_1, j_2)_J$:
- $(1/2, 1/2)_0$
- $(3/2, 3/2)_0$, $(3/2, 3/2)_2$
- $(1/2, 3/2)_1$, $(1/2, 3/2)_2$

Note: jj coupling doesn't use $L$ and $S$ quantum numbers—these are not good quantum numbers when spin-orbit dominates.

**Detailed Example: Cerium ($4f^1 5d^1$) in jj Coupling**

Cerium has one electron in the $4f$ shell and one in the $5d$ shell.

**Step 1: Individual $j$ values**

For the $4f$ electron ($l=3$):
- $j = l \pm 1/2 = 5/2$ or $7/2$
- Spin-orbit splits these: $j=5/2$ is lower in energy for less than half-filled shells

For the $5d$ electron ($l=2$):
- $j = l \pm 1/2 = 3/2$ or $5/2$

**Step 2: Coupling to total $J$**

**Important:** Since the electrons are in different shells ($n=4$ for $4f$ vs $n=5$ for $5d$), they are **distinguishable** by their principal quantum number. This means the Pauli exclusion principle does not restrict their coupling—all $J$ values from coupling $j_f$ and $j_d$ are allowed.

| $j_f$ | $j_d$ | Possible $J$ | Label |
|:-----:|:-----:|:------------:|:-----:|
| $5/2$ | $3/2$ | $1, 2, 3, 4$ | $(5/2, 3/2)_J$ |
| $5/2$ | $5/2$ | $0, 1, 2, 3, 4, 5$ | $(5/2, 5/2)_J$ |
| $7/2$ | $3/2$ | $2, 3, 4, 5$ | $(7/2, 3/2)_J$ |
| $7/2$ | $5/2$ | $1, 2, 3, 4, 5, 6$ | $(7/2, 5/2)_J$ |

**Step 3: Energy ordering**

In heavy atoms like Ce, the lowest energy configuration typically has the lowest individual $j$ values:
- $4f$ electron: $j_f = 5/2$ (lower)
- $5d$ electron: $j_d = 3/2$ (lower)

Coupling these gives levels $(5/2, 3/2)_J$ with $J = 1, 2, 3, 4$.

The lowest total $J$ from this group is $J=1$, but the actual ground state depends on the residual interaction between the $j$-coupled electrons.

**Comparison with LS coupling:**

In LS coupling for $f^1 d^1$:
- $L = 3 + 2, 3 + 2 - 1, ..., |3-2| = 5, 4, 3, 2, 1$ (H, G, F, D, P)
- $S = 0$ or $1$ (singlet or triplet)
- Possible terms: $^3H$, $^1H$, $^3G$, $^1G$, $^3F$, $^1F$, $^3D$, $^1D$, $^3P$, $^1P$

The ground term is $^3H$ (maximum $S$, then maximum $L$), giving levels $^3H_4$, $^3H_5$, $^3H_6$.

**In Ce**, neither pure scheme applies perfectly, but jj coupling provides a better description due to the strong spin-orbit interaction in the $4f$ electron.

### 5.5 Comparison and Physical Interpretation

| Feature | LS Coupling | jj Coupling |
|:-------:|:-----------:|:-----------:|
| **Dominant interaction** | Electrostatic repulsion | Spin-orbit coupling |
| **Good quantum numbers** | $L$, $S$, $J$ | $j_i$, $J$ only |
| **Level labeling** | $^{2S+1}L_J$ | $(j_1, j_2, ...)J$ |
| **Applies to** | Light atoms ($Z < 30$) | Heavy atoms ($Z > 50$) |
| **Example elements** | C, N, O, Fe | Pb, Hg, rare earths |

**Intermediate Coupling**

In the transition region ($Z \approx 30-50$), neither pure LS nor pure jj coupling applies. This is called **intermediate coupling**.

**What does "mixtures of LS terms" mean?**

In pure LS coupling, the eigenstates are eigenstates of $L^2$ and $S^2$. But when neither electrostatic nor spin-orbit interaction dominates, the true Hamiltonian eigenstates are superpositions of different LS terms.

For example, in intermediate coupling, the ground state might be:
$$|\Psi_{\text{ground}}\rangle = \alpha |^3P\rangle + \beta |^1D\rangle + \gamma |^1S\rangle$$

where $\alpha$, $\beta$, $\gamma$ are mixing coefficients determined by the relative strengths of the interactions.

**Physical picture:**
- In LS coupling: $L$ and $S$ are approximately conserved separately
- In jj coupling: individual $j_i$ are approximately conserved
- In intermediate coupling: no angular momentum is perfectly conserved; all are partially mixed

The energy levels cannot be simply labeled by pure term symbols, though they may still be approximately characterized by their dominant LS or jj character.

**The Physical Origin**

LS coupling works when electrons "feel" each other's spatial distribution more strongly than their own spin-orbit interaction. jj coupling works when each electron's own spin-orbit interaction dominates, so they act more independently.

### 5.6 Hund's Rules: Complete Statement and Physical Origin

**The Rules:**

1. **Maximum Spin Rule**: The term with the highest multiplicity (maximum $S$) has the lowest energy.
   
   *Physical origin*: 
   
   **Why does symmetric spin = maximum $S$?**
   
   For $N$ electrons, the maximum total spin $S = N/2$ occurs when all spins are parallel (all $m_s = +1/2$ or all $m_s = -1/2$). The spin wavefunction for this state is:
   $$\chi_{S=N/2, M_S=N/2} = |\uparrow\uparrow\uparrow...\uparrow\rangle$$
   
   This is symmetric under any pair exchange because swapping two up spins doesn't change the state.
   
   In general, for a given number of electrons:
   - Higher $S$ means more parallel spins
   - More parallel spins → more symmetric spin wavefunction
   - Maximum $S$ = completely symmetric spin wavefunction
   
   **Why does antisymmetric spatial wavefunction keep electrons apart?**
   
   An antisymmetric spatial wavefunction satisfies:
   $$\psi_{\text{space}}(\mathbf{r}_1, \mathbf{r}_2) = -\psi_{\text{space}}(\mathbf{r}_2, \mathbf{r}_1)$$
   
   At $\mathbf{r}_1 = \mathbf{r}_2$ (same position):
   $$\psi_{\text{space}}(\mathbf{r}, \mathbf{r}) = -\psi_{\text{space}}(\mathbf{r}, \mathbf{r}) \implies \psi_{\text{space}}(\mathbf{r}, \mathbf{r}) = 0$$
   
   **The probability of finding two electrons at the same position is zero!**
   
   This creates a "Fermi hole"—a region around each electron where the other electron is excluded. The average electron-electron separation is larger, reducing the Coulomb repulsion energy:
   $$\langle V_{\text{rep}} \rangle = \int d^3r_1 d^3r_2 \, \frac{e^2}{|\mathbf{r}_1 - \mathbf{r}_2|} |\psi(\mathbf{r}_1, \mathbf{r}_2)|^2$$
   
   When electrons are kept apart (larger $|\mathbf{r}_1 - \mathbf{r}_2|$ on average), this integral gives a smaller value—lower energy.

2. **Maximum Orbital Rule**: For a given spin multiplicity, the term with the maximum $L$ has the lowest energy.
   
   *Physical origin*: 
   
   **Why higher $L$ means electrons stay apart:**
   
   For a given spin state (fixed $S$), different values of total orbital angular momentum $L$ correspond to different spatial correlations between electrons.
   
   Consider two electrons in a p-shell. The possible total $L$ values are $L = 0, 1, 2$ (S, P, D terms). 
   
   **The key insight:** Electrons with higher $L$ have their angular momentum vectors more aligned. In the semiclassical picture:
   - High $L$ ($L = l_1 + l_2$): Both electrons orbit in the same direction
   - Low $L$ ($L = |l_1 - l_2|$): Electrons orbit in opposite directions
   
   When electrons orbit in the same direction (high $L$), they maintain roughly opposite positions, maximizing their average separation. This reduces Coulomb repulsion. The spatial wavefunction for high-$L$ states has nodes in the relative coordinate, creating a "correlation hole" where $\Psi \approx 0$ when electrons are close together.

3. **Minimum/Maximum $J$ Rule**: 
   - Less than half-filled subshell: level with minimum $J$ is lowest
   - More than half-filled subshell: level with maximum $J$ is lowest
   
   *Physical origin*: This comes from the sign of the spin-orbit coupling constant. For less than half-filled, spin-orbit coupling is "normal" ($\zeta > 0$), favoring $J = |L-S|$. For more than half-filled, the effective $\zeta < 0$ (hole picture), favoring $J = L+S$.

### 5.7 Permutation Symmetry and Young Diagrams in Atomic Spectroscopy

**Atomic spectroscopy** provides a concrete application of permutation symmetry and Young diagrams. The notation used throughout this chapter ($^{2S+1}L_J$ terms, singlet/triplet states) originates from the interplay between electron spin and orbital symmetries.

#### Young Diagram vs. Young Tableau

Before proceeding, a clarification of terminology:

- **Young Diagram (Young图)**: An array of boxes representing the partition of an integer. Only the shape matters—no numbers inside. For example, three boxes in a row represents total symmetry, while three boxes in a column represents total antisymmetry.

- **Young Tableau (Young表)**: A Young diagram with the numbers $1, 2, ..., n$ inserted into the boxes, each used exactly once. A **standard Young tableau** has numbers increasing left-to-right in rows and top-to-bottom in columns.

The diagram tells us the *symmetry type*; the tableau helps enumerate *basis states*.

#### Example: Three p-Electrons (Nitrogen Atom $2p^3$)

Consider the ground state configuration of atomic nitrogen: three electrons in the $2p$ subshell. This is a staple example in atomic spectroscopy.

**The Setup:**
- Each electron has orbital angular momentum $l=1$ and spin $s=1/2$
- Total Hilbert space dimension: $6^3 = 216$ (without Pauli exclusion)
- With Pauli exclusion: only 20 valid states

**Permutation Symmetry Constraints:**

The total wavefunction must be **antisymmetric** under electron exchange. This requires:
- Symmetric orbital × Antisymmetric spin, OR
- Antisymmetric orbital × Symmetric spin

**Young Diagrams for $S_3$ (three electrons):**

| Spin Symmetry | Young Diagram | Spin $S$ | Dimension |
|:-------------:|:-------------:|:--------:|:---------:|
| Fully symmetric | [3] (three boxes in a row) | $3/2$ | 4 |
| Mixed symmetry | [2,1] (hook shape) | $1/2$ | 2 (two copies) |
| Fully antisymmetric | [1,1,1] (three boxes in column) | $0$ | 0 (vanishes for spin-1/2) |

**Orbital-Spin Association:**

| Spin State | Orbital State | Allowed $L$ | Spectroscopic Terms |
|:----------:|:-------------:|:-----------:|:-------------------:|
| $S=3/2$ (symmetric) | $L=0$ (antisymmetric) | $J=3/2$ | $^4S_{3/2}$ |
| $S=1/2$ (mixed) | $L=1,2$ (mixed) | $J=1/2, 3/2, 5/2$ | $^2P_{1/2,3/2}$, $^2D_{3/2,5/2}$ |

**The Complete Set of 20 States:**

$$^4S_{3/2}, \quad ^2D_{5/2}, \quad ^2D_{3/2}, \quad ^2P_{3/2}, \quad ^2P_{1/2}$$

**Physical Interpretation:**

The quartet term $^4S$ (spin $S=3/2$, all spins parallel) requires a completely antisymmetric orbital wavefunction—meaning all three electrons avoid each other in space. This is achieved when the total orbital angular momentum vanishes ($L=0$), creating a spherically symmetric but internally correlated distribution.

The doublet terms ($^2D$, $^2P$) have mixed symmetry in both spin and orbital spaces. The two distinct $^2D$ (and $^2P$) terms arise from the two equivalent representations of the mixed symmetry type [2,1].

**Why 20 States?**

Without the Pauli exclusion principle, we'd have $6^3 = 216$ possible states (6 spin-orbitals for each of 3 electrons). The antisymmetry requirement restricts us to placing at most 2 electrons per orbital (one spin-up, one spin-down). Counting ways to place 3 arrows (↑ or ↓) in 3 boxes (the $m_l = -1, 0, +1$ orbitals) with at most 2 per box gives exactly 20 configurations—matching our group theory result.

---

## Part VI: Spherical Harmonics and Central Potentials

The algebraic machinery developed so far finds immediate application in the physics of central force fields, where the potential depends only on the radial coordinate $V(r)$. Angular momentum plays a central role because the spherical symmetry of such systems guarantees that $[H, L^2] = [H, L_z] = 0$, allowing simultaneous eigenstates of energy and angular momentum. This leads to the separation of the Schrödinger equation into radial and angular parts.

### 6.1 Separation of Variables in Spherical Coordinates

For a particle in a central potential $V(r)$, the Hamiltonian is:

$$H = -\frac{\hbar^2}{2\mu}\nabla^2 + V(r)$$

In spherical coordinates:

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2}\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$$

The angular part is related to $L^2$:

$$L^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$$

Therefore:
$$H = -\frac{\hbar^2}{2\mu}\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{L^2}{2\mu r^2} + V(r)$$

### 6.2 Simultaneous Eigenfunctions and Spherical Harmonics

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

| $l$ | $m$ | $Y_l^m(\theta, \phi)$ |
|:---:|:---:|:---------------------:|
| 0 | 0 | $\sqrt{\frac{1}{4\pi}}$ |
| 1 | 0 | $\sqrt{\frac{3}{4\pi}}\cos\theta$ |
| 1 | $\pm 1$ | $\mp\sqrt{\frac{3}{8\pi}}\sin\theta e^{\pm i\phi}$ |
| 2 | 0 | $\sqrt{\frac{5}{16\pi}}(3\cos^2\theta - 1)$ |

<img src="/images/angular-momentum/spherical_harmonics_overview.png" width="700px" alt="Spherical harmonics probability density">

*Angular probability density $|Y_l^m|^2$ for $l=0,1,2$ states (x-z plane cross-section).*

**The Shape of p Orbitals: Angular Momentum as a Visible Manifestation**

The p orbitals, often depicted with their familiar "two lobes" shape, correspond to the spherical harmonics $Y_1^{-1}$, $Y_1^0$, and $Y_1^{+1}$ associated with the three possible values $m_l = -1, 0, +1$.

Physically, the angular momentum vector $\mathbf{L}$ does not point along a fixed direction. Instead, it **precesses** about the $z$-axis, tracing out a cone. The $L_z$ eigenvalue $\hbar m$ represents the projection onto the quantization axis, but the full vector $\mathbf{L}$ has magnitude $\sqrt{l(l+1)}\hbar > |m|\hbar$, meaning there is always a component perpendicular to $z$.

The asymmetric angular shape of p orbitals arises precisely because $l=1$. The probability density $|Y_l^m|^2$ reflects this precession: instead of showing the angular momentum pointing in a definite direction, the orbital shape represents the time-averaged probability distribution of a vector that is constantly sweeping around the cone.

In this sense, **the shape of the orbital is the visible manifestation of orbital angular momentum**.

**Reference:** For a Lie algebra perspective on angular momentum and the hidden SO(4) symmetry of the hydrogen atom, see Chapter 30 of *Non-relativistic Quantum Theory* by Lam (2009). The SO(4) approach uses two commuting SU(2) subalgebras generated by $\mathbf{L}^+ = \frac{1}{2}(\mathbf{L} + \mathbf{M}')$ and $\mathbf{L}^- = \frac{1}{2}(\mathbf{L} - \mathbf{M}')$, where $\mathbf{M}' = \sqrt{-\frac{m}{2E}}\mathbf{M}$ is a rescaled Runge-Lenz vector with the same dimensions as angular momentum. The Casimir operators $C = \mathbf{L}^+ \cdot \mathbf{L}^+ + \mathbf{L}^- \cdot \mathbf{L}^-$ yield $2l_+(l_+ + 1) = 2l_-(l_- + 1)$, giving the principal quantum number $n = 2l_+ + 1$ and explaining the $n^2$-fold degeneracy of hydrogen energy levels.

### 6.3 Angular Momentum in Central Force Fields: Key Theorems

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

The solution $u \propto r^{-l}$ gives $R = u/r \propto r^{-l-1}$, which is singular at $r = 0$ for all $l$.

**For $l \geq 1$:** The probability integral
$$\int_0^\epsilon |R|^2 r^2 dr \propto \int_0^\epsilon r^{-2l} dr$$
diverges at the origin, so the wavefunction cannot be normalized.

**For $l = 0$:** $R \propto 1/r$ leads to $u = rR \propto 1$ (constant). This fails for **two reasons**:

1. **Boundary condition at origin:** The radial wavefunction must satisfy $u(0) = 0$ (probability must vanish at $r=0$). A constant $u \propto 1$ violates this.

2. **Normalization at infinity:** The normalization integral $\int_0^\infty |u|^2 dr = \int_0^\infty 1 \, dr$ diverges linearly as $r \to \infty$.

Both the **origin** (boundary condition) and the **upper limit** (normalization) make this solution unphysical.

**Physical requirement:** A physical wavefunction must be finite everywhere and have finite energy. The $s = -l$ solution fails both criteria and must be discarded.

The regular solution is:
$$\boxed{u_{nl}(r) \propto r^{l+1} \quad \Rightarrow \quad R_{nl}(r) = \frac{u_{nl}}{r} \propto r^l}$$

**Behavior Summary:**
- **s-waves ($l=0$)**: $R_{n0}(0) \neq 0$, finite probability at origin
- **p-waves ($l=1$)**: $R_{n1} \propto r$, linear suppression
- **d-waves ($l=2$)**: $R_{n2} \propto r^2$, quadratic suppression

Higher angular momentum states are increasingly excluded from the nucleus by the centrifugal barrier.

## Part VII: Symmetry and Group Theory in Physics

Angular momentum theory is deeply rooted in group representation theory. This part explains the mathematical structures underlying symmetries and their physical interpretations.

### 7.1 Representations and Irreducibility

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

In quantum mechanics, states are **rays**: $|\psi\rangle$ and $e^{i\phi}|\psi\rangle$ represent the same physical state. Operators need only satisfy the group law **up to a phase**:
$$D(g_1)D(g_2) = e^{i\omega(g_1,g_2)} D(g_1g_2)$$

**Example: Spin-1/2 and 2π Rotations**

For spin-1/2:
$$D^{(1/2)}(R_z(\theta)) = e^{-i\theta\sigma_z/2}$$

Key fact: $R_z(2\pi) = I$ in SO(3), but:
$$D^{(1/2)}(R_z(2\pi)) = e^{-i\pi\sigma_z} = -I \neq I$$

**Why?** Spin-1/2 is a representation of **SU(2)**, not SO(3). The map SU(2) $\to$ SO(3) is 2-to-1: both $U$ and $-U$ in SU(2) map to the same rotation in SO(3). When we try to represent SO(3) using the SU(2) matrices, we get a phase ambiguity:
$$D(R_z(2\pi)) = -I = e^{i\pi} D(I)$$

Since $|\psi\rangle$ and $-|\psi\rangle$ give the same probabilities, this $-1$ phase is unobservable. Thus spin-1/2 forms a **projective representation** of SO(3).

**3. Fundamental Representation**

The **fundamental representation** is the defining representation of the group—the matrix representation used to define the group itself.

**SU(2):** Defined as $2 \times 2$ unitary matrices with $\det = 1$, acting on $\mathbb{C}^2$ (spinors).

**SU(3):** Defined as $3 \times 3$ unitary matrices with $\det = 1$, acting on $\mathbb{C}^3$ (quark triplet).

**4. Adjoint Representation**

The **adjoint representation** is where the group acts on its own Lie algebra (generator space) via **similarity transformation**:
$$T \xrightarrow{g} g T g^{-1}$$

For SU(2), this is the spin-1 (vector) representation. For SU(3), the adjoint is 8-dimensional (gluons).

**Why similarity transformation?** The Lie algebra transforms under the group by conjugation, preserving the commutation relations.

---

**Characters and Orthogonality**

The **character** of a representation is the trace: $\chi_j(g) = \text{Tr}[D^{(j)}(g)]$. Characters depend only on the **conjugacy class** (e.g., rotation angle $\theta$, not axis).

**Deriving the character formula:**

For spin-$j$, the rotation about any axis by angle $\theta$ has eigenvalues $e^{-im\theta}$ for $m = -j, ..., j$. Therefore:
$$\chi_j(\theta) = \sum_{m=-j}^{j} e^{-im\theta}$$

This geometric series sums to:
$$\chi_j(\theta) = \frac{\sin((j+1/2)\theta)}{\sin(\theta/2)}$$

**Examples:**
- **Spin-0:** $\chi_0(\theta) = 1$
- **Spin-1/2:** $\chi_{1/2}(\theta) = 2\cos(\theta/2)$
- **Spin-1:** $\chi_1(\theta) = 1 + 2\cos\theta$

**Orthogonality relation:**

Characters of different irreps are orthogonal when integrated over the group:
$$\int_0^{2\pi} d\theta \, \sin^2\frac{\theta}{2} \, \chi_j(\theta)\chi_{j'}(\theta) \propto \delta_{jj'}$$

**Application: Decompose $\frac{1}{2} \otimes \frac{1}{2}$**

**The mechanism:** When we combine two spin-1/2 particles, the total Hilbert space is $2 \times 2 = 4$ dimensional. We want to decompose this into irreducible representations of the rotation group.

**Step 1: Form the product character**

For two spin-1/2 particles, the product character (trace of the tensor product representation) is:
$$\chi_{1/2}(\theta) \cdot \chi_{1/2}(\theta) = 4\cos^2(\theta/2) = 2 + 2\cos\theta$$

**Step 2: Project onto irreducible representations**

The character orthogonality theorem says: if a representation decomposes as $D = \bigoplus_j n_j D^{(j)}$, then:
$$n_j = \frac{\int d\theta \, \rho(\theta) \chi(\theta) \chi_j(\theta)}{\int d\theta \, \rho(\theta) \chi_j^2(\theta)}$$

where $\rho(\theta) = \sin^2(\theta/2)$ is the Haar measure for SU(2).

**Step 3: Calculate coefficients**

For $j=0$ (singlet, $\chi_0 = 1$):
$$n_0 = \frac{\int_0^{2\pi} d\theta \, \sin^2\frac{\theta}{2} \cdot (2 + 2\cos\theta) \cdot 1}{\int_0^{2\pi} d\theta \, \sin^2\frac{\theta}{2} \cdot 1} = \frac{\pi}{\pi} = 1$$

For $j=1$ (triplet, $\chi_1 = 1 + 2\cos\theta$):
$$n_1 = \frac{\int_0^{2\pi} d\theta \, \sin^2\frac{\theta}{2} \cdot (2 + 2\cos\theta) \cdot (1 + 2\cos\theta)}{\int_0^{2\pi} d\theta \, \sin^2\frac{\theta}{2} \cdot (1 + 2\cos\theta)^2} = \frac{\pi}{\pi} = 1$$

**Result:** One singlet ($j=0$, dimension 1) and one triplet ($j=1$, dimension 3):
$$\frac{1}{2} \otimes \frac{1}{2} = 0 \oplus 1$$

This matches the direct counting: $1 + 3 = 4 = 2 \times 2$.

### 7.2 Lie Algebras: Why the Identity?

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

### 7.3 SU(2) vs. SO(3): Double Cover

**Same Algebra, Different Topology**

SU(2) and SO(3) have identical Lie algebras but different global topology:

| Property | SO(3) | SU(2) |
|----------|-------|-------|
| Elements | 3×3 orthogonal matrices | 2×2 unitary, $\det = 1$ |
| Topology | 3D ball (antipodal Identification) | 3-sphere $S^3$ |
| Loops | Non-contractible loops exist | Simply connected |
| Periodicity | $R(2\pi) = I$ | $U(2\pi) = -I$, $U(4\pi) = I$ |

**Fundamental Group Explained:**

The **fundamental group** $\pi_1$ classifies "loops" (closed paths) in the group manifold:

**SO(3):** $\pi_1 = \mathbb{Z}_2$ (two elements)

Visualize SO(3) as a solid ball of radius $\pi$:
- A rotation by angle $\theta$ about axis $\mathbf{n}$ is represented by point $\theta\mathbf{n}$ in the ball
- **Antipodal identification:** Points on the surface satisfy $\pi\mathbf{n} \sim -\pi\mathbf{n}$ because rotation by $\pi$ about $\mathbf{n}$ equals rotation by $\pi$ about $-\mathbf{n}$

**Why the $2\pi$ rotation cannot be shrunk:**

A $2\pi$ rotation about the z-axis corresponds to a path from the center to point $(0, 0, \pi)$ on the surface. At the surface, this point is **identified** with $(0, 0, -\pi)$. The path then "jumps" to $(0, 0, -\pi)$ and returns to the center.

This creates a loop that goes from center $\to$ north pole $\to$ (jump to south pole) $\to$ center. You cannot continuously shrink this loop to a point because:
1. The endpoints of the "jump" are identified (the same point in SO(3))
2. But in the ball visualization, they are opposite points
3. Any attempt to shrink the loop would require breaking the identification

**SU(2):** $\pi_1 = \{e\}$ (only identity)
- SU(2) is a 3-sphere $S^3$: $U = a_0 I + i\mathbf{a}\cdot\boldsymbol{\sigma}$ with $a_0^2 + |\mathbf{a}|^2 = 1$
- **No identifications**—all points are distinct
- Every loop can be shrunk to a point (simply connected)

**SU(2):** $\pi_1 = \{e\}$ (only identity)
- SU(2) is a 3-sphere $S^3$: $U = a_0 I + i\mathbf{a}\cdot\boldsymbol{\sigma}$ with $a_0^2 + |\mathbf{a}|^2 = 1$
- No identifications—all points are distinct
- Every loop can be shrunk to a point (simply connected)

**The Double Cover:**

$$
\text{SU(2)}/\mathbb{Z}_2 \cong \text{SO(3)}
$$

This means: Identify $U \sim -U$ in SU(2), and the result is SO(3).

**Explicit map from SU(2) to SO(3):**

Take SU(2) element: $U(\theta, \mathbf{n}) = e^{-i\theta \mathbf{n}\cdot\boldsymbol{\sigma}/2}$

The corresponding SO(3) rotation $R(\theta, \mathbf{n})$ rotates by angle $\theta$ about axis $\mathbf{n}$.

**Key observations:**
1. Both use the **same** angle $\theta$ and axis $\mathbf{n}$
2. SU(2): $U(\theta + 4\pi, \mathbf{n}) = U(\theta, \mathbf{n})$ (period $4\pi$)
3. SO(3): $R(\theta + 2\pi, \mathbf{n}) = R(\theta, \mathbf{n})$ (period $2\pi$)
4. **Two-to-one:** Both $U(\theta, \mathbf{n})$ and $U(\theta + 2\pi, \mathbf{n}) = -U(\theta, \mathbf{n})$ map to the same $R(\theta, \mathbf{n})$

**SO(4) and SU(2) × SU(2):**

The SO(4) algebra decomposes as:
$$\mathbf{M} = \frac{1}{2}(\mathbf{L} + \mathbf{K}), \quad \mathbf{N} = \frac{1}{2}(\mathbf{L} - \mathbf{K})$$

giving $[M_i, N_j] = 0$. This suggests:
$$\text{SO(4)} \cong \text{SU(2)}_M \times \text{SU(2)}_N$$

But with a subtlety: if $(U_M, U_N)$ generates an SO(4) element, then $(-U_M, -U_N)$ generates the **same** SO(4) element (both signs flip together). This identification is written as:
$$\text{SO(4)} \cong (\text{SU(2)} \times \text{SU(2)})/\mathbb{Z}_2$$

**What does $/\mathbb{Z}_2$ mean?** It means we identify $(U, V) \sim (-U, -V)$—the two pairs differing by overall sign represent the same group element.

### 7.4 SU(3) Flavor vs. SU(3) Color

**Global vs. Local (Gauge) Symmetry**

| Property | Flavor SU(3) | Color SU(3) |
|----------|-------------|-------------|
| Type | **Global** | **Local (Gauge)** |
| Transformation | Same everywhere | $U(x)$ varies with position |
| Connection | None | Gluon field $A_\mu^a(x)$ |
| Approximate? | Yes (broken by quark masses) | Exact |
| Role | Classifies hadrons | Generates strong force |

**Why "Connection" matters:**

In differential geometry, a **connection** (gauge field) tells you how to compare vectors at different points. For a local symmetry that varies from point to point, you need a connection to maintain covariance under transformations. This connection IS the gauge field (gluon).

**Why local symmetry generates interactions:**

To make a derivative $\partial_\mu$ covariant under local transformations, you must replace it with a **covariant derivative**:
$$D_\mu = \partial_\mu + igA_\mu$$

The kinetic term $|D_\mu\psi|^2$ then contains interaction terms like $g\bar{\psi}A_\mu\psi$, meaning the gauge field $A_\mu$ (gluon) necessarily interacts with matter (quarks).

**Color Singlet Rule:**

Only **color singlets** (states invariant under SU(3) color) have finite energy. **Color-charged states** (octet $\mathbf{8}$, decuplet $\mathbf{10}$, etc.) are confined—they have infinite energy and cannot exist as isolated particles.

**Quark color charges:**
- Quarks are in fundamental $\mathbf{3}$: they carry color charge (r, g, or b)
- Gluons are in adjoint $\mathbf{8}$: they also carry color charge
- Singlets (mesons, baryons) are color-neutral: no net color charge

**Mesons:** $\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$ — singlet $\mathbf{1}$ is physical

**Baryons:** $\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$ — singlet $\mathbf{1}$ is physical

### 7.5 SU(3): Roots, Weights, and Young Tableaux

**SU(3) Rank = 2: Two Quantum Numbers**

SU(3) has 8 generators. The maximal set of commuting generators (Cartan subalgebra) has dimension 2, typically chosen as $I_3$ (third component of isospin) and $Y$ (hypercharge). This means states in SU(3) representations need **two quantum numbers** $(i_3, y)$ to label them.

**Roots: The 6 Ladder Operators**

SU(3) has 6 ladder operators ($I_\pm, U_\pm, V_\pm$) that change the weight $(i_3, y)$:
- $I_\pm$: changes $(i_3, y)$ by $(\pm 1, 0)$
- $U_\pm$: changes $(i_3, y)$ by $(\mp 1/2, \pm 1)$  
- $V_\pm$: changes $(i_3, y)$ by $(\pm 1/2, \pm 1)$

**Why exactly 6 roots?**

The SU(3) algebra has structure constants $f_{abc}$ that determine how generators commute. For the algebra to close under commutation:

1. If $\vec{\alpha}$ and $\vec{\beta}$ are roots, then $\vec{\alpha} + \vec{\beta}$ must also be a root (or zero)
2. The angles between roots are quantized to specific values by the algebra

In 2D weight space, the only configuration that satisfies these constraints with all angles compatible is 6 roots at 60° intervals (forming a hexagon).

**Building the Fundamental $\mathbf{3}$**

Start from the highest weight state $u$ with $(i_3, y) = (1/2, 1/3)$:
- Apply $I_-$: $u \to d$ at $(-1/2, 1/3)$
- Apply $V_-$: $u \to s$ at $(0, -2/3)$

The three states $(u, d, s)$ form the quark triplet.

**Building the Adjoint $\mathbf{8}$**

The adjoint representation comes from $\mathbf{3} \otimes \bar{\mathbf{3}}$ (quark-antiquark). With 3 quark flavors and 3 antiquark flavors, we have $3 \times 3 = 9$ combinations. Here's how they organize into the octet + singlet:

**Step 1: The 6 off-diagonal combinations**

When quark and antiquark have different flavors, we get states with non-zero $(I_3, Y)$. Calculate quantum numbers by adding quark and antiquark values:

| Combination | Quark $(i_3, y)$ | Antiquark $(i_3, y)$ | Total $(I_3, Y)$ | Physical State |
|:-----------:|:----------------:|:--------------------:|:----------------:|:--------------:|
| $u\bar{d}$ | $(+1/2, +1/3)$ | $(+1/2, -1/3)$ | $(+1, 0)$ | $\Sigma^+$ |
| $d\bar{u}$ | $(-1/2, +1/3)$ | $(-1/2, -1/3)$ | $(-1, 0)$ | $\Sigma^-$ |
| $u\bar{s}$ | $(+1/2, +1/3)$ | $(0, +2/3)$ | $(+1/2, +1)$ | $p$ |
| $s\bar{u}$ | $(0, -2/3)$ | $(-1/2, +1/3)$ | $(-1/2, -1)$ | $\Xi^-$ |
| $d\bar{s}$ | $(-1/2, +1/3)$ | $(0, +2/3)$ | $(-1/2, +1)$ | $n$ |
| $s\bar{d}$ | $(0, -2/3)$ | $(+1/2, +1/3)$ | $(+1/2, -1)$ | $\Xi^0$ |

**How the quantum numbers add:**
- $I_3$ adds algebraically: $I_3(q) + I_3(\bar{q})$
- $Y$ adds algebraically: $Y(q) + Y(\bar{q})$ (note: antiquark has opposite hypercharge)

These 6 states sit at the vertices of the weight diagram hexagon.

**Step 2: The 3 diagonal combinations (where quark = antiquark flavor)**

For $u\bar{u}, d\bar{d}, s\bar{s}$, both $I_3 = 0$ and $Y = 0$. But we can't use these raw combinations because:

1. The trace $u\bar{u} + d\bar{d} + s\bar{s}$ is invariant under SU(3) — this is the singlet $\mathbf{1}$
2. The remaining 2 orthogonal combinations form part of the octet

**Constructing the physical states:**

First, isolate the singlet (normalize to 1):
$$\text{Singlet} = \frac{1}{\sqrt{3}}(u\bar{u} + d\bar{d} + s\bar{s})$$

This is the $\mathbf{1}$ representation. It transforms as a scalar (no indices).

Now construct octet states from the remaining 2 degrees of freedom. We need states that:
- Are orthogonal to the singlet
- Have definite isospin properties

**$\Sigma^0$ (isospin triplet, $I=1$):**
The isospin triplet $(\Sigma^+, \Sigma^0, \Sigma^-)$ needs $\Sigma^0$ as the $I_3 = 0$ member. Since $\Sigma^+ \sim u\bar{d}$ and $\Sigma^- \sim d\bar{u}$, the $I_3 = 0$ combination must be:
$$\Sigma^0 = \frac{1}{\sqrt{2}}(u\bar{u} - d\bar{d})$$
This is antisymmetric under $u \leftrightarrow d$, matching the isospin-1 property.

**$\Lambda$ (isospin singlet, $I=0$):**
The remaining orthogonal combination (orthogonal to both singlet and $\Sigma^0$) is:
$$\Lambda = \frac{1}{\sqrt{6}}(u\bar{u} + d\bar{d} - 2s\bar{s})$$
This is symmetric under $u \leftrightarrow d$ and has no isospin ($I=0$).

#### Young Diagrams: A Visual Approach to SU(3) Representations

Young diagrams provide a graphical device to represent SU(3) representations and determine how they combine under tensor products. This method translates abstract algebra into concrete geometric language.

**What is a Young diagram?**

A Young diagram consists of boxes arranged in left-aligned rows, with row lengths that do not increase from top to bottom. For SU(3) flavor symmetry (up, down, strange quarks):

- **Single box** $\boxed{\phantom{x}}$ represents the fundamental $\mathbf{3} = \{u, d, s\}$
- **Row of boxes** indicates symmetrization of indices
- **Column of boxes** indicates antisymmetrization of indices
- **Maximum 3 rows** in SU(3): complete antisymmetrization of 4 indices vanishes identically

**Basic Rules for SU(3):**

1. Each box represents a tensor index transforming as the fundamental $\mathbf{3}$
2. Boxes in the same row → symmetric indices
3. Boxes in the same column → antisymmetric indices  
4. Row lengths are non-increasing from top to bottom

**Dimension Formula:**

To compute the dimension of a multiplet:
$$\dim = \prod_{\text{boxes}} \frac{N + c - r}{h}$$

where:
- $N = 3$ (fundamental dimension for SU(3))
- $r$ = row index (0, 1, 2, ... from top)
- $c$ = column index (0, 1, 2, ... from left)
- $h$ = hook length = (boxes to right) + (boxes below) + 1

**Example 1: Two Quarks $\mathbf{3} \otimes \mathbf{3}$**

Add a second box to the first in all admissible ways:

*Configuration A: Two boxes in a row (symmetric)*
$$\boxed{\phantom{x}}\boxed{\phantom{x}} \rightarrow \mathbf{6}$$

- Box 1: $r=0, c=0, h=2$ → factor = $(3+0-0)/2 = 3/2$
- Box 2: $r=0, c=1, h=1$ → factor = $(3+1-0)/1 = 4$
- Dimension: $\frac{3}{2} \times 4 = 6$

The six symmetric states: $uu, dd, ss, (ud+du), (us+su), (ds+sd)$

*Configuration B: Two boxes in a column (antisymmetric)*
$$\begin{array}{|c|}\hline \phantom{x} \\ \hline \phantom{x} \\ \hline\end{array} \rightarrow \bar{\mathbf{3}}$$

- Box 1: $r=0, c=0, h=2$ → factor = $3/2$
- Box 2: $r=1, c=0, h=1$ → factor = $(3+0-1)/1 = 2$
- Dimension: $\frac{3}{2} \times 2 = 3$

The three antisymmetric states: $(ud-du), (us-su), (ds-sd) \sim \bar{u}, \bar{d}, \bar{s}$

Result: $\mathbf{3} \otimes \mathbf{3} = \mathbf{6} \oplus \bar{\mathbf{3}}$

**Example 2: Three Quarks $\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3}$ (Baryons)**

Starting from $\mathbf{3} \otimes \mathbf{3}$ results, add a third box:

*Fully symmetric (three in a row):*
$$\boxed{\phantom{x}}\boxed{\phantom{x}}\boxed{\phantom{x}} \rightarrow \mathbf{10}$$

- Box 1: $(3+0-0)/3 = 1$
- Box 2: $(3+1-0)/2 = 2$  
- Box 3: $(3+2-0)/1 = 5$
- Dimension: $1 \times 2 \times 5 = 10$ (decuplet)

*Mixed symmetry (hook shape, partition {2,1}):*

There are **two distinct hook diagrams**, each giving dimension 8:

**Diagram 2a:** (first two boxes symmetric, third antisymmetric with first)
```
┌───┬───┐
│ A │ B │
├───┼───┘
│ C │
└───┘
```

- Box A: $r=0, c=0$, 1 box right, 1 below → $h=1+1+1=3$ → factor = $(3+0-0)/3 = 1$
- Box B: $r=0, c=1$, 0 right, 0 below → $h=0+0+1=1$ → factor = $(3+1-0)/1 = 4$
- Box C: $r=1, c=0$, 0 right, 0 below → $h=0+0+1=1$ → factor = $(3+0-1)/1 = 2$
- **Dimension: $1 \times 4 \times 2 = 8$**

**Diagram 2b:** (alternative labeling of the same shape)

Actually, the two octets come from two different ways of building the hook—starting from different intermediate states in the tensor product construction. Both have the same shape {2,1} but correspond to different "heritages" in the iteration:

1. **First octet**: Built by adding the third box to the symmetric $\mathbf{6}$ (two boxes in a row), placing the third box below the first
2. **Second octet**: Built by adding the third box to the antisymmetric $\bar{\mathbf{3}}$ (two boxes in a column), placing the third box to the right of the top box

Both constructions yield the same final diagram shape but represent different combinations in the full tensor product space, hence two distinct $\mathbf{8}$ representations.

*Fully antisymmetric (three in column, partition {1,1,1}):*
```
┌───┐
│ A │
├───┤
│ B │
├───┤
│ C │
└───┘
```

- Box A: $r=0, c=0$, 0 right, 2 below → $h=0+2+1=3$ → factor = $(3+0-0)/3 = 1$
- Box B: $r=1, c=0$, 0 right, 1 below → $h=0+1+1=2$ → factor = $(3+0-1)/2 = 1$
- Box C: $r=2, c=0$, 0 right, 0 below → $h=0+0+1=1$ → factor = $(3+0-2)/1 = 1$
- **Dimension: $1 \times 1 \times 1 = 1$ (singlet)**

The single antisymmetric state is: $(ud)s + (ds)u + (su)d - (du)s - (sd)u - (us)d$, where $(ud)$ denotes the antisymmetric pair $ud - du$.

Result: $\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$

**Why Young Diagrams Are Useful:**

Young diagrams provide an immediate visual handle on symmetry properties, making it possible to identify allowed representations without lengthy algebraic manipulations. They do not determine which particles exist, but rather which symmetry patterns are allowed—the group SU(3) fixes the structure, and Young diagrams offer the most transparent way to read it.

### 7.6 Scattering Amplitudes and Isospin: Reaction Channels

Symmetry principles powerfully constrain scattering processes. When a system possesses isospin symmetry, different reaction channels are related by Clebsch-Gordan coefficients.

**The Basic Idea:**

Consider scattering in the isospin basis. The total isospin $I$ is conserved (assuming exact SU(2) isospin symmetry). For a given process, the scattering amplitude depends only on the total isospin:
$$\langle I, I_3 | T | I, I_3 \rangle = A_I$$

Physical states (like $\pi^+ p$, $\pi^- p$, etc.) are superpositions of isospin eigenstates. The amplitude for a specific reaction is obtained by projecting onto the isospin basis:
$$\mathcal{M}(a + b \to c + d) = \sum_I \langle cd | I \rangle \langle I | ab \rangle A_I$$

**Example: Pion-Nucleon Scattering**

The pion-nucleon system has total isospin $I = 1/2$ or $I = 3/2$:
- Pion: $I = 1$ (triplet: $\pi^+, \pi^0, \pi^-$)
- Nucleon: $I = 1/2$ (doublet: $p, n$)

The relevant Clebsch-Gordan decompositions:
$$| \pi^+ p \rangle = | I = 3/2, I_3 = 3/2 \rangle$$
$$| \pi^- p \rangle = \sqrt{\frac{1}{3}} | I = 3/2, I_3 = -1/2 \rangle - \sqrt{\frac{2}{3}} | I = 1/2, I_3 = -1/2 \rangle$$

This gives the scattering amplitudes:
$$\mathcal{M}(\pi^+ + p \to \pi^+ + p) = A_{3/2}$$
$$\mathcal{M}(\pi^- + p \to \pi^- + p) = \frac{1}{3}A_{3/2} + \frac{2}{3}A_{1/2}$$
$$\mathcal{M}(\pi^- + p \to \pi^0 + n) = \frac{\sqrt{2}}{3}(A_{3/2} - A_{1/2})$$

**Physical Consequence:**

If $A_{3/2} \gg A_{1/2}$ (as happens near the $\Delta(1232)$ resonance with $I = 3/2$), we predict:
$$\frac{\sigma(\pi^+ + p)}{\sigma(\pi^- + p)} \approx 3$$

This ratio is experimentally observed, confirming the isospin structure.

**Connection to SU(3):**

When extending from SU(2) isospin to SU(3) flavor, similar relations connect different hadronic reaction channels. The scattering amplitudes for processes like $K^- + p \to \Lambda + \pi^0$, $K^- + p \to \Sigma^0 + \pi^0$, etc., are related by SU(3) Clebsch-Gordan coefficients. This allows predictions of cross-section ratios without detailed dynamical calculations.

**Young Diagrams in Scattering:**

Young diagrams provide a visual way to track permutation symmetry in scattering processes. For multi-particle states:
- The initial state symmetry (represented by a Young diagram) must match the final state symmetry for scattering to occur
- Permutation symmetry constrains which partial waves contribute
- For identical particles, the overall wavefunction symmetry (spatial × spin × isospin) determines allowed reactions

This symmetry-based approach, pioneered by Wigner and extended by many others, allows powerful predictions about scattering processes without solving the full dynamical equations.

