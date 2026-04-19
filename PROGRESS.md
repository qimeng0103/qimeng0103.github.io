# My Blog 工作进度跟踪

记录所有博客写作和项目维护的进度。

---

## 📊 当前活跃任务

### 高优先级
- [x] 备考 TeX 更新 — 二维谐振子耦合与简并微扰论
  - [x] 编写 `tex/exam-prep/ustc-phd-prep.tex` 新章节（核心页 + 补充说明页）
  - [x] 编译 PDF 并通过
  - [x] 复制 PDF 到 `docs/public/exam-prep/`
  - [x] 更新 `about.md` 日期与 Contents 列表

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

- [x] 第十五次修改 - 重写7.5节SU(3)解释
- [x] 构建检查 - 通过
- [x] 推送部署 - 完成

- [x] 第十六次修改 - Young图/pseudo-real/SO(4)修正
- [x] 构建检查 - 通过
- [x] 推送部署 - 完成

- [x] 新博文 - Lieb晶格/交错磁/QSH/Planar Josephson junctions中的Majorana探索
  - [x] 建立代码探索文件夹 `content/lieb-majorana-junction/`
  - [x] 创建博文初稿 `docs/posts/condensed-matter/lieb-lattice-majorana-josephson-junctions.md`
  - [x] 更新主页、文章列表页、侧边栏配置
  - [x] 补充详细理论推导（短结极限Majorana条件）
  - [x] 添加数值验证和图像
  - [x] 构建检查与部署

### 中优先级  
- [ ] 

### 低优先级
- [ ] 

---

### 2026-04-17 - 备考 TeX 调整（删除 A-B 公式详细推导）

**工作内容：**

- 删除 Josephson 效应章节中 Ambegaokar-Baratoff 公式的长篇详细推导（Step 1–5，约 200 行）。
- 替换为精简的"结论版"：直接给出 $I_c R_N = \pi\Delta/2e$（$T=0$）及有限温度修正公式，明确标注"考场上只需熟记结论，不要求掌握推导细节"。
- 重新编译 PDF（88 页）并同步到 `docs/public/exam-prep/`。

### 2026-04-17 - 备考 TeX 修正（Josephson 效应 $I_c$ 与 $E_J$ 逻辑顺序）

**工作内容：**

- 修正 Josephson 效应章节中"与双态模型参数 $K$ 的联系"小节的推导逻辑顺序。
- 原表述"从 $I_c = 4enK/\hbar$ 可得 $E_J = \hbar I_c/2e$"存在循环/倒置问题。
- 改为：先说明宏观双态模型给出 $I_c = 4enK/\hbar$；再指出 $E_J = \hbar I_c/2e$ 是由 $E_J(\varphi) = -E_J\cos\varphi$ 与 $I = (2e/\hbar)\partial_\varphi E_J$ 直接得到的基本关系；由此一致导出 $E_J = 2nK$，再代入 A-B 公式求 $K$。
- 重新编译 PDF 并同步。

### 2026-04-17 - 备考 TeX 修正（超导伦敦方程推导细化）

**工作内容：**

- 删除超导电流公式后关于"有些教材把库珀对电荷记为 e"的备注说明，统一直接使用 $2e$ 显式写法。
- 将"伦敦方程与穿透深度"小节从一句话带过扩展为完整五步推导：
  - Step 1：规范条件 $
ablaarphi = -(2e/\hbar)ec{A}$（$ec{J}=0$ 时）
  - Step 2：对 $ec{J}$ 取旋度，利用 $
abla	imes
ablaarphi = 0$ 得到 $
abla	imesec{J} = (2e)^2 n_s ec{B}/m$
  - Step 3：结合麦克斯韦-安培定律 $
abla	imesec{B} = \mu_0ec{J}$，利用 $
abla	imes(
abla	imesec{B}) = -
abla^2ec{B}$ 导出伦敦方程 $
abla^2ec{B} = ec{B}/\lambda^2$
  - Step 4：一维半无限平板边界的显式解 $B(x) = B_0 e^{-x/\lambda}$
  - Step 5：物理意义——屏蔽电流、迈斯纳效应、指数衰减、与理想导体的区别
- 在"忽略位移电流"处添加脚注，简要解释位移电流的物理含义及静磁学近似下可忽略的原因。
- 重新编译 PDF（89 页）并同步到 `docs/public/exam-prep/`。

### 2026-04-17 - 备考 TeX 大幅精简（Josephson 效应推导）

**工作内容：**

