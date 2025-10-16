# Development

Prerequisites

- Node.js v20 (recommended)
- npm

Setup

1. Install dependencies:
   - `npm install`
2. Run in development:
   - `npm run serve`
3. Lint code:
   - `npm run lint`
4. Build for production:
   - `npm run build`

Conventions

- Vue single-file components live under `src/components` and `src/components/sections`.
- Keep section-specific data close to its component (current pattern).
- Prefer assets under `src/assets/...` and reference them via relative paths in components.

Notes

- Build output goes to `docs/` (configured in `vue.config.js`). Do not hand-edit files there.
- Router uses hash history with base `'/portfolio/'`, which aligns with GitHub Pages hosting.
