# Blog Writer Skill

## 任务
为 my-blog 项目编写和发布科研博客文章。

## 项目结构

本项目采用 **双轨制** 内容管理：

```
my-blog/
├── docs/posts/           # Blog 文章（英文，公开）
│   ├── quantum-mechanics/
│   ├── condensed-matter/
│   └── ...
├── tex/exam-prep/        # 备考 PDF（中文，内部）
│   ├── preamble.tex      # 导言区配置
│   └── ustc-phd-prep.tex # 主文件
└── ...
```

### 双轨制说明

| 维度 | Blog (`docs/posts/`) | TeX PDF (`tex/exam-prep/`) |
|------|---------------------|---------------------------|
| **语言** | 英文 | 中文 + 英文术语备注 |
| **受众** | 公开，学术社区 | 个人备考 |
| **内容** | 详细推导 + 概念启发 | 核心结论 + 解题技巧 + 附录推导 |
| **排版** | Markdown，单栏 | LaTeX，双栏高密度 |
| **视觉** | 简洁 | Beamer 风格彩色框 |

## 核心规则

### 1. 添加/修改文章时必须同步更新多个文件

**Blog 更新后，视内容相关性同步更新 `tex/exam-prep/ustc-phd-prep.tex`。**

**必须同步的文件：**
- ✅ `docs/index.md` - 主页 Recent Articles
- ✅ `docs/posts/index.md` - 文章列表页（如需要）
- ✅ `docs/.vitepress/config.mjs` - 侧边栏（如新分类）
- ⚠️ `tex/exam-prep/ustc-phd-prep.tex` - 备考 PDF（如相关内容适合考试复习）

主页 Recent Articles 格式：
```html
<div class="latest-articles">
  <h2>Recent Articles</h2>
  
  <div class="article-entry">
    <div class="article-date">YYYY-MM-DD</div>
    <div class="article-info">
      <h3><a href="/posts/category/article-slug">Article Title</a></h3>
      <p>Brief description of the article content</p>
    </div>
  </div>
  
  <!-- 最多显示 4-5 篇最新文章，按日期倒序排列 -->
</div>
```

### 2. 文章元信息格式

每篇文章开头必须包含日期和标签：
```markdown
# Article Title

📅 **Date:** YYYY-MM-DD | 🏷️ **Tags:** Tag1, Tag2 | 📂 **Category:** Category Name

---

## Introduction
...
```

### 3. 同步更新 TeX 备考资料（如适用）

当 Blog 文章包含适合考试复习的内容时，提取核心信息到 `tex/exam-prep/ustc-phd-prep.tex`：

**完整工作流程：**

```bash
# Step 1: 编辑 tex 文件
cd tex/exam-prep
vim ustc-phd-prep.tex  # 添加新内容到对应章节

# Step 2: 编译 PDF
xelatex ustc-phd-prep.tex
# 如有交叉引用，需编译两次：
# xelatex ustc-phd-prep.tex && xelatex ustc-phd-prep.tex

# Step 3: 复制 PDF 到网站目录
cp ustc-phd-prep.pdf ../../docs/public/exam-prep/

# Step 4: 更新 about.md 中的日期
cd ../..
date=$(date +%Y-%m-%d)
# 修改 docs/about.md 中的 "Last updated: YYYY-MM-DD"

# Step 5: Git 提交
git add docs/about.md docs/public/exam-prep/ustc-phd-prep.tex tex/exam-prep/ustc-phd-prep.tex
git commit -m "tex: add XXX content and update PDF (updated: $date)"
git push origin main
```

**提取原则：**
- **正文部分（双栏）：** 核心公式、解题套路、二级结论、快速识别方法
- **附录部分：** 完整推导、详细理解、长难推导过程

