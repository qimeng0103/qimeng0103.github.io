# Stationary Perturbation Theory: Non-Degenerate vs Degenerate Cases

📅 **Date:** 2026-03-30 | 🏷️ **Tags:** Quantum Mechanics, Perturbation Theory | 📂 **Category:** Quantum Mechanics Notes

---

## Introduction

Stationary perturbation theory addresses the eigenvalue problem when the Hamiltonian can be decomposed as

$$
\hat{H} = \hat{H}_0 + \lambda \hat{V}
$$

where $\hat{H}_0$ is exactly solvable with known spectrum $\hat{H}_0|n^{(0)}\rangle = E_n^{(0)}|n^{(0)}\rangle$, and $\lambda\hat{V}$ is a small perturbation. The central task is to systematically construct corrections to energy and eigenstates as power series in $\lambda$.

The mathematical structure fundamentally differs between **non-degenerate** and **degenerate** unperturbed levels. This distinction is not merely technical—it reflects deep physical differences in how perturbations interact with symmetries.

---

## Part I: Non-Degenerate Perturbation Theory

### Perturbation Expansion Framework

We seek solutions to the full Schrödinger equation:

$$
\hat{H}|n\rangle = E_n|n\rangle
$$

Expanding both energy and state in powers of $\lambda$:

$$
E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \lambda^3 E_n^{(3)} + \cdots = \sum_{k=0}^{\infty} \lambda^k E_n^{(k)}
$$

$$
|n\rangle = |n^{(0)}\rangle + \lambda |n^{(1)}\rangle + \lambda^2 |n^{(2)}\rangle + \cdots = \sum_{k=0}^{\infty} \lambda^k |n^{(k)}\rangle
$$

Intermediate normalization is imposed: $\langle n^{(0)} | n \rangle = 1$, which implies $\langle n^{(0)} | n^{(k)}\rangle = 0$ for $k \geq 1$.

### Order-by-Order Equation Separation

Substituting expansions into the Schrödinger equation:

$$
(\hat{H}_0 + \lambda\hat{V})\sum_{k=0}^{\infty}\lambda^k|n^{(k)}\rangle = \sum_{j=0}^{\infty}\lambda^j E_n^{(j)} \sum_{k=0}^{\infty}\lambda^k|n^{(k)}\rangle
$$

Collecting terms by powers of $\lambda$:

$$
\sum_{k=0}^{\infty}\lambda^k \hat{H}_0|n^{(k)}\rangle + \sum_{k=0}^{\infty}\lambda^{k+1}\hat{V}|n^{(k)}\rangle = \sum_{j,k=0}^{\infty}\lambda^{j+k}E_n^{(j)}|n^{(k)}\rangle
$$

Matching coefficients of $\lambda^N$ on both sides yields the **hierarchy of perturbation equations**:

$$
\boxed{\hat{H}_0|n^{(N)}\rangle + \hat{V}|n^{(N-1)}\rangle = \sum_{k=0}^{N} E_n^{(N-k)}|n^{(k)}\rangle}
$$

Rearranging:

$$
(\hat{H}_0 - E_n^{(0)})|n^{(N)}\rangle = \sum_{k=1}^{N}E_n^{(N-k)}|n^{(k)}\rangle - \hat{V}|n^{(N-1)}\rangle + E_n^{(N)}|n^{(0)}\rangle
$$

Or more compactly:

$$
(\hat{H}_0 - E_n^{(0)})|n^{(N)}\rangle = -\hat{V}|n^{(N-1)}\rangle + \sum_{j=0}^{N-1}E_n^{(N-j)}|n^{(j)}\rangle
$$

---

### Zeroth Order ($N=0$)

$$
\hat{H}_0|n^{(0)}\rangle = E_n^{(0)}|n^{(0)}\rangle
$$

This is the unperturbed problem, solved by assumption.

---

### First Order ($N=1$)

$$
(\hat{H}_0 - E_n^{(0)})|n^{(1)}\rangle = (E_n^{(1)} - \hat{V})|n^{(0)}\rangle
$$

**Energy correction:** Project onto $\langle n^{(0)}|$:

$$
\langle n^{(0)}|(\hat{H}_0 - E_n^{(0)})|n^{(1)}\rangle = E_n^{(1)} - \langle n^{(0)}|\hat{V}|n^{(0)}\rangle
$$

