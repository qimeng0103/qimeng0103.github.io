# Articles

<style>
.article-index {
  margin-top: 32px;
}

.category-section {
  margin-bottom: 48px;
}

.category-section h2 {
  font-family: var(--vp-font-family-serif);
  font-size: 20px;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--vp-c-divider);
  letter-spacing: -0.01em;
}

.article-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.article-item {
  display: flex;
  align-items: baseline;
  gap: 20px;
  padding: 16px 0;
  border-bottom: 1px solid var(--vp-c-divider);
}

.article-item:last-child {
  border-bottom: none;
}

.article-date {
  font-family: var(--vp-font-family-mono);
  font-size: 13px;
  color: var(--vp-c-text-3);
  white-space: nowrap;
  min-width: 90px;
}

.article-title {
  font-family: var(--vp-font-family-serif);
  font-size: 16px;
  font-weight: 600;
}

.article-title a {
  color: var(--vp-c-text-1);
  text-decoration: none;
  border-bottom: none;
  transition: color 0.2s ease;
}

.article-title a:hover {
  color: var(--vp-c-brand-1);
}

.article-desc {
  font-size: 14px;
  color: var(--vp-c-text-3);
  margin-top: 4px;
}

.tag-list {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 32px;
  padding-top: 32px;
  border-top: 1px solid var(--vp-c-border);
}

.tag {
  font-family: var(--vp-font-family-mono);
  font-size: 12px;
  padding: 4px 10px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  color: var(--vp-c-text-3);
  text-decoration: none;
  transition: all 0.2s ease;
}

.tag:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg);
}

@media (max-width: 640px) {
  .article-item {
    flex-direction: column;
    gap: 4px;
  }
  
  .article-date {
    min-width: auto;
  }
}
</style>

<div class="article-index">

<div class="category-section">
  <h2>Technical Articles</h2>
  <ul class="article-list">
    <li class="article-item">
      <span class="article-date">2024-01-15</span>
      <div>
        <div class="article-title"><a href="./example">Mathematical Formulas and Code Examples</a></div>
        <div class="article-desc">Demonstration of LaTeX equations and syntax highlighting</div>
      </div>
    </li>
  </ul>
</div>

<div class="category-section">
  <h2>Research Notes</h2>
  <ul class="article-list">
    <!-- Add research notes here -->
  </ul>
</div>

<div class="tag-list">
  <span class="tag">research-notes</span>
  <span class="tag">technical</span>
  <span class="tag">tutorial</span>
  <span class="tag">literature</span>
</div>

</div>
