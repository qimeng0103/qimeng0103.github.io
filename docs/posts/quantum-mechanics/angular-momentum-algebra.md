---
title: "Angular Momentum Algebra and Its Applications"
description: "Comprehensive treatment of angular momentum theory: algebraic structure, spin systems, Clebsch-Gordan coefficients, central force fields, and identical particle systems"
date: 2026-04-04
tags: ["quantum mechanics", "angular momentum", "spin", "Clebsch-Gordan coefficients", "central force field", "identical particles"]
category: "quantum-mechanics"
math: true
---

# Angular Momentum Algebra and Its Applications

This article presents a systematic treatment of angular momentum theory in quantum mechanics. We begin with the fundamental commutation relations and ladder operator formalism, then discuss the matrix representations for various spin systems. The article provides detailed derivations of Clebsch-Gordan coefficients for angular momentum addition. Finally, we explore applications to central force field problems and systems of identical particles.

---

## Part I: Fundamental Commutation Relations and Algebraic Structure

### 1.1 Definition of Angular Momentum Operators

In quantum mechanics, angular momentum is defined through operators satisfying specific commutation relations. The orbital angular momentum operator is:

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

The allowed values of $j$ and $m$ are determined by the algebraic structure. Starting from the constraint that $J^2 \geq J_z^2$ as positive operators, we obtain $-j \leq m \leq j$. The requirement that ladder operators terminate the sequence leads to $j = 0, 1/2, 1, 3/2, ...$.

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

**Step 1: Constraint from $J^2$**

Since $J^2 = J_x^2 + J_y^2 + J_z^2 \geq J_z^2$ (all terms are positive operators):

$$\langle j, m|J^2|j, m\rangle \geq \langle j, m|J_z^2|j, m\rangle$$

$$\hbar^2 j(j+1) \geq \hbar^2 m^2$$

Therefore:
$$\boxed{-j \leq m \leq j}$$

For a given $j$, there are $2j + 1$ possible values of $m$.

**Step 2: Finding the Maximum $m$**

Since $m$ is bounded above by $j$, there must exist a state $|j, j\rangle$ such that:

$$J_+|j, j\rangle = 0$$

**Step 3: Using the Operator Identity**

$$J_-J_+ = (J_x - iJ_y)(J_x + iJ_y) = J_x^2 + J_y^2 + i[J_x, J_y] = J^2 - J_z^2 - \hbar J_z$$

Applying to $|j, j\rangle$:

$$J_-J_+|j, j\rangle = (J^2 - J_z^2 - \hbar J_z)|j, j\rangle = 0$$

$$\hbar^2 j(j+1) - \hbar^2 j^2 - \hbar^2 j = \hbar^2[j(j+1) - j^2 - j] = 0$$

This is satisfied for any $j$.

**Step 4: Finding the Minimum $m$**

Similarly, there must be a lowest state $|j, m_{\min}\rangle$ with:

$$J_-|j, m_{\min}\rangle = 0$$

Using $J_+J_- = J^2 - J_z^2 + \hbar J_z$:

$$J_+J_-|j, m_{\min}\rangle = (J^2 - J_z^2 + \hbar J_z)|j, m_{\min}\rangle = 0$$

$$\hbar^2 j(j+1) - \hbar^2 m_{\min}^2 + \hbar^2 m_{\min} = 0$$

$$j(j+1) = m_{\min}(m_{\min} - 1)$$

This quadratic has solutions $m_{\min} = j + 1$ (impossible since $m \leq j$) or:

$$\boxed{m_{\min} = -j}$$

**Step 5: Quantization Condition**

Starting from $m = -j$ and applying $J_+$ repeatedly must eventually reach $m = j$. After $n$ applications:

$$m = -j + n = j$$

Therefore:
$$2j = n$$

$$\boxed{j = 0, \frac{1}{2}, 1, \frac{3}{2}, 2, ...}$$

Angular momentum is quantized in integer or half-integer units.

### 2.5 Normalization Constants

To find the proportionality constants, assume:

$$J_+|j, m\rangle = C_+|j, m+1\rangle$$

