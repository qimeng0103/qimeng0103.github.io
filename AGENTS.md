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

### 添加/修改文章时必须同步更新以下文件

1. **`docs/index.md`** - 主页 Recent Articles 部分
   - 添加新文章条目到列表顶部
   - 保持最多 4-5 篇最新文章
   - 按日期倒序排列

2. **`docs/posts/index.md`** - 文章列表页（如需要）
   - 添加新文章到对应分类

3. **`docs/.vitepress/config.mjs`** - 侧边栏配置（如添加新分类）
   - 在 sidebar 中添加新文章链接

4. **`tex/exam-prep/ustc-phd-prep.tex`** - 备考 PDF（如相关内容适合放入）
   - 将 Blog 文章的核心结论提取到 PDF 对应章节
   - 在 Appendix 添加详细推导（如需要）
   - **⚠️ 编译 PDF 并更新网页链接：**
     ```bash
     cd tex/exam-prep
     xelatex ustc-phd-prep.tex              # 编译生成 PDF
     cp ustc-phd-prep.pdf ../../docs/public/exam-prep/  # 复制到网站目录
     ```
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
- [ ] 文章列表页已更新（如需要）
- [ ] 侧边栏配置已更新（如需要）
- [ ] Git 提交并推送到 main 分支

## 开发命令

```bash
npm run docs:dev      # 本地预览
npm run docs:build    # 构建
npm run docs:preview  # 预览构建结果
```

## 部署

推送到 `main` 分支后，GitHub Actions 自动部署到 GitHub Pages。

网站地址：https://qimeng0103.github.io
