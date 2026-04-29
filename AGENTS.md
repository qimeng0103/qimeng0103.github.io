# My Blog - Agent Context

## 项目简介

基于 [VitePress](https://vitepress.dev/) 构建的个人科研博客，使用 Markdown 格式管理文章。

## 目录结构

```
my-blog/
├── docs/
│   ├── .vitepress/
│   │   └── config.mjs          # VitePress 配置（侧边栏导航）
│   ├── posts/                  # 博客文章
│   │   ├── quantum-mechanics/  # 量子力学笔记
│   │   ├── condensed-matter/   # 凝聚态物理笔记
│   │   └── index.md            # 文章列表页
│   ├── images/                 # 图片资源
│   └── index.md                # 主页（⚠️ 重要：必须同步更新 Recent Articles）
├── .kimi/skills/               # Kimi Agent 技能文档
│   └── blog-writer/SKILL.md    # 博客写作规范
├── .github/workflows/          # GitHub Actions 自动部署
└── package.json
```

## 双轨制内容管理

本项目采用 **Blog (英文) + TeX PDF (中文备考)** 双轨制：

### 1. Blog (`docs/posts/`) - 公开英文文章
- **语言：** 全英文
- **目的：** 学术写作训练，公开分享
- **内容：** 详细推导 + 概念理解 + 物理图像
- **格式：** Markdown

### 2. TeX PDF (`tex/exam-prep/`) - 内部备考资料
- **语言：** 中文为主，英文术语备注
- **目的：** 中科大物理博士考试备考
- **内容：**
  - **正文：** 核心结论、解题技巧、二级结论（简洁，双栏高密度）
  - **附录：** 完整推导、详细理解（完备参考）
- **格式：** LaTeX (Article 类 + Beamer 风格彩色框)

## ⚠️ 重要规则

### 强制死命令：每次文件修改后必须立即 Git

**任何对项目文件的修改完成后，必须立即执行以下命令（禁止拖延、禁止批量累积）：**

```bash
cd /home/mengq8/my-blog
git add <修改的文件>
git commit -m "<描述本次修改的简洁消息>"
git push origin main
```

**违反后果：** 未提交的修改可能在后续操作中被覆盖、遗忘或与其他更改混淆，导致数据丢失或部署不一致。

---

### 强制死命令：增删文章后必须检查全站一致性

**任何文章的新增、删除、重命名或分类变更后，必须立即检查并确保以下三个位置的内容严格一致：**

| 位置 | 检查项 |
|------|--------|
| `docs/index.md` | Recent Articles 条目与当前实际文章一一对应 |
| `docs/posts/index.md` | 各分类下的文章列表与当前实际文章一一对应 |
| `docs/.vitepress/config.mjs` | 侧边栏导航链接与当前实际文章一一对应 |

**检查方法：** 在 `docs/posts/` 目录下确认实际存在的文章文件，逐个核对上述三个文件是否包含且仅包含这些文章。

**违反后果：** 出现死链、404 错误、文章存在但首页不显示、或已删除文章仍在导航中残留。

---

### 添加/修改文章时必须同步更新以下文件

1. **`docs/index.md`** - 主页 Recent Articles 部分
   - 添加新文章条目到列表顶部
   - 保持最多 4-5 篇最新文章
   - 按日期倒序排列
   - **删除文章时必须同步删除此处的对应条目**

2. **`docs/posts/index.md`** - 文章列表页（如需要）
   - 添加新文章到对应分类
   - **删除文章时必须同步删除此处的对应条目**

3. **`docs/.vitepress/config.mjs`** - 侧边栏配置（如添加新分类）
   - 在 sidebar 中添加新文章链接
   - **删除文章时必须同步删除此处的对应链接**

4. **`tex/exam-prep/ustc-phd-prep.tex`** - 备考 PDF（如相关内容适合放入）
   - 将 Blog 文章的核心结论提取到 PDF 对应章节
   - 在 Appendix 添加详细推导（如需要）
   - **⚠️ 编译 PDF 并同步到所有副本位置：**
     ```bash
     cd tex/exam-prep
     xelatex -interaction=nonstopmode -output-directory=../../docs/public/exam-prep ustc-phd-prep.tex
     xelatex -interaction=nonstopmode -output-directory=../../docs/public/exam-prep ustc-phd-prep.tex
     ```
   - **⚠️ 必须同步所有 PDF 副本（重要教训）：**
     编译完成后，项目内可能存在多份同名 PDF 副本。必须用 `find` 定位并全部更新，防止打开旧版本：
     ```bash
     find /home/mengq8/my-blog -name "ustc-phd-prep.pdf" -type f
     # 然后手动 cp 最新 PDF 到所有发现的目录
     ```
     常见副本位置包括但不限于：
     - `docs/public/exam-prep/ustc-phd-prep.pdf`（主发布目录）
     - `tex/exam-prep/ustc-phd-prep.pdf`（编译输出目录）
     - `docs/.vitepress/dist/exam-prep/ustc-phd-prep.pdf`（构建产物目录）
     - `node_modules/.cache/gh-pages/.../exam-prep/ustc-phd-prep.pdf`（gh-pages 缓存）
   - **更新 about.md：**
     - 修改 `Last updated: YYYY-MM-DD` 为当前日期
     - **检查并更新内容介绍**（如新增章节，需要在 Contents 列表中添加）
   - 确保 PDF 下载链接 `/exam-prep/ustc-phd-prep.pdf` 可正常访问

### Blog 文章格式规范

#### 文件命名规范

**使用内容描述性命名，不包含人名或书名：**
- ✅ `bound-states-resonances-scattering.md`
- ✅ `stationary-perturbation-theory.md`
- ❌ `zeng-jinyan-chapters-3-4-5.md` (包含人名)
- ❌ `landau-chapter-1.md` (包含人名)

**命名原则：**
1. 使用主题关键词，小写，单词间用连字符分隔
2. 不包含作者姓名（如 zeng-jinyan, landau）
3. 不包含书名（如 qm-special-topics）
4. 不包含章节号（用主题代替 chapter-3-4-5）

#### 内容风格要求

**客观知识呈现（重要！）：**
- ❌ **禁止提及来源**：博文中不得出现作者姓名、书名、章节引用（如 "according to Sakurai", "in Zeng's book", "Chapter 3"）
- ✅ **纯粹知识内容**：直接呈现物理概念、数学推导、定理证明，不说明来源
- ✅ **全文英文**：所有正文内容必须使用英文

**推导完整性（重要！）：**
- ❌ **禁止简化表述**：不允许 "It can be shown that...", "After some algebra...", "The result follows..." 等省略推导的说法
- ✅ **完整数学推导**：每一步变换都必须写出，包括中间步骤
- ✅ **详细计算过程**：波函数归一化、积分计算、代数运算必须完整展示
- ✅ **显式求解**：所有边界条件、匹配条件必须显式写出并求解
- ✅ **物理意义说明**：每个方程、每个结果的物理意义必须解释

**示意图规范（Python matplotlib）：**
- ✅ **统一工具**：使用 `utils/plot_style.py` 保持全站图表风格一致
- ✅ **存放位置**：绘图脚本在 `utils/`，输出到 `docs/images/{category}/`
- ✅ **编译流程**：
  ```bash
  python3 utils/generate_figures.py
  ```
- ✅ **必要图像**：势阱结构、波函数匹配、共振曲线、相移图、散射几何
- ✅ **配色方案**：使用 `plot_style.py` 中定义的学术配色（深蓝、暗红、绿色、紫色等）

**⚠️ Young图/表格内图片尺寸规范（重要教训）：**
- **表格内图片**：必须使用 `<img>` HTML标签替代Markdown `![]()`，并设置明确 `width` 属性
  ```markdown
  | Partition | Young Diagram |
  |-----------|:-------------:|
  | (3) | <img src="/images/..." width="60px"> |
  ```
- **正文图片尺寸**：使用HTML控制大小，避免过大或过小
  ```markdown
  <img src="/images/..." width="600px" alt="描述">
  ```
- **小图版本**：为表格专门生成小尺寸版本（宽度30-60px），避免撑大表格
- **图题格式**：图片说明使用斜体 `*描述*` 放在图片下方
- **组合图**：相关图表应组合成一张图（如并排显示三种Young图），避免多个独立图片

**⚠️ MathJax 数学公式渲染规范（重要教训）：**
- **禁止使用 Unicode 特殊字符在公式内**：如 `✓` (U+2713)、`✗` (U+2717) 等会导致 MathJax 渲染失败，后续内容可能无法正确显示
  ```markdown
  ❌ $$... = 0$$ ✓          # 不要在公式后直接使用 unicode 对勾
  ✅ $$... = 0 \quad \checkmark$$  # 使用 LaTeX 命令替代
  ```
- **行内标记用 LaTeX 命令**：
  - 对勾：使用 `\checkmark` (需 `\usepackage{amssymb}`，VitePress MathJax 默认支持)
  - 叉号：使用 `\times` 或 `\cancel{...}`
  - 点乘：使用 `\cdot` 而非 `·`
- **公式内的文本**：使用 `\text{...}` 包裹，如 `$E = mc^2 \text{ (Einstein)}$`
- **多行公式**：使用 `aligned` 环境，不要用多个 `$$` 块拼接
  ```markdown
  $$
  \begin{aligned}
  A &= B \\
    &= C
  \end{aligned}
  $$
  ```
- **构建后验证**：每次修改公式后必须执行 `npm run docs:build` 并检查生成的 HTML，确保：
  1. 公式渲染正确，无乱码或截断
  2. 公式后的内容正常显示（没有被吞掉或错位）
  3. 特别是检查 `Step X` 等标题是否正确分割

#### 文章头部格式

```markdown
# Article Title

📅 **Date:** YYYY-MM-DD | 🏷️ **Tags:** Tag1, Tag2 | 📂 **Category:** Category Name

---

## Introduction

Article content in English, supporting LaTeX math:
- Inline: $E = mc^2$
- Display:
  $$
  \hat{H}\psi = E\psi
  $$
```

### TeX PDF 格式规范

```latex
% 使用预定义的颜色框
\begin{modelbox}[Bloch 定理]
核心结论和物理图像...
\end{modelbox}

\begin{tipbox}[解题技巧]
快速识别和解题套路...
\end{tipbox}

\begin{derivationbox}[详细推导]
附录中的完整推导...
\end{derivationbox}
```

**可用框类型：**
- `modelbox` (蓝色) - 物理模型和定理
- `tipbox` (红色) - 解题技巧和识别方法
- `formulabox` (绿色) - 重要公式和二级结论
- `warnbox` (橙色) - 警示和常见错误
- `insightbox` (紫色) - 概念理解和物理图像
- `cheatbox` (黄色) - 速查备忘
- `derivationbox` (灰色) - 附录推导
- `errorbox` (深红色) - **错题与思路短路库**（最重要！记录考试/练习中的错误）
- `thinkbox` (青色) - 解题思路模板和总结

### 错题库使用规范

**目的：** 记录做题过程中的错误、卡壳点和思维短路，防止重复犯错

**记录时机：**
- 做完真题后发现错误
- 模拟考试中的失误
- 练习时思路卡壳超过 5 分钟的地方

**记录格式（使用 `errorbox`）：**
```latex
\begin{errorbox}{年份/来源 - 错误类型}{colback=white}
\textbf{题目：}简述题目或关键词

\textbf{我的错误/卡壳：}具体描述

\textbf{错误类型：}\key{计算错误/概念错误/思路短路}

\textbf{正确解法：}正确思路

\textbf{教训：}\examnote{快速识别和预防方法}
\end{errorbox}
```

**错误类型分类：**
1. **计算错误** - 粗心、公式记错、积分限错误
2. **概念错误** - 误解物理概念、混淆相似公式
3. **思路短路** - 不知道从何入手、方法选择错误

### 发布检查清单

- [ ] 文章已保存到正确目录 `docs/posts/{category}/`
- [ ] 文章包含日期、标签、分类元信息
- [ ] **主页 Recent Articles 已更新**
- [ ] **文章列表页 `docs/posts/index.md` 已更新（⚠️ 必须在对应分类下添加新文章链接）**
- [ ] **⚠️ Daily Papers 主页 `docs/posts/paper-notes/index.md` 已更新** — 添加新 issue 或更新当前 issue 的论文列表
- [ ] 侧边栏配置已更新（如需要）
- [ ] Git 提交并推送到 main 分支

---

## 📄 PDF 文献处理规范

### 阅读深度要求（⚠️ 强制执行）

**禁止的行为：**
- ❌ **快速扫描** - 不能只看标题和摘要
- ❌ **跳过公式** - 必须阅读关键公式和推导
- ❌ **忽略图表** - 必须理解图注和图表内容
- ❌ **遗漏作者** - 必须提取完整作者列表和机构信息
- ❌ **简化方法** - 不能省略技术细节，要记录关键步骤

**必须完成：**
- ✅ **完整阅读摘要** - 提取背景、方法、结果、意义
- ✅ **通读引言** - 理解研究动机和核心问题
- ✅ **分析方法章节** - 理解技术路线和关键参数
- ✅ **识别核心结果** - 提取主要发现和创新点
- ✅ **理解图表** - 图题、坐标轴、数据趋势
- ✅ **提取完整元数据** - 标题、全部作者、年份、期刊、DOI

### PDF 类型处理

**文本版 PDF：**
```bash
pdftotext input.pdf output.txt
```

**扫描版 PDF：**
```bash
# 1. 检测（如果 pdftotext 输出为空则是扫描版）
pdftotext -f 1 -l 3 input.pdf - | head -5

# 2. 转为图片
mkdir -p /tmp/pdf_scan
pdftoppm -f 1 -l 5 -png input.pdf /tmp/pdf_scan/page

# 3. 逐个识别图片（使用图片阅读工具）
# 4. 清理
rm -rf /tmp/pdf_scan
```

### 文献报告格式

```markdown
## Paper #N: [完整标题]

**Authors**: [作者列表]  
**Journal**: [期刊] ([年份])  
**DOI**: [链接]  
**Key words**: [关键词]  
**Year**: [年份]

### Summary
[2-3句话概括核心贡献。数学符号用LaTeX，如$\pi$-energy, $Z_2$]

### Core Concepts
- **[概念]**: [详细解释，数学符号用$...$]
- **[概念2]**: [如$(d-2)$维，$\pi$模式等]

### Key Innovations
1. **[创新]**: [描述，如实现$>50$个Floquet周期]
2. **[创新2]**: [描述，如测量$\langle\Gamma(t)\rangle$]

### Technical Approach
- [方法细节，数学表达式用LaTeX]
- [如:$H=\hbar\omega_i n_i+\hbar J_{ij}(a_i^\dagger a_j+h.c.)$]

### Main Results
- [结果1，数值数据如$N_0=3.51$]
- [结果2，如能谱在$-\pi$到$\pi$范围]

### Reading Notes
- [ ] [待深入理解的问题]
```

**⚠️ 数学符号强制规范：**
- 所有数学符号必须用 LaTeX `$...$` 格式
- 希腊字母：`\pi`, `\alpha`, `\beta`, `\Gamma` 等
- 上下标：`^` 和 `_`，如 `$Z_0$`, `$U^n$`
- 特殊函数：`$\operatorname{tr}(U^n)$`, `$\langle\Gamma\rangle$`
- 乘号：`$6 \times 6$` 用 `\times`
- 不等式：`$>50$` 用 `$` 包裹

**⚠️ 禁止在博客中添加 PDF 文件链接 - 只提供 DOI/arXiv 外部链接**

## 开发命令

```bash
npm run docs:dev      # 本地预览
npm run docs:build    # 构建
npm run docs:preview  # 预览构建结果
```

## 部署

推送到 `main` 分支后，GitHub Actions 自动部署到 GitHub Pages。

网站地址：https://qimeng0103.github.io
