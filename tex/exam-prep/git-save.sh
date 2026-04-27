#!/bin/bash
# 考试资料快速保存脚本
# 用法: ./git-save.sh "提交信息"

MSG="${1:-更新备考资料 $(date +%Y-%m-%d %H:%M)}"

echo "=== Git 快速保存 ==="
echo "提交信息: $MSG"

# 添加源文件（忽略编译产物）
git add preamble.tex ustc-phd-prep.tex sec*.tex AGENTS.md 2>/dev/null

# 检查是否有变更要提交
if git diff --cached --quiet; then
    echo "没有新变更需要提交"
    exit 0
fi

# 提交
git commit -m "$MSG"
echo "已提交到本地"

# 可选：推送（注释掉，需要时手动执行）
# git push
echo "如需推送: git push"
