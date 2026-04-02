# Blog Writer Skill

## 任务
为 my-blog 项目编写和发布科研博客文章。

## 核心规则

### 1. 添加/修改文章时必须同步更新主页

**每次添加或修改文章后，必须更新 `docs/index.md` 中的 Recent Articles 部分。**

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

### 3. 检查清单（发布前必做）

- [ ] 文章已保存到 `docs/posts/{category}/article-slug.md`
- [ ] 文章开头包含日期、标签、分类信息
- [ ] **主页 `docs/index.md` 的 Recent Articles 已更新**
- [ ] **文章列表页 `docs/posts/index.md` 已更新（如需要）**
- [ ] 侧边栏配置 `docs/.vitepress/config.mjs` 已更新（如需要）
- [ ] Git 提交信息清晰描述更改
- [ ] 推送到 origin main 后检查部署状态

### 4. 文件位置

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
```

### 5. 数学公式规范

- 行内公式：`$E = mc^2$`
- 独立公式：
  ```markdown
  $$
  \hat{H}\psi = E\psi
  $$
  ```
- 多行对齐使用 `aligned` 环境

### 6. Git 工作流

```bash
# 添加所有更改（包括主页更新）
git add docs/posts/category/new-article.md docs/index.md
git commit -m "docs: add article about XXXX and update homepage"
git push origin main
```

## 参考示例

参见已发布的文章：
- `docs/posts/quantum-mechanics/stationary-perturbation-theory.md`
- `docs/posts/condensed-matter/green-functions-quantum-transport.md`