Using $J_-J_+ = J^2 - J_z^2 - \hbar J_z$:

$$\langle j, m|J_-J_+|j, m\rangle = |C_+|^2\langle j, m+1|j, m+1\rangle = |C_+|^2$$

$$= \langle j, m|(J^2 - J_z^2 - \hbar J_z)|j, m\rangle = \hbar^2[j(j+1) - m^2 - m]$$

$$= \hbar^2(j - m)(j + m + 1)$$

Choosing the phase convention (Condon-Shortley):

$$\boxed{J_+|j, m\rangle = \hbar\sqrt{(j-m)(j+m+1)}|j, m+1\rangle}$$

Similarly:
$$\boxed{J_-|j, m\rangle = \hbar\sqrt{(j+m)(j-m+1)}|j, m-1\rangle}$$

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

## Part IV: Applications of Angular Momentum Algebra

Based on classic problems from the *Physics Problem Collection (量子力学大题典)* by Zhang Yongde.

### 4.1 Fourth Power Expectation Values of Angular Momentum Components

For a particle in the orbital angular momentum state $|lm\rangle$ with $l = 1$, the expectation value $\langle L_x^4 \rangle$ can be calculated using the ladder operator representation.

**Ladder Operator Method**

The $L_x$ operator can be expressed in terms of ladder operators:
$$L_x = \frac{1}{2}(L_+ + L_-)$$

Therefore:
$$L_x^4 = \frac{1}{16}(L_+ + L_-)^4$$

When expanding $(L_+ + L_-)^4$, the non-zero terms in the $|lm\rangle$ state are those with equal numbers of $L_+$ and $L_-$ operators. For $l = 1$, a useful property in this subspace is:
$$L_x^3 = L_x, \quad L_y^3 = L_y$$

This implies the pattern:
$$L_x^{2m+1} = L_x, \quad L_x^{2m} = L_x^2$$

**General Result for $\langle L_x^2 \rangle$ and $\langle L_y^2 \rangle$**

Using the angular momentum algebra:
$$\langle L_x^2 \rangle = \langle L_y^2 \rangle = \frac{1}{2}[l(l+1) - m^2]\hbar^2$$

For $l = 1$:
$$\langle L_x^2 \rangle = \langle L_y^2 \rangle = \frac{1}{2}(2 - m^2)\hbar^2$$

Therefore:
$$\langle L_x^4 \rangle = \langle L_x^2 \rangle = \frac{1}{2}(2 - m^2)\hbar^4$$

**Specific Values:**
- For $m = 0$: $\langle L_x^4 \rangle = \hbar^4$
- For $m = \pm 1$: $\langle L_x^4 \rangle = \frac{1}{2}\hbar^4$

### 4.2 Measurement Probabilities for $L_x$ in $Y_{20}$ State

When a particle is in the common eigenstate $Y_{20}$ of $(L^2, L_z)$, we can determine the possible measured values of $L_x$ and their corresponding probabilities using coordinate rotation methods.

**Rotation Method**

The spherical harmonics $Y_{2m}(\theta, \phi)$ are eigenfunctions of $L_z$. To find $L_x$ eigenstates, we perform a coordinate rotation $x \to y$, $y \to z$, $z \to x$.

**Explicit Forms of $Y_{2m}$:**

$$Y_{2,\pm 2} = \frac{1}{2}\sqrt{\frac{15}{8\pi}}\frac{(x \pm iy)^2}{r^2}$$

$$Y_{2,\pm 1} = \mp\sqrt{\frac{15}{8\pi}}\frac{(x \pm iy)z}{r^2}$$

$$Y_{2,0} = \sqrt{\frac{5}{16\pi}}\frac{2z^2 - x^2 - y^2}{r^2}$$

**Eigenstates of $L_x$ (denoted $Y_{2m}^x$):**

By cyclic permutation:

$$Y_{2,0}^x = -\frac{1}{2}Y_{2,0} + \frac{\sqrt{3}}{2\sqrt{2}}(Y_{2,-2} + Y_{2,2})$$

