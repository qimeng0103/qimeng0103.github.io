---
title: "Angular Momentum Algebra and Its Applications"
description: "Comprehensive treatment of angular momentum theory: algebraic structure, spin systems, Clebsch-Gordan coefficients, central force fields, and identical particle systems"
date: 2026-04-04
tags: ["quantum mechanics", "angular momentum", "spin", "Clebsch-Gordan coefficients", "central force field", "identical particles"]
category: "quantum-mechanics"
math: true
---

# Angular Momentum Algebra and Its Applications

This article presents a systematic treatment of angular momentum theory in quantum mechanics. We begin with the fundamental algebraic structure—commutation relations and ladder operators—then develop the matrix representations and explicit wave function formalism (spherical harmonics) for orbital angular momentum. Building on this foundation, we explore the addition of angular momenta and the resulting Clebsch-Gordan theory. The latter half of the article develops the deeper group-theoretic perspective (rotation groups SO(3) and SU(2)), and concludes with applications to many-particle systems using Young tableaux.

The logical progression follows: **Algebraic Structure** → **Representation Theory** → **Wave Function Realization** → **Angular Momentum Addition** → **Group Theory** → **Many-Particle Applications**.

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

**Long-wavelength approximation:** For nuclear $\gamma$-decay, the photon wavelength $\lambda = 2\pi/k$ is much larger than the nuclear size ($R \sim 5$ fm). Since $kR \ll 1$:
$$e^{-i\mathbf{k}\cdot\mathbf{r}} \approx 1 - i\mathbf{k}\cdot\mathbf{r} + ...$$

The leading term (constant 1) gives **electric dipole (E1)** transitions. Higher order terms give electric quadrupole (E2), magnetic dipole (M1), etc.

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

The factor $(kR)^{2L}$ arises from the long-wavelength expansion. Let's clarify what each multipole corresponds to:

**Long-wavelength expansion of the photon phase factor:**
$$e^{-i\mathbf{k}\cdot\mathbf{r}} = 1 - i\mathbf{k}\cdot\mathbf{r} + \frac{(-i\mathbf{k}\cdot\mathbf{r})^2}{2!} + ...$$

**Multipole content:**
| Term | Operator | Multipole | Scaling | Status |
|------|----------|-----------|---------|--------|
| $1$ | constant | E0 (monopole) | 1 | Forbidden (charge conservation) |
| $\mathbf{k}\cdot\mathbf{r}$ | $\sim r Y_1^m$ | E1 (dipole) | $kR$ | Allowed (if selection rules permit) |
| $(\mathbf{k}\cdot\mathbf{r})^2$ | $\sim (kr)^2 Y_2^m$ | E2 (quadrupole) | $(kR)^2$ | Allowed |
| ... | ... | $EL$ | $(kR)^L$ | Allowed |

**Key point:** The E1 operator is the **linear term** $\mathbf{k}\cdot\mathbf{r} \sim kR$, not the constant term. The constant term would be E0 (electric monopole), but this is forbidden by charge conservation (it would correspond to changing the total charge, which photon emission cannot do).

The matrix element of the E1 operator involves:
$$\langle f | \hat{O}_{E1} | i \rangle \sim \langle f | \mathbf{k}\cdot\hat{\mathbf{R}} | i \rangle \sim k \langle f | \hat{R} | i \rangle$$

Since $\hat{R}$ is of order nuclear radius $R$ within the nucleus:
$$|\langle f | \hat{O}_{E1} | i \rangle|^2 \sim (kR)^2$$

For E2 (quadrupole):
$$|\langle f | \hat{O}_{E2} | i \rangle|^2 \sim (kR)^4$$

**Typical values for nuclear $\gamma$-decay:**
- Photon energy: $E_\gamma \sim 0.1 - 10$ MeV
- Photon wave number: $k = E_\gamma / \hbar c \sim 10^{-3} - 10^{-1}$ fm$^{-1}$
- Nuclear radius: $R \sim 5$ fm
- Therefore: $kR \sim 0.005 - 0.5$ (typically $\sim 0.1$)

**Relative transition probabilities:**
- E1: $\sim (kR)^2 \sim 10^{-2}$
- E2/M1: $\sim (kR)^4 \sim 10^{-4}$ (100× smaller)
- E3: $\sim (kR)^6 \sim 10^{-6}$ (10000× smaller)

**When is E1 Forbidden? Selection Rules:**

E1 transitions require:
1. **Angular momentum:** $|j_i - j_f| \leq 1 \leq j_i + j_f$ (triangle rule with $L=1$)
2. **Parity:** $\pi_i \neq \pi_f$ (parity must change)

**Nuclear Physics Notation Guide:**
- $^{A}X$: Nucleus with mass number $A$ and element $X$
- $nl_j$: Single-particle orbital with principal quantum number $n$, orbital $l$ ($s,p,d,f,...$ for $l=0,1,2,3,...$), and total angular momentum $j$
- $J^\pi$: State with total angular momentum $J$ and parity $\pi$ ($+$ = even, $-$ = odd)

**Example 1: E1 Allowed — Oxygen-17**
$^{17}$O: $1d_{5/2} \to 2p_{3/2}$ 

**Reaction:** Proton transitions from $d$-shell to $p$-shell.
- $j_i = 5/2$ (initial, $d_{5/2}$ orbital), $j_f = 3/2$ (final, $p_{3/2}$ orbital)
- Angular momentum check: $|5/2 - 3/2| = 1 \leq 1 \leq 5/2 + 3/2 = 4$ ✓ (satisfied)
- Parity check: $l_i = 2$ ($d$-orbital, parity $(-1)^2 = +1$), $l_f = 1$ ($p$-orbital, parity $(-1)^1 = -1$)
- Parity changes: $(+1) \times (-1) = -1$ ✓ (satisfied)
- **Result:** E1 allowed, dominates the decay

**Example 2: E1 Forbidden by Parity — Oxygen-17**
$^{17}$O: $1d_{5/2} \to 1d_{3/2}$ 

**Reaction:** Proton stays in $d$-shell but changes $j$ from $5/2$ to $3/2$.
- $j_i = 5/2$, $j_f = 3/2$: $|5/2 - 3/2| = 1 \leq 1 \leq 4$ ✓ (angular momentum OK)
- Parity check: $l_i = l_f = 2$ (both $d$-orbitals, parity $(-1)^2 = +1$)
- Parity product: $(+1) \times (+1) = +1$ ✗ (does NOT change; E1 requires $-1$)
- **Result:** E1 forbidden. Transition proceeds via M1 (magnetic dipole) or E2 (electric quadrupole), which are $\sim 100\times$ slower.

**Example 3: E1 Forbidden by Angular Momentum — Carbon-12**
$^{12}$C: $0^+_1 \to 0^+_2$ (first excited $0^+$ state decaying to ground state)

**Reaction:** Collective excitation of the nucleus with $J=0$ decays to ground state $J=0$.
- $j_i = 0$, $j_f = 0$: E1 requires $L=1$, but $|0-0| = 0 \nleq 1$ (triangle rule violated)
- **Physical reason:** A vector operator (E1 has $L=1$) cannot connect two states both with $J=0$. The photon must carry away angular momentum, but $0 = 0 + 1$ is impossible.
- **Result:** E1 absolutely forbidden. This transition proceeds via E2 (electric quadrupole), with a lifetime much longer than typical E1 transitions.

**Note:** The $0^+ \to 0^+$ transition cannot occur via single-photon emission at all because a photon always carries at least $L=1$ (one unit of angular momentum). Such transitions proceed via internal conversion (energy transfer to atomic electrons) or two-photon emission.

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

3. **Computational efficiency:** The sum over $m_i$ and $m_f$ can be performed using the orthogonality relation of 3j symbols, giving a simple closed-form result for the angular distribution.

---

## Part V: Group Representation Theory and Its Physical Applications

The addition of angular momenta discussed in Part IV has a deep group-theoretic interpretation. This part develops the mathematical framework of group representations, Lie algebras, and their applications across atomic, nuclear, and particle physics.

### 5.1 Foundations of Group Representation Theory

**What is a Group Representation?**

A **representation** of a group $G$ is a homomorphism from $G$ to the group of linear operators on a vector space $V$. In physics terms: we map abstract group elements to concrete matrices that act on quantum states.

$$D: G \to \text{GL}(V)$$

where $\text{GL}(V)$ is the general linear group on $V$.

**Example: Rotation Group SO(3)**
- Abstract group element: rotation by angle $\theta$ about axis $\mathbf{n}$
- Representation: $3 \times 3$ rotation matrix $R(\mathbf{n}, \theta)$ acting on 3D vectors
- Quantum representation: operator $e^{-i\theta \mathbf{n} \cdot \mathbf{J}/\hbar}$ acting on Hilbert space

**Faithful vs. Non-Faithful Representations**

A representation is **faithful** if different group elements map to different operators (injective homomorphism):
$$g_1 \neq g_2 \implies D(g_1) \neq D(g_2)$$

**Example of faithful representation:** The spin-1/2 representation of SU(2). Every SU(2) element $\pm U$ corresponds to a distinct operator on the 2D spinor space.

**Example of non-faithful representation:** The spin-1 representation of SO(3). Rotations by $2\pi$ and $4\pi$ about any axis both map to the identity operator, even though they are different group elements.

**Reducible vs. Irreducible Representations**

A representation is **reducible** if the vector space $V$ can be decomposed into invariant subspaces:
$$V = V_1 \oplus V_2 \oplus \cdots$$
where each $V_i$ is mapped to itself under all group operations.

A representation is **irreducible** if no such decomposition exists—the space $V$ is "as small as possible" under the group action.

**Physical Significance:**
- **Irreducible representations** correspond to "elementary" multiplet structures
- In angular momentum theory, each value of $j$ labels an irreducible representation of SO(3)
- The $(2j+1)$ states $|j, m\rangle$ with $m = -j, ..., j$ form a basis for this irreducible space

**Direct Sum and Tensor Product**

When we combine two systems with angular momenta $j_1$ and $j_2$:
- **Direct sum:** $D^{(j_1)} \oplus D^{(j_2)}$ describes a system that is EITHER in state $j_1$ OR in state $j_2$ (incoherent mixture)
- **Tensor product:** $D^{(j_1)} \otimes D^{(j_2)}$ describes a system composed of BOTH angular momenta (composite system)

