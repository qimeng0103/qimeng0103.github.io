import { defineConfig } from 'vitepress'

// 你的 GitHub 用户名（请修改这里）
const GITHUB_USERNAME = 'qimeng0103'

export default defineConfig({
  title: '我的科研博客',
  description: "Qi Meng's research notes, tech articles and learning insights"
  base: `/${GITHUB_USERNAME}.github.io/`,
  
  // 语言配置
  lang: 'zh-CN',
  
  // Markdown 配置
  markdown: {
    math: true,
    lineNumbers: true,
  },
  
  // 主题配置
  themeConfig: {
    // 导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '文章', link: '/posts/' },
      { text: '关于', link: '/about' },
    ],
    
    // 侧边栏
    sidebar: {
      '/posts/': [
        {
          text: '文章列表',
          items: [
            { text: '示例文章：公式与代码', link: '/posts/example' },
          ]
        }
      ]
    },
    
    // 社交链接
    socialLinks: [
      { icon: 'github', link: `https://github.com/${GITHUB_USERNAME}` }
    ],
    
    // 页脚
    footer: {
      message: '基于 VitePress 构建',
      copyright: 'Copyright © 2024'
    },
    
    // 搜索
    search: {
      provider: 'local'
    },
    
    // 编辑链接
    editLink: {
      pattern: `https://github.com/${GITHUB_USERNAME}/${GITHUB_USERNAME}.github.io/edit/main/docs/:path`,
      text: '在 GitHub 上编辑此页'
    },
    
    // 大纲
    outline: {
      label: '本页目录'
    },
    
    // 文档页脚
    docFooter: {
      prev: '上一页',
      next: '下一页'
    },
    
    // 返回顶部
    returnToTopLabel: '返回顶部',
    
    // 菜单
    sidebarMenuLabel: '菜单',
    
    // 暗色模式
    darkModeSwitchLabel: '主题',
  },
  
  // Head 配置
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    // KaTeX CSS（用于数学公式）
    ['link', { 
      rel: 'stylesheet', 
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css'
    }],
  ],
  
  // 最后更新时间
  lastUpdated: true,
})
