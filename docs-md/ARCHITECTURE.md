# Architecture

Overview

- Framework: Vue 3 + Vue Router + Element Plus
- Build output: `docs/` (for GitHub Pages) via `vue.config.js`
- Router: hash history with base `'/portfolio/'`
- Content sources:
  - Projects are defined inline in `src/components/sections/ProjectsSection.vue`
  - Blogs are defined in `src/assets/blogs/blogs.json`

Directory Layout (key paths)

- App shell: `src/App.vue`, `src/main.js`
- Routing: `src/router/index.js`
- Top-level views: `src/components/LandingPage.vue`, `src/components/PortfolioPage.vue`
- Sections: `src/components/sections/*`
  - Projects: `ProjectsSection.vue` (+ `project/TabsComponent.vue`, `project/LandingComponent.vue`)
  - Blogs: `BlogsSection.vue`
  - About: `AboutSection.vue`
  - Github: `GithubSection.vue`
  - Tools: `ToolsSection.vue`
- Navigation: `src/components/NavBar.vue`
- Assets: `src/assets/{fonts,icons,portrait,projects,tools,blogs}`

Routing

- Hash-based routes (`createWebHashHistory('/portfolio/')`) all render `LandingPage.vue`, which conditionally shows sections and scrolls into view.
- Paths configured: `/`, `/projects`, `/blogs`, `/github`, `/about`.

State and Data

- Projects: an array `allProjects` is declared inside `ProjectsSection.vue` and filtered by tab selection.
- Blogs: an array loaded from `src/assets/blogs/blogs.json`, sorted by date in `BlogsSection.vue`.
- About content: HTML strings defined in `AboutSection.vue`.

Styling

- Scoped styles in each component, with some shared fonts from `src/assets/fonts`.
- Element Plus provides layout and UI primitives (e.g., `el-row`, `el-col`).