$$Y_{2,\pm 1}^x = \pm\frac{i}{2}(Y_{2,2} - Y_{2,-2}) + \frac{i}{2}(Y_{2,1} - Y_{2,-1})$$

$$Y_{2,\pm 2}^x = -\frac{\sqrt{3}}{2\sqrt{2}}Y_{2,0} \mp \frac{1}{2}(Y_{2,1} + Y_{2,-1}) - \frac{1}{4}(Y_{2,-2} + Y_{2,2})$$

**Expanding $Y_{2,0}$ in $L_x$ Eigenstates:**

From the expression for $Y_{2,0}^x$, we can invert to find:

$$Y_{2,0} = -\frac{1}{2}Y_{2,0}^x - \frac{\sqrt{3}}{2\sqrt{2}}(Y_{2,-2}^x + Y_{2,2}^x)$$

**Measurement Probabilities:**

The possible measured values of $L_x$ are $0, \pm\hbar, \pm 2\hbar$ with probabilities:

| $L_x$ Value | Probability |
|-------------|-------------|
| $0$ | $\frac{1}{4}$ |
| $\pm\hbar$ | $0$ |
| $\pm 2\hbar$ | $\frac{3}{8}$ each |

**Alternative Method using Expectation Values**

The probabilities $P_m^{(20)}$ for measuring $L_x = m\hbar$ satisfy:

1. Normalization: $P_0 + 2P_1 + 2P_2 = 1$
2. $\langle L_x^2 \rangle = 2\hbar^2$: $2P_1 \cdot \hbar^2 + 2P_2 \cdot 4\hbar^2 = 2\hbar^2$
3. $\langle L_x^4 \rangle = 12\hbar^4$: $2P_1 \cdot \hbar^4 + 2P_2 \cdot 16\hbar^4 = 12\hbar^4$

Solving this system yields:
$$P_0 = \frac{1}{4}, \quad P_1 = 0, \quad P_2 = \frac{3}{8}$$

### 4.3 Action of Ladder Operators on Angular Momentum States

**General Formulas (Condon-Shortley Phase Convention):**

$$J_{\pm}|jm\rangle = \sqrt{(j \mp m)(j \pm m + 1)}\hbar|j, m \pm 1\rangle$$

**Products of Ladder Operators:**

$$L_-L_+|lm\rangle = [l(l+1) - m(m+1)]\hbar^2|lm\rangle$$

$$L_+L_-|lm\rangle = [l(l+1) - m(m-1)]\hbar^2|lm\rangle$$

**Double-Step Operators:**

$$L_+^2|lm\rangle = \sqrt{[l(l+1)-m(m+1)][l(l+1)-(m+1)(m+2)]}\hbar^2|l,m+2\rangle$$

$$L_-^2|lm\rangle = \sqrt{[l(l+1)-m(m-1)][l(l+1)-(m-1)(m-2)]}\hbar^2|l,m-2\rangle$$

These formulas are essential for calculating higher-order expectation values and transition matrix elements.

---

## Part V: Addition of Angular Momenta and Clebsch-Gordan Coefficients

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

This is analogous to the classical vector addition where the resultant vector's magnitude ranges from the difference to the sum.

### 4.5 Two Spin-1/2 System: Detailed CG Coefficient Calculation

For two spin-1/2 particles ($j_1 = j_2 = 1/2$):

$$j = |1/2 - 1/2|, ..., 1/2 + 1/2 = 0, 1$$

**Triplet States (j = 1):**

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

**Singlet State (j = 0):**

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

### 4.6 CG Coefficient Table for Two Spin-1/2

The CG coefficients for coupling two spin-1/2 particles are summarized below:

| Coupled State | Uncoupled State | CG Coefficient |
|:-------------:|:---------------:|:--------------:|
| $j=1, m=1$ | $\|\uparrow\uparrow\rangle$ | $1$ |
| $j=1, m=0$ | $\frac{1}{\sqrt{2}}(\|\uparrow\downarrow\rangle + \|\downarrow\uparrow\rangle)$ | $\frac{1}{\sqrt{2}}$ |
| $j=1, m=-1$ | $\|\downarrow\downarrow\rangle$ | $1$ |
| $j=0, m=0$ | $\frac{1}{\sqrt{2}}(\|\uparrow\downarrow\rangle - \|\downarrow\uparrow\rangle)$ | $\frac{1}{\sqrt{2}}$ |