- 用户指出"约瑟夫森效应的推导有点复杂了，不用讲那么多 Ambegaokar-Baratoff 的事情，Josephson 推导出这个关系在他们之前"。
- 将"2. 约瑟夫森效应的推导"从约 260 行精简为约 100 行：
  - **删除**：氨分子 NH₃ 双阱类比长篇故事、BCS 基态回顾、隧穿哈密顿量详细推导、库珀对二阶隧穿虚过程分析、Ambegaokar-Baratoff 公式与 $K$ 的联系、有限温度修正大段说明等微观内容。
  - **保留**：宏观波函数与有效双态哈密顿量设定、耦合薛定谔方程、实部/虚部分离、DC Josephson 关系 $I=I_c\sinarphi$、AC Josephson 关系 $\hbar\dot{arphi}=2eV$、能量视角 $E_J(arphi)=-E_J\cosarphi$。
  - **改写**：强调 Josephson（1962）是从弱耦合宏观量子态直接预言这些关系，$K$ 是一个可由实验测定的唯象参数，无需依赖后来的 A-B 微观推导。
- 重新编译 PDF（86 页）并同步。

### 2026-04-17 - 备考 TeX 补充（超导零电阻效应的微观解释）

**工作内容：**

- 在伦敦方程/迈斯纳效应章节后补充"零电阻效应的微观解释"段落。
- 内容涵盖：正常金属电阻来源于电子散射与动量弛豫；超导体中库珀对作为玻色子发生 BEC，宏观量子相干使得单个杂质/声子无法破坏凝聚态（能量代价至少为 $\Delta$）；低温下 $k_BT \ll \Delta$，无法产生准粒子激发，因此形成无耗散的持续电流。
- 强调核心概念：超导零电阻的本质是"宏观量子相干保护下的无耗散流动"，而非经典电子来不及碰撞。
- 重新编译 PDF（86 页）并同步。

### 2026-04-17 - 备考 TeX 修正（Josephson 效应 $K$ 的表述与时间反演对称性）

**工作内容：**

