# 示例文章：公式与代码演示

这篇文章展示了 VitePress 对数学公式、代码高亮和图片的支持。

## 数学公式

### 行内公式

这是一个行内公式：$E = mc^2$，爱因斯坦著名的质能方程。

### 独立公式

二次方程的求根公式：

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### 多行对齐


$$
\begin{aligned}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{aligned}
$$


### 矩阵

$$
\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

### 概率与统计

正态分布的概率密度函数：

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

## 代码高亮

### Python 示例

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    """Sigmoid 函数"""
    return 1 / (1 + np.exp(-x))

# 生成数据
x = np.linspace(-10, 10, 100)
y = sigmoid(x)

# 绘图
plt.plot(x, y)
plt.title('Sigmoid Function')
plt.xlabel('x')
plt.ylabel('σ(x)')
plt.grid(True)
plt.show()
```

### JavaScript 示例

```javascript
// 快速排序实现
function quickSort(arr) {
  if (arr.length <= 1) return arr;
  
  const pivot = arr[Math.floor(arr.length / 2)];
  const left = arr.filter(x => x < pivot);
  const middle = arr.filter(x => x === pivot);
  const right = arr.filter(x => x > pivot);
  
  return [...quickSort(left), ...middle, ...quickSort(right)];
}

// 测试
const numbers = [3, 6, 8, 10, 1, 2, 1];
console.log(quickSort(numbers)); // [1, 1, 2, 3, 6, 8, 10]
```

### LaTeX 示例

```latex
\documentclass{article}
\usepackage{amsmath}

\begin{document}

\begin{equation}
    \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\end{equation}

\end{document}
```

## 图片展示

### 本地图片

```markdown
![示例图片](/images/example.png)
```

### 网络图片

![VitePress Logo](https://vitepress.dev/vitepress-logo-mini.svg)

## 表格

| 算法 | 时间复杂度 | 空间复杂度 | 稳定性 |
|------|-----------|-----------|--------|
| 冒泡排序 | $O(n^2)$ | $O(1)$ | 稳定 |
| 快速排序 | $O(n\log n)$ | $O(\log n)$ | 不稳定 |
| 归并排序 | $O(n\log n)$ | $O(n)$ | 稳定 |
| 堆排序 | $O(n\log n)$ | $O(1)$ | 不稳定 |

## 引用与链接

> "数学是科学的皇后，数论是数学的皇后。" —— 高斯

更多阅读：
- [VitePress 文档](https://vitepress.dev/)
- [KaTeX 支持符号](https://katex.org/docs/supported.html)

---

*文章最后更新于：2024-01-15*
