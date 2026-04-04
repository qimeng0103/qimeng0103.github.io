---
title: "Angular Momentum Algebra in Quantum Mechanics"
description: "Comprehensive treatment of angular momentum theory including commutation relations, ladder operators, eigenvalue spectra, and addition of angular momenta with detailed derivations"
date: 2026-04-04
tags: ["quantum mechanics", "angular momentum", "ladder operators", "Clebsch-Gordan coefficients", "rotation group"]
category: "quantum-mechanics"
math: true
---

# Angular Momentum Algebra in Quantum Mechanics

This article presents a systematic treatment of angular momentum theory in quantum mechanics, covering the algebraic structure based on commutation relations, the ladder operator method for determining eigenvalue spectra, the matrix representations, and the theory of angular momentum addition. Detailed mathematical derivations are provided throughout.

---

## Part I: Fundamental Commutation Relations and Algebraic Structure

### 1.1 Definition of Angular Momentum Operators

In quantum mechanics, angular momentum is defined through operators that satisfy specific commutation relations. The orbital angular momentum operator is:

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

**Key Question**: What are the allowed values of $j$ and $m$?

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

Angular momentum is quantized in integer or half-integer units!

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

## Part III: Matrix Representations

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

### 3.2 Example: Spin-1/2 (j = 1/2)

For $j = 1/2$, there are two states: $|1/2, 1/2\rangle \equiv |\uparrow\rangle$ and $|1/2, -1/2\rangle \equiv |\downarrow\rangle$.

**Matrix Elements:**

$$J_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \frac{\hbar}{2}\sigma_z$$

$$J_+ = \hbar\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$$

$$J_- = \hbar\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$$

$$J_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \frac{\hbar}{2}\sigma_x$$

$$J_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \frac{\hbar}{2}\sigma_y$$

The matrices $\sigma_i$ are the famous **Pauli matrices**.

### 3.3 Example: Spin-1 (j = 1)

For $j = 1$, the basis is $|1, 1\rangle$, $|1, 0\rangle$, $|1, -1\rangle$.

$$J_z = \hbar\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}$$

$$J_+ = \hbar\begin{pmatrix} 0 & \sqrt{2} & 0 \\ 0 & 0 & \sqrt{2} \\ 0 & 0 & 0 \end{pmatrix}, \quad J_- = \hbar\begin{pmatrix} 0 & 0 & 0 \\ \sqrt{2} & 0 & 0 \\ 0 & \sqrt{2} & 0 \end{pmatrix}$$

$$J_x = \frac{\hbar}{\sqrt{2}}\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \quad J_y = \frac{\hbar}{\sqrt{2}}\begin{pmatrix} 0 & -i & 0 \\ i & 0 & -i \\ 0 & i & 0 \end{pmatrix}$$

---

## Part IV: Addition of Angular Momenta

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

### 4.3 Coupled Basis

The total angular momentum $J^2$ and $J_z$ have eigenstates:

$$|j, m\rangle = \sum_{m_1, m_2} C(j_1, j_2, j; m_1, m_2, m)|j_1, m_1; j_2, m_2\rangle$$

where $C(j_1, j_2, j; m_1, m_2, m)$ are the **Clebsch-Gordan coefficients**.

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

### 4.5 Example: Addition of Two Spin-1/2

For two spin-1/2 particles ($j_1 = j_2 = 1/2$):

$$j = |1/2 - 1/2|, ..., 1/2 + 1/2 = 0, 1$$

**Triplet States (j = 1):**

$$|1, 1\rangle = |\uparrow\uparrow\rangle$$

$$|1, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)$$

$$|1, -1\rangle = |\downarrow\downarrow\rangle$$

**Singlet State (j = 0):**

$$|0, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$

These states are important in quantum information (Bell states) and atomic physics (exchange interaction).

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
| Number of states for given $j$ | $2j + 1$ |

### Ladder Operator Matrix Elements

$$J_+|j, m\rangle = \hbar\sqrt{(j-m)(j+m+1)}|j, m+1\rangle$$
$$J_-|j, m\rangle = \hbar\sqrt{(j+m)(j-m+1)}|j, m-1\rangle$$

### Angular Momentum Addition

**Triangle Rule:**
$$|j_1 - j_2| \leq j \leq j_1 + j_2$$

**Clebsch-Gordan Expansion:**
$$|j, m\rangle = \sum_{m_1+m_2=m} \langle j_1, m_1; j_2, m_2|j, m\rangle |j_1, m_1\rangle|j_2, m_2\rangle$$

**Key Property:**
$$m = m_1 + m_2$$

### Pauli Matrices (Spin-1/2)

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Identity:**
$$\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$$

