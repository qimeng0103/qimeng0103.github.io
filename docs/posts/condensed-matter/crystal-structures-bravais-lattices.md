# Crystal Structures: From Bravais Lattices to Reciprocal Space

📅 **Date:** 2026-04-04 | 🏷️ **Tags:** Condensed Matter, Crystallography, Solid State Physics | 📂 **Category:** Condensed Matter Notes

---

## Introduction

The crystalline state represents one of the most fundamental manifestations of matter in the solid phase. In this comprehensive treatment, we develop the theoretical framework for describing periodic structures in solids, from the definition of crystal lattices and the classification of Bravais lattices to the construction of reciprocal space and the Brillouin zone. Every definition and derivation is presented with complete mathematical rigor.

---

## Part I: Crystal Structure and Bravais Lattices

### The Nature of Crystallization

At sufficiently low temperatures, matter typically adopts a crystalline state characterized by periodic arrangements of atoms or molecular building blocks. This phenomenon arises from fundamental thermodynamic and quantum mechanical principles:

**Physical basis for crystallization:**

1. **Energy minimization:** A system of interacting particles seeks the equilibrium configuration corresponding to the absolute minimum of the interaction potential
2. **Translational symmetry:** For macroscopically large systems of identical building blocks, periodic arrangements emerge naturally because each building block experiences an identical environment
3. **Entropy considerations:** At low temperatures, the ordered state with greater symmetry (lower entropy) becomes thermodynamically favorable

There exist also non-crystalline solids (amorphous semiconductors, glasses, polymers, metallic glasses), which retain short-range order but lack long-range periodicity. These systems typically occupy local energy minima from which they cannot escape at low temperatures due to thermally insurmountable potential barriers.

### Defining Crystal Lattices

**Definition:** A crystal lattice consists of lattice points in space described by position vectors $\mathbf{R}_n$ that can be expressed as integer linear combinations of $d$ linearly independent basis vectors in $d$ dimensions:

$$
\mathbf{R}_n = \sum_{i=1}^{d} n_i \mathbf{a}_i
$$

where $\mathbf{n} = (n_1, \ldots, n_d)$ denotes a $d$-tuple of integers, and the basis vectors $\mathbf{a}_i$ span the **unit cell** whose periodic continuation fills all space.

**Properties of basis vectors:**
- The basis vectors need not be orthogonal to each other
- The angles between them are denoted by $\alpha_i$
- The volume of the unit cell is given by:
  - For $d=2$: $V_{\text{cell}} = |\mathbf{a}_1 \times \mathbf{a}_2|$
  - For $d=3$: $V_{\text{cell}} = |\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)|$

**Primitive unit cell:** The smallest possible unit cell whose periodic repetition fills space.

### Crystal Systems in Two Dimensions

For $d=2$, there exist **4 crystal systems** determined by symmetry constraints:

| Crystal System | Conditions | Symmetry Properties |
|---------------|------------|-------------------|
| **Square** | $a_1 = a_2$, $\alpha_1 = 90°$ | 4-fold rotational symmetry, reflection at 2 axes, inversion |
| **Rectangular** | $a_1 \neq a_2$, $\alpha_1 = 90°$ | Reflection at 2 axes, inversion |
| **Hexagonal (Triangular)** | $a_1 = a_2$, $\alpha_1 = 60°$ | 6-fold rotational symmetry, reflections at 3 axes, inversion |
| **Oblique** | $a_1 \neq a_2$, $\alpha_1 \neq 90°$ | Inversion only |

**Fundamental constraint:** In both $d=2$ and $d=3$, crystal lattices can only exhibit 2-, 3-, 4-, or 6-fold rotational symmetry. This is a mathematical necessity for space-filling periodic structures.

### Crystal Systems in Three Dimensions

For $d=3$, there are **7 crystal systems** and **14 Bravais lattices**:

**1. Cubic System** ($a_1 = a_2 = a_3 = a$, $\alpha_1 = \alpha_2 = \alpha_3 = 90°$)
- 3 Bravais lattices: simple cubic (sc), face-centered cubic (fcc), body-centered cubic (bcc)

**Primitive vectors for cubic lattices:**

*Simple cubic (sc):*
$$
\mathbf{a}_1 = a\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad
\mathbf{a}_2 = a\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad
\mathbf{a}_3 = a\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
$$
$$V_{\text{cell}} = a^3$$

