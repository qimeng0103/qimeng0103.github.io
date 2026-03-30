# Stationary Perturbation Theory: Non-Degenerate vs Degenerate Cases

---

date: 2026-03-30
tags:
  - Quantum Mechanics
  - Perturbation Theory
categories:
  - Quantum Mechanics Notes

---

## Introduction

Stationary perturbation theory is one of the most powerful approximation methods in quantum mechanics. When the Hamiltonian of a system can be written as

$$
\hat{H} = \hat{H}_0 + \lambda \hat{V}
$$

where $\hat{H}_0$ is exactly solvable and $\lambda \hat{V}$ is a small perturbation, we can systematically calculate corrections to the energy eigenvalues and eigenstates.

The crucial distinction arises when considering whether the unperturbed energy level is **non-degenerate** or **degenerate**. This distinction fundamentally changes the mathematical structure of the perturbation expansion.

---

## Part I: Non-Degenerate Perturbation Theory

### Setup

For a non-degenerate level $|n^{(0)}\rangle$ with energy $E_n^{(0)}$:

$$
\hat{H}_0 |n^{(0)}\rangle = E_n^{(0)} |n^{(0)}\rangle
$$

We expand both energy and state in powers of $\lambda$:

$$
E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \lambda^3 E_n^{(3)} + \cdots
$$

$$
|n\rangle = |n^{(0)}\rangle + \lambda |n^{(1)}\rangle + \lambda^2 |n^{(2)}\rangle + \cdots
$$

with the intermediate normalization $\langle n^{(0)} | n \rangle = 1$.

### Zeroth-Order

$$E_n^{(0)}, \quad |n^{(0)}\rangle$$

These are the known solutions of the unperturbed Hamiltonian.

### First-Order Corrections

**Energy correction:**

$$
E_n^{(1)} = \langle n^{(0)} | \hat{V} | n^{(0)} \rangle = V_{nn}
$$

**State correction:**

Expanding in the basis of unperturbed states:

$$
|n^{(1)}\rangle = \sum_{m \neq n} c_m^{(1)} |m^{(0)}\rangle
$$

The coefficients are:

$$
c_m^{(1)} = \frac{\langle m^{(0)} | \hat{V} | n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} = \frac{V_{mn}}{E_n^{(0)} - E_m^{(0)}}
$$

Thus:

$$
|n^{(1)}\rangle = \sum_{m \neq n} \frac{V_{mn}}{E_n^{(0)} - E_m^{(0)}} |m^{(0)}\rangle
$$

### Second-Order Corrections

**Energy correction:**

$$
E_n^{(2)} = \langle n^{(0)} | \hat{V} | n^{(1)} \rangle = \sum_{m \neq n} \frac{|V_{mn}|^2}{E_n^{(0)} - E_m^{(0)}}
$$

This can also be written as:

$$
E_n^{(2)} = \sum_{m \neq n} \frac{|\langle m^{(0)} | \hat{V} | n^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}
$$

**State correction:**

$$
|n^{(2)}\rangle = \sum_{m \neq n} \left[ \sum_{k \neq n} \frac{V_{mk} V_{kn}}{(E_n^{(0)} - E_m^{(0)})(E_n^{(0)} - E_k^{(0)})} - \frac{V_{mn} V_{nn}}{(E_n^{(0)} - E_m^{(0)})^2} \right] |m^{(0)}\rangle
$$

Or more explicitly:

$$
|n^{(2)}\rangle = \sum_{m \neq n} \left[ \sum_{k \neq n} \frac{V_{mk} V_{kn}}{(E_n^{(0)} - E_m^{(0)})(E_n^{(0)} - E_k^{(0)})} \right] |m^{(0)}\rangle - |n^{(1)}\rangle \langle n^{(0)} | n^{(1)} \rangle
$$

where the second term ensures proper normalization.

### Third-Order Energy Correction

The third-order energy correction is given by:

$$
E_n^{(3)} = \langle n^{(0)} | \hat{V} | n^{(2)} \rangle = \sum_{m \neq n} \sum_{k \neq n} \frac{V_{nm} V_{mk} V_{kn}}{(E_n^{(0)} - E_m^{(0)})(E_n^{(0)} - E_k^{(0)})} - E_n^{(1)} \sum_{m \neq n} \frac{|V_{mn}|^2}{(E_n^{(0)} - E_m^{(0)})^2}
$$

This can be reorganized as:

$$
E_n^{(3)} = \sum_{m \neq n} \sum_{k \neq n} \frac{V_{nm} V_{mk} V_{kn}}{(E_n^{(0)} - E_m^{(0)})(E_n^{(0)} - E_k^{(0)})} - V_{nn} \sum_{m \neq n} \frac{|V_{mn}|^2}{(E_n^{(0)} - E_m^{(0)})^2}
$$

An alternative compact form:

$$
E_n^{(3)} = \sum_{m \neq n} \sum_{k \neq n} \frac{V_{nm} V_{mk} V_{kn}}{(E_n^{(0)} - E_m^{(0)})(E_n^{(0)} - E_k^{(0)})} - E_n^{(1)} \sum_{m \neq n} \frac{|V_{mn}|^2}{(E_n^{(0)} - E_m^{(0)})^2}
$$

### Summary for Non-Degenerate Case

**Energy up to third order:**

$$
\boxed{E_n \approx E_n^{(0)} + V_{nn} + \sum_{m \neq n} \frac{|V_{mn}|^2}{E_n^{(0)} - E_m^{(0)}} + E_n^{(3)}}
$$

**State up to second order:**

$$
\boxed{|n\rangle \approx |n^{(0)}\rangle + \sum_{m \neq n} \frac{V_{mn}}{E_n^{(0)} - E_m^{(0)}} |m^{(0)}\rangle + |n^{(2)}\rangle}
$$

where the denominators $(E_n^{(0)} - E_m^{(0)})^{-1}$ indicate the critical role of energy level spacing.

---

## Part II: Degenerate Perturbation Theory

### The Problem

When the unperturbed energy level $E_n^{(0)}$ is $g$-fold degenerate:

$$
\hat{H}_0 |n, i\rangle = E_n^{(0)} |n, i\rangle, \quad i = 1, 2, \ldots, g
$$

the standard non-degenerate perturbation theory **fails** because the denominators $(E_n^{(0)} - E_m^{(0)})$ vanish for states within the degenerate subspace.

### The Resolution

The key insight is that the perturbation $\hat{V}$ generally **lifts the degeneracy**. The correct zeroth-order states are not arbitrary linear combinations, but specific superpositions diagonalizing $\hat{V}$ within the degenerate subspace.

### Step 1: Construct the Perturbation Matrix

Define the $g \times g$ matrix:

$$
V_{ij} = \langle n, i | \hat{V} | n, j \rangle
$$

### Step 2: Diagonalize the Perturbation Matrix

Solve the eigenvalue problem within the degenerate subspace:

$$
\sum_{j=1}^{g} V_{ij} c_j^{(k)} = E_n^{(1,k)} c_i^{(k)}
$$

The eigenvalues $E_n^{(1,k)}$ ($k = 1, 2, \ldots, g$) give the **first-order energy corrections**, which typically split the degenerate level.

### Step 3: Determine the Correct Zeroth-Order States

The eigenvectors define the "good" zeroth-order states:

$$
|n, k^{(0)}\rangle = \sum_{i=1}^{g} c_i^{(k)} |n, i\rangle
$$

These states are now uniquely determined (up to phase) and diagonalize $\hat{V}$:

$$
\langle n, k^{(0)} | \hat{V} | n, l^{(0)} \rangle = E_n^{(1,k)} \delta_{kl}
$$

### Higher-Order Corrections in Degenerate Case

Once the degeneracy is lifted at first order, we can apply standard non-degenerate perturbation theory to each new level, provided that:

$$
E_n^{(1,k)} \neq E_n^{(1,l)} \quad \text{for} \quad k \neq l
$$

The second-order energy correction becomes:

$$
E_n^{(2,k)} = \sum_{m \notin D} \frac{|\langle m^{(0)} | \hat{V} | n, k^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}
$$

where the sum excludes all states $m$ in the degenerate subspace $D$.

### Summary for Degenerate Case

**First-order energy splitting:**

$$
\boxed{E_{n,k} \approx E_n^{(0)} + E_n^{(1,k)}}
$$

where $E_n^{(1,k)}$ are eigenvalues of the perturbation matrix $V_{ij}$.

**Correct zeroth-order states:**

$$
\boxed{|n, k^{(0)}\rangle = \sum_{i=1}^{g} c_i^{(k)} |n, i\rangle}
$$

where $c_i^{(k)}$ are eigenvectors of $V_{ij}$.

---

## Part III: Key Differences and Physical Interpretation

### Mathematical Structure

| Aspect | Non-Degenerate | Degenerate |
|--------|---------------|------------|
| Zeroth-order state | Unique $\vert n^{(0)}\rangle$ | Arbitrary superposition within subspace |
| First-order energy | $V_{nn}$ | Eigenvalues of $V_{ij}$ matrix |
| State correction | Simple sum over $m \neq n$ | Requires diagonalization first |
| Convergence | Power series in $\lambda$ | May require resummation if degeneracy not fully lifted |

### Physical Interpretation

**Non-degenerate case:** The perturbation slightly modifies an isolated energy level. The system adiabatically follows a unique eigenstate.

**Degenerate case:** The perturbation selects specific linear combinations that respect the symmetry of $\hat{V}$. This is closely related to the concept of "symmetry breaking."

### When Degenerate Theory is Necessary

Even if the unperturbed levels are non-degenerate, degenerate perturbation theory becomes relevant when:

1. Two levels become nearly degenerate: $|E_n^{(0)} - E_m^{(0)}| \lesssim |V_{mn}|$
2. The perturbation has a degenerate subspace (e.g., spin degeneracy)

In such cases, one should first diagonalize $\hat{V}$ in the nearly degenerate subspace.

---

## Part IV: Example - Stark Effect in Hydrogen

### Non-Degenerate Case: Ground State

For hydrogen ground state $|100\rangle$ with energy $E_1^{(0)}$:

$$
E_1^{(1)} = \langle 100 | e\mathcal{E}z | 100 \rangle = 0 \quad \text{(by parity)}
$$

Second-order Stark effect:

$$
E_1^{(2)} = \sum_{n=2}^{\infty} \frac{|\langle n00 | e\mathcal{E}z | 100 \rangle|^2}{E_1^{(0)} - E_n^{(0)}}
$$

### Degenerate Case: n=2 Level

The $n=2$ level has 4-fold degeneracy: $|200\rangle$, $|210\rangle$, $|211\rangle$, $|21,-1\rangle$.

The perturbation matrix in the basis $\{|200\rangle, |210\rangle, |211\rangle, |21,-1\rangle\}$:

$$
V = e\mathcal{E} \begin{pmatrix}
0 & \langle 200 | z | 210 \rangle & 0 & 0 \\
\langle 210 | z | 200 \rangle & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Since $z = r\cos\theta$ only connects $l=0$ and $l=1$, $m=0$ states:

$$
\langle 200 | z | 210 \rangle = -3a_0
$$

Diagonalizing the $2 \times 2$ block:

Eigenvalues: $\pm 3e\mathcal{E}a_0$

The linear Stark splitting demonstrates the power of degenerate perturbation theory.

---

## References

1. Sakurai, J.J. & Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. (Cambridge University Press, 2020).

2. Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. (Springer, 1994).

3. Landau, L.D. & Lifshitz, E.M. *Quantum Mechanics: Non-Relativistic Theory*, 3rd ed. (Pergamon, 1977).