Since $\hat{H}_0$ is Hermitian, $\langle n^{(0)}|\hat{H}_0 = E_n^{(0)}\langle n^{(0)}|$, the LHS vanishes:

$$
\boxed{E_n^{(1)} = \langle n^{(0)}|\hat{V}|n^{(0)}\rangle = V_{nn}}
$$

**State correction:** Expand $|n^{(1)}\rangle = \sum_{m \neq n} c_m^{(1)}|m^{(0)}\rangle$ and project onto $\langle m^{(0)}|$ for $m \neq n$:

$$
(E_m^{(0)} - E_n^{(0)})c_m^{(1)} = -\langle m^{(0)}|\hat{V}|n^{(0)}\rangle
$$

$$
\boxed{c_m^{(1)} = \frac{V_{mn}}{E_n^{(0)} - E_m^{(0)}}}
$$

$$
\boxed{|n^{(1)}\rangle = \sum_{m \neq n} \frac{V_{mn}}{E_n^{(0)} - E_m^{(0)}}|m^{(0)}\rangle}
$$

---

### Second Order ($N=2$)

$$
(\hat{H}_0 - E_n^{(0)})|n^{(2)}\rangle = E_n^{(2)}|n^{(0)}\rangle + E_n^{(1)}|n^{(1)}\rangle - \hat{V}|n^{(1)}\rangle
$$

**Energy correction:** Project onto $\langle n^{(0)}|$:

$$
0 = E_n^{(2)} + E_n^{(1)}\underbrace{\langle n^{(0)}|n^{(1)}\rangle}_{0} - \langle n^{(0)}|\hat{V}|n^{(1)}\rangle
$$

$$
\boxed{E_n^{(2)} = \langle n^{(0)}|\hat{V}|n^{(1)}\rangle = \sum_{m \neq n} \frac{|V_{mn}|^2}{E_n^{(0)} - E_m^{(0)}}}
$$

**State correction:** Expand $|n^{(2)}\rangle = \sum_{m \neq n} c_m^{(2)}|m^{(0)}\rangle$. For $m \neq n$:

$$
(E_m^{(0)} - E_n^{(0)})c_m^{(2)} = E_n^{(1)}c_m^{(1)} - \sum_{k \neq n} c_k^{(1)}\langle m^{(0)}|\hat{V}|k^{(0)}\rangle
$$

$$
c_m^{(2)} = \sum_{k \neq n} \frac{V_{mk}V_{kn}}{(E_n^{(0)} - E_m^{(0)})(E_n^{(0)} - E_k^{(0)})} - \frac{V_{mn}V_{nn}}{(E_n^{(0)} - E_m^{(0)})^2}
$$

$$
\boxed{|n^{(2)}\rangle = \sum_{m \neq n}\left[\sum_{k \neq n}\frac{V_{mk}V_{kn}}{(E_n^{(0)} - E_m^{(0)})(E_n^{(0)} - E_k^{(0)})} - \frac{V_{mn}V_{nn}}{(E_n^{(0)} - E_m^{(0)})^2}\right]|m^{(0)}\rangle}
$$

---

### Third Order Energy Correction

From $E_n^{(3)} = \langle n^{(0)}|\hat{V}|n^{(2)}\rangle$:

$$
\boxed{E_n^{(3)} = \sum_{m \neq n}\sum_{k \neq n}\frac{V_{nm}V_{mk}V_{kn}}{(E_n^{(0)} - E_m^{(0)})(E_n^{(0)} - E_k^{(0)})} - V_{nn}\sum_{m \neq n}\frac{|V_{mn}|^2}{(E_n^{(0)} - E_m^{(0)})^2}}
$$

---

### Summary: Non-Degenerate Perturbation Series

$$
\boxed{E_n = E_n^{(0)} + V_{nn} + \sum_{m \neq n}\frac{|V_{mn}|^2}{E_n^{(0)} - E_m^{(0)}} + E_n^{(3)} + O(\lambda^4)}
$$

$$
\boxed{|n\rangle = |n^{(0)}\rangle + \sum_{m \neq n}\frac{V_{mn}}{E_n^{(0)} - E_m^{(0)}}|m^{(0)}\rangle + |n^{(2)}\rangle + O(\lambda^3)}
$$

---

## Part II: Degenerate Perturbation Theory