*Face-centered cubic (fcc):*
$$
\mathbf{a}_1 = \frac{a}{2}\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad
\mathbf{a}_2 = \frac{a}{2}\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \quad
\mathbf{a}_3 = \frac{a}{2}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}
$$
$$V_{\text{cell}} = \frac{a^3}{4}$$

The factor of 4 arises because there are effectively 4 lattice points per conventional cubic cell: 8 corners (each shared by 8 cells) contribute $8 \times \frac{1}{8} = 1$ point, and 6 face centers (each shared by 2 cells) contribute $6 \times \frac{1}{2} = 3$ points.

*Body-centered cubic (bcc):*
$$
\mathbf{a}_1 = \frac{a}{2}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \quad
\mathbf{a}_2 = \frac{a}{2}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \quad
\mathbf{a}_3 = \frac{a}{2}\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}
$$
$$V_{\text{cell}} = \frac{a^3}{2}$$

There are 2 lattice points per conventional cell: 1 center point plus 8 corners at $\frac{1}{8}$ weight each.

**2. Other Crystal Systems:**

| System | Unit Cell Properties | Bravais Lattices |
|--------|---------------------|------------------|
| **Tetragonal** | $a_1 = a_2 \neq a_3$, all $\alpha = 90°$ | Simple, body-centered |
| **Orthorhombic** | $a_1 \neq a_2 \neq a_3$, all $\alpha = 90°$ | Simple, base-centered, body-centered, face-centered |
| **Monoclinic** | $a_1 \neq a_2 \neq a_3$, $\alpha_1 = \alpha_3 = 90° \neq \alpha_2$ | Simple, base-centered |
| **Rhombohedral** | $a_1 = a_2 = a_3$, $\alpha_1 = \alpha_2 = \alpha_3 \neq 90°$ | 1 lattice |
| **Hexagonal** | $a_1 = a_2 \neq a_3$, $\alpha_1 = \alpha_2 = 90°$, $\alpha_3 = 120°$ | 1 lattice |
| **Triclinic** | All $a_i$ unequal, all $\alpha_i \neq 90°$ | 1 lattice |

### Symmetry Groups

**Point group:** The set of discrete symmetry operations (rotations, reflections, inversion) that transform the lattice into itself while keeping a point fixed. Each crystal system has a characteristic point group.

**Space group:** All symmetry operations including lattice translations and combinations of point group operations with translations.

**Example — Cubic symmetry group $O_h$:**
- 3 fourfold rotation axes (through cube face centers): rotations by $90° = 2\pi/4$
- 4 threefold rotation axes (space diagonals): rotations by $120° = 2\pi/3$
- 6 twofold rotation axes (through opposite edge midpoints): rotations by $180° = \pi$
- These 24 operations form the **octahedral group O**
- Including inversion: 48 elements total in $O_h$

---

## Part II: The Wigner-Seitz Cell

### Definition and Construction

**Definition:** The Wigner-Seitz cell centered around a lattice point is the set of all points in space whose distance to this lattice point is smaller than to any other lattice point.

**Geometric construction procedure:**

1. Draw connecting lines from the reference lattice point to all other lattice points
2. Construct the perpendicular bisector planes to each of these connecting lines
3. The Wigner-Seitz cell is the smallest volume enclosed by these bisecting planes

**Properties:**
- The Wigner-Seitz cell has the same volume as the primitive unit cell
- For simple cubic: Wigner-Seitz cell is a cube
- For fcc: Wigner-Seitz cell is a rhombic dodecahedron (12 faces)
- For bcc: Wigner-Seitz cell is a truncated octahedron (14 faces: 8 from nearest neighbors, 6 from next-nearest neighbors)

---

## Part III: Reciprocal Lattice and Brillouin Zone

### Motivation and Definition

In periodic systems, wavevectors satisfying Bragg reflection conditions play a special role. To identify these wavevectors systematically, we introduce the **reciprocal lattice**.

**Definition:** The reciprocal lattice vectors $\mathbf{Q}$ are defined by the condition:

$$
e^{i\mathbf{Q} \cdot \mathbf{R}} = 1 \quad \text{for all direct lattice vectors } \mathbf{R}
$$

Equivalently:

$$
\mathbf{Q} \cdot \mathbf{R} = 2\pi N \quad \text{where } N \in \mathbb{Z}
$$

