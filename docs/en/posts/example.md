# Example: Formulas and Code

---

date: 2024-01-15
tags:
  - tutorial
  - vitepress
  - latex
categories:
  - tech-notes

---

This is an example article demonstrating various supported features, including mathematical formulas, code highlighting, and tables. These features are perfect for writing research notes and technical documentation.

## 🧮 Mathematical Formulas

### Inline Formulas

Einstein's famous mass-energy equivalence: $E = mc^2$, which reveals the equivalence of mass and energy.

In condensed matter physics, we often use the Schrödinger equation: $i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi$ to describe quantum system evolution.

### Display Formulas

**Gaussian Integral**:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

**Euler's Formula** (often called the most beautiful formula in mathematics):

$$
e^{i\pi} + 1 = 0
$$

### Complex Formula Examples

**BCS Gap Equation**:

$$
\Delta_k = -\sum_{k'} V_{kk'} \frac{\Delta_{k'}}{2E_{k'}} \tanh\left(\frac{E_{k'}}{2k_B T}\right)
$$

where $E_k = \sqrt{\xi_k^2 + \Delta_k^2}$ is the quasiparticle excitation energy.

**Green's Function (Matsubara frequency representation)**:

$$
G(\mathbf{r}, \mathbf{r}', i\omega_n) = \sum_{\alpha} \frac{\psi_{\alpha}(\mathbf{r}) \psi_{\alpha}^*(\mathbf{r}')}{i\omega_n - \epsilon_{\alpha}}
$$

### Matrices and Vectors

**Pauli Matrices**:

$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

**Dirac Equation**:

$$
(i\gamma^\mu \partial_\mu - m)\psi = 0
$$

## 💻 Code Highlighting

### Python Example: Numerical Computing

```python
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

def calculate_band_structure(H_k):
    """
    Calculate band structure
    
    Parameters:
    -----------
    H_k : ndarray
        Hamiltonian in momentum space, shape (N_k, N_bands, N_bands)
    
    Returns:
    --------
    energies : ndarray
        Eigenenergies, shape (N_k, N_bands)
    """
    N_k, N_bands, _ = H_k.shape
    energies = np.zeros((N_k, N_bands))
    
    for i, H in enumerate(H_k):
        # Diagonalize Hamiltonian
        eigvals = linalg.eigvalsh(H)
        energies[i] = eigvals
    
    return energies

# Generate sample data
k_points = np.linspace(-np.pi, np.pi, 100)
H_k = np.array([[np.cos(k), np.sin(k)], 
                [np.sin(k), -np.cos(k)]] for k in k_points)

energies = calculate_band_structure(H_k)

# Plot bands
plt.figure(figsize=(8, 6))
plt.plot(k_points, energies[:, 0], 'b-', label='Band 1')
plt.plot(k_points, energies[:, 1], 'r-', label='Band 2')
plt.xlabel('k')
plt.ylabel('Energy')
plt.legend()
plt.grid(True)
plt.show()
```

### Julia Example: High-Performance Computing

```julia
using LinearAlgebra
using Plots

"""
Calculate topological invariant (Chern number)
"""
function chern_number(H::Function, N::Int=100)
    # Define Brillouin zone grid
    kx = range(-π, π, length=N)
    ky = range(-π, π, length=N)
    
    F = zeros(ComplexF64, N, N)  # Berry curvature
    
    for i in 1:N, j in 1:N
        # Calculate Berry curvature
        k = [kx[i], ky[j]]
        H_matrix = H(k)
        
        # Diagonalize
        eigenvalues, eigenvectors = eigen(Hermitian(H_matrix))
        u = eigenvectors[:, 1]  # Occupied state wavefunction
        
        # Calculate Berry connection and curvature (simplified example)
        F[i,j] = compute_berry_curvature(H, k, N)
    end
    
    # Chern number = (1/2π) ∫ F dk_x dk_y
    C = sum(real(F)) * (2π/N)^2 / (2π)
    return round(Int, real(C))
end

# Haldane model example
function haldane_hamiltonian(k::Vector{Float64}; t=1.0, t2=0.1, M=0.5)
    kx, ky = k
    
    # Nearest-neighbor hopping
    d1 = 2t * cos(kx) + 4t2 * cos(kx/2) * cos(sqrt(3)*ky/2)
    d2 = 2t * sin(kx) - 4t2 * sin(kx/2) * cos(sqrt(3)*ky/2)
    d3 = M - 4t2 * sin(sqrt(3)*ky/2) * sin(kx/2)
    
    # Pauli matrix expansion
    H = d1 * [0 1; 1 0] + d2 * [0 -im; im 0] + d3 * [1 0; 0 -1]
    return H
end

# Calculate Chern number
C = chern_number(k -> haldane_hamiltonian(k, M=0.5))
println("Chern number = $C")  # Should output 1
```

## 📊 Tables

### Comparison of Common Numerical Methods

| Method | Applicable Systems | Accuracy | Computational Complexity | Main Applications |
|--------|-------------------|----------|------------------------|------------------|
| Exact Diagonalization | Small systems | Exact | $O(N^3)$ | Ground state properties, correlation functions |
| DMRG | 1D systems | High accuracy | $O(m^3)$ | Strongly correlated systems |
| Quantum Monte Carlo | Sign-problem-free systems | Statistical error | $O(N)$ | Finite temperature properties |
| Tensor Networks | Low-dimensional systems | Controllable | Variable | Dynamics, thermodynamics |
| Neural Quantum States | Various systems | Network-dependent | High | Many-body wavefunction representation |

### Physical Constants Table

| Constant | Symbol | Value | Unit |
|----------|--------|-------|------|
| Planck constant | $h$ | $6.626 \times 10^{-34}$ | J·s |
| Reduced Planck constant | $\hbar$ | $1.055 \times 10^{-34}$ | J·s |
| Boltzmann constant | $k_B$ | $1.381 \times 10^{-23}$ | J/K |
| Electron charge | $e$ | $1.602 \times 10^{-19}$ | C |
| Electron mass | $m_e$ | $9.109 \times 10^{-31}$ | kg |

## 📝 Other Markdown Features

### Blockquotes

> Quantum mechanics does not say that the world is divided into observers and observed. Observers and observed are part of the same world.
> 
> — Hugh Everett

### Lists

Basic steps in research work:

1. **Literature Review**
   - Understand current state of the field
   - Identify research questions
   - Find suitable methods

2. **Theoretical Derivation**
   - Establish mathematical models
   - Perform analytical calculations
   - Verify special cases

3. **Numerical Simulation**
   - Write computational code
   - Test code correctness
   - Run large-scale computations

4. **Results Analysis**
   - Data visualization
   - Physical picture construction
   - Write research reports

### Task Lists

- [x] Complete theoretical derivation
- [x] Write numerical code
- [x] Run test cases
- [ ] Large-scale computation
- [ ] Results visualization
- [ ] Write paper

## 🎨 Images

You can easily insert images:

```markdown
![Description](/images/your-image.png)
```

Images will be automatically centered with shadow effects.

## 🔗 Links

- External link: [VitePress Documentation](https://vitepress.dev)
- Internal link: [About Me](/en/about)
- Literature citation: [[1]](#references)

---

## 📚 References

1. Kohn, W. & Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. *Phys. Rev.* **140**, A1133 (1965).

2. Thouless, D. J., Kohmoto, M., Nightingale, M. P. & den Nijs, M. Quantized Hall Conductance in a Two-Dimensional Periodic Potential. *Phys. Rev. Lett.* **49**, 405 (1982).

3. White, S. R. Density matrix formulation for quantum renormalization groups. *Phys. Rev. Lett.* **69**, 2863 (1992).
