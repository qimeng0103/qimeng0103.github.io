# tex/exam-prep/ Agent Instructions

## 死命令：版本控制

**每次对 `.tex` 文件或 `preamble.tex` 做任何修改后，必须立即执行 `git add` 和 `git commit`。**

这是硬性要求，没有例外。包括但不限于：
- 新增、删除或修改章节内容
- 调整公式、表格、列表
- 修改 `preamble.tex` 中的宏包或环境定义
- 编译测试（即使只是生成 `.pdf`）

### 具体操作流程

```bash
cd /home/mengq8/my-blog
# 1. 添加变更
git add tex/exam-prep/
# 2. 提交（写明修改内容）
git commit -m "<修改说明>"
```

如果修改范围很小（单文件、单章节），可以只添加该文件：

```bash
git add tex/exam-prep/ustc-phd-prep.tex
git commit -m "fix: <具体说明>"
```

### 为什么这是死命令

`ustc-phd-prep.tex` 及其子文件是**未提交的本地修改**，`git checkout` 或任何覆盖操作会**永久丢失**这些改动且无法通过 `git reflog` 恢复。历史已经证明：一次疏忽的 `git checkout` 曾导致约 5000 行本地修改全部丢失，不得不从 128 页 PDF 手动重建。

**永远不要假设 "这次改一点点没关系"。**

## 编译规范

- 编译器：`xelatex`（必须，用于 CJK 字体支持）
- 每次内容修改后应重新编译验证
- 编译产物（`.aux`, `.toc`, `.log`, `.out`）可保留，但**不应提交 `.pdf` 到 git**（PDF 通过 `docs/public/` 同步即可）

## 文件结构

| 文件 | 说明 |
|------|------|
| `ustc-phd-prep.tex` | 主文档，包含 Part 划分和 `\input{}` 调用 |
| `preamble.tex` | 导言区，宏包、环境定义、颜色设置 |
| `sec06.tex` ~ `sec14.tex`, `sec23.tex` | 各章节子文件，通过 `\input{}` 插入主文档 |

## 修改注意事项

- 新增章节时，在 `ustc-phd-prep.tex` 的合适位置插入 `\input{secXX}`
- 章节子文件应自包含，不依赖特定页码或分页
- 使用标准 LaTeX 环境（`section/subsection`, `align*`, `itemize/enumerate`）
- 若需自定义环境，优先在 `preamble.tex` 中定义，保持子文件简洁
