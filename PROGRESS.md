# My Blog 工作进度跟踪

记录所有博客写作和项目维护的进度。

---

## 📊 当前活跃任务

### 高优先级
- [x] 第十次修改 - SO(4)推导修正、简化表述、Young图调整
- [x] 构建检查 - 通过
- [x] 推送部署 - 完成

- [x] 第十一次修改 - 删除5.6示例表格
- [x] 构建检查 - 通过
- [x] 推送部署 - 完成

- [x] 第十二次修改 - 重写6.4.4 SO(4)能量推导
- [x] 构建检查 - 通过
- [x] 推送部署 - 完成

- [x] 第十三次修改 - 删除表格/重写7.5
- [x] 构建检查 - 通过
- [x] 推送部署 - 完成

- [x] 第十四次修改 - 修复SO(4)/jj coupling/相关细节
- [x] 构建检查 - 通过
- [x] 推送部署 - 完成

### 中优先级  
- [ ] 

### 低优先级
- [ ] 

---

## 📝 会话记录

### 2026-04-08 - 第十四次修改（修复SO(4)/jj coupling/相关细节）

**用户反馈的问题及修复：**

1. **6.4.4 SO(4)推导** - 移除"close but not exact"的模糊表述
   - 直接给出从$2j(j+1)$到能量公式的推导
   - 说明精确结果需要量子力学算符排序的修正

2. **jj Coupling精简** (Line 1399)
   - 删除冗长的文字解释
   - 改为简洁的表格格式展示允许/禁止的J值

3. **电子相关解释简化** (Line 1554)
   - 删除co-rotating frame的详细描述
   - 删除旋转木马的比喻
   - 直接说明高L态减少库仑排斥的机制

4. **球谐函数"rotated by 90°"修正** (Line 1658)
   - 删除错误的"just rotated by 90°"表述
   - 正确解释p_x和Y_1^{±1}概率分布的关系

5. **7.1 Summary table** - 确认已在之前的提交中删除

---

### 2026-04-08 - 第十三次修改（删除表格/重写7.5）

**用户反馈的问题及修复：**

1. **删除7.1 Projective Representation最后的summary table**
   - 删除了Property/Integer spin/Half-integer spin对比表格

2. **删除7.3中"Why the sign matters"整段**
   - 删除了Case 1 (Integer spin)详细解释
   - 删除了Case 2 (Half-integer spin)详细解释
   - 删除了Conclusion段落
   - 直接保留简洁的核心解释

3. **完全重写7.5节，去掉所有图**
   - 删除所有图像引用（su3_root_diagram.png, su3_fundamental_triplet.png, su3_octet_baryons.png）
   - 删除LaTeX Young diagram图形（\\begin{array}画框）
   - 删除SU(3) Representations表格
   - 保留纯文字解释：
     * SU(3) roots和weights的文字描述
     * Adjoint 8表示的系统构建方法（6个顶点态+2个中心态）
     * Young tableaux规则的文字描述
     * Permutation symmetry为什么参与SU(3)表示分解的解释

**7.5现在包含的核心内容：**
- SU(3) Rank = 2的解释
- 6个root operators ($I_\pm, U_\pm, V_\pm$)的作用
- Fundamental 3表示的构建
- Adjoint 8表示的系统构建（分步骤说明）
- Young tableaux规则（文字版）
- 为什么permutation symmetry重要
- 张量积分解的文字解释

---

### 2026-04-08 - 第十二次修改（重写6.4.4 SO(4)能量推导）

**问题：** 6.4.4节的能量推导完全混乱，包含不一致的μ因子和错误的中间步骤。

**重写内容：**
1. 使用关键恒等式：$\mathbf{L}^2 + \mathbf{A}^2 = -\frac{\mu k^2}{2\hat{H}} + \hbar^2$
2. 正确关联SO(4) Casimir算符与氢原子能量
3. 清晰定义主量子数 $n = 2j + 1$ 与SO(4)表示的关系
4. 移除之前混乱的中间步骤（特别是包含不一致μ因子的部分）
5. 说明为什么代数方法有效（SO(4)对称性确保$\mathbf{K}^2$仅依赖于$n$）

**参考：** arXiv:1504.04269 (SO(4) symmetry and hydrogen atom)

---

### 2026-04-08 - 第十次修改（SO(4)推导、简化表述、Young图调整）

**用户反馈的问题及修复：**