### The Problem: Breakdown of Non-Degenerate Theory

For a $g$-fold degenerate level $E_n^{(0)}$:

$$
\hat{H}_0|n, i\rangle = E_n^{(0)}|n, i\rangle, \quad i = 1, 2, \ldots, g
$$

The unperturbed eigenstates form a $g$-dimensional degenerate subspace $\mathcal{H}_n^{(0)} = \text{span}\{|n, i\rangle\}$. Any orthonormal basis of this subspace is equally valid:

$$
|n, \alpha\rangle = \sum_{i=1}^{g} U_{\alpha i}|n, i\rangle
$$

where $U$ is an arbitrary $g \times g$ unitary matrix.

**Critical observation:** In first-order state correction, the coefficient

$$
c_m^{(1)} = \frac{\langle m^{(0)}|\hat{V}|n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}
$$

diverges when $|m^{(0)}\rangle$ is also in the degenerate subspace (denominator vanishes). This is not merely a technical obstacle—it signals that the perturbation theory structure itself must be reformulated.

### The Physical Origin of the Problem

The perturbation $\hat{V}$ generically **lifts the degeneracy**. After turning on $\lambda\hat{V}$, the $g$ degenerate levels split into distinct energies. The key question is: **which zeroth-order states evolve into which perturbed states?**

Consider the limit $\lambda \to 0^+$. The perturbed states $|n, k(\lambda)\rangle$ with energies $E_{n,k}(\lambda)$ must approach some zeroth-order states:

$$
\lim_{\lambda \to 0^+} |n, k(\lambda)\rangle = |n, k^{(0)}\rangle \in \mathcal{H}_n^{(0)}
$$

The issue is that the "correct" zeroth-order states $|n, k^{(0)}\rangle$ are determined by $\hat{V}$—they are not arbitrary. Non-degenerate perturbation theory implicitly assumes the zeroth-order state is uniquely defined, which fails when any superposition within $\mathcal{H}_n^{(0)}$ is valid.

### The Resolution: Diagonalization in the Degenerate Subspace

To identify the correct zeroth-order basis, we examine the first-order equation more carefully. Consider the $k$-th perturbed state that emerges from the originally degenerate level. Expand it as:

$$
|\psi_{n,k}\rangle = |n, k^{(0)}\rangle + \lambda|n, k^{(1)}\rangle + \cdots
$$

where $|n, k^{(0)}\rangle \in \mathcal{H}_n^{(0)}$ is the "correct" zeroth-order state we seek, and $|\psi_{n,k}\rangle$ denotes the exact eigenstate. The first-order equation is:

$$
(\hat{H}_0 - E_n^{(0)})|n, k^{(1)}\rangle = (E_{n,k}^{(1)} - \hat{V})|n, k^{(0)}\rangle
$$

To solve this, expand $|n, k^{(0)}\rangle$ in the original basis $|n, i\rangle$ ($i = 1, \ldots, g$) and project onto $\langle n, i|$:

$$
\sum_{j=1}^{g} \langle n, i|\hat{V}|n, j\rangle c_j^{(k)} = E_{n,k}^{(1)} c_i^{(k)}
$$

This is the **secular equation**—an eigenvalue problem within the degenerate subspace:

$$
\boxed{\mathbf{V}^{(n)} \mathbf{c}^{(k)} = E_{n,k}^{(1)} \mathbf{c}^{(k)}}
$$

where $V_{ij}^{(n)} = \langle n, i|\hat{V}|n, j\rangle$ is the $g \times g$ perturbation matrix restricted to $\mathcal{H}_n^{(0)}$.

### Why Diagonalization is Necessary: The Consistency Requirement

Consider the first-order equation for the state correction:

$$
(\hat{H}_0 - E_n^{(0)})|n, k^{(1)}\rangle = (E_{n,k}^{(1)} - \hat{V})|n, k^{(0)}\rangle
$$

**Key observation:** The operator $(\hat{H}_0 - E_n^{(0)})$ sends every state in the degenerate subspace to zero:

$$
(\hat{H}_0 - E_n^{(0)})|n, i\rangle = 0 \quad \text{for all } i = 1, \ldots, g
$$

Therefore, the left-hand side has **no component in** $\mathcal{H}_n^{(0)}$. For the equation to hold, the right-hand side must also have no component in $\mathcal{H}_n^{(0)}$.

