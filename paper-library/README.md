# Paper Library - Daily Collection Mode

> 今日合集模式：所有文献放在同一篇博客里，满了手动开下期

## 工作流

```
papers/                   # 放入文件（自动删除）
├── paper1.pdf
├── paper2.pdf  
└── arxiv.txt

./lib add papers/*        # 全部加入今日合集

生成：docs/posts/paper-notes/YYYY-MM-DD-issue-N.md

Paper #1: xxx
Paper #2: xxx
Paper #3: xxx
...

满了？→ ./lib close      # 关闭本期，下期自动新开
```

## 命令

```bash
# 添加文献到今日合集
./lib add papers/*.pdf           # 批量PDF
./lib add paper.pdf              # 单个PDF
./lib arxiv 2404.12345           # arXiv ID

# 查看状态
./lib status                     # 本期收录了几篇

# 满了一期
./lib close                      # 关闭本期，下次自动开新
```

## 今日合集格式

```markdown
# Daily Papers - 2026-04-09 (Issue #1)

## Paper #1: Topological Insulators Review
**Domain**: `topology`  
**Why collected**: (填写)

## Paper #2: Majorana Fermions
**Domain**: `superconductivity`  
**Why collected**: (填写)

*Issue status: 🟢 Open (accepting more papers)*
```

## 特点

- ✅ 多篇文献在同一博客文章（一期）
- ✅ 自动编号 Paper #1, #2, #3...
- ✅ 满了手动 `close`，下期自动新开
- ✅ 每篇保留：领域 + 收藏理由 + 审美标签
- ✅ 同时维护 BibTeX

## 分类（英文）

topology, superconductivity, quantum-info, many-body, qft-cmt, transport, magnetism, cold-atom, graphene-2d, numerics, cft-holography, general