1. **6.4.4 Step 5 推导修正**
   - 发现问题：原推导中等式不匹配，解不出正确的E表达式
   - 参考arXiv:1504.04269和arXiv:2006.12498等文献
   - 修正方法：使用更清晰的Casimir operator方法
   - 关键公式：$\mathbf{L}^2 + \mathbf{A}^2 = -\frac{\mu k^2}{2\hat{H}}$
   - 对于SO(4)表示：$\mathbf{L}^2 + \mathbf{A}^2 = n^2 - 1$
   - 得出能量公式：$E_n = -\frac{\mu k^2}{2\hbar^2 n^2}$

2. **7.1.2 Projective Representation 简化**
   - 原文过于啰嗦，包含过多解释性文字
   - 简化后保留核心概念和关键例子
   - 删除重复的解释（如多次解释$2\pi$旋转）
   - 保留Summary table进行对比

3. **7.5 Young Diagrams 调整**
   - 移除大图像（young_3x3_product.png等）
   - 只保留小的LaTeX Young diagram表格
   - 使用$\begin{array}$环境生成简洁的图形

---

### 2026-04-08 - 第九次修改（详细解释和修正）

**用户反馈的问题及修复：**

1. **jj coupling - 半整数j情况** (Line 1399)
   - 明确解释公式$(-1)^{2j-J}$适用于所有j，包括半整数
   - 给出具体计算：对于$j=1/2$，$2j=1$（奇数），所以对称性由$(1-J)$的奇偶性决定
   - 列出所有情况的详细表格（$j=1/2$和$j=3/2$的允许/禁止J值）
   - 解释为什么半整数j的工作方式与整数相同

2. **SU(3) root diagram图像角标** 
   - 重新生成图像确保$I_-$和$V_-$角标正确显示

3. **Radial equation边界条件** (Line 1749)
   - 明确说明$l=0$问题有两个方面：
     - **原点**：违反边界条件$u(0)=0$
     - **无穷远**：归一化积分发散

4. **SO(4)推导Step 5** (Line 1934)
   - 修正等式推导，简化展示过程
   - 给出最终正确的能量公式

5. **Spherical harmonics概率密度** (Line 1676)
   - 添加实轨道与复球谐函数概率密度的关系说明
   - 证明$|p_x|^2$与$|Y_1^{\pm 1}|^2$的关系
   - 明确说明交叉项在积分时消失

6. **"Why 3 ladders"解释** (Line 2362)
   - 添加更清晰的逐步推理：
     - 根向量连接不同权重
     - 代数闭合约束几何
     - SU(3)的具体约束条件
     - 为什么2个不够，4个不行，只有6个（六边形）满足

---

### 2026-04-08 - 第八次修改（图像和表格修复）

### 2026-04-08 - 第七次修改（细节修复）

**用户反馈的问题及修复：**

1. **7.1 Application: Decompose机理** (Line 2122)
   - 添加明确的3步机制说明
   - 解释character orthogonality theorem的公式
   - 说明$n_j$系数的计算方法
   - 添加验证：$1 + 3 = 4 = 2 \times 2$

2. **7.3表格ID缩写** (Line 2173)
   - "antipodal ID" → "antipodal Identification"

3. **Case 1 Integer spin表示等式解释** (Line 2230)
   - 说明$D^{(j)}(U)$是$(2j+1) \times (2j+1)$表示矩阵
   - 说明表示空间是$|j,m\rangle$ basis
   - 添加$I_{3\times 3}$和$I_{2\times 2}$的显式标注

4. **SU(3) root structure具体解释** (Line 2318)
   - 添加具体代数约束：$[E_{\vec{\alpha}}, E_{\vec{\beta}}] \propto E_{\vec{\alpha}+\vec{\beta}}$
   - 添加几何证明sketch：角度限制和六边形强制
   - 解释为什么不是2个或4个roots

5. **Fundamental triplet图像修复**
   - 修复$V_-$箭头对齐（沿三角形边精确对齐）
   - $I$标注已经改为$I_-$（之前已修复）

---

### 2026-04-08 - 第六次修改（SU(3)图像和Spherical Harmonics）

**用户反馈的问题及修复：**

1. **SU(3) ladder operators解释** (Line 2290)
   - 添加解释：为什么2个量子数需要3个independent ladders
   - 解释物理意义：$(u, d, s)$是三角形，没有单个ladder能连接所有三个态

2. **SU(3)图像修复**
   - Fundamental triplet：显示从highest weight构建过程，只标注用到的lowering operators ($I_-$, $V_-$)
   - Adjoint octet：修复对齐问题，使用精确坐标绘制六边形
   - 重新生成所有SU(3)图像

3. **Spherical Harmonics证明** (Line 1656)
   - 添加$|Y_l^m|^2 = |Y_l^{-m}|^2$的显式证明
   - 使用性质$Y_l^{-m} = (-1)^m (Y_l^m)^*$