**Triplet States (Symmetric, S=1):**
- |1,1⟩ = |↑↑⟩
- |1,0⟩ = (|↑↓⟩ + |↓↑⟩)/√2  
- |1,-1⟩ = |↓↓⟩

**Singlet State (Antisymmetric, S=0):**
- |0,0⟩ = (|↑↓⟩ - |↓↑⟩)/√2

### 4.7 Orbital-Spin Coupling (j = l ± 1/2)

For an electron with orbital angular momentum $l$ and spin $s = 1/2$:

$$j = l + 1/2 \quad \text{or} \quad j = l - 1/2 \quad (\text{for } l \geq 1)$$

**States with $j = l + 1/2$:**

$$|j = l + 1/2, m_j\rangle = \sqrt{\frac{l + m_j + 1/2}{2l + 1}}|l, m_j - 1/2; 1/2, 1/2\rangle + \sqrt{\frac{l - m_j + 1/2}{2l + 1}}|l, m_j + 1/2; 1/2, -1/2\rangle$$

**States with $j = l - 1/2$:**

$$|j = l - 1/2, m_j\rangle = -\sqrt{\frac{l - m_j + 1/2}{2l + 1}}|l, m_j - 1/2; 1/2, 1/2\rangle + \sqrt{\frac{l + m_j + 1/2}{2l + 1}}|l, m_j + 1/2; 1/2, -1/2\rangle$$

---

## Part V: Group Representation Theory and Young Tableaux

### 5.1 Rotation Groups SO(3) and SU(2)

