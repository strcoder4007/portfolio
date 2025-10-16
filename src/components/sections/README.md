# Sections

Rendered inside `LandingPage.vue` based on the current route.

- `IntroSection.vue` — left-side intro panel.
- `ProjectsSection.vue` — projects list with filters.
  - `project/TabsComponent.vue` — tag tabs and filter control.
  - `project/LandingComponent.vue` — grid/cards layout for projects.
  - `project/ProjectComponent.vue` — project card.
- `BlogsSection.vue` — blogs rendered from `src/assets/blogs/blogs.json`.
- `GithubSection.vue` — GitHub stats section.
- `AboutSection.vue` — about content as HTML strings.
- `ToolsSection.vue` — static tools grid.
