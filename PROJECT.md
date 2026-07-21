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
- [x] 首页 index.html
- [x] 关于页面 about.html
- [x] 产品总览 products.html
- [x] 氢气陶瓷球 hydrogen-ceramic-ball.html
- [x] 抗菌陶瓷球 maca-kdf-ceramic-ball.html
- [x] MPH+中和球 mph-condensate-neutralizer.html
- [x] 应用概览 application.html
- [x] 解决方案 solutions.html
- [x] 博客列表 blog.html
- [x] 联系页面 contact.html
- [x] 全局样式 style.css
- [x] 交互脚本 script.js
- [x] Ghost 文章模板
- [x] GitHub Actions 自动部署
- [ ] 批量替换域名（emuqi.com → GitHub Pages）
- [ ] 配置自定义域名（emuqi.com CNAME 指向 GitHub Pages）
- [ ] 应用详情页（5个子页面）
- [ ] Ghost 博客上线