4. **d-orbitals介绍** (Line 1643)
   - 添加$d_{xz}$, $d_{yz}$, $d_{xy}$, $d_{x^2-y^2}$的详细描述
   - 说明它们与$Y_2^{\pm 1}$, $Y_2^{\pm 2}$的线性组合关系

**待处理：**
- Young Tableaux图像修复（需要用户提供Python程序或具体需求）

---

### 2026-04-08 - 第五次修改（用户审阅反馈）

**用户指出的问题及修复：**

1. **$l=0$波函数发散问题** (Line 1719)
   - 原文：声称动能产生delta函数发散
   - 修改：改为边界条件解释——$u \propto 1$导致不归一化，违反原点边界条件

2. **删除"Sketch of proof"** (Line 1756-1768)
   - 原文：冗长的commutator计算概述
   - 修改：简化为一句"可以显式验证$[\hat{H}, \hat{\mathbf{A}}] = 0$"

3. **删除"lengthy commutator algebra"** (两处)
   - Line 1765: "The full calculation involves lengthy commutator algebra"
   - Line 1822: "derived via lengthy commutator algebra"
   - Line 1876: "careful commutator algebra"
   - 修改：直接删除这些修饰语

4. **SO(4)推导中的$(j,j)$符号** (Line 1907)
   - 原文：突然引入$(j,j)$，用户困惑
   - 修改：明确解释$j = m = n$的来源，解释$n = 2j+1$与氢原子简并度的关系

---

### 2026-04-08 - 第四次修改（用户问题专项）

**用户困惑的5个具体问题及解决方案：**

1. **SU(3)为何有6个root vectors（vs SU(2)的2个）**
   - 添加解释：SU(3)有3个独立升降算符($I_\pm, U_\pm, V_\pm$) vs SU(2)只有1个($J_\pm$)
   - 给出显式$(\Delta i_3, \Delta y)$值
   - 生成root diagram图像(hexagon)

2. **Weight diagrams**
   - 生成fundamental triplet图($\mathbf{3}$: triangle)
   - 生成adjoint octet图($\mathbf{8}$: hexagon with doubly-occupied center)
   - 标注$(i_3, y)$量子数

3. **Young tableaux mechanics**
   - 解释$\bar{\mathbf{3}} \neq \mathbf{3}$的原因：covariant vs contravariant indices
   - 说明$\bar{\mathbf{3}}$构造：$\epsilon^{ijk}q_j q_k$（antisymmetric pair）
   - 给出$\mathbf{3} \otimes \mathbf{3}$的机械计算步骤

4. **SO(3) topology - antipodal identification**
   - 详细解释"antipodal identification": $\pi\mathbf{n} \sim -\pi\mathbf{n}$
   - 解释non-contractible loop为何不能shrink（jump跨越identified boundary）
   - 对比SU(2)的$S^3$（no identification, simply connected）

5. **Representation types (integer vs half-integer)**
   - 强调$D^{(j)}(-U) = (-1)^{2j} D^{(j)}(U)$决定true vs projective
   - 添加对比表格：integer spin → true rep, half-integer → projective rep
   - 明确$2\pi$ rotation对两者不同效果

**生成的图像：**
- `su3_root_diagram.png` - 6 root vectors forming hexagon
- `su3_fundamental_triplet.png` - quark triplet $\mathbf{3}$
- `su3_octet_baryons.png` - baryon octet $\mathbf{8}$

---

### 2026-04-08 - 第三次修改完成

**修改内容：**

1. **7.1 Projective Representation**: 强调SO(3)群中$R_z(2\pi)=I$但量子算符$D=-I$的区别
2. **7.1 Characters**: 添加详细推导和显式计算例子
3. **7.3 Fundamental Group**: 改进解释（3D ball vs 3-sphere可视化）
4. **7.3 Double Cover**: 明确角度对应关系，解释$\mathbb{Z}_2$ quotient
5. **7.5 SU(3)**: 
   - 解释rank 2来源
   - 添加root vector显式计算
   - 解释weight构建
   - 说明Young tableaux的便利之处
6. **5.2-5.6**: 
   - 简化闭壳层解释
   - 简化multiplicity讨论
   - 删除runner比喻
   - 删除Ce例子
   - 强调不同shell电子的可区分性

**提交**: `fab47c8`

---

## 📈 文章进度看板

| 文章 | 分类 | 状态 | 进度 | 备注 |
|------|------|------|------|------|
| angular-momentum-algebra.md | quantum-mechanics | 🟢 已完成 | 已部署 | 全部修改完成 |

---

**最后更新：** 2026-04-08