**The requirement:** We must choose $E_{n,k}^{(1)}$ and $|n, k^{(0)}\rangle$ such that:

$$
\langle n, i|(E_{n,k}^{(1)} - \hat{V})|n, k^{(0)}\rangle = 0 \quad \text{for all } i = 1, \ldots, g
$$

This is exactly the secular equation. The diagonalization is **not an optional simplification**—it is a **consistency requirement** that ensures the right-hand side lies entirely outside the degenerate subspace, making the equation solvable.

### First-Order Results in Degenerate Theory

**Energy splitting:** The eigenvalues $E_{n,k}^{(1)}$ ($k = 1, \ldots, g$) give first-order corrections. Generically, these are distinct, lifting the degeneracy.

**Correct zeroth-order states:** The eigenvectors $\mathbf{c}^{(k)}$ define:

$$
\boxed{|n, k^{(0)}\rangle = \sum_{i=1}^{g} c_i^{(k)}|n, i\rangle}
$$

These states diagonalize $\hat{V}$ within $\mathcal{H}_n^{(0)}$:

$$
\langle n, k^{(0)}|\hat{V}|n, l^{(0)}\rangle = E_{n,k}^{(1)}\delta_{kl}
$$

This off-diagonal vanishing is crucial: it ensures that when we compute first-order state corrections involving states outside $\mathcal{H}_n^{(0)}$, no divergent terms appear from within the degenerate subspace.

### Higher-Order Corrections

Once the degeneracy is lifted at first order (assuming $E_{n,k}^{(1)} \neq E_{n,l}^{(1)}$ for $k \neq l$), standard non-degenerate theory applies to each $|n, k^{(0)}\rangle$. The second-order energy correction is:

$$
\boxed{E_{n,k}^{(2)} = \sum_{m \notin \mathcal{D}_n} \frac{|\langle m^{(0)}|\hat{V}|n, k^{(0)}\rangle|^2}{E_n^{(0)} - E_m^{(0)}}}
$$

where $\mathcal{D}_n$ denotes the degenerate subspace. The sum explicitly excludes states within $\mathcal{H}_n^{(0)}$.

---

### The Apparent Paradox: Subspace Restriction vs. Full Space

A subtle point deserves clarification. First-order energy corrections are obtained by diagonalizing $\hat{V}$ **only within** $\mathcal{H}_n^{(0)}$, yet first-order state corrections involve mixing with states **outside** $\mathcal{H}_n^{(0)}$. This seemingly asymmetric treatment requires explanation.

**The key insight: two distinct problems are being solved sequentially**

**Step 1: Identify the correct zeroth-order states**

Before perturbation, any superposition in $\mathcal{H}_n^{(0)}$ is valid. The perturbation $\hat{V}$ selects specific combinations—these are the states that will evolve continuously as $\lambda$ increases from zero. To find them, we solve the eigenvalue problem **within the degenerate subspace only**.

Write the correct zeroth-order state as a superposition of the original basis states:

$$
\vert n, k^{(0)}\rangle = c_1^{(k)}\vert n, 1\rangle + c_2^{(k)}\vert n, 2\rangle + \cdots + c_g^{(k)}\vert n, g\rangle = \sum_{i=1}^{g} c_i^{(k)}\vert n, i\rangle
$$

The secular equation requires that for each basis state $\vert n, i\rangle$:

$$
\sum_{j=1}^{g} \langle n, i\vert\hat{V}\vert n, j\rangle c_j^{(k)} = E_{n,k}^{(1)} c_i^{(k)}
$$

This is a system of $g$ linear equations. In matrix form:

$$
\begin{pmatrix} 
V_{11} & V_{12} & \cdots & V_{1g} \\
V_{21} & V_{22} & \cdots & V_{2g} \\
\vdots & \vdots & \ddots & \vdots \\
V_{g1} & V_{g2} & \cdots & V_{gg}
\end{pmatrix}
\begin{pmatrix} c_1^{(k)} \\ c_2^{(k)} \\ \vdots \\ c_g^{(k)} \end{pmatrix}
= E_{n,k}^{(1)} 
\begin{pmatrix} c_1^{(k)} \\ c_2^{(k)} \\ \vdots \\ c_g^{(k)} \end{pmatrix}
$$

**What this equation is actually doing:**

