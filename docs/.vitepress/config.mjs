import { defineConfig } from 'vitepress'

// 你的 GitHub 用户名
const GITHUB_USERNAME = 'qimeng0103'

export default defineConfig({
  title: 'Qi Meng',
  titleTemplate: ':title | Research Blog',
  description: 'Qi Meng 的个人科研博客 - 凝聚态物理、量子计算与数值模拟',
  
  // 网站基础路径（用户/组织页面直接使用根路径）
  // base: '/',  // 如果使用自定义域名，取消注释这一行
  
  // 语言配置
  lang: 'zh-CN',
  
  // 最后更新时间
  lastUpdated: true,
  
  // 清理 URL（去掉 .html 后缀）
  cleanUrls: true,
  
  // Markdown 配置
  markdown: {
    math: true,
    lineNumbers: true,
    config: (md) => {
      // 可以在这里添加更多 Markdown 插件
    }
  },
  
  // 主题配置
  themeConfig: {
    // 站点标题（显示在导航栏）
    siteTitle: 'Qi Meng',
    
    // Logo
    logo: '/images/avatar.svg',
    
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
      message: '基于 VitePress 构建 | <a href="https://github.com/qimeng0103/qimeng0103.github.io">查看源码</a>',
      copyright: 'Copyright © 2024 Qi Meng. All Rights Reserved.'
    },
    
    // 搜索
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索',
            buttonAriaLabel: '搜索文档'
          },
          modal: {
            noResultsText: '未找到相关结果',
            resetButtonTitle: '清除搜索',
            footer: {
              selectText: '选择',
              navigateText: '切换',
              closeText: '关闭'
            }
          }
        }
      }
    },
    
    // 编辑链接
    editLink: {
      pattern: `https://github.com/${GITHUB_USERNAME}/${GITHUB_USERNAME}.github.io/edit/main/docs/:path`,
      text: '在 GitHub 上编辑此页'
    },
    
    // 大纲
    outline: {
      label: '本页目录',
      level: [2, 3]
    },
    
    // 文档页脚
    docFooter: {
      prev: '← 上一页',
      next: '下一页 →'
    },
    
    // 返回顶部
    returnToTopLabel: '↑ 返回顶部',
    
    // 侧边栏菜单
    sidebarMenuLabel: '菜单',
    
    // 暗色模式
    darkModeSwitchLabel: '🌓 主题',
    
    // 语言菜单
    langMenuLabel: '多语言',
    
    // 外部链接图标
    externalLinkIcon: true
  },
  
  // Head 配置
  head: [
    // Favicon
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    
    // 字体：Inter + JetBrains Mono
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { 
      rel: 'stylesheet', 
      href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;500;600;700&display=swap'
    }],
    
    // KaTeX CSS（用于数学公式）
    ['link', { 
      rel: 'stylesheet', 
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css'
    }],
    
    // Open Graph / 社交媒体
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Qi Meng | Research Blog' }],
    ['meta', { property: 'og:description', content: 'Qi Meng 的个人科研博客 - 凝聚态物理、量子计算与数值模拟' }],
    ['meta', { property: 'og:site_name', content: 'Qi Meng Research Blog' }],
    
    // Twitter Card
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'Qi Meng | Research Blog' }],
    ['meta', { name: 'twitter:description', content: 'Qi Meng 的个人科研博客 - 凝聚态物理、量子计算与数值模拟' }],
    
    // 作者信息
    ['meta', { name: 'author', content: 'Qi Meng' }],
    
    // 主题色
    ['meta', { name: 'theme-color', content: '#4f46e5' }],
    
    // 移动端优化
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no' }]
  ],
  
  // 构建配置
  build: {
    // 输出目录
    outDir: '.vitepress/dist',
    
    // 资源目录
    assetsDir: 'assets',
    
    // 是否生成 sitemap
    sitemap: {
      hostname: `https://${GITHUB_USERNAME}.github.io`
    }
  },
  
  // Vite 配置
  vite: {
    // 可以在这里添加 Vite 插件
    plugins: []
  }
})
