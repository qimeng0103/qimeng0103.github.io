# 示例文章：公式与代码演示

---

date: 2024-01-15
tags:
  - 教程
  - VitePress
  - LaTeX
categories:
  - 技术笔记

---

这是一篇示例文章，展示了博客支持的各种功能，包括数学公式、代码高亮、表格等。这些功能非常适合用来撰写科研笔记和技术文档。

## 🧮 数学公式

### 行内公式

这是爱因斯坦著名的质能方程：$E = mc^2$，它揭示了质量与能量的等价关系。

在凝聚态物理中，我们经常使用薛定谔方程：$i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi$ 来描述量子系统的演化。

### 独立公式

**高斯积分**：

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

**欧拉公式**（被誉为数学中最美的公式）：

$$
e^{i\pi} + 1 = 0
$$

### 复杂公式示例

**BCS 理论中的能隙方程**：

$$
\Delta_k = -\sum_{k'} V_{kk'} \frac{\Delta_{k'}}{2E_{k'}} \tanh\left(\frac{E_{k'}}{2k_B T}\right)
$$

其中 $E_k = \sqrt{\xi_k^2 + \Delta_k^2}$ 是准粒子激发能。

**格林函数（ Matsubara 频率表示）**：

$$
G(\mathbf{r}, \mathbf{r}', i\omega_n) = \sum_{\alpha} \frac{\psi_{\alpha}(\mathbf{r}) \psi_{\alpha}^*(\mathbf{r}')}{i\omega_n - \epsilon_{\alpha}}
$$

### 矩阵和向量

**泡利矩阵**：

$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

**狄拉克方程**：

$$
(i\gamma^\mu \partial_\mu - m)\psi = 0
$$

## 💻 代码高亮

### Python 示例：数值计算

```python
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

def calculate_band_structure(H_k):
    """
    计算能带结构
    
    Parameters:
    -----------
    H_k : ndarray
        动量空间哈密顿量，shape (N_k, N_bands, N_bands)
    
    Returns:
    --------
    energies : ndarray
        本征能量，shape (N_k, N_bands)
    """
    N_k, N_bands, _ = H_k.shape
    energies = np.zeros((N_k, N_bands))
    
    for i, H in enumerate(H_k):
        # 对角化哈密顿量
        eigvals = linalg.eigvalsh(H)
        energies[i] = eigvals
    
    return energies

# 生成示例数据
k_points = np.linspace(-np.pi, np.pi, 100)
H_k = np.array([[np.cos(k), np.sin(k)], 
                [np.sin(k), -np.cos(k)]] for k in k_points)

energies = calculate_band_structure(H_k)

# 绘制能带
plt.figure(figsize=(8, 6))
plt.plot(k_points, energies[:, 0], 'b-', label='Band 1')
plt.plot(k_points, energies[:, 1], 'r-', label='Band 2')
plt.xlabel('k')
plt.ylabel('Energy')
plt.legend()
plt.grid(True)
plt.show()
```

### Julia 示例：高性能计算

```julia
using LinearAlgebra
using Plots

"""
计算拓扑不变量（陈数）
"""
function chern_number(H::Function, N::Int=100)
    # 定义布里渊区网格
    kx = range(-π, π, length=N)
    ky = range(-π, π, length=N)
    
    F = zeros(ComplexF64, N, N)  # Berry 曲率
    
    for i in 1:N, j in 1:N
        # 计算 Berry 曲率
        k = [kx[i], ky[j]]
        H_matrix = H(k)
        
        # 对角化
        eigenvalues, eigenvectors = eigen(Hermitian(H_matrix))
        u = eigenvectors[:, 1]  # 占据态波函数
        
        # 计算 Berry 联络和曲率（简化示例）
        F[i,j] = compute_berry_curvature(H, k, N)
    end
    
    # 陈数 = (1/2π) ∫ F dk_x dk_y
    C = sum(real(F)) * (2π/N)^2 / (2π)
    return round(Int, real(C))
end

# Haldane 模型示例
function haldane_hamiltonian(k::Vector{Float64}; t=1.0, t2=0.1, M=0.5)
    kx, ky = k
    
    # 最近邻跃迁
    d1 = 2t * cos(kx) + 4t2 * cos(kx/2) * cos(sqrt(3)*ky/2)
    d2 = 2t * sin(kx) - 4t2 * sin(kx/2) * cos(sqrt(3)*ky/2)
    d3 = M - 4t2 * sin(sqrt(3)*ky/2) * sin(kx/2)
    
    # 泡利矩阵展开
    H = d1 * [0 1; 1 0] + d2 * [0 -im; im 0] + d3 * [1 0; 0 -1]
    return H
end

# 计算陈数
C = chern_number(k -> haldane_hamiltonian(k, M=0.5))
println("Chern number = $C")  # 应输出 1
```

## 📊 表格展示

### 常见数值方法对比

| 方法 | 适用系统 | 精度 | 计算复杂度 | 主要应用 |
|------|---------|------|-----------|---------|
| 精确对角化 | 小系统 | 精确 | $O(N^3)$ | 基态性质、关联函数 |
| DMRG | 1D 系统 | 高精度 | $O(m^3)$ | 强关联系统 |
| 量子蒙特卡洛 | 无符号问题系统 | 统计误差 | $O(N)$ | 有限温度性质 |
| 张量网络 | 低维系统 | 可控 | 可变 | 动力学、热力学 |
| 神经网络量子态 | 各种系统 | 依赖网络 | 高 | 多体波函数表示 |

### 物理常数表

| 常数 | 符号 | 数值 | 单位 |
|------|------|------|------|
| 普朗克常数 | $h$ | $6.626 \times 10^{-34}$ | J·s |
| 约化普朗克常数 | $\hbar$ | $1.055 \times 10^{-34}$ | J·s |
| 玻尔兹曼常数 | $k_B$ | $1.381 \times 10^{-23}$ | J/K |
| 电子电荷 | $e$ | $1.602 \times 10^{-19}$ | C |
| 电子质量 | $m_e$ | $9.109 \times 10^{-31}$ | kg |

## 📝 其他 Markdown 功能

### 引用块

> 量子力学并没有说世界被分成了观察者和被观察者。观察者和被观察者是同一个世界的一部分。
> 
> —— 休·艾弗雷特 (Hugh Everett)

### 列表情境

研究工作的基本步骤：

1. **文献调研**
   - 了解领域现状
   - 确定研究问题
   - 寻找合适的方法

2. **理论推导**
   - 建立数学模型
   - 进行解析计算
   - 验证特殊情况

3. **数值模拟**
   - 编写计算程序
   - 测试代码正确性
   - 运行大规模计算

4. **结果分析**
   - 数据可视化
   - 物理图像构建
   - 撰写研究报告

### 任务列表

- [x] 完成理论推导
- [x] 编写数值代码
- [x] 运行测试算例
- [ ] 大规模计算
- [ ] 结果可视化
- [ ] 撰写论文

## 🎨 图片展示

你可以轻松插入图片：

```markdown
![图片描述](/images/your-image.png)
```

图片会自动居中显示，并带有阴影效果。

## 🔗 链接

- 外部链接：[VitePress 官方文档](https://vitepress.dev)
- 内部链接：[关于我](/about)
- 文献引用：[[1]](#references)

---

## 📚 参考文献

1. Kohn, W. & Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. *Phys. Rev.* **140**, A1133 (1965).

2. Thouless, D. J., Kohmoto, M., Nightingale, M. P. & den Nijs, M. Quantized Hall Conductance in a Two-Dimensional Periodic Potential. *Phys. Rev. Lett.* **49**, 405 (1982).

3. White, S. R. Density matrix formulation for quantum renormalization groups. *Phys. Rev. Lett.* **69**, 2863 (1992).