### Derivation of Reciprocal Lattice Vectors

Given primitive vectors $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ of the direct lattice, the reciprocal lattice primitive vectors are:

$$
\mathbf{q}_1 = 2\pi \frac{\mathbf{a}_2 \times \mathbf{a}_3}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
$$

$$
\mathbf{q}_2 = 2\pi \frac{\mathbf{a}_3 \times \mathbf{a}_1}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
$$

$$
\mathbf{q}_3 = 2\pi \frac{\mathbf{a}_1 \times \mathbf{a}_2}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}
$$

**Verification of orthogonality relation:**

The construction ensures:

$$
\mathbf{a}_i \cdot \mathbf{q}_j = 2\pi \delta_{ij}
$$

**Proof:**

For $i = j = 1$:

$$
\mathbf{a}_1 \cdot \mathbf{q}_1 = 2\pi \frac{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)} = 2\pi
$$

For $i = 1, j = 2$:

$$
\mathbf{a}_1 \cdot \mathbf{q}_2 = 2\pi \frac{\mathbf{a}_1 \cdot (\mathbf{a}_3 \times \mathbf{a}_1)}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)} = 0
$$

since $\mathbf{a}_3 \times \mathbf{a}_1$ is perpendicular to $\mathbf{a}_1$.

**General reciprocal lattice vectors:**

$$
\mathbf{Q} = \nu_1 \mathbf{q}_1 + \nu_2 \mathbf{q}_2 + \nu_3 \mathbf{q}_3, \quad \nu_i \in \mathbb{Z}
$$

Then for any $\mathbf{R} = N_1\mathbf{a}_1 + N_2\mathbf{a}_2 + N_3\mathbf{a}_3$:

$$
\mathbf{Q} \cdot \mathbf{R} = 2\pi(\nu_1 N_1 + \nu_2 N_2 + \nu_3 N_3) = 2\pi N
$$

### Volume Relationship

**Theorem:** The volume of the reciprocal lattice primitive cell is $(2\pi)^3/V_{\text{cell}}$.

**Proof:**

$$
V_{\text{recip}} = |\mathbf{q}_1 \cdot (\mathbf{q}_2 \times \mathbf{q}_3)|
$$

Substituting the expressions for $\mathbf{q}_i$ and using vector identities:

$$
\mathbf{q}_1 \cdot (\mathbf{q}_2 \times \mathbf{q}_3) = \frac{(2\pi)^3}{[\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)]^3} (\mathbf{a}_2 \times \mathbf{a}_3) \cdot [(\mathbf{a}_3 \times \mathbf{a}_1) \times (\mathbf{a}_1 \times \mathbf{a}_2)]
$$

Using the vector identity $(\mathbf{C} \times \mathbf{A}) \times (\mathbf{A} \times \mathbf{B}) = [\mathbf{C} \cdot (\mathbf{A} \times \mathbf{B})] \mathbf{A}$:

$$
(\mathbf{a}_3 \times \mathbf{a}_1) \times (\mathbf{a}_1 \times \mathbf{a}_2) = [\mathbf{a}_3 \cdot (\mathbf{a}_1 \times \mathbf{a}_2)] \mathbf{a}_1 = V_{\text{cell}} \, \mathbf{a}_1
$$

Therefore:

$$
\mathbf{q}_1 \cdot (\mathbf{q}_2 \times \mathbf{q}_3) = \frac{(2\pi)^3}{V_{\text{cell}}^3} (\mathbf{a}_2 \times \mathbf{a}_3) \cdot (V_{\text{cell}} \, \mathbf{a}_1) = \frac{(2\pi)^3}{V_{\text{cell}}^2} [\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)] = \frac{(2\pi)^3}{V_{\text{cell}}}
$$

### Examples of Reciprocal Lattices

**Simple cubic (sc):**

Direct lattice: $\mathbf{a}_1 = a\hat{x}$, $\mathbf{a}_2 = a\hat{y}$, $\mathbf{a}_3 = a\hat{z}$

$$
\mathbf{q}_1 = \frac{2\pi}{a}\hat{x}, \quad \mathbf{q}_2 = \frac{2\pi}{a}\hat{y}, \quad \mathbf{q}_3 = \frac{2\pi}{a}\hat{z}
$$

The reciprocal lattice of sc is also simple cubic with lattice constant $2\pi/a$.

