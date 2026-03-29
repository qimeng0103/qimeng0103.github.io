# 我的个人科研博客

基于 [VitePress](https://vitepress.dev/) 构建的个人博客，支持数学公式、代码高亮和全文搜索。

## 功能特性

- ✅ **Markdown 原生支持** - 专注于内容创作
- ✅ **数学公式** - LaTeX 语法（行内和独立公式）
- ✅ **代码高亮** - 多语言支持，带行号
- ✅ **全文搜索** - 基于本地索引
- ✅ **响应式设计** - 适配各种设备
- ✅ **暗色/亮色主题** - 自动切换
- ✅ **GitHub Pages 自动部署**

## 快速开始

### 1. 配置 GitHub 信息

编辑 `docs/.vitepress/config.mjs`，修改以下内容：

```javascript
const GITHUB_USERNAME = 'qimeng0103'  // 修改这里
```

编辑 `docs/index.md`，修改个人信息：
- 名字
- 研究方向
- 联系方式

### 2. 本地预览

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run docs:dev
```

访问 http://localhost:5173 预览博客。

### 3. 编写文章

在 `docs/posts/` 目录下创建 Markdown 文件：

```markdown
---
title: 文章标题
date: 2024-01-15
---

# 文章标题

文章内容...
```

### 4. 部署到 GitHub Pages

#### 方法一：GitHub Actions 自动部署

1. 在 GitHub 创建仓库 `qimeng0103.github.io`
2. 将代码推送到仓库
3. 在仓库设置中启用 GitHub Pages（选择 GitHub Actions 源）
4. 推送后会自动构建并部署

#### 方法二：手动部署

```bash
# 构建
npm run docs:build

# 将 docs/.vitepress/dist 目录内容推送到 gh-pages 分支
```

## 文章模板

```markdown
# 文章标题

## 数学公式

行内公式：$E = mc^2$

独立公式：
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

## 代码块

```python
def hello():
    print("Hello, World!")
```

## 图片

![描述](/images/your-image.png)

## 参考

- [链接1](https://example.com)
- [链接2](https://example.com)
```

## 常用命令

| 命令 | 说明 |
|------|------|
| `npm run docs:dev` | 启动开发服务器 |
| `npm run docs:build` | 构建生产版本 |
| `npm run docs:preview` | 本地预览生产版本 |

## 目录结构

```
my-blog/
├── docs/                     # 文档根目录
│   ├── .vitepress/          # VitePress 配置
│   │   ├── config.mjs       # 主配置文件
│   │   └── theme/           # 自定义主题
│   ├── posts/               # 博客文章
│   ├── images/              # 图片资源
│   ├── index.md             # 首页
│   └── about.md             # 关于页面
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions 部署
└── package.json
```

## 参考文档

- [VitePress 文档](https://vitepress.dev/)
- [Markdown 扩展](https://vitepress.dev/guide/markdown)
- [KaTeX 支持的符号](https://katex.org/docs/supported.html)

---

如有问题，欢迎提交 Issue 或 PR！