The matrix element $V_{ij} = \langle n, i\vert\hat{V}\vert n, j\rangle$ tells us how much the perturbation couples basis states $\vert n, i\rangle$ and $\vert n, j\rangle$. If we start with an arbitrary superposition, $\hat{V}$ will tend to mix the components. The eigenvalue problem finds those **special superpositions** where the state is "stable" under the action of $\hat{V}$—meaning $\hat{V}$ acting on the state just returns the same state scaled by $E_{n,k}^{(1)}$.

**Why only within $\mathcal{H}_n^{(0)}$?** Because we are not yet asking how the state changes due to mixing with outside states; we are asking which starting point within the degenerate manifold is the "right" one. States outside have $E_m^{(0)} \neq E_n^{(0)}$, so they cannot be degenerate with our level and do not participate in this selection process.

**Step 2: Calculate corrections to these selected states**

Once the correct zeroth-order states $|n, k^{(0)}\rangle$ are identified (with distinct $E_{n,k}^{(1)}$), we treat each as the starting point for standard perturbation theory. Now the first-order state correction involves the full Hilbert space:

$$
|n, k^{(1)}\rangle = \sum_{m \notin \mathcal{D}_n} \frac{\langle m^{(0)}|\hat{V}|n, k^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}|m^{(0)}\rangle
$$

Note the sum excludes $\mathcal{D}_n$ because after diagonalization, $\langle m^{(0)}|\hat{V}|n, k^{(0)}\rangle = 0$ for $m^{(0)} \in \mathcal{D}_n$ with $m \neq k$. The degenerate states are "orthogonal" under $\hat{V}$.

**Why the asymmetry is natural:**

| Stage | Scope | Physical meaning |
|-------|-------|------------------|
| Finding correct zeroth-order states | $\mathcal{H}_n^{(0)}$ only | Breaking the degeneracy; selecting eigenbasis of residual symmetry |
| Computing first-order state corrections | Full space minus $\mathcal{D}_n$ | Admixture of non-degenerate states; standard perturbation theory |

**Notation note:** $\vert m^{(0)}\rangle \in \mathcal{D}_n$ denotes states in the degenerate subspace.

The energy correction appears "local" because it answers: *which state in the degenerate manifold am I following?* The state correction is "global" because it answers: *how much does this state mix with everything else?*

---

### The Secular Equation: Origin of the Name

The eigenvalue equation $\mathbf{V}^{(n)}\mathbf{c} = E^{(1)}\mathbf{c}$ is historically called the **secular equation** (Latin *saeculum* = generation/century, Greek *αιών* = long period). In celestial mechanics, this term refers to equations describing **slow, long-term evolution** of orbital elements (as opposed to rapid periodic variations).

In quantum perturbation theory, the first-order energy splitting $E_{n,k}^{(1)}$ is the "secular" effect. It represents a slow drift in energy, in contrast to the rapid oscillations associated with transitions between distinct unperturbed levels. These oscillations have frequency $(E_n^{(0)} - E_m^{(0)})/\hbar$ for $m \notin \mathcal{D}_n$, which is large compared to the splitting scale. The secular equation captures the slow evolution within the degenerate manifold, while non-degenerate perturbation theory describes fast oscillatory mixing with outside states.

The matrix $\mathbf{V}^{(n)}$ is sometimes called the **secular matrix**.

---

### When Degenerate Theory Reduces to Non-Degenerate

Degenerate perturbation theory subsumes the non-degenerate case as a limit. This occurs when the perturbation matrix in the degenerate subspace is **already diagonal**:

$$
\mathbf{V}^{(n)} = \begin{pmatrix} V_{11} & 0 & \cdots & 0 \\ 0 & V_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & V_{gg} \end{pmatrix}
$$

**Consequences:**

1. **Original basis is already "correct":** The basis states $|n, i\rangle$ are eigenstates of $\mathbf{V}^{(n)}$
2. **First-order energies:** $E_{n,i}^{(1)} = V_{ii} = \langle n, i|\hat{V}|n, i\rangle$ (identical to non-degenerate formula)
3. **No diagonalization required:** The secular equation is trivially satisfied

