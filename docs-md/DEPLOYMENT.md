# Deployment

Build Output

- The production build writes to `docs/` (see `vue.config.js`).
- GitHub Pages can serve from the `docs/` folder of the `main` branch.

Steps

1. Build the site:
   - `npm run build`
2. Commit and push the updated `docs/` artifacts.
3. In the repository settings on GitHub:
   - Enable GitHub Pages
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/docs`

Base Path

- `publicPath` and router history are configured for `/portfolio/`.
- If the repo name or hosting path changes, update both:
  - `vue.config.js` (`publicPath`, `outputDir` if needed)
  - `src/router/index.js` (base passed to `createWebHashHistory`)

Local Preview of Build

- Serve `docs/` with any static server, for example:
  - `npx serve docs`
