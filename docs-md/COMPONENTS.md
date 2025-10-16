# Components Overview

App and Bootstrapping

- `src/App.vue` — Root component, renders `NavBar` and main router view.
- `src/main.js` — App bootstrap, installs router and mounts the app.
- `src/router/index.js` — Routes (`/`, `/projects`, `/blogs`, `/github`, `/about`), hash history.

Layout and Navigation

- `src/components/NavBar.vue` — Responsive navigation bar, controls route changes and section scrolling.
- `src/components/LandingPage.vue` — Two-column layout: left intro panel, right dynamic section container.
- `src/components/PortfolioPage.vue` — Legacy/simple page rendering the project landing component.

Sections

- `src/components/sections/IntroSection.vue` — Intro card with basic profile and links.
- `src/components/sections/ProjectsSection.vue` — Projects listing with tag-based tabs; owns `allProjects` data.
- `src/components/sections/BlogsSection.vue` — Blog list, loads entries from `src/assets/blogs/blogs.json` and sorts by date.
- `src/components/sections/GithubSection.vue` — GitHub stats section.
- `src/components/sections/ToolsSection.vue` — Static tool cards with icons in `src/assets/tools`.
- `src/components/sections/AboutSection.vue` — About content (HTML strings).

Project Subcomponents

- `src/components/sections/project/TabsComponent.vue` — Tag tabs + filter logic.
- `src/components/sections/project/LandingComponent.vue` — Project cards/grid rendering for `projectList`.
- `src/components/sections/project/ProjectComponent.vue` — Individual project card.