**TeX 框类型选择（Beamer 风格）：**
```latex
\begin{modelbox}[物理模型名]
% 蓝色框 - 物理定理和模型
核心结论 + 物理图像 + 考试触发词
\end{modelbox}

\begin{tipbox}[题型/技巧名]
% 红色框 - 解题技巧和识别方法
快速识别特征 + 决策树 + 解题步骤
\end{tipbox}

\begin{formulabox}[公式名]
% 绿色框 - 重要公式和二级结论
公式 + 物理意义 + 使用条件
\end{formulabox}

\begin{warnbox}[常见陷阱]
% 橙色框 - 易错点和警示
典型错误 + 避免方法 + 单位陷阱
\end{warnbox}

\begin{insightbox}[概念理解]
% 紫色框 - 物理图像和直观理解
物理本质 + 类比 + 记忆技巧
\end{insightbox}

\begin{cheatbox}[速查备忘]
% 黄色框 - 快速参考列表
对易关系 / 常用积分 / 常数值
\end{cheatbox}

\begin{derivationbox}[推导名]
% 灰色框 - 附录详细推导（放在 \appendix 部分）
完整数学推导过程，逐步展开
\end{derivationbox}

\begin{errorbox}{题目来源 - 错误类型}{colback=white}
% 深红色框 - 错题与思路短路（最醒目，警示性最强）
\textbf{题目：}简述题目内容或关键词

\textbf{我的错误/卡壳：}描述具体错误

\textbf{错误类型：}\key{计算错误/概念错误/思路短路}

\textbf{正确解法：}正确的思路或公式

\textbf{教训：}\examnote{如何避免类似错误}
\end{errorbox}

\begin{thinkbox}[解题思路模板]
% 青色框 - 解题技巧总结
\textbf{步骤 1 - XXXX：}...
\end{thinkbox}
```

**英文术语标注命令：**
```latex
% 在中文文本中标注英文术语
Bloch 定理（\en{Bloch's theorem}）描述了...

% 重要强调
\key{关键概念}

% 考试提醒
\examnote{看到 XX 立即写 YY}
```

**编译命令：**
```bash
cd tex/exam-prep
pdflatex ustc-phd-prep.tex
```

### 4. 检查清单（发布前必做）

Blog 更新：
- [ ] 文章已保存到 `docs/posts/{category}/article-slug.md`
- [ ] 文章开头包含日期、标签、分类信息（英文）
- [ ] **主页 `docs/index.md` 的 Recent Articles 已更新**
- [ ] **文章列表页 `docs/posts/index.md` 已更新（如需要）**
- [ ] 侧边栏配置 `docs/.vitepress/config.mjs` 已更新（如需要）

TeX 更新（如适用）：
- [ ] 核心结论已提取到 `tex/exam-prep/ustc-phd-prep.tex`
- [ ] 使用了正确的颜色框类型
- [ ] 英文术语已用 `\en{}` 标注
- [ ] 详细推导已添加到 Appendix（如需要）
- [ ] **错题/思路短路已记录到 "错题与思路短路库" 章节（如适用）**
- [ ] PDF 编译成功无错误 (`xelatex ustc-phd-prep.tex`)
- [ ] PDF 已复制到 `docs/public/exam-prep/ustc-phd-prep.pdf`
- [ ] about.md 中的 `Last updated` 日期已更新为当前日期

Git：
- [ ] 提交信息清晰描述更改（如 "blog: add Bloch theorem; tex: add to model section"）
- [ ] 推送到 origin main
- [ ] 检查网站部署状态

### 5. 文件位置

```
docs/posts/
├── quantum-mechanics/
│   ├── stationary-perturbation-theory.md
│   └── time-dependent-perturbation-theory.md
├── condensed-matter/
│   ├── green-functions-quantum-transport.md
│   └── phonons-lattice-dynamics.md
└── index.md              # 文章列表页

docs/index.md             # 主页（必须更新 Recent Articles）
docs/.vitepress/config.mjs # 侧边栏配置（如添加新分类）
tex/exam-prep/            # 备考 PDF 目录
├── preamble.tex          # 导言区（颜色、框定义）
└── ustc-phd-prep.tex     # 主文件
```

### 6. 数学公式规范

Blog (Markdown)：
- 行内公式：`$E = mc^2$`
- 独立公式：
  ```markdown
  $$
  \egin{aligned}
  \hat{H}\psi &= E\psi \\
  E_n &= \hbar\omega(n+1/2)
  \end{aligned}
  $$
  ```

TeX (LaTeX)：
- 使用 `aligned` 环境对齐多行公式
- 使用 `\[` `\]` 代替 $$ 以获得正确间距
- 矢量用 `\mathbf{k}`，算符用 `\hat{H}`

### 7. Git 工作流

```bash
# 添加所有更改
# Blog 文章 + 主页更新
git add docs/posts/category/new-article.md docs/index.md

# 如同时更新 TeX
git add tex/exam-prep/ustc-phd-prep.tex

# 提交
git commit -m "blog: add Bloch theorem article; tex: update model section

- Add detailed derivation of Bloch theorem
- Include physical interpretation and exam tips
- Add to TeX modelbox with quick recognition guide"

git push origin main
```

## 参考示例

Blog 文章：
- `docs/posts/quantum-mechanics/stationary-perturbation-theory.md`
- `docs/posts/condensed-matter/green-functions-quantum-transport.md`

TeX PDF 框示例：
- `tex/exam-prep/ustc-phd-prep.tex` 中的 `modelbox`, `tipbox` 等