**Face-centered cubic (fcc):**

Using the primitive vectors given earlier:

$$
\mathbf{q}_1 = \frac{2\pi}{a}(-\hat{x} + \hat{y} + \hat{z}), \quad
\mathbf{q}_2 = \frac{2\pi}{a}(\hat{x} - \hat{y} + \hat{z}), \quad
\mathbf{q}_3 = \frac{2\pi}{a}(\hat{x} + \hat{y} - \hat{z})
$$

The reciprocal lattice of fcc is **body-centered cubic (bcc)**.

**Body-centered cubic (bcc):**

The reciprocal lattice of bcc is **face-centered cubic (fcc)**.

### The Brillouin Zone

**Definition:** The **first Brillouin zone** is the Wigner-Seitz cell of the reciprocal lattice.

**Significance:** The first Brillouin zone defines the fundamental domain in reciprocal space ($\mathbf{k}$-space) for describing electronic states and excitations in periodic crystals. Due to periodicity, all physically distinct states can be represented by wavevectors within the first Brillouin zone.

**Construction:** Identify the reciprocal lattice points nearest to the origin, construct the perpendicular bisector planes to the lines connecting the origin to these points, and take the smallest enclosed volume.

---

## Part IV: Crystal Structures with Basis

### The Basis Concept

A complete crystal structure specification requires:
1. The type of Bravais lattice
2. The **basis**: positions of atoms within each primitive cell

The atom positions are given by:

$$
\mathbf{R}_{n\mu} = \mathbf{R}_n + \mathbf{r}_\mu
$$

where $\mathbf{R}_n$ is a lattice vector and $\mathbf{r}_\mu$ gives the position of the $\mu$-th atom within the unit cell.

### Important Crystal Structures

**Sodium Chloride (NaCl) Structure:**
- Bravais lattice: fcc
- Basis: two atoms at $(0, 0, 0)$ and $\frac{1}{2}(\hat{x} + \hat{y} + \hat{z})$
- Lattice constant: $a \approx 5.6$ Å (typical)
- Each ion has 6 nearest neighbors of the opposite type

**Cesium Chloride (CsCl) Structure:**
- Bravais lattice: simple cubic
- Basis: two atoms at $(0, 0, 0)$ and $\frac{1}{2}(\hat{x} + \hat{y} + \hat{z})$
- Lattice constant: $a \approx 4.11$ Å
- Each ion has 8 nearest neighbors

**Diamond Structure:**
- Bravais lattice: fcc
- Basis: two identical atoms at $(0, 0, 0)$ and $\frac{1}{4}(\hat{x} + \hat{y} + \hat{z})$
- 8 atoms per conventional cubic cell
- Each atom has 4 nearest neighbors at distance $\sqrt{3}a/4$ forming a tetrahedron
- Examples: C (diamond), Si, Ge

**Hexagonal Close-Packed (hcp) Structure:**
- Bravais lattice: simple hexagonal
- Basis: two atoms at positions allowing dense packing
- Each atom has 12 nearest neighbors
- Examples: Be, Mg, Zn, Cd, Ti

---

## Summary

| Concept | Definition | Key Formula |
|---------|------------|-------------|
| **Lattice vector** | Integer combination of basis vectors | $\mathbf{R}_n = \sum_i n_i \mathbf{a}_i$ |
| **Primitive cell volume** | $V_{\text{cell}} = |\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)|$ | 3D: triple product |
| **Reciprocal vectors** | Orthogonal to direct lattice | $\mathbf{a}_i \cdot \mathbf{q}_j = 2\pi \delta_{ij}$ |
| **Reciprocal lattice** | Points satisfying $\mathbf{Q} \cdot \mathbf{R} = 2\pi N$ | $\mathbf{Q} = \sum_i \nu_i \mathbf{q}_i$ |
| **Brillouin zone** | Wigner-Seitz cell of reciprocal lattice | Fundamental domain in $\mathbf{k}$-space |

---

## References

1. Ashcroft, N.W. & Mermin, N.D. *Solid State Physics* (Brooks Cole, 1976). Chapter 4-5

2. Kittel, C. *Introduction to Solid State Physics*, 8th ed. (Wiley, 2005). Chapters 1-2

3. Czycholl, G. *Solid State Theory, Volume 1* (Springer, 2023). Chapter 2
