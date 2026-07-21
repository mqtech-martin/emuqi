# emuqi.com — 木齐科技国际品牌站

## 项目背景

为山东木齐健康科技有限公司构建品牌国际站 `emuqi.com`，采用 GitHub Pages 静态站 + Ghost 内容站的混合架构。

**目标**: 低维护、高自动化、强 SEO、轻便更新

**负责人**: 陈滨 (Martin Chen)
- 清华大学 MBA
- 山东木齐健康科技 CEO
- 20 年营销管理与跨境贸易经验

**品牌定位**: 氢健康 · AI+制造 · 跨境贸易

## 技术架构

| 组件 | 技术 | 用途 |
|------|------|------|
| 主站 emuqi.com | GitHub Pages (HTML/CSS/JS) | 品牌展示、项目介绍 |
| 内容站 blog.emuqi.com | Ghost Pro | Blog/Vlog/Newsletter |
| 自动部署 | GitHub Actions | git push → 自动上线 |

## 自动化工作流

1. **策划**: Motion 选题规划
2. **开发**: MiMo Code 更新主站 → git push
3. **创作**: MiMo Code 生成 Ghost 草稿 → Ghost 发布
4. **分发**: Ghost Newsletter + X/Twitter 自动交叉引流

## 进度

- [x] SSH 密钥配置
- [x] GitHub 仓库创建
- [x] 项目备忘录
- [ ] 首页 index.html
- [ ] 关于页面 about.html
- [ ] 项目展示 projects.html
- [ ] 全局样式 style.css
- [ ] 交互脚本 script.js
- [ ] Ghost 文章模板
- [ ] GitHub Actions 部署
- [ ] 域名绑定 & 上线
