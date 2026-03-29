import { defineConfig } from 'vitepress'

// 你的 GitHub 用户名
const GITHUB_USERNAME = 'qimeng0103'

// 共享的搜索配置
const searchConfig = {
  provider: 'local',
  options: {
    locales: {
      root: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索文档' },
          modal: {
            noResultsText: '未找到相关结果',
            resetButtonTitle: '清除搜索',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' }
          }
        }
      },
      en: {
        translations: {
          button: { buttonText: 'Search', buttonAriaLabel: 'Search docs' },
          modal: {
            noResultsText: 'No results found',
            resetButtonTitle: 'Clear search',
            footer: { selectText: 'Select', navigateText: 'Navigate', closeText: 'Close' }
          }
        }
      }
    }
  }
}

export default defineConfig({
  // 最后更新时间
  lastUpdated: true,
  
  // 清理 URL
  cleanUrls: true,
  
  // Markdown 配置
  markdown: {
    math: true,
    lineNumbers: true,
  },
  
  // 国际化配置
  locales: {
    root: {
      label: '中文',
      lang: 'zh-CN',
      title: 'Qi Meng',
      titleTemplate: ':title | 科研博客',
      description: 'Qi Meng 的个人科研博客 - 凝聚态物理、量子计算与数值模拟',
      themeConfig: {
        siteTitle: 'Qi Meng',
        logo: '/images/avatar.svg',
        nav: [
          { text: '首页', link: '/' },
          { text: '文章', link: '/posts/' },
          { text: '关于', link: '/about' },
        ],
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
        footer: {
          message: '基于 VitePress 构建 | <a href="https://github.com/qimeng0103/qimeng0103.github.io">查看源码</a>',
          copyright: 'Copyright © 2024 Qi Meng. All Rights Reserved.'
        },
        outline: { label: '本页目录', level: [2, 3] },
        docFooter: { prev: '← 上一页', next: '下一页 →' },
        returnToTopLabel: '↑ 返回顶部',
        sidebarMenuLabel: '菜单',
        darkModeSwitchLabel: '🌓 主题',
        langMenuLabel: '🌐 语言',
      }
    },
    en: {
      label: 'English',
      lang: 'en-US',
      title: 'Qi Meng',
      titleTemplate: ':title | Research Blog',
      description: 'Qi Meng Research Blog - Condensed Matter Physics, Quantum Computing & Numerical Simulations',
      link: '/en/',
      themeConfig: {
        siteTitle: 'Qi Meng',
        logo: '/images/avatar.svg',
        nav: [
          { text: 'Home', link: '/en/' },
          { text: 'Articles', link: '/en/posts/' },
          { text: 'About', link: '/en/about' },
        ],
        sidebar: {
          '/en/posts/': [
            {
              text: 'Articles',
              items: [
                { text: 'Example: Formulas and Code', link: '/en/posts/example' },
              ]
            }
          ]
        },
        footer: {
          message: 'Built with VitePress | <a href="https://github.com/qimeng0103/qimeng0103.github.io">View Source</a>',
          copyright: 'Copyright © 2024 Qi Meng. All Rights Reserved.'
        },
        outline: { label: 'On this page', level: [2, 3] },
        docFooter: { prev: '← Previous', next: 'Next →' },
        returnToTopLabel: '↑ Back to Top',
        sidebarMenuLabel: 'Menu',
        darkModeSwitchLabel: '🌓 Theme',
        langMenuLabel: '🌐 Language',
      }
    }
  },
  
  // 主题配置（共享）
  themeConfig: {
    // 社交链接
    socialLinks: [
      { icon: 'github', link: `https://github.com/${GITHUB_USERNAME}` }
    ],
    
    // 搜索
    search: searchConfig,
    
    // 编辑链接
    editLink: {
      pattern: `https://github.com/${GITHUB_USERNAME}/${GITHUB_USERNAME}.github.io/edit/main/docs/:path`,
      text: 'Edit this page on GitHub'
    },
    
    // 外部链接图标
    externalLinkIcon: true
  },
  
  // Head 配置
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    
    // 字体
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { 
      rel: 'stylesheet', 
      href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;500;600;700&display=swap'
    }],
    
    // KaTeX CSS
    ['link', { 
      rel: 'stylesheet', 
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css'
    }],
    
    // Open Graph
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'Qi Meng Research Blog' }],
    
    // Twitter Card
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    
    // 作者信息
    ['meta', { name: 'author', content: 'Qi Meng' }],
    
    // 主题色
    ['meta', { name: 'theme-color', content: '#4f46e5' }],
    
    // 移动端优化
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no' }]
  ]
})