The tensor product decomposes into irreducible representations:
$$D^{(j_1)} \otimes D^{(j_2)} = \bigoplus_{j=|j_1-j_2|}^{j_1+j_2} D^{(j)}$$
This is the group-theoretic statement of angular momentum addition.

### 5.2 Lie Algebras and Their Structure

**From Lie Group to Lie Algebra**

A Lie group is a continuous group where group elements can be parameterized smoothly. The **Lie algebra** is the tangent space at the identity, consisting of the generators of infinitesimal transformations.

For a group element $g(\theta)$ depending on parameter $\theta$:
$$\text{Generator} \propto \frac{d}{d\theta}g(\theta)\bigg|_{\theta=0}$$

**Structure Constants**

The generators $\{T_a\}$ satisfy commutation relations:
$$[T_a, T_b] = i\sum_c f_{abc} T_c$$

The coefficients $f_{abc}$ are the **structure constants** that completely characterize the Lie algebra.

**SU(2) and SO(3) Algebras**

Both SU(2) and SO(3) share the same Lie algebra structure:
$$[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k$$

Structure constants: $f_{ijk} = \varepsilon_{ijk}$ (Levi-Civita symbol)

**Key difference:**
- SO(3): $R_z(2\pi) = I$ (identity)
- SU(2): $U_z(2\pi) = -I$ (minus identity)

SU(2) is the **universal covering group** of SO(3). The relationship is:
$$\text{SU(2)}/\mathbb{Z}_2 \cong \text{SO(3)}$$

For integer $j$, representations of SU(2) factor through to SO(3). For half-integer $j$, they do not—they are "projective representations" of SO(3).

### 5.3 SU(3) and the Eightfold Way

**SU(3) Algebra**

SU(3) is the group of $3 \times 3$ unitary matrices with determinant 1. It has 8 generators (compared to 3 for SU(2)).

The standard basis uses Gell-Mann matrices $\lambda_a$ ($a = 1, ..., 8$):
$$T_a = \frac{1}{2}\lambda_a$$

Commutation relations:
$$[T_a, T_b] = i\sum_c f_{abc} T_c$$

where $f_{abc}$ are the SU(3) structure constants.

**Physical Application: Quark Model**

In particle physics, SU(3) flavor symmetry organizes hadrons into multiplets:
- **Quarks:** Up, down, strange form a triplet (fundamental representation $\mathbf{3}$)
- **Baryons:** Proton, neutron, etc. form octets and decuplets
- **Mesons:** Pions, kaons, etc. form octets and singlets

The SU(3) representations are labeled by two integers $(p, q)$:
- $(1, 0)$: Triplet $\mathbf{3}$ (quarks)
- $(0, 1)$: Antitriplet $\bar{\mathbf{3}}$ (antiquarks)
- $(1, 1)$: Octet $\mathbf{8}$ (octet baryons like proton, neutron)
- $(3, 0)$: Decuplet $\mathbf{10}$ (decuplet baryons like $\Delta$, $\Omega^-$)

**Tensor Product in SU(3):**
$$\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$$

This explains why baryons (3 quarks) appear as singlets, octets, and decuplets.

### 5.4 Roots and Weights

**Cartan Subalgebra**

For a Lie algebra of rank $r$, the **Cartan subalgebra** is the maximal set of commuting generators $\{H_i\}$ ($i = 1, ..., r$).

- SU(2): Rank 1, one Cartan generator $J_z$
- SU(3): Rank 2, two Cartan generators $I_3$ (isospin) and $Y$ (hypercharge)

**Weights**

In a representation, the **weight vectors** are the eigenvalues of the Cartan generators:
$$H_i |\Lambda\rangle = \Lambda_i |\Lambda\rangle$$

The collection $(\Lambda_1, ..., \Lambda_r)$ is the weight.

**Example for SU(2):**
- States $|j, m\rangle$ have weight $m$ (eigenvalue of $J_z$)
- For $j = 1/2$: weights are $\pm 1/2$
- For $j = 1$: weights are $-1, 0, +1$

**Roots**

**Root vectors** are the weights of the **adjoint representation** (the representation where the Lie algebra acts on itself).

For SU(2):
- The adjoint representation has dimension 3 (generators $J_+, J_-, J_z$)
- Root vectors: $\pm 1$ (from $[J_z, J_\pm] = \pm J_\pm$)

For SU(3):
- The adjoint representation is the octet (dimension 8)
- Roots form a hexagon in the weight space
- Simple roots: $\vec{\alpha}_1 = (1, 0)$ and $\vec{\alpha}_2 = (-1/2, \sqrt{3}/2)$

**Physical Interpretation:**
- Roots represent the "building blocks" of symmetry transformations
- Weights label states within representations
- The highest weight uniquely identifies an irreducible representation

### 5.5 Atomic Physics: LS and jj Coupling

**Term Symbols**

In atomic physics, electron configurations are described by **term symbols**:
$$^{2S+1}L_J$$

where:
- $S$ = total spin angular momentum
- $L$ = total orbital angular momentum (S=0, P=1, D=2, F=3, ...)
- $J$ = total angular momentum ($|L-S| \leq J \leq L+S$)
- $2S+1$ = spin multiplicity (singlet, doublet, triplet, ...)

**Example:** The ground state of carbon ($1s^2 2s^2 2p^2$) has terms including $^3P_0$, $^3P_1$, $^3P_2$, $^1D_2$, $^1S_0$.

**LS Coupling (Russell-Saunders Coupling)**

For light atoms, spin-orbit coupling is weak:
1. Couple orbital angular momenta: $\mathbf{L} = \sum_i \mathbf{l}_i$
2. Couple spins: $\mathbf{S} = \sum_i \mathbf{s}_i$
3. Couple $L$ and $S$ to get total $J$: $\mathbf{J} = \mathbf{L} + \mathbf{S}$

Selection rules for electric dipole transitions:
- $\Delta L = 0, \pm 1$ (but $L=0 \to L=0$ forbidden)
- $\Delta S = 0$ (spin doesn't change in electric dipole)
- $\Delta J = 0, \pm 1$ (but $J=0 \to J=0$ forbidden)

**jj Coupling**

For heavy atoms, spin-orbit coupling is strong:
1. Each electron couples its own $l$ and $s$: $\mathbf{j}_i = \mathbf{l}_i + \mathbf{s}_i$
2. Couple individual $j_i$ to get total $J$: $\mathbf{J} = \sum_i \mathbf{j}_i$

This scheme is used for heavy elements (large $Z$) where relativistic effects are important.

**Hund's Rules**

For determining the ground state term:
1. Maximum $S$ (maximize parallel spins)
2. For given $S$, maximum $L$
3. For less than half-filled subshell: minimum $J$; for more than half-filled: maximum $J$

**Example: Nitrogen ($2p^3$)**
- Three electrons in $p$ orbitals ($l=1, s=1/2$)
- By rule 1: Maximum $S = 3/2$ (all spins parallel)
- By rule 2: For $S=3/2$, the spatial wavefunction must be antisymmetric, giving $L=0$
- By rule 3: Half-filled ($p^3$), so minimum $J = |L-S| = 3/2$
- Ground term: $^4S_{3/2}$

### 5.6 Isospin and SU(2) Flavor Symmetry

**Nucleon Isospin**

Proton and neutron are nearly identical in their strong interactions—they form an isospin doublet:
$$|I=1/2, I_3=+1/2\rangle = |p\rangle$$
$$|I=1/2, I_3=-1/2\rangle = |n\rangle$$

Isospin is mathematically identical to spin, with operators $I_1, I_2, I_3$ satisfying:
$$[I_i, I_j] = i\varepsilon_{ijk}I_k$$

**Pions**

The three pions form an isospin triplet:
$$|I=1, I_3=+1\rangle = |\pi^+\rangle$$
$$|I=1, I_3=0\rangle = |\pi^0\rangle$$
$$|I=1, I_3=-1\rangle = |\pi^-\rangle$$

**Isospin in Reactions**

Strong interactions conserve isospin. Example:
$$p + p \to d + \pi^+$$

Initial state: Two protons in $I=1$ state (antisymmetric space, symmetric isospin)
Final state: Deuteron ($I=0$) + $\pi^+$ ($I=1, I_3=+1$)

Isospin analysis helps predict reaction cross sections and branching ratios.

**Gell-Mann–Nishijima Formula**

For hadrons:
$$Q = I_3 + \frac{B+S}{2}$$

where $Q$ = charge, $I_3$ = isospin projection, $B$ = baryon number, $S$ = strangeness.

This formula, extended to SU(3), led to the prediction of the $\Omega^-$ baryon.

### 5.7 Orbital Symmetries and Atomic Structure

**Central Field Approximation**

In multi-electron atoms, each electron moves in an effective central potential $V(r)$ created by the nucleus and other electrons. This preserves orbital angular momentum:
$$[H, L^2] = 0, \quad [H, L_z] = 0$$

**Electron Configuration Notation**

Electrons are labeled by $(n, l)$ with $l = 0, 1, 2, ...$ designated as $s, p, d, f, g, ...$

- $n$ = principal quantum number (shell)
- $l$ = orbital angular momentum
- Maximum $2(2l+1)$ electrons per subshell (Pauli principle)

**Filling Order:**
$$1s \to 2s \to 2p \to 3s \to 3p \to 4s \to 3d \to 4p \to ...$$

**Periodic Table Structure**

- **s-block:** Groups 1-2 ($ns^1$ or $ns^2$)
- **p-block:** Groups 13-18 ($ns^2 np^{1-6}$)
- **d-block:** Transition metals ($(n-1)d^{1-10} ns^{0-2}$)
- **f-block:** Lanthanides/Actinides ($(n-2)f$)

**Symmetry and Selection Rules**

Electric dipole transitions require:
- $\Delta l = \pm 1$ (parity change)
- $\Delta m = 0, \pm 1$

These rules arise from the properties of spherical harmonics under rotations.

### 5.8 Rotation Groups SO(3) and SU(2)

Angular momentum operators generate rotations in quantum mechanics. The commutation relations $[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k$ define the Lie algebra of the rotation group.

**SO(3) - The 3D Rotation Group**

SO(3) is the group of proper rotations in three-dimensional space. Each rotation can be parameterized by:
- An axis $\mathbf{n}$ (unit vector)
- An angle $\theta$

The rotation operator is:
$$R(\mathbf{n}, \theta) = e^{-i\theta \mathbf{n} \cdot \mathbf{J}/\hbar}$$

**Generators of Rotations: The Infinitesimal Point of View**

The angular momentum operators $\mathbf{J}$ are the **generators** of rotations. To understand what this means, we need to examine how rotations behave for infinitesimal angles.

**The Key Idea: Lie Group and Lie Algebra**

Rotations form a **Lie group** (specifically, the group SO(3) or SU(2)). A fundamental theorem in group theory states that the local structure of a Lie group near the identity is completely determined by its **Lie algebra**—the tangent space at the identity element.

The generators are the basis elements of this Lie algebra. They encode "the direction in which you can move" within the group, starting from the identity.

**Infinitesimal Rotations:**

For a rotation by a small angle $\delta\theta$ about axis $\mathbf{n}$:
$$R(\mathbf{n}, \delta\theta) \approx I - i\delta\theta \left(\frac{\mathbf{n} \cdot \mathbf{J}}{\hbar}\right)$$

or equivalently:
$$R(\mathbf{n}, \delta\theta) \approx I - \frac{i}{\hbar}\delta\theta (\mathbf{n} \cdot \mathbf{J})$$

Here, $\mathbf{n} \cdot \mathbf{J}$ is the generator associated with rotations about axis $\mathbf{n}$. The factor $i/\hbar$ is a conventional normalization choice in quantum mechanics.

**Why This Form?**

Rotation operators must be **unitary** (to preserve quantum state normalization) and form a **group** (composition of rotations gives another rotation). The exponential form ensures both:
$$R(\mathbf{n}, \theta) = e^{-i\theta (\mathbf{n} \cdot \mathbf{J})/\hbar}$$

**Extracting the Generator:**

Given the rotation operator $R_z(\theta) = e^{-i\theta J_z/\hbar}$, how do we "find" $J_z$? We differentiate at the identity ($\theta = 0$):

$$J_z = i\hbar \frac{d R_z(\theta)}{d \theta}\bigg|_{\theta=0}$$

This is a derivative with respect to the **group parameter** $\theta$, evaluated at the identity element of the group. It extracts the "tangent vector" to the group manifold at the identity—this is precisely the Lie algebra element (generator).

**Physical Interpretation:**

- $R_z(\theta)$ describes "where you end up" after rotating by angle $\theta$
- $J_z$ describes "which direction you're initially moving" as you start to rotate
- Just as velocity is the derivative of position with respect to time, $J_z$ is the derivative of the rotation operator with respect to the rotation angle

**Analogy with Momentum:**

This is directly analogous to how momentum generates spatial translations:
$$T(a) = e^{-iap_x/\hbar}, \quad p_x = i\hbar \frac{dT(a)}{da}\bigg|_{a=0}$$

Just as $p_x$ generates translations in $x$, the angular momentum components $J_i$ generate rotations about their respective axes. Both are generators of symmetry transformations—momentum for translations, angular momentum for rotations.

**Why the Commutation Relations?**

The commutation relations $[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k$ reflect the structure of the rotation group. If we perform two infinitesimal rotations in different orders, the difference is a third rotation:
- Rotate by $\delta\alpha$ about $x$, then by $\delta\beta$ about $y$
- vs. rotate by $\delta\beta$ about $y$, then by $\delta\alpha$ about $x$

The difference is a rotation by $\delta\alpha\delta\beta$ about $z$. This geometric fact translates directly into the algebraic commutation relations.

**Lie Algebra Structure:**

The generators $\{J_i\}$ form a **Lie algebra**—a vector space with a bilinear operation (the commutator) satisfying:
1. Antisymmetry: $[J_i, J_j] = -[J_j, J_i]$
2. Jacobi identity: $[J_i, [J_j, J_k]] + [J_j, [J_k, J_i]] + [J_k, [J_i, J_j]] = 0$

The commutation relations define the structure constants ($\varepsilon_{ijk}$ for angular momentum), which completely characterize the local structure of the rotation group.

**SU(2) - The Special Unitary Group**

SU(2) is the group of $2 \times 2$ unitary matrices with determinant 1. It is the double cover of SO(3):
- Every SO(3) rotation corresponds to two SU(2) elements ($\pm U$)
- For integer $j$, the representations correspond to SO(3)
- For half-integer $j$, the representations correspond to SU(2)

**The Double Cover: SU(2) vs SO(3)**

The relationship $\text{SU(2)}/\mathbb{Z}_2 \cong \text{SO(3)}$ means that SU(2) "covers" SO(3) twice. This is a subtle but crucial point:

**The Physical Picture:**
- SO(3) describes rotations in 3D space. A rotation by $2\pi$ (360°) returns to the identity.
- SU(2) describes how spinors transform. A rotation by $2\pi$ gives a *minus sign*: $|\psi\rangle \to -|\psi\rangle$. You need a rotation by $4\pi$ (720°) to return to the original state!

**Why This Happens:**

Consider a rotation by angle $\theta$ about the $z$-axis:
- In SO(3): $R_z(2\pi) = I$ (identity)
- In SU(2): $U_z(2\pi) = -I$ (minus identity)

The SU(2) matrix $U$ and $-U$ correspond to the *same* SO(3) rotation. This is the "double cover": each SO(3) rotation has two SU(2) representatives.

**Physical Manifestation:**

This isn't just mathematics—it has physical consequences:
- **Fermions** (spin-1/2, 3/2, ...) pick up a minus sign under $2\pi$ rotation. This is why they obey Fermi-Dirac statistics and the Pauli exclusion principle.
- **Bosons** (spin-0, 1, 2, ...) return to their original state after $2\pi$ rotation.

**The Neutron Interference Experiment:**
In 1975, Werner et al. demonstrated this by splitting a neutron beam, rotating one path by $2\pi$ using a magnetic field, and recombining the beams. The observed interference pattern confirmed the sign change—neutrons (spin-1/2) truly need a $4\pi$ rotation to return to their original state.

**Relationship:**
$$\text{SU(2)}/\mathbb{Z}_2 \cong \text{SO(3)}$$

The quotient by $\mathbb{Z}_2$ means we identify $U \sim -U$ in SU(2), giving us SO(3). For integer spin representations, $U$ and $-U$ act identically (since $e^{-im\theta}$ with $m$ integer is unchanged by $\theta \to \theta + 2\pi$), so these representations are "faithful" representations of SO(3). For half-integer spins, they are representations of SU(2) but not of SO(3).

### 5.2 Irreducible Representations and the Meaning of "Representation"

**What is a "Representation"?**

The term "representation" in group theory can be confusing. Intuitively, a representation is a concrete realization of abstract group elements as matrices acting on a vector space. For the rotation group, instead of thinking about abstract rotations, we represent each rotation as a matrix that transforms quantum states.

**Crucial Distinction: The Representation Space vs. the Choice of Basis**

For a fixed angular momentum $j$, the **representation space** is the $(2j+1)$-dimensional Hilbert space spanned by the states $\{|j, m\rangle\}$ where $m = -j, -j+1, \ldots, j$. This space is **unique** for a given $j$—it is not something we choose for convenience, but a property determined by the algebraic structure.

However, **within this fixed space**, we can choose different bases:
- The standard basis $\{|j, m\rangle\}$ (eigenstates of $J_z$)
- The eigenstates of $J_x$ or $J_y$
- Any rotated basis

These different bases are related by unitary transformations *within* the same representation space. The representation is like a vector space with a specific dimension; the basis is like choosing coordinate axes within that space.

**Why Fixed $j$ Corresponds to a Fixed Representation:**

When we fix $j$, we are selecting a specific irreducible representation $D^{(j)}$. All states with this $j$ transform into each other under rotations, but they never mix with states of different $j$. The different $m$ values are not different representations—they are different *states within the same representation*.

Think of it this way:
- **Representation** = the "species" of angular momentum (spin-0, spin-1/2, spin-1, etc.)
- **States $|j, m\rangle$** = the "members" of that species with different orientations

**Singlet, Doublet, Triplet, Quartet: What do these "-let" terms mean?**

The suffix "-let" indicates a multiplet—a collection of states that are related by symmetry operations. The prefix indicates the number of states:

| Term | $j$ | Number of States $(2j+1)$ | Meaning |
|:----:|:---:|:------------------------:|:--------|
| **Singlet** | 0 | 1 | Single state (no orientation degree of freedom) |
| **Doublet** | 1/2 | 2 | Two states (spin up/down) |
| **Triplet** | 1 | 3 | Three states ($m = -1, 0, +1$) |
| **Quartet** | 3/2 | 4 | Four states ($m = -3/2, -1/2, +1/2, +3/2$) |

These terms originated in atomic spectroscopy:
- A "singlet" state has $S = 0$ (total spin zero)
- A "doublet" has $S = 1/2$ (like a single electron)
- A "triplet" has $S = 1$ (like two parallel spins)

**Important:** A particle with spin-$1/2$ *is* a doublet; the two states $|\uparrow\rangle$ and $|\downarrow\rangle$ are not two different representations, but two basis states within the same spin-1/2 representation.

**Dimension of Representation:**
$$d_j = 2j + 1$$

This is the number of linearly independent states in the representation, equal to the number of possible $m$ values.

**Character of Rotation: What Is It and Why Do We Care?**

The **character** $\chi_j(\theta)$ is defined as the **trace** (sum of diagonal elements) of the representation matrix for a rotation by angle $\theta$:

$$\chi_j(\theta) = \text{Tr}[D^{(j)}(R(\theta))] = \sum_{m=-j}^{j} \langle j,m|D^{(j)}(R(\theta))|j,m\rangle$$

**Key Property: Characters are Class Functions**

In group theory, rotations by the same angle about different axes are called **conjugate elements** (they belong to the same "conjugacy class"). A fundamental theorem states that the trace of a matrix is invariant under similarity transformations:

$$\text{Tr}[U^{-1}AU] = \text{Tr}[A]$$

This means the character depends **only on the rotation angle** $\theta$, not on the specific axis of rotation. This is a huge simplification—it means we can characterize representations without worrying about the infinite number of possible rotation axes!

**Explicit Formula:**

$$\chi_j(\theta) = \sum_{m=-j}^{j} e^{-im\theta} = \frac{\sin[(j+1/2)\theta]}{\sin(\theta/2)}$$

The first form comes from summing the diagonal matrix elements $D^{(j)}_{mm}(\theta) = e^{-im\theta}$ (for rotations about the $z$-axis). The second form is a closed-form expression obtained by summing the geometric series.

**Example:** For spin-1/2 ($j = 1/2$):
$$\chi_{1/2}(\theta) = e^{-i\theta/2} + e^{i\theta/2} = 2\cos(\theta/2)$$

**Orthogonality Relation: The "Fingerprint" of Representations**

The orthogonality relation:
$$\int_0^{2\pi} \chi_{j_1}(\theta) \chi_{j_2}(\theta) \sin^2\frac{\theta}{2} d\theta = \pi \delta_{j_1 j_2}$$

is a powerful tool in representation theory. Here's what it means:

1. **Different representations are orthogonal:** If $j_1 \neq j_2$, the integral is zero. This mathematically proves that different $j$ values correspond to genuinely different, independent representations.

2. **Characters form an orthogonal basis:** The characters $\chi_j(\theta)$ can be viewed as functions of $\theta$. This relation says these functions are orthogonal with respect to the measure $\sin^2(\theta/2)d\theta$.

**Physical Interpretation:**

Think of the character as a "fingerprint" of the representation. Just as different people have different fingerprints, different representations have different character functions. The orthogonality relation is like saying "no two fingerprints match"—each representation is uniquely identified by its character.

**Application: Decomposing Tensor Products**

One major use of characters is to decompose tensor products. When we combine two angular momenta:
$$D^{(j_1)} \otimes D^{(j_2)} = \bigoplus_j n_j D^{(j)}$$

The multiplicities $n_j$ (how many times each $j$ appears) can be computed using characters:
$$n_j = \int d\theta \, \chi_{j_1}(\theta)\chi_{j_2}(\theta)\chi_j^*(\theta) \times (\text{measure factor})$$

This is much easier than working with the full matrix representations!

**Summary: Understanding "Representation" in Context**

To solidify the concept of representation, here's a comprehensive summary:

**What a Representation IS:**
- A concrete matrix realization of an abstract group
- A vector space with a specific dimension $(2j+1)$ where group elements act as linear operators
- The set of transformation rules for a physical quantity under symmetry operations

**What a Representation is NOT:**
- Not a choice of basis (bases are choices *within* a representation)
- Not a specific state (states are vectors *in* the representation space)
- Not optional—it is determined by the algebraic structure

**Physical Analogies:**

| Concept | Analogy | Meaning |
|:--------|:--------|:--------|
| **Representation** | The "species" of particle | Spin-0, spin-1/2, spin-1, etc. |
| **Representation Space** | The "arena" where states live | All possible orientations of that spin |
| **Basis States $\|j,m\rangle$** | Specific "stances" or "poses" | Pointing up, down, or in superposition |
| **Rotation Operator** | The "machinery" of transformation | How states change when you rotate the system |

**Why This Matters:**

When we say "the spin-1 representation," we are referring to the **three-dimensional vector space** of all possible spin-1 states. The three states $|1,1\rangle$, $|1,0\rangle$, $|1,-1\rangle$ are not three different representations—they are three orthogonal directions in the *same* representation space. Just as $\hat{x}$, $\hat{y}$, $\hat{z}$ are three basis vectors in 3D space, these $|j,m\rangle$ states are basis vectors in the spin-1 representation space.

### 5.3 Young Tableaux for Permutation Symmetry

**Where Do Young Diagrams Come From?**

Young diagrams originated in the representation theory of the **symmetric group** $S_n$ (the group of all permutations of $n$ objects). When we have $n$ identical particles, exchanging them corresponds to the action of $S_n$. The wavefunction's symmetry properties under particle exchange are classified by the irreducible representations of $S_n$.

**Key Insight:** For spin-1/2 particles, the total spin states (singlet, triplet, etc.) are intimately connected to the permutation symmetry of the spin wavefunction. Young diagrams provide a visual way to classify these symmetry types.

**The Connection to Angular Momentum:**

For $n$ spin-1/2 particles:
- The total spin $S$ determines the permutation symmetry of the spin state
- Young diagrams with $n$ boxes classify the irreducible representations of $S_n$
- Each diagram corresponds to a specific total spin $S$ and degeneracy $(2S+1)$

**Basic Rules for Constructing Young Diagrams:**

1. **Each box represents one particle** — $n$ boxes for $n$ particles
2. **Rows represent symmetric combinations** — particles in the same row are symmetrized
3. **Columns represent antisymmetric combinations** — particles in the same column are antisymmetrized
4. **Diagrams are left-justified** — rows cannot be longer than the row above

**Partitions and Young Diagrams:**

A partition of $n$ is a way of writing $n$ as a sum of positive integers: $n = \lambda_1 + \lambda_2 + ...$ where $\lambda_1 \geq \lambda_2 \geq ...$. Each partition corresponds to a unique Young diagram with row lengths $\lambda_i$.

**Examples:**

<img src="/images/angular-momentum/young_partition_examples.png" width="700px" alt="Young diagram examples for various partitions">

*Young diagrams for different partitions. Top row: 3-particle partitions. Bottom row: 4-particle partitions. The shape determines the symmetry type: horizontal rows give symmetric combinations, vertical columns give antisymmetric combinations.*

**Young Diagrams for Two Particles:**

<img src="/images/angular-momentum/two_particle_young_new.png" width="350px" alt="Young Diagrams for Two Particles">

*Left: Symmetric representation (partition (2), triplet $S=1$, dimension 3). Right: Antisymmetric representation (partition (1,1), singlet $S=0$, dimension 1)*

**Young Diagrams for Three Particles:**

<img src="/images/angular-momentum/young_3_all_combined.png" width="600px" alt="Young Diagrams for Three Particles">

*Left: Totally symmetric (quartet, $S=3/2$, dim=4). Center: Mixed symmetry (doublet, $S=1/2$, dim=2). Right: Totally antisymmetric (not for spin-1/2)*

### 5.4 Hook Length Formula

The dimension of a representation corresponding to a Young diagram with $n$ boxes is given by the hook length formula:

$$d = \frac{n!}{\prod_{\text{boxes}} h_i}$$

**Understanding the Hook Length $h_i$:**

For each box in the Young diagram, draw a "hook"—a line going right along the row and down along the column. The hook length $h_i$ counts:
- The box itself (= 1)
- Boxes to the right in the same row
- Boxes below in the same column

$$h_i = 1 + (\text{boxes to right}) + (\text{boxes below})$$

**Visual Example: Hook Lengths for Partition (2,1)**

<img src="/images/angular-momentum/young_21_hook_lengths.png" width="350px" alt="Young diagram (2,1) with hook lengths labeled">

*The partition (2,1) with hook lengths labeled in each box. The dimension is calculated as $d = 3!/(3 \cdot 1 \cdot 1) = 2$.*

**How to calculate each hook length:**

For each box, draw a "hook" line going right along the row and down along the column. Count:
- The box itself (= 1)
- Boxes to the right in the same row
- Boxes below in the same column

**Box positions and hook lengths:**
- **Top-left box (labeled 3):** 1 (self) + 1 (right) + 1 (below) = **3**
- **Top-right box (labeled 1):** 1 (self) + 0 (right) + 0 (below) = **1**
- **Bottom-left box (labeled 1):** 1 (self) + 0 (right) + 0 (below) = **1**

**The +1 is essential**—it accounts for the box itself (the box at the "elbow" of the hook). Without this +1, the formula would give incorrect dimensions.

**Dimension Calculation:**
$$d = \frac{3!}{3 \cdot 1 \cdot 1} = 2$$

This matches our knowledge that the mixed symmetry representation for three spin-1/2 particles has dimension 2 (two doublet states).

**Hook Length Calculation Example: Three Spin-1/2 Particles**

For three spin-1/2 particles, the Young diagrams and their properties are:

<img src="/images/angular-momentum/young_3_symmetric.png" width="200px" alt="Symmetric diagram (3)">

*Symmetric diagram (3): Hook lengths are 3, 2, 1. Dimension: $\frac{3!}{3 \cdot 2 \cdot 1} = 1$ (for each $m$ value, total $2S+1 = 4$)*

<img src="/images/angular-momentum/young_21_mixed.png" width="180px" alt="Mixed symmetry diagram (2,1)">

*Mixed symmetry diagram (2,1): Hook lengths are 3, 1, 1. Dimension: $\frac{3!}{3 \cdot 1 \cdot 1} = 2$ (two doublet states)*

**How to Read a Young Diagram: Step-by-Step Analysis**

**Step 1: Identify the Partition**

Count the number of boxes in each row. The partition is written as $(\lambda_1, \lambda_2, ...)$ where $\lambda_i$ is the number of boxes in row $i$.

- One row of $n$ boxes → partition $(n)$ (totally symmetric)
- $n$ rows of 1 box → partition $(1,1,...,1)$ (totally antisymmetric)
- Intermediate shapes → mixed symmetry

**Step 2: Determine the Symmetry Type**

- **More rows → more antisymmetric**: A tall, thin diagram represents mostly antisymmetric states
- **More columns → more symmetric**: A short, wide diagram represents mostly symmetric states
- **Square-ish → mixed symmetry**: Intermediate shapes represent states with both symmetric and antisymmetric character

**Step 3: Calculate the Dimension (Number of Standard Young Tableaux)**

A **standard Young tableau** is a filling of the boxes with numbers $1, 2, ..., n$ such that:
- Numbers increase left to right along rows
- Numbers increase top to bottom down columns

The number of such fillings equals the dimension of the representation.

**Example: Partition (2,1) for 3 particles**

Possible standard Young tableaux for partition $(2,1)$:

<img src="/images/angular-momentum/young_tableaux_21_example.png" width="280px" alt="Standard Young tableaux for partition (2,1)">

*There are exactly 2 such fillings, so the dimension is 2. This matches our calculation using the hook length formula!*

**Step 4: Connect to Physical States**

For spin-1/2 particles:
1. Count the dimension $d$ using hook lengths
2. The total spin degeneracy is $(2S+1) = d$
3. Solve for $S$: $S = (d-1)/2$

**Complete Analysis Table for Two and Three Spin-1/2 Particles:**

| Particles | Partition | Symmetry | Spin $S$ | Dim $(2S+1)$ | Visual |
|:---------:|:---------:|:--------:|:--------:|:------------:|:------:|
| 2 | $(2)$ | Symmetric | 1 (Triplet) | 3 | <img src="/images/angular-momentum/young_2_pure.png" width="40px"> |
| 2 | $(1,1)$ | Antisymmetric | 0 (Singlet) | 1 | <img src="/images/angular-momentum/young_11_pure.png" width="20px"> |
| 3 | $(3)$ | Totally Symmetric | 3/2 (Quartet) | 4 | <img src="/images/angular-momentum/young_3_pure.png" width="60px"> |
| 3 | $(2,1)$ | Mixed | 1/2 (Doublet) | 2 | <img src="/images/angular-momentum/young_21_pure.png" width="40px"> |
| 3 | $(1,1,1)$ | Totally Antisymmetric | — | 0 (impossible) | <img src="/images/angular-momentum/young_111_pure.png" width="20px"> |

**Key Observations:**

1. **Pauli Exclusion Principle**: For spin-1/2, we cannot have three particles in a totally antisymmetric spin state. This is why the partition $(1,1,1)$ has dimension 0 for spin-1/2 (you'd need at least spin-1 particles).

2. **Spin-Statistics Connection**: The symmetry of the spin wavefunction determines the symmetry required of the spatial wavefunction:
   - Symmetric spin (triplet, $S=1$) → Antisymmetric spatial
   - Antisymmetric spin (singlet, $S=0$) → Symmetric spatial

3. **Maximum Spin**: The totally symmetric diagram always corresponds to the maximum possible spin ($S = n/2$ for $n$ spin-1/2 particles).

### 5.5 Connection to Angular Momentum Addition

The CG decomposition derived in Part IV has an elegant group-theoretic interpretation. When adding angular momenta $\mathbf{J} = \mathbf{J}_1 + \mathbf{J}_2$, the tensor product of representations decomposes into irreducible representations according to:

$$D^{(j_1)} \otimes D^{(j_2)} = \bigoplus_{j=|j_1-j_2|}^{j_1+j_2} D^{(j)}$$

This is precisely the **Clebsch-Gordan series**. The triangle rule $|j_1 - j_2| \leq j \leq j_1 + j_2$ reflects which irreducible representations appear in the decomposition. The dimension check $(2j_1+1)(2j_2+1) = \sum_{j}(2j+1)$ confirms that the total number of states is conserved in the decomposition.

**Physical Interpretation:** The coupled basis states $|j, m\rangle$ transform as the irreducible representation $D^{(j)}$ under rotations, while the uncoupled basis $|j_1, m_1; j_2, m_2\rangle$ transforms as the tensor product $D^{(j_1)} \otimes D^{(j_2)}$. The CG coefficients are the unitary transformation matrix elements between these two bases.

---

## Part VI: Central Force Field Problems

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

| $l$ | $m$ | $Y_l^m(\theta, \phi)$ | Name |
|:---:|:---:|:---------------------:|:----:|
| 0 | 0 | $\sqrt{\frac{1}{4\pi}}$ | s-wave |
| 1 | 0 | $\sqrt{\frac{3}{4\pi}}\cos\theta$ | p$_z$ |
| 1 | $\pm 1$ | $\mp\sqrt{\frac{3}{8\pi}}\sin\theta e^{\pm i\phi}$ | p$_{\pm}$ |
| 2 | 0 | $\sqrt{\frac{5}{16\pi}}(3\cos^2\theta - 1)$ | d$_{z^2}$ |

**Physical Interpretation:**

- **$|Y_l^m|^2$** gives the angular probability distribution
- **$l = 0$ (s-wave):** Spherically symmetric
- **$l = 1$ (p-wave):** Has nodal planes (dumbbell shape)
- **$l = 2$ (d-wave):** More complex angular structure

The magnetic quantum number $m$ determines the orientation:
- For $m = 0$: Maximum amplitude along $z$-axis
- For $m = \pm l$: Maximum amplitude in $xy$-plane (toroidal shape for large $l$)

### 6.3 Measurement Probabilities for $L_x$ in $Y_{20}$ State

As an application of spherical harmonics and angular momentum algebra, consider a particle in the $Y_{20}$ eigenstate. While this state is an eigenstate of $L_z$ with $m = 0$, it is **not** an eigenstate of $L_x$. We can determine the possible measured values of $L_x$ and their corresponding probabilities.

**Rotation Method**

To find $L_x$ eigenstates, we can use coordinate rotation. The spherical harmonics transform under rotation according to the representation $D^{(l)}$.

**Explicit Forms of $Y_{2m}$:**

$$Y_{2,\pm 2} = \frac{1}{2}\sqrt{\frac{15}{8\pi}}\frac{(x \pm iy)^2}{r^2}$$

$$Y_{2,\pm 1} = \mp\sqrt{\frac{15}{8\pi}}\frac{(x \pm iy)z}{r^2}$$

$$Y_{2,0} = \sqrt{\frac{5}{16\pi}}\frac{2z^2 - x^2 - y^2}{r^2}$$

**Eigenstates of $L_x$ (denoted $Y_{2m}^x$):**

By cyclic permutation $x \to y$, $y \to z$, $z \to x$:

$$Y_{2,0}^x = -\frac{1}{2}Y_{2,0} + \frac{\sqrt{3}}{2\sqrt{2}}(Y_{2,-2} + Y_{2,2})$$

**Expanding $Y_{2,0}$ in $L_x$ Eigenstates:**

Inverting the above relation:

$$Y_{2,0} = -\frac{1}{2}Y_{2,0}^x - \frac{\sqrt{3}}{2\sqrt{2}}(Y_{2,-2}^x + Y_{2,2}^x)$$

**Measurement Probabilities:**

When measuring $L_x$ in the $Y_{20}$ state, the possible values and their probabilities are:

| $L_x$ Value | Probability |
|-------------|-------------|
| $0$ | $\frac{1}{4}$ |
| $\pm\hbar$ | $0$ |
| $\pm 2\hbar$ | $\frac{3}{8}$ each |

**Alternative Method using Expectation Values**

The probabilities can also be found by solving the system:

1. Normalization: $P_0 + 2P_1 + 2P_2 = 1$
2. $\langle L_x^2 \rangle = 2\hbar^2$: $2P_1 \cdot \hbar^2 + 2P_2 \cdot 4\hbar^2 = 2\hbar^2$
3. $\langle L_x^4 \rangle = 12\hbar^4$: $2P_1 \cdot \hbar^4 + 2P_2 \cdot 16\hbar^4 = 12\hbar^4$

Solving yields: $P_0 = \frac{1}{4}$, $P_1 = 0$, $P_2 = \frac{3}{8}$.

This example illustrates how eigenstates of one angular momentum component ($L_z$) can be expressed as superpositions of eigenstates of another component ($L_x$).

### 6.4 Angular Momentum in Central Force Fields: Key Theorems

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

**Theorem 2: Radial wavefunction behavior near origin**

For a particle with angular momentum $l$ in a central potential, the radial wavefunction behaves as:

$$R_{nl}(r) \xrightarrow{r \to 0} r^l$$

**Physical Interpretation:**

The centrifugal barrier $\frac{\hbar^2 l(l+1)}{2\mu r^2}$ prevents particles with $l \geq 1$ from reaching the origin. Only s-waves ($l = 0$) have non-zero probability density at $r = 0$.

### 6.5 Radial Equation and Angular Momentum Barrier

Substituting into the Schrödinger equation:

$$\left[-\frac{\hbar^2}{2\mu}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{d}{dr}\right) + \frac{\hbar^2 l(l+1)}{2\mu r^2} + V(r)\right]R_{nl}(r) = E R_{nl}(r)$$

Define $u_{nl}(r) = r R_{nl}(r)$:

$$\left[-\frac{\hbar^2}{2\mu}\frac{d^2}{dr^2} + V_{\text{eff}}(r)\right]u_{nl}(r) = E u_{nl}(r)$$

with the effective potential:

$$\boxed{V_{\text{eff}}(r) = V(r) + \frac{\hbar^2 l(l+1)}{2\mu r^2}}$$

The second term is the **centrifugal barrier** arising from angular momentum. This term effectively prevents the particle from reaching the origin when $l \neq 0$.

**Physical Interpretation of the Centrifugal Barrier**

The radial equation describes one-dimensional motion in the effective potential. The centrifugal term $\frac{\hbar^2 l(l+1)}{2\mu r^2}$ acts as a repulsive barrier that:
- Diverges as $r \to 0$ for $l \geq 1$
- Pushes the wavefunction away from the origin
- Explains why s-states ($l = 0$) have non-zero probability at $r = 0$ while higher angular momentum states vanish at the origin

For small $r$, the behavior of the radial function is:
$$R_{nl}(r) \xrightarrow{r \to 0} r^l$$

This shows that higher angular momentum states are increasingly suppressed near the origin.

### 6.6 Runge-Lenz Vector and Hydrogen Atom Degeneracy

The hydrogen atom possesses an additional conserved quantity beyond angular momentum—the Runge-Lenz vector.

**Definition of the Runge-Lenz Vector**

$$\mathbf{A} = \frac{1}{2\mu}(\mathbf{p} \times \mathbf{L} - \mathbf{L} \times \mathbf{p}) - \frac{e^2}{4\pi\varepsilon_0}\frac{\mathbf{r}}{r}$$

For the Coulomb potential, this simplifies to:

$$\mathbf{A} = \frac{1}{\mu}\mathbf{p} \times \mathbf{L} - \frac{e^2}{4\pi\varepsilon_0}\frac{\mathbf{r}}{r}$$

**Conservation of the Runge-Lenz Vector**

$$[H, \mathbf{A}] = 0$$

This conservation law is responsible for the "accidental" degeneracy of hydrogen energy levels—all states with the same principal quantum number $n$ but different $l$ have the same energy.

**Connection to Angular Momentum**

The Runge-Lenz vector satisfies:
$$\mathbf{A} \cdot \mathbf{L} = \mathbf{L} \cdot \mathbf{A} = 0$$

$$\mathbf{A}^2 = \left(\frac{e^2}{4\pi\varepsilon_0}\right)^2 + \frac{2H}{\mu}(L^2 + \hbar^2)$$

These relations, combined with the angular momentum algebra, form an SO(4) symmetry group that explains the $n^2$ degeneracy of hydrogen levels.

**Physical Significance**

The existence of the Runge-Lenz vector as a conserved quantity is special to the $1/r$ potential (Coulomb and gravitational). It implies closed elliptical orbits in classical mechanics and the degeneracy in quantum mechanics.

### 6.7 Hydrogen Atom Energy Levels and Angular Momentum

For the Coulomb potential $V(r) = -\frac{e^2}{4\pi\varepsilon_0 r}$:

The energy eigenvalues are:

$$\boxed{E_n = -\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2} = -\frac{13.6 \text{ eV}}{n^2}}$$

where $n = 1, 2, 3, ...$ is the principal quantum number.

For each $n$, the allowed values of $l$ are $l = 0, 1, 2, ..., n-1$.

For each $l$, there are $2l+1$ values of $m$.

The total degeneracy of level $n$ is:
$$g_n = \sum_{l=0}^{n-1}(2l+1) = n^2$$

### 6.8 Three-Dimensional Isotropic Harmonic Oscillator

For $V(r) = \frac{1}{2}\mu\omega^2 r^2$:

The energy eigenvalues are:

$$\boxed{E_N = \left(N + \frac{3}{2}\right)\hbar\omega}$$

where $N = 2n_r + l = 0, 1, 2, ...$ with $n_r = 0, 1, 2, ...$ being the radial quantum number.

For a given $N$, the allowed values of $l$ are $l = N, N-2, N-4, ..., 1$ or $0$.

The degeneracy of level $N$ is:
$$g_N = \frac{(N+1)(N+2)}{2}$$

---

## Part VII: Systems of Identical Particles and Young Tableaux Applications

The quantum mechanics of identical particles imposes fundamental symmetry constraints on many-body wavefunctions. For fermions (half-integer spin), the total wavefunction must be antisymmetric under particle exchange, while for bosons (integer spin), it must be symmetric. These requirements deeply affect how angular momenta combine in multi-particle systems. This part applies the Young tableaux formalism from Part V to classify symmetry types and derives the connection between total spin and exchange symmetry, with applications to the helium atom and lithium atom.

### 7.1 Symmetry Requirements for Many-Particle States

For a system of $N$ identical particles, the total wavefunction must satisfy specific symmetry properties under particle exchange:

- **Bosons** (integer spin): Wavefunction is **symmetric** under exchange of any two particles
- **Fermions** (half-integer spin): Wavefunction is **antisymmetric** under exchange of any two particles

### 7.2 Two-Particle Systems

For two identical particles with single-particle states $|\alpha\rangle$ and $|\beta\rangle$:

**Symmetric State (Bosons):**
$$|\psi_S\rangle = \frac{1}{\sqrt{2}}(|\alpha\rangle_1|\beta\rangle_2 + |\beta\rangle_1|\alpha\rangle_2)$$

**Antisymmetric State (Fermions):**
$$|\psi_A\rangle = \frac{1}{\sqrt{2}}(|\alpha\rangle_1|\beta\rangle_2 - |\beta\rangle_1|\alpha\rangle_2)$$

### 7.3 Spin and Spatial Degrees of Freedom

For two spin-1/2 fermions (e.g., electrons), the total wavefunction is:

$$\Psi(1, 2) = \psi_{\text{spatial}}(\mathbf{r}_1, \mathbf{r}_2) \cdot \chi_{\text{spin}}$$

**Spin Singlet (Antisymmetric):**
$$\chi_{00} = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$

The spatial part must be **symmetric**:
$$\psi_S(\mathbf{r}_1, \mathbf{r}_2) = \frac{1}{\sqrt{2}}[\phi_a(\mathbf{r}_1)\phi_b(\mathbf{r}_2) + \phi_b(\mathbf{r}_1)\phi_a(\mathbf{r}_2)]$$

**Spin Triplet (Symmetric):**
$$\chi_{11} = |\uparrow\uparrow\rangle, \quad \chi_{10} = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle), \quad \chi_{1-1} = |\downarrow\downarrow\rangle$$

The spatial part must be **antisymmetric**:
$$\psi_A(\mathbf{r}_1, \mathbf{r}_2) = \frac{1}{\sqrt{2}}[\phi_a(\mathbf{r}_1)\phi_b(\mathbf{r}_2) - \phi_b(\mathbf{r}_1)\phi_a(\mathbf{r}_2)]$$

### 7.4 Total Angular Momentum of Two-Particle Systems

For two identical particles each with angular momentum $j$, the total angular momentum $J$ can range from $0$ (or $1$ if $j$ is half-integer) to $2j$.

**Symmetry of Coupled States:**

Under particle exchange $P_{12}$:

$$P_{12}|J, M\rangle = (-1)^{2j-J}|J, M\rangle$$

**Proof:**

The exchange of two identical particles is equivalent to a rotation by $\pi$ about the y-axis (or any axis perpendicular to the quantization axis). Under this rotation:

$$P_{12}|j_1, m_1; j_2, m_2\rangle = (-1)^{j_1+j_2-J}|j_2, m_2; j_1, m_1\rangle$$

For identical particles ($j_1 = j_2 = j$), the symmetry of the state $|J, M\rangle$ under exchange is $(-1)^{2j-J}$.

**Important Results:**

- For two spin-1/2 particles ($j = 1/2$):
  - $J = 1$ (triplet): $(-1)^{1-1} = +1$ (symmetric)
  - $J = 0$ (singlet): $(-1)^{1-0} = -1$ (antisymmetric)

- For two spin-1 particles ($j = 1$):
  - $J = 2, 0$: symmetric
  - $J = 1$: antisymmetric

**Connection to Statistics:**
- Fermions (half-integer spin): Total wavefunction must be antisymmetric
  - If $2j$ is odd, symmetric spin requires antisymmetric spatial, and vice versa
- Bosons (integer spin): Total wavefunction must be symmetric
  - If $2j$ is even, symmetric spin requires symmetric spatial, and vice versa

### 7.5 Exchange Interaction and Helium Atom

**Exchange Interaction: Theoretical Foundation**

For two identical particles, the exchange operator $P_{12}$ can be expressed in terms of spin operators. For spin-1/2 particles:

$$P_{12}^{\text{spin}} = \frac{1}{2}(1 + \boldsymbol{\sigma}_1 \cdot \boldsymbol{\sigma}_2)$$

Using the identity $\boldsymbol{\sigma}_1 \cdot \boldsymbol{\sigma}_2 = 2\mathbf{S}_1 \cdot \mathbf{S}_2/(\hbar^2/4) - 3$ for spin-1/2:

$$\mathbf{S}_1 \cdot \mathbf{S}_2 = \frac{\hbar^2}{2}\left(\boldsymbol{\sigma}_1 \cdot \boldsymbol{\sigma}_2\right) = \frac{\hbar^2}{2}\left(2P_{12}^{\text{spin}} - 1\right)$$

The eigenvalues of $P_{12}^{\text{spin}}$ are:
- $P_{12}^{\text{spin}} = +1$ for triplet states ($S = 1$)
- $P_{12}^{\text{spin}} = -1$ for singlet states ($S = 0$)

Therefore:
$$\langle \mathbf{S}_1 \cdot \mathbf{S}_2 \rangle = \begin{cases} +\frac{\hbar^2}{4} & \text{(triplet)} \\ -\frac{3\hbar^2}{4} & \text{(singlet)} \end{cases}$$

**Helium Atom: Spatial Wavefunction Symmetry**

For helium, the Hamiltonian is:
$$H = \frac{\mathbf{p}_1^2}{2m} + \frac{\mathbf{p}_2^2}{2m} - \frac{Ze^2}{4\pi\varepsilon_0 r_1} - \frac{Ze^2}{4\pi\varepsilon_0 r_2} + \frac{e^2}{4\pi\varepsilon_0 |\mathbf{r}_1 - \mathbf{r}_2|}$$

The total wavefunction must be antisymmetric under particle exchange:
$$\Psi(1, 2) = \psi_{\text{spatial}}(\mathbf{r}_1, \mathbf{r}_2) \cdot \chi_{\text{spin}}$$

**First-Order Perturbation Theory:**

Treating the electron-electron repulsion $V_{12} = \frac{e^2}{4\pi\varepsilon_0 r_{12}}$ as perturbation:

$$E^{(1)} = \langle V_{12} \rangle = \iint |\psi_{\text{spatial}}(\mathbf{r}_1, \mathbf{r}_2)|^2 \frac{e^2}{4\pi\varepsilon_0 |\mathbf{r}_1 - \mathbf{r}_2|} d^3r_1 d^3r_2$$

For the $1s^2$ configuration, using hydrogenic wavefunctions:
$$\psi_{1s}(r) = \frac{1}{\sqrt{\pi a_0^3}}e^{-r/a_0}$$

**Direct Integral (Coulomb):**
$$J = \iint |\psi_{1s}(\mathbf{r}_1)|^2 |\psi_{1s}(\mathbf{r}_2)|^2 \frac{e^2}{4\pi\varepsilon_0 r_{12}} d^3r_1 d^3r_2 = \frac{5}{8}\frac{Ze^2}{4\pi\varepsilon_0 a_0}$$

**Exchange Integral:**
$$K = \iint \psi_{1s}^*(\mathbf{r}_1)\psi_{1s}^*(\mathbf{r}_2) \frac{e^2}{4\pi\varepsilon_0 r_{12}} \psi_{1s}(\mathbf{r}_2)\psi_{1s}(\mathbf{r}_1) d^3r_1 d^3r_2$$

For different spatial orbitals (e.g., $1s2s$ configuration), the exchange integral is non-zero and leads to energy splitting.

**Energy Splitting:**

| State | Spin Symmetry | Spatial Symmetry | Energy |
|:-----:|:-------------:|:----------------:|:------:|
| Singlet | Antisymmetric | Symmetric | $E_0 + J + K$ |
| Triplet | Symmetric | Antisymmetric | $E_0 + J - K$ |

where $K > 0$, so the triplet state has lower energy (exchange interaction favors parallel spins).

**Parahelium vs Orthohelium:**

**Parahelium (Singlet, $S = 0$):**
- Spatial wavefunction is symmetric
- Electrons can be close together ($r_{12} \to 0$ is allowed)
- Higher electron-electron repulsion: $\langle V_{12} \rangle = J + K$
- Higher total energy

**Orthohelium (Triplet, $S = 1$):**
- Spatial wavefunction is antisymmetric: $\psi(\mathbf{r}, \mathbf{r}) = 0$
- Electrons avoid each other (Fermi hole)
- Lower electron-electron repulsion: $\langle V_{12} \rangle = J - K$
- Lower total energy

This effective spin-dependent interaction is the **exchange interaction**.

**Angular Momentum Classification ($^{2S+1}L_J$ notation):**

| Configuration | Term Symbol | Spin | Spatial | Energy (eV) |
|:-------------:|:-----------:|:----:|:-------:|:-----------:|
| $1s^2$ | $^1S_0$ | Singlet | Symmetric | -79.0 (ground) |
| $1s2s$ | $^3S_1$ | Triplet | Antisymmetric | -59.0 (excited) |
| $1s2s$ | $^1S_0$ | Singlet | Symmetric | -58.6 (excited) |
| $1s2p$ | $^3P_{0,1,2}$ | Triplet | Antisymmetric | -58.3 (excited) |

**Hund's First Rule:** The term with the maximum multiplicity (maximum $S$) lies lowest in energy. This is a direct consequence of the exchange interaction favoring parallel spins.

**Mathematical Origin:**

The exchange splitting arises because:
$$\langle V_{12} \rangle_{\text{singlet}} - \langle V_{12} \rangle_{\text{triplet}} = 2K > 0$$

This energy difference is not due to any magnetic interaction between spins, but purely from the requirement of overall antisymmetry and the electrostatic repulsion between electrons.

### 7.6 Exchange Operator and Total Angular Momentum

**Exchange Operator Definition**

For two identical particles, define the exchange operator $P_{12}$:

$$P_{12}|\psi(1, 2)\rangle = |\psi(2, 1)\rangle$$

**Properties of the Exchange Operator**

$$P_{12}^2 = I$$

Therefore, the eigenvalues of $P_{12}$ are $\pm 1$:
- $P_{12} = +1$: Symmetric state
- $P_{12} = -1$: Antisymmetric state

**Connection to Total Spin for Two Spin-1/2 Particles**

For two spin-1/2 particles, the exchange operator acting on the spin state is:

$$P_{12}^{\text{spin}} = \frac{1}{2}(1 + \boldsymbol{\sigma}_1 \cdot \boldsymbol{\sigma}_2)$$

Using $\mathbf{S}_1 \cdot \mathbf{S}_2 = \frac{\hbar^2}{4}\boldsymbol{\sigma}_1 \cdot \boldsymbol{\sigma}_2$ and the total spin $\mathbf{S} = \mathbf{S}_1 + \mathbf{S}_2$:

$$\mathbf{S}^2 = S_1^2 + S_2^2 + 2\mathbf{S}_1 \cdot \mathbf{S}_2 = \frac{3\hbar^2}{2} + 2\mathbf{S}_1 \cdot \mathbf{S}_2$$

Therefore:
$$\mathbf{S}_1 \cdot \mathbf{S}_2 = \frac{1}{2}\mathbf{S}^2 - \frac{3\hbar^2}{4}$$

For the spin states:
- Singlet ($S = 0$): $\mathbf{S}_1 \cdot \mathbf{S}_2 = -\frac{3\hbar^2}{4}$
  $$P_{12}^{\text{spin}}|S=0\rangle = \frac{1}{2}(1 + \frac{4}{\hbar^2}(-\frac{3\hbar^2}{4}))|S=0\rangle = -|S=0\rangle$$

- Triplet ($S = 1$): $\mathbf{S}_1 \cdot \mathbf{S}_2 = \frac{\hbar^2}{4}$
  $$P_{12}^{\text{spin}}|S=1\rangle = \frac{1}{2}(1 + \frac{4}{\hbar^2}(\frac{\hbar^2}{4}))|S=1\rangle = +|S=1\rangle$$

**General Rule**

For two identical particles with total spin $S$:
$$P_{12} = (-1)^{S+1} \quad \text{(for fermions)}$$

This shows that:
- Half-integer total spin ($S = 0, 2, 4, ...$ in units of $\hbar$): Antisymmetric
- Integer total spin ($S = 1, 3, 5, ...$ in units of $\hbar$): Symmetric

### 7.7 Addition of Three Angular Momenta and Permutation Symmetry

For three spin-1/2 particles, we first combine two spins, then add the third:

**Step 1**: Combine particles 1 and 2:
- $s_{12} = 1$ (triplet, symmetric under exchange of 1 and 2)
- $s_{12} = 0$ (singlet, antisymmetric under exchange of 1 and 2)

**Step 2**: Add particle 3:

For $s_{12} = 1$:
$$s = 1 + 1/2 = 3/2 \quad \text{or} \quad s = 1 - 1/2 = 1/2$$

For $s_{12} = 0$:
$$s = 0 + 1/2 = 1/2$$

**Total Spin States and Their Symmetry Properties**

**$s = 3/2$ (Quartet, totally symmetric):**

All four states are symmetric under exchange of any pair of particles:

$$|3/2, 3/2\rangle = |\uparrow\uparrow\uparrow\rangle$$

$$|3/2, 1/2\rangle = \frac{1}{\sqrt{3}}(|\downarrow\uparrow\uparrow\rangle + |\uparrow\downarrow\uparrow\rangle + |\uparrow\uparrow\downarrow\rangle)$$

$$|3/2, -1/2\rangle = \frac{1}{\sqrt{3}}(|\downarrow\downarrow\uparrow\rangle + |\downarrow\uparrow\downarrow\rangle + |\uparrow\downarrow\downarrow\rangle)$$

$$|3/2, -3/2\rangle = |\downarrow\downarrow\downarrow\rangle$$

**Verification of Symmetry:**

For $|3/2, 1/2\rangle$, applying exchange operator $P_{12}$:
$$P_{12}|3/2, 1/2\rangle = \frac{1}{\sqrt{3}}(|\uparrow\downarrow\uparrow\rangle + |\downarrow\uparrow\uparrow\rangle + |\uparrow\uparrow\downarrow\rangle) = |3/2, 1/2\rangle$$

Similar results hold for $P_{13}$ and $P_{23}$.

**$s = 1/2$ (Doublet, mixed symmetry):**

Two orthogonal doublet states with different symmetry properties under particle exchange:

**State A** (antisymmetric under $P_{12}$):
$$|1/2, 1/2\rangle_A = \frac{1}{\sqrt{2}}(|\downarrow\uparrow\uparrow\rangle - |\uparrow\downarrow\uparrow\rangle)$$

This state changes sign under exchange of particles 1 and 2.

**State B** (symmetric under $P_{12}$, but orthogonal to quartet):
$$|1/2, 1/2\rangle_B = \frac{1}{\sqrt{6}}(|\downarrow\uparrow\uparrow\rangle + |\uparrow\downarrow\uparrow\rangle - 2|\uparrow\uparrow\downarrow\rangle)$$

Under cyclic permutation $(1 \to 2 \to 3 \to 1)$, these states transform into each other, forming a 2-dimensional representation of the cyclic group.

**Explicit Derivation of Mixed Symmetry States:**

The two doublet states can be constructed using the standard Clebsch-Gordan procedure:

1. Start with the quartet state $|3/2, 1/2\rangle$ which is totally symmetric
2. Apply the lowering operator $S_- = S_{1-} + S_{2-} + S_{3-}$ to generate the full quartet
3. Construct the first doublet state $|1/2, 1/2\rangle_A$ by requiring:
   - Orthogonality to $|3/2, 1/2\rangle$
   - Antisymmetry under $P_{12}$
   
Explicit calculation:
$$|1/2, 1/2\rangle_A \propto |\downarrow\uparrow\uparrow\rangle - |\uparrow\downarrow\uparrow\rangle$$

After normalization:
$$|1/2, 1/2\rangle_A = \frac{1}{\sqrt{2}}(|\downarrow\uparrow\uparrow\rangle - |\uparrow\downarrow\uparrow\rangle)$$

The second doublet state $|1/2, 1/2\rangle_B$ is obtained by requiring:
- Orthogonality to both $|3/2, 1/2\rangle$ and $|1/2, 1/2\rangle_A$
- Symmetry under $P_{12}$

This gives:
$$|1/2, 1/2\rangle_B = \frac{1}{\sqrt{6}}(|\downarrow\uparrow\uparrow\rangle + |\uparrow\downarrow\uparrow\rangle - 2|\uparrow\uparrow\downarrow\rangle)$$

**Action of Ladder Operators:**

Applying $S_- = S_{1-} + S_{2-} + S_{3-}$:

For State A:
$$S_-|1/2, 1/2\rangle_A = \hbar|1/2, -1/2\rangle_A$$

where:
$$|1/2, -1/2\rangle_A = \frac{1}{\sqrt{2}}(|\downarrow\downarrow\uparrow\rangle - |\downarrow\uparrow\downarrow\rangle)$$

For State B:
$$S_-|1/2, 1/2\rangle_B = \hbar|1/2, -1/2\rangle_B$$

where:
$$|1/2, -1/2\rangle_B = \frac{1}{\sqrt{6}}(|\downarrow\downarrow\uparrow\rangle + |\downarrow\uparrow\downarrow\rangle - 2|\uparrow\downarrow\downarrow\rangle)$$

**Connection to Lithium Atom:**

In the lithium atom ($1s^2 2s^1$ configuration):
- The two $1s$ electrons form a singlet (antisymmetric spin state)
- The $2s$ electron adds angular momentum $s = 1/2$
- The total spin can be $S = 0$ or $S = 1$
- The $S = 1$ state (spin doublet) is the ground state

This coupling scheme is essential for understanding the fine structure and hyperfine structure of multi-electron atoms.

**Young Tableaux Classification with Diagrams**

<img src="/images/angular-momentum/young_3_all_combined.png" width="600px" alt="Young Diagrams for Three Particles">

The symmetry types of three-particle states can be classified using Young diagrams:

1. **Totally Symmetric** ( quartet, $s = 3/2$ ): Partition $(3)$, Dimension 4
   - One row of three boxes
   - Corresponds to the partition $(3)$ of $S_3$
   
2. **Mixed Symmetry** ( doublets, $s = 1/2$ ): Partition $(2,1)$, Dimension 2
   - Two boxes in the first row, one in the second
   - Corresponds to the partition $(2,1)$ of $S_3$
   
3. **Totally Antisymmetric**: Partition $(1,1,1)$, Dimension 0 (for spin-1/2)
   - One column of three boxes
   - Not available for spin-1/2, requires $j \geq 1$

**Hook Length and Dimension Calculation**

The number of standard Young tableaux (dimension of representation) is:
$$d = \frac{n!}{\prod_{i} h_i}$$

where $h_i$ is the hook length of box $i$.

**Mixed Symmetry Example: Partition (2,1)**

For the mixed symmetry diagram (2,1):

<img src="/images/angular-momentum/young_21_mixed.png" width="120px" alt="Mixed symmetry diagram (2,1)">

Box positions and hook lengths:
- Position (1,1): right=1, below=1, self=1 → $h = 3$
- Position (1,2): right=0, below=0, self=1 → $h = 1$  
- Position (2,1): right=0, below=0, self=1 → $h = 1$

$$d = \frac{3!}{3 \cdot 1 \cdot 1} = 2$$

This confirms there are two independent doublet states.

**Connection to Angular Momentum**

For three identical fermions with spin-1/2:
- The totally symmetric spin states ($s = 3/2$) must be combined with antisymmetric spatial wavefunctions
- The mixed symmetry spin states ($s = 1/2$) must be combined with spatial wavefunctions of the same mixed symmetry type

This constraint is crucial for understanding the structure of three-electron atoms like lithium and three-nucleon systems like $^3$He.

### 7.8 Slater Determinant and Total Angular Momentum Coupling

For $N$ identical fermions, the antisymmetric wavefunction can be written as a Slater determinant:

$$\Psi(1, 2, ..., N) = \frac{1}{\sqrt{N!}}\begin{vmatrix}
\phi_1(1) & \phi_1(2) & \cdots & \phi_1(N) \\
\phi_2(1) & \phi_2(2) & \cdots & \phi_2(N) \\
\vdots & \vdots & \ddots & \vdots \\
\phi_N(1) & \phi_N(2) & \cdots & \phi_N(N)
\end{vmatrix}$$

If any two particles occupy the same state ($\phi_i = \phi_j$), the determinant vanishes. This is the **Pauli exclusion principle**.

**Properties of the Slater Determinant:**

1. **Antisymmetry:** Interchanging two columns (particle coordinates) changes the sign of the determinant
2. **Normalization:** The factor $1/\sqrt{N!}$ ensures proper normalization when single-particle states are orthonormal
3. **Expansion:** The determinant can be expanded using the Levi-Civita symbol:
   $$\Psi = \frac{1}{\sqrt{N!}} \sum_{\sigma \in S_N} \text{sgn}(\sigma) \prod_{i=1}^N \phi_i(\sigma(i))$$

**Example: Helium Ground State ($1s^2$)**

For two electrons in the $1s$ orbital with opposite spins:

$$\Psi(1, 2) = \frac{1}{\sqrt{2}}\begin{vmatrix}
\psi_{1s}(1)\alpha(1) & \psi_{1s}(2)\alpha(2) \\
\psi_{1s}(1)\beta(1) & \psi_{1s}(2)\beta(2)
\end{vmatrix}$$

$$= \frac{1}{\sqrt{2}}\psi_{1s}(1)\psi_{1s}(2)[\alpha(1)\beta(2) - \beta(1)\alpha(2)]$$

$$= \psi_{1s}(1)\psi_{1s}(2) \cdot \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$

This is the spin singlet state, required by antisymmetry since both electrons occupy the same spatial orbital.

**Connection to LS Coupling:**

For multi-electron atoms, the total angular momentum $\mathbf{J} = \mathbf{L} + \mathbf{S}$ is constructed from:
- Total orbital angular momentum $\mathbf{L} = \sum_i \mathbf{l}_i$
- Total spin angular momentum $\mathbf{S} = \sum_i \mathbf{s}_i$

The Slater determinant ensures the overall antisymmetry of the wavefunction. The spatial and spin parts must combine to give the correct permutation symmetry:

| Configuration | Spatial Symmetry | Spin Symmetry | Total $S$ |
|:-------------:|:----------------:|:-------------:|:---------:|
| $(1s)^2$ | Symmetric | Antisymmetric | $S = 0$ |
| $(1s)(2s)$ | Symmetric | Antisymmetric | $S = 0$ |
| $(1s)(2s)$ | Antisymmetric | Symmetric | $S = 1$ |

**Matrix Elements in Slater Determinant Basis:**

For operators that are sums of single-particle operators $F = \sum_i f(i)$:
$$\langle\Psi|F|\Psi\rangle = \sum_{i=1}^N \langle\phi_i|f|\phi_i\rangle$$

For two-particle operators $G = \sum_{i<j} g(i,j)$:
$$\langle\Psi|G|\Psi\rangle = \sum_{i<j} [\langle\phi_i\phi_j|g|\phi_i\phi_j\rangle - \langle\phi_i\phi_j|g|\phi_j\phi_i\rangle]$$

The second term is the **exchange integral**, arising from antisymmetry.

**Application to Atomic Structure:**

The Slater determinant formalism is essential for:
- Hartree-Fock calculations
- Configuration interaction methods
- Understanding Hund's rules
- Calculating term symbols ($^{2S+1}L_J$)

For example, the carbon atom ground state configuration $(1s)^2(2s)^2(2p)^2$ has possible terms $^1S$, $^1D$, and $^3P$, with $^3P_0$ being the ground state according to Hund's rules.

---

## Summary and Key Formulas

### Fundamental Commutation Relations

| Relation | Expression |
|----------|------------|
| Basic commutator | $[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k$ |
| With $J^2$ | $[J^2, J_i] = 0$ |
| Ladder operators | $[J_z, J_\pm] = \pm\hbar J_\pm$ |

### Eigenvalue Spectrum

| Quantity | Eigenvalue |
|----------|------------|
| $J^2$ | $\hbar^2 j(j+1)$ where $j = 0, 1/2, 1, 3/2, ...$ |
| $J_z$ | $\hbar m$ where $m = -j, -j+1, ..., j-1, j$ |
| Number of states | $2j + 1$ |

### Ladder Operator Matrix Elements

$$J_+|j, m\rangle = \hbar\sqrt{(j-m)(j+m+1)}|j, m+1\rangle$$
$$J_-|j, m\rangle = \hbar\sqrt{(j+m)(j-m+1)}|j, m-1\rangle$$

### Pauli Matrices (Spin-1/2)

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$$\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$$

### Angular Momentum Addition

**Triangle Rule:**
$$|j_1 - j_2| \leq j \leq j_1 + j_2$$

**Clebsch-Gordan Expansion:**
$$|j, m\rangle = \sum_{m_1+m_2=m} \langle j_1, m_1; j_2, m_2|j, m\rangle |j_1, m_1\rangle|j_2, m_2\rangle$$

**Two Spin-1/2 CG Coefficients:**

| Coupled State | $\vert \uparrow\uparrow\rangle$ | $\vert \uparrow\downarrow\rangle$ | $\vert \downarrow\uparrow\rangle$ | $\vert \downarrow\downarrow\rangle$ |
|:-------------:|:-----------:|:-----------:|:-----------:|:-----------:|
| $\vert 1, 1\rangle$ | $1$ | $0$ | $0$ | $0$ |
| $\vert 1, 0\rangle$ | $0$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{\sqrt{2}}$ | $0$ |
| $\vert 1, -1\rangle$ | $0$ | $0$ | $0$ | $1$ |
| $\vert 0, 0\rangle$ | $0$ | $\frac{1}{\sqrt{2}}$ | $-\frac{1}{\sqrt{2}}$ | $0$ |

### Central Force Field

**Effective Potential:**
$$V_{\text{eff}}(r) = V(r) + \frac{\hbar^2 l(l+1)}{2\mu r^2}$$

**Centrifugal Barrier and Wavefunction Behavior:**
$$R_{nl}(r) \xrightarrow{r \to 0} r^l$$

**Hydrogen Atom Energy and Degeneracy:**
$$E_n = -\frac{13.6 \text{ eV}}{n^2}, \quad g_n = n^2$$

**Runge-Lenz Vector (Conserved for $1/r$ Potential):**
$$\mathbf{A} = \frac{1}{\mu}\mathbf{p} \times \mathbf{L} - \frac{e^2}{4\pi\varepsilon_0}\frac{\mathbf{r}}{r}, \quad [H, \mathbf{A}] = 0$$

### Identical Particles and Exchange Symmetry

**Two-Particle Symmetric/Antisymmetric States:**
$$|\psi_{S/A}\rangle = \frac{1}{\sqrt{2}}(|\alpha\beta\rangle \pm |\beta\alpha\rangle)$$

**Exchange Operator and Total Spin:**
$$P_{12}^{\text{spin}} = \frac{1}{2}(1 + \boldsymbol{\sigma}_1 \cdot \boldsymbol{\sigma}_2)$$

**Relation between Exchange Symmetry and Total Spin:**
$$P_{12}|S=0\rangle = -|S=0\rangle, \quad P_{12}|S=1\rangle = +|S=1\rangle$$

**Slater Determinant for $N$ Fermions:**
$$\Psi = \frac{1}{\sqrt{N!}}\det[\phi_i(j)]$$

### Group Representation Theory

**Rotation Groups:**
$$\text{SO(3)} \cong \text{SU(2)}/\mathbb{Z}_2$$

**Character Formula:**
$$\chi_j(\theta) = \frac{\sin[(j+1/2)\theta]}{\sin(\theta/2)}$$

**Dimension of Representation:**
$$d_j = 2j + 1$$

### Young Tableaux

**Hook Length Formula:**
$$d = \frac{n!}{\prod_i h_i}$$

**Three-Particle Symmetry Types:**

| Partition | Young Diagram | Spin | Dimension |
|-----------|:-------------:|:----:|:---------:|
| $(3)$ | <img src="/images/angular-momentum/young_3_symmetric_small.png" width="60px"> | $s = 3/2$ | 4 |
| $(2,1)$ | <img src="/images/angular-momentum/young_21_mixed_small.png" width="50px"> | $s = 1/2$ | 2 |
| $(1,1,1)$ | <img src="/images/angular-momentum/young_111_antisymmetric_small.png" width="30px"> | (not for spin-1/2) | 0 |

**Exchange Symmetry and Total Angular Momentum:**
$$P_{12}|J, M\rangle = (-1)^{2j-J}|J, M\rangle$$