**Physical interpretation:** When $\mathbf{V}^{(n)}$ is diagonal, the perturbation does not mix the degenerate states at first order. Each $|n, i\rangle$ evolves independently with its own energy shift $V_{ii}$, precisely as in non-degenerate theory. The degeneracy is still lifted (unless $V_{ii} = V_{jj}$ for some $i \neq j$), but the lifting occurs without inducing transitions within the subspace.

**Example:** A magnetic field applied to hydrogen $n=2$ states. The field couples to $L_z$ and $S_z$, which are diagonal in the $|n, l, m_l, m_s\rangle$ basis. First-order Zeeman splitting is obtained without diagonalizing any matrix—the basis states are already the "good" states.

**Mathematical equivalence:** If we formally treat each degenerate state as non-degenerate and apply standard formulas, we obtain the same result because:
- $E_{n,i}^{(1)} = \langle n, i|\hat{V}|n, i\rangle$ (matches diagonal element)
- The problematic denominator $(E_n^{(0)} - E_n^{(0)})^{-1}$ never appears because we never sum over other degenerate states

This validates that degenerate perturbation theory is the **general framework**, with non-degenerate theory emerging when the degenerate subspace structure is trivial.

---

## Part III: Structural Comparison

| Aspect | Non-Degenerate | Degenerate |
|--------|---------------|------------|
| Zeroth-order state | Unique $\vert n^{(0)}\rangle$ | Superposition in $\mathcal{H}_n^{(0)}$ (determined by $\hat{V}$) |
| First-order energy | $V_{nn}$ (single value) | Eigenvalues of $\mathbf{V}^{(n)}$ (generically $g$ distinct values) |
| Key operation | Direct expansion | Diagonalize $\hat{V}$ in $\mathcal{H}_n^{(0)}$ first |
| State correction | Sum over all $m \neq n$ | Sum excludes degenerate subspace |
| Consistency condition | Automatic | Requires secular equation solvability |

### Physical Interpretation

**Non-degenerate case:** The system adiabatically follows a unique eigenstate. Perturbation theory tracks continuous deformation of an isolated level.

**Degenerate case:** The perturbation acts as a **symmetry-breaking operator** within the degenerate subspace, selecting specific linear combinations. The diagonalization finds the eigenbasis of the residual symmetry.

---

## Part IV: Example — Stark Effect in Hydrogen

### Ground State ($n=1$, Non-Degenerate)

$|100\rangle$ is non-degenerate. First-order correction:

$$
E_1^{(1)} = \langle 100|e\mathcal{E}z|100\rangle = 0 \quad \text{(parity selection rule)}
$$

Second order:

$$
E_1^{(2)} = \sum_{n=2}^{\infty}\sum_{l,m}\frac{|\langle nlm|e\mathcal{E}z|100\rangle|^2}{E_1^{(0)} - E_n^{(0)}} = -\frac{9}{4}a_0^3\mathcal{E}^2
$$

Quadratic Stark effect (energy shifts downward, induced dipole aligns with field).

### $n=2$ Level (4-Fold Degenerate)

Basis: $|200\rangle$, $|210\rangle$, $|211\rangle$, $|21,-1\rangle$.

Selection rule: $z = r\cos\theta$ connects $\Delta l = \pm 1$, $\Delta m = 0$.

Perturbation matrix in this basis:

$$
\mathbf{V} = e\mathcal{E}\begin{pmatrix}
0 & \langle 200|z|210\rangle & 0 & 0 \\
\langle 210|z|200\rangle & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix} = -3e\mathcal{E}a_0\begin{pmatrix}
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Diagonalizing the $2 \times 2$ block: eigenvalues $\pm 3e\mathcal{E}a_0$ with eigenstates $(|200\rangle \mp |210\rangle)/\sqrt{2}$.

**First-order splitting:**

$$
E_{2\pm}^{(1)} = \pm 3e\mathcal{E}a_0, \quad E_{2,|m|=1}^{(1)} = 0 \text{ (doubly degenerate)}
$$

Linear Stark effect—characteristic signature of degenerate perturbation theory. The perturbation lifts the $l$-degeneracy (but not $m$-degeneracy, due to residual symmetry).

---

## References

1. Sakurai, J.J. & Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. (Cambridge University Press, 2020). §5.1–5.3

2. Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. (Springer, 1994). Chapter 17

3. Landau, L.D. & Lifshitz, E.M. *Quantum Mechanics: Non-Relativistic Theory*, 3rd ed. (Pergamon, 1977). §38–39