- 修正"Josephson 原始推导并不需要知道 $K$ 的微观表达式"的不准确表述。改为：明确指出 Josephson（1962）的原始论文确实利用了隧穿哈密顿量从微观上推导了相位-电流关系；同时说明在备考/唯象层面可把 $K$ 当作实验参数。
- 补充恢复"为什么 $K$ 是实数？——时间反演对称性"的论证：超导态的时间反演对称性要求隧穿哈密顿量满足 $\mathcal{T}H\mathcal{T}^{-1}=H$，从而双态子空间中的非对角元 $K=K^*$ 为实数，因此总可通过选择相对相位使 $K>0$。
- 重新编译 PDF（86 页）并同步。
- （后续微调）删除关于"Josephson 1962 年原始论文利用隧穿哈密顿量"的历史说明，进一步简化表述。
- （再微调）删除"在考场上可把它当作一个可由实验测定的唯象参数"的冗余说明。
- 补充说明"为什么总可以取 $K>0$"：通过整体相位旋转吸收复数相位因子，强调 Josephson 效应只依赖相对相位差 $\varphi = \varphi_2 - \varphi_1$，因此总可选择相位参考使 $K$ 为实正数。
- （再改写）将"规范变换/吸收相位"的抽象说法改为完全代数化的机械操作：假设 $K=|K|e^{i\theta_0}$，直接写出电流公式 $I \propto \sin(\varphi+\theta_0)$，然后做换元 $\tilde{\varphi}=\varphi+\theta_0$，说明这只是一个固定的常数平移，不影响任何可测量，从而彻底消去学生对"规范变换"的恐惧。
- （用户反馈：不是要删掉，而是要帮他克服这个恐惧）新增一个 `insightbox`"规范变换的机械操作指南"，里面用三步法拆解恐惧来源、用三角函数类比、给出考场标准作答流程，让学生面对"证明 K 可取为实数"这类题时有固定的答题模板。
- （再改写）修正 insightbox 内部的格式拥挤问题，在每个 Step 标题后增加空行；删除"教材故弄玄虚""一句话心法"等过于随意的表述，语气改得更学术、更中性；补充说明"gauge 掉"是规范变换的口语说法；保留机械操作的核心精神。
- （最终改写）用户反馈：DC Josephson 部分太啰嗦，且没有体现波函数规范变换影响 K 相位吸收的完整逻辑链。删除 insightbox，将"为什么总可以取 K>0"改写成简洁的连续推导：先承认 $K=|K|e^{i\theta_0}$；再写出波函数整体相位变换 $\psi_{1,2} \to \psi_{1,2}e^{i\alpha_{1,2}}$，说明 $K$ 获得因子 $e^{i(\alpha_2-\alpha_1)}$ 而 $\varphi$ 同步变为 $\varphi+(\alpha_2-\alpha_1)$；主动选择 $\alpha_2-\alpha_1=-\theta_0$ 使 $K' = |K|$ 且 $\sin(\varphi'+\theta_0)=\sin\varphi'$；最后指出可测量只依赖相对相位差，故总可取 $K>0$。把"波函数→规范变换→K 相位吸收→标准形式"的完整逻辑链一次性说清楚了。
- （再细化）用户指出"两侧宏观波函数乘相位后，$H_{\text{eff}}$ 非对角元 $K$ 多出一个相位因子"这一步的推导逻辑需要更清楚。将原文一句话带过改为完整代数推导：写出代入薛定谔方程 $i\hbar \partial_t(\psi_1' e^{-i\alpha_1}) = E_1 \psi_1' e^{-i\alpha_1} + K \psi_2' e^{-i\alpha_2}$，两边乘 $e^{i\alpha_1}$ 后得到 $i\hbar \dot{\psi}_1' = E_1 \psi_1' + K e^{i(\alpha_1-\alpha_2)} \psi_2'$；同理第二个方程给出 $K e^{i(\alpha_2-\alpha_1)}$，由厄米性确认新的耦合常数为 $K' = K e^{i(\alpha_2-\alpha_1)}$。同时明确写出相对相位差如何同步变化，以及主动选择 $\alpha_2-\alpha_1=-\theta_0$ 后电流公式如何化为标准形式。
- （再修正+心理建设）将"统一写成"改为"从第二个方程直接读出"；在规范变换推导中插入"关键认知"段落，用确定性语言帮助学生克服对"gauge 掉"的恐惧：明确规范变换的触发条件（公式里出现不可观测的固定常数）、操作本质（清理冗余自由度）、以及它不需要灵感的特点。
- （紧急 bugfix）用户反馈 PDF 中 	extbf{} 没有正常显示。经查，Josephson 效应章节中"关键认知"段落的多个 	extbf 命令被错误写成了双反斜杠 `\\textbf`，导致 xelatex 将其渲染为普通文本而非加粗。已全局修复并重新编译 PDF。
- 大幅扩展 AC Josephson 效应与能量视角的推导细节：
  - AC 效应：分 4 步详细推导（电势能差来源、实部方程相减细节、积分求相位、物理解释恒定直流电压为何产生交流电流）
  - 能量视角：分 3 步详细推导（$E_J(arphi)=-E_J\cos\varphi$ 的物理意义、$I=(2e/\hbar)\partial_\varphi E_J$ 的完整推导、电荷-相位正则对易关系 $[\hat{n},\hat{\varphi}]=-i$ 的物理意义）
- 重新编译 PDF（88 页）并同步。
- （用户要求"这里严格的做"）修正 AC Josephson 效应 Step 2：删除近似写法，改为严格保留 $K\cos\varphi$ 的完整实部方程，明确写出第二式减第一式的完整代数展开，得到 $-\hbar(\dot\varphi_2-\dot\varphi_1) = (E_2-E_1) + K\cos\varphi(n_1-n_2)/\sqrt{n_1n_2}$；指出由于库珀对密度极大，隧穿只引起 $|n_1-n_2| \ll n_{1,2}$ 的微弱扰动，因此残余项可严格忽略，最终得到 $\hbar\dot\varphi = 2eV$。
- （用户要求"这里也要严格的做"）彻底重写"磁场中相位梯度的推导"小节，将其扩展为 6 步严格推导：明确规范条件、定义相位差并指出空间分离问题、构造闭合回路应用相位约束、分解回路积分、用斯托克斯定理计算磁通、取极限得到相位梯度。

### 2026-04-17 - 备考 TeX 新增章节（双 delta 势 Born 散射 3D）

**工作内容：**

- 新增章节"量子力学：双 $\delta$ 势的 Born 近似散射（3D）"，放在第 \ref{sec:double-delta} 节（1D 双 $\delta$ 势垒共振透射）之后，作为 3D 推广。
- 核心页（双栏）包含：
  - modelbox — 中子-氢分子双 $\delta$ 势散射题目复刻
  - tipbox — 考点分析（Born 近似触发条件、$\delta$ 势傅里叶变换、双源干涉、几何关系）
  - derivationbox — 4 步标准解题过程（傅里叶积分、微分截面、几何因子展开、极大值方向）
  - formulabox — 通用截面公式、$\vec{a}=a\hat{z}$ 特例、极大值条件
  - errorbox — 常见错误（1D/3D $\delta$ 势量纲混淆、约化质量遗漏、$\vec{q}\cdot\vec{a}$ 与 $qa$ 混淆、$q$ 的大小计算）
  - insightbox — 物理直觉（杨氏双缝量子版本、与 1D 双 $\delta$ 势垒的对照表、X 射线/电子衍射/双量子点联系）
  - thinkbox — 6 步解题模板
- 补充说明页（单栏）包含：
  - 题型反射弧标签
  - Born 近似公式来源（Lippmann-Schwinger 一阶迭代）
  - 傅里叶积分详细计算
  - $\vec{q}\cdot\vec{a}$ 的完整展开（含一般取向公式）
  - 极大/极小值方向分析（$ka\gg1$ 时的圆锥形极大值环）
  - 与 1D 双 $\delta$ 势垒的数学联系（高能极限下透射率与 3D 截面的对比）
  - 完整知识点列表与拓展延伸（$N$ 散射中心结构因子、连续势与电荷密度傅里叶变换、中子散射实验）
- 重新编译 PDF（93 页）并同步到 `docs/public/exam-prep/`。
- （用户反馈：不知道何时用 Born 公式、何时用分波法）新增两个层面的决策指南：
  - 核心页：删除超格的 cheatbox，保留 thinkbox 的 6 步解题模板
  - 补充说明页新增"Born 近似与分波法的系统对比"小节：详细阐述两种方法在势对称性、能量尺度、题目提示、计算复杂度、物理图像五个维度的差异；末尾附速查表 + 考场提示，帮助用户建立系统化的决策框架。

### 2026-04-17 - 备考 TeX 修正（伦敦方程推导符号修正）

**工作内容：**

- 修正伦敦方程推导中的符号不一致问题。原表述"取电流方向（大小）可写成"提前去掉了 $q=-2e$ 的负号，导致 Step 2 中 $
abla	imesec{J}$ 算成正的，与 Step 3 最终得到的伦敦方程 $
abla^2ec{B} = +ec{B}/\lambda^2$ 差一个负号。
- 改为：明确写出完整矢量表达式 $ec{J} = -rac{2e n_s}{m}(\hbar
ablaarphi + 2eec{A})$，说明负号来源于库珀对带负电；Step 2 中取旋度得到 $
abla	imesec{J} = -(2e)^2 n_s ec{B}/m$；Step 3 代入麦克斯韦方程后两边负号抵消，严格导出标准的伦敦方程。
- 重新编译 PDF（89 页）并同步。

### 2026-04-17 - 备考 TeX 修正（双 delta Born insightbox 表格超栏修复）

**工作内容：**

- 修复 `insightbox` 中 1D/3D 双 $\delta$ 势对照表在双栏排版下超宽（overfull \hbox 16.57pt）的问题。
- **第一次尝试**：将三列 `tabular` 替换为两个并排 `minipage` 内的纯文本，虽消除超宽但用户反馈缺乏表格结构性。
- **最终方案**：在每个 `minipage` 内保留 `tabular`（属性 | 值，带边框），用 `\resizebox{\linewidth}{!}{...}` 自动缩放使表格恰好 fit 单栏宽度。既保留表格的边框和行列对齐感，又不超栏。
- 重新编译 PDF（93 页），overfull hbox 消除，仅余 2.3pt（其他位置，可忽略）和既有 vbox 警告。


---

## 📝 会话记录

### 2026-04-15 - 备考 TeX 更新（二维谐振子耦合与简并微扰论）

**工作内容：**

1. **新增第三章节**：二维谐振子耦合与简并微扰论
   - **严格解路径**：构造对称/反对称算符 $b_1 = (a_1+a_2)/\sqrt{2}$，$b_2 = (a_1-a_2)/\sqrt{2}$ 对角化哈密顿量
   - **微扰论路径**：在 $N=2$ 简并子空间 $\{|2,0\rangle, |1,1\rangle, |0,2\rangle\}$ 内构建微扰矩阵并求解一级修正
   - **结果校验**：微扰论一级修正 $E^{(1)} = 0, \pm 2\lambda$ 与严格解完全一致

2. **完整框体覆盖**：
   - `modelbox` — 题目复刻
   - `tipbox` — 考点分析（对称/反对称组合、简并子空间、系数陷阱）
   - `derivationbox` — 标准解题过程（严格解 + 微扰论双路径）
   - `formulabox` — 核心结论
   - `errorbox` — 常见错误（变换焦虑、简并遗漏、系数计算、非简并误用）
   - `insightbox` — 物理直觉（能量流转、经典耦合振子、分束器/双位点跳跃类比）
   - `thinkbox` — 解题模板

3. **补充说明页**：
   - 题型反射弧标签
   - $b_1, b_2$ 对易关系详细验证
   - 哈密顿量严格对角化完整推导
   - 微扰矩阵详细构建与特征向量求解
   - 与 SU(2) 代数的联系（$J_\pm = a_1^\dagger a_2$ 等）
   - 多模推广与实验联系

4. **同步更新**：
   - 编译 PDF（12页）并复制到 `docs/public/exam-prep/`
   - 更新 `about.md`：Last updated 改为 2026-04-15，添加 Current Contents 列表

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