Angular momentum operators generate rotations in quantum mechanics. The commutation relations $[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k$ define the Lie algebra of the rotation group.

**SO(3) - The 3D Rotation Group**

SO(3) is the group of proper rotations in three-dimensional space. Each rotation can be parameterized by:
- An axis $\mathbf{n}$ (unit vector)
- An angle $\theta$

The rotation operator is:
$$R(\mathbf{n}, \theta) = e^{-i\theta \mathbf{n} \cdot \mathbf{J}/\hbar}$$

**SU(2) - The Special Unitary Group**

SU(2) is the group of $2 \times 2$ unitary matrices with determinant 1. It is the double cover of SO(3):
- Every SO(3) rotation corresponds to two SU(2) elements ($\pm U$)
- For integer $j$, the representations correspond to SO(3)
- For half-integer $j$, the representations correspond to SU(2)

**Relationship:**
$$\text{SU(2)}/\mathbb{Z}_2 \cong \text{SO(3)}$$

### 5.2 Irreducible Representations

For angular momentum $j$, the $(2j+1)$ states $|j, m\rangle$ form an irreducible representation of the rotation group.

**Dimension of Representation:**
$$d_j = 2j + 1$$

**Character of Rotation:**

The character (trace of the representation matrix) for rotation by angle $\theta$ about any axis is:
$$\chi_j(\theta) = \sum_{m=-j}^{j} e^{-im\theta} = \frac{\sin[(j+1/2)\theta]}{\sin(\theta/2)}$$

**Orthogonality Relation:**
$$\int_0^{2\pi} \chi_{j_1}(\theta) \chi_{j_2}(\theta) \sin^2\frac{\theta}{2} d\theta = \pi \delta_{j_1 j_2}$$

### 5.3 Young Tableaux for Permutation Symmetry

Young tableaux provide a graphical method to classify the symmetry types of many-particle states under particle exchange.

**Basic Rules for Constructing Young Diagrams:**

1. Each box represents one particle
2. Rows represent symmetric combinations
3. Columns represent antisymmetric combinations
4. The number of boxes equals the number of particles

**Young Diagrams for Two Particles:**

<img src="/images/angular-momentum/two_particle_young_new.png" width="500px" alt="Young Diagrams for Two Particles">

*Left: Symmetric representation (partition (2), triplet $S=1$, dimension 3). Right: Antisymmetric representation (partition (1,1), singlet $S=0$, dimension 1)*

**Young Diagrams for Three Particles:**

<img src="/images/angular-momentum/young_3_all_combined.png" width="600px" alt="Young Diagrams for Three Particles">

*Left: Totally symmetric (quartet, $S=3/2$, dim=4). Center: Mixed symmetry (doublet, $S=1/2$, dim=2). Right: Totally antisymmetric (not for spin-1/2)*

### 5.4 Hook Length Formula

The dimension of a representation corresponding to a Young diagram with $n$ boxes is given by the hook length formula:

$$d = \frac{n!}{\prod_{\text{boxes}} h_i}$$

where $h_i$ is the hook length of box $i$ (number of boxes to the right in the same row + number below in the same column + 1).

**Hook Length Calculation Example: Three Spin-1/2 Particles**

For three spin-1/2 particles, the Young diagrams and their properties are:

<img src="/images/angular-momentum/young_3_symmetric.png" width="200px" alt="Symmetric diagram (3)">

*Symmetric diagram (3): Hook lengths are 3, 2, 1. Dimension: $\frac{3!}{3 \cdot 2 \cdot 1} = 1$ (for each $m$ value, total $2S+1 = 4$)*

<img src="/images/angular-momentum/young_21_mixed.png" width="180px" alt="Mixed symmetry diagram (2,1)">

*Mixed symmetry diagram (2,1): Hook lengths are 3, 1, 1. Dimension: $\frac{3!}{3 \cdot 1 \cdot 1} = 2$ (two doublet states)*

### 5.5 Connection to Angular Momentum Addition

When adding angular momenta $\mathbf{J} = \mathbf{J}_1 + \mathbf{J}_2$, the product of representations decomposes as:

$$D^{(j_1)} \otimes D^{(j_2)} = \bigoplus_{j=|j_1-j_2|}^{j_1+j_2} D^{(j)}$$

**Dimension Check:**
$$(2j_1+1)(2j_2+1) = \sum_{j=|j_1-j_2|}^{j_1+j_2} (2j+1)$$

**CG Decomposition Pattern:**

The decomposition follows the triangle rule:
$$D^{(j_1)} \otimes D^{(j_2)} = \bigoplus_{j=|j_1-j_2|}^{j_1+j_2} D^{(j)}$$

**Dimension Verification:**
$$(2j_1+1)(2j_2+1) = \sum_{j=|j_1-j_2|}^{j_1+j_2}(2j+1)$$

**Example: Two Spin-1/2 Particles ($j_1 = j_2 = 1/2$)**

| Uncoupled Basis | Coupled States |
|:----------------|:---------------|
| $|\uparrow\uparrow\rangle$ | $|j=1, m=1\rangle$ (Triplet) |
| $\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)$ | $|j=1, m=0\rangle$ (Triplet) |
| $|\downarrow\downarrow\rangle$ | $|j=1, m=-1\rangle$ (Triplet) |
| $\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ | $|j=0, m=0\rangle$ (Singlet) |

*Total: $2 \times 2 = 4$ states decompose into $j=1$ (3 states) $\oplus$ $j=0$ (1 state)*

---

## Part VI: Central Force Field Problems

### 5.1 Separation of Variables in Spherical Coordinates

For a particle in a central potential $V(r)$, the Hamiltonian is:

$$H = -\frac{\hbar^2}{2\mu}\nabla^2 + V(r)$$

In spherical coordinates:

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2}\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$$

The angular part is related to $L^2$:

$$L^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$$

Therefore:
$$H = -\frac{\hbar^2}{2\mu}\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{L^2}{2\mu r^2} + V(r)$$

### 5.2 Simultaneous Eigenfunctions

Since $[H, L^2] = [H, L_z] = [L^2, L_z] = 0$, we have simultaneous eigenfunctions:

$$\psi(r, \theta, \phi) = R_{nl}(r)Y_l^m(\theta, \phi)$$

