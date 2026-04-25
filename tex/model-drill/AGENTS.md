# model-drill/ Agent Instructions

## 死命令：版本控制

**每次对 `.tex` 文件或 `preamble.tex` 做任何修改后，必须立即执行 `git add` 和 `git commit`。**

这是硬性要求，没有例外。包括但不限于：
- 新增、删除或修改模型内容
- 调整公式、表格、列表
- 修改 `preamble.tex` 中的宏包或环境定义
- 编译测试（即使只是生成 `.pdf`）

### 具体操作流程

```bash
cd /home/mengq8/my-blog
# 1. 添加变更
git add tex/model-drill/
# 2. 提交（写明修改内容）
git commit -m "<修改说明>"
```

如果修改范围很小（单文件、单模型），可以只添加该文件：

```bash
git add tex/model-drill/models/xxx.tex
git commit -m "add: <模型名称> - <具体内容>"
```

### 为什么这是死命令

`model-drill.tex` 及其子文件是**未提交的本地修改**，`git checkout` 或任何覆盖操作会**永久丢失**这些改动且无法通过 `git reflog` 恢复。

**永远不要假设 "这次改一点点没关系"。**

## 编译规范

- 编译器：`xelatex`（必须，用于 CJK 字体支持）
- 每次内容修改后应重新编译验证
- 编译产物（`.aux`, `.toc`, `.log`, `.out`）可保留，但**不应提交 `.pdf` 到 git**

## 文件结构

| 文件/目录 | 说明 |
|-----------|------|
| `model-drill.tex` | 主文档，包含 Part 划分和 `\input{}` 调用 |
| `preamble.tex` | 导言区，宏包、环境定义、颜色设置 |
| `models/` | 模型子文件目录，每个模型一个 `.tex` 文件 |
| `models/template-model.tex` | 模板文件，复制后重命名使用 |

## 新增模型的标准流程

1. 复制 `models/template-model.tex` 为 `models/<model-name>.tex`
2. 按模板中的 7 个模块填写内容
3. 在 `model-drill.tex` 的对应 Part 下添加 `\input{models/<model-name>}`
4. 编译验证：`xelatex model-drill.tex`
5. **立即 git commit**

## 模型内容规范

每个模型必须包含以下模块（按 template-model.tex）：
1. **模型定义框**（`modelbox`）：哈密顿量、参数、边界条件
2. **关键公式框**（`formulabox`）：必须能独立推导的核心公式
3. **训练点框**（`drillbox`）：考法变体、常见组合
4. **技巧框**（`tipbox`）：快速识别标志、解题捷径
5. **易错框**（`errorbox`）：常见失误、边界条件遗漏
6. **洞察框**（`insightbox`）：物理图像、与相似模型的对比
7. **推导附录**（`derivationbox`，可选）：供自我检验的详细推导
