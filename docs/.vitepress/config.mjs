import { defineConfig } from 'vitepress'

// Your GitHub username
const GITHUB_USERNAME = 'qimeng0103'

// Shared search configuration
const searchConfig = {
  provider: 'local',
  options: {
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

export default defineConfig({
  // Last updated
  lastUpdated: true,
  
  // Clean URLs
  cleanUrls: true,
  
  // Language
  lang: 'en-US',
  title: 'Qi Meng',
  titleTemplate: ':title | Research Blog',
  description: 'Qi Meng Research Blog - Condensed Matter Physics, Quantum Computing & Numerical Simulations',
  
  // Markdown config
  markdown: {
    math: true,
    lineNumbers: true,
  },
  
  // Theme config
  themeConfig: {
    siteTitle: 'Qi Meng',
    
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Articles', link: '/posts/' },
      { text: 'About', link: '/about' },
    ],
    
    sidebar: {
      '/posts/': [
        {
          text: 'Articles',
          items: [
            { text: 'Example: Formulas and Code', link: '/posts/example' },
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
    darkModeSwitchLabel: 'Theme',
    
    // Social links
    socialLinks: [
      { icon: 'github', link: `https://github.com/${GITHUB_USERNAME}` }
    ],
    
    // Search
    search: searchConfig,
    
    // Edit link
    editLink: {
      pattern: `https://github.com/${GITHUB_USERNAME}/${GITHUB_USERNAME}.github.io/edit/main/docs/:path`,
      text: 'Edit this page on GitHub'
    },
    
    // External link icon
    externalLinkIcon: true
  },
  
  // Head config
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    
    // Fonts - Academic style (serif headings + sans-serif body)
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { 
      rel: 'stylesheet', 
      href: 'https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@400;600;700&family=Source+Sans+Pro:wght@400;600&family=JetBrains+Mono:wght@400;500&display=swap'
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
    
    // Author
    ['meta', { name: 'author', content: 'Qi Meng' }],
    
    // Theme color - Deep navy blue
    ['meta', { name: 'theme-color', content: '#1a365d' }],
    
    // Mobile viewport
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no' }]
  ]
})
