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

### 文章格式规范

```markdown
# 文章标题

📅 **Date:** YYYY-MM-DD | 🏷️ **Tags:** Tag1, Tag2 | 📂 **Category:** Category Name

---

## Introduction

文章内容，支持 LaTeX 数学公式：
- 行内：$E = mc^2$
- 独立：
  $$
  \hat{H}\psi = E\psi
  $$
```

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
