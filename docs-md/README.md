# Developer Docs

This folder contains maintainable Markdown docs for the Vue 3 portfolio project. It is separate from the production `docs/` directory, which is the build output configured in `vue.config.js`.

Contents:

- Architecture: `docs-md/ARCHITECTURE.md`
- Development: `docs-md/DEVELOPMENT.md`
- Deployment: `docs-md/DEPLOYMENT.md`
- Content Guide: `docs-md/CONTENT_GUIDE.md`
- Components Overview: `docs-md/COMPONENTS.md`

Notes:

- Do not add Markdown files to `docs/` — that directory is overwritten on build (`npm run build`).
- Reference images from `src/assets/...` when documenting features.