where:
- $Y_l^m(\theta, \phi)$ are the spherical harmonics (eigenfunctions of $L^2$ and $L_z$)
- $L^2 Y_l^m = \hbar^2 l(l+1) Y_l^m$
- $L_z Y_l^m = \hbar m Y_l^m$ with $m = -l, -l+1, ..., l$

### 5.6 Angular Momentum in Central Force Fields: Key Theorems

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

### 5.7 Radial Equation and Angular Momentum Barrier

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

### 5.8 Runge-Lenz Vector and Hydrogen Atom Degeneracy

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

### 5.9 Hydrogen Atom Energy Levels and Angular Momentum

For the Coulomb potential $V(r) = -\frac{e^2}{4\pi\varepsilon_0 r}$:

The energy eigenvalues are:

$$\boxed{E_n = -\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2} = -\frac{13.6 \text{ eV}}{n^2}}$$

where $n = 1, 2, 3, ...$ is the principal quantum number.

For each $n$, the allowed values of $l$ are $l = 0, 1, 2, ..., n-1$.

For each $l$, there are $2l+1$ values of $m$.

The total degeneracy of level $n$ is:
$$g_n = \sum_{l=0}^{n-1}(2l+1) = n^2$$

### 5.10 Three-Dimensional Isotropic Harmonic Oscillator

For $V(r) = \frac{1}{2}\mu\omega^2 r^2$:

The energy eigenvalues are:

$$\boxed{E_N = \left(N + \frac{3}{2}\right)\hbar\omega}$$

where $N = 2n_r + l = 0, 1, 2, ...$ with $n_r = 0, 1, 2, ...$ being the radial quantum number.

For a given $N$, the allowed values of $l$ are $l = N, N-2, N-4, ..., 1$ or $0$.

The degeneracy of level $N$ is:
$$g_N = \frac{(N+1)(N+2)}{2}$$

---

## Part VII: Systems of Identical Particles and Young Tableaux Applications

### 6.1 Symmetry Requirements for Many-Particle States

For a system of $N$ identical particles, the total wavefunction must satisfy specific symmetry properties under particle exchange:

- **Bosons** (integer spin): Wavefunction is **symmetric** under exchange of any two particles
- **Fermions** (half-integer spin): Wavefunction is **antisymmetric** under exchange of any two particles

### 6.2 Two-Particle Systems

For two identical particles with single-particle states $|\alpha\rangle$ and $|\beta\rangle$:

**Symmetric State (Bosons):**
$$|\psi_S\rangle = \frac{1}{\sqrt{2}}(|\alpha\rangle_1|\beta\rangle_2 + |\beta\rangle_1|\alpha\rangle_2)$$

**Antisymmetric State (Fermions):**
$$|\psi_A\rangle = \frac{1}{\sqrt{2}}(|\alpha\rangle_1|\beta\rangle_2 - |\beta\rangle_1|\alpha\rangle_2)$$

### 6.3 Spin and Spatial Degrees of Freedom

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

### 6.4 Total Angular Momentum of Two-Particle Systems

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

### 6.5 Exchange Interaction and Helium Atom

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

### 6.6 Exchange Operator and Total Angular Momentum

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

### 6.7 Addition of Three Angular Momenta and Permutation Symmetry

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

### 6.8 Slater Determinant and Total Angular Momentum Coupling

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

| Coupled State | $|\uparrow\uparrow\rangle$ | $|\uparrow\downarrow\rangle$ | $|\downarrow\uparrow\rangle$ | $|\downarrow\downarrow\rangle$ |
|:-------------:|:-----------:|:-----------:|:-----------:|:-----------:|
| $|1, 1\rangle$ | $1$ | $0$ | $0$ | $0$ |
| $|1, 0\rangle$ | $0$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{\sqrt{2}}$ | $0$ |
| $|1, -1\rangle$ | $0$ | $0$ | $0$ | $1$ |
| $|0, 0\rangle$ | $0$ | $\frac{1}{\sqrt{2}}$ | $-\frac{1}{\sqrt{2}}$ | $0$ |

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
