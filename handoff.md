# Portfolio - Project Handoff

## Overview

**Portfolio** is a responsive portfolio website built with Vue 3 and Element Plus UI library. It's designed to showcase the owner's machine learning engineering skills, projects, and experience.

## Tech Stack

- **Framework**: Vue 3 (Composition API)
- **UI Library**: Element Plus
- **Router**: Vue Router 4
- **Build Tool**: Vue CLI (Webpack)
- **Styling**: SCSS + Element Plus components

## Project Structure

```
portfolio/
├── src/
│   ├── main.js              # Entry point
│   ├── App.vue              # Root component
│   ├── router/
│   │   └── index.js        # Vue Router configuration
│   ├── components/         # Vue components
│   ├── assets/             # Static assets (images, styles)
│   └── ...
├── public/                 # Static public assets
├── docs/                   # Documentation
├── docs-md/               # Markdown documentation
├── package.json
├── vue.config.js          # Vue CLI configuration
├── babel.config.js        # Babel configuration
├── .eslintrc.js           # ESLint configuration
└── README.md
```

## Getting Started

```bash
cd /Users/str/Projects/portfolio

# Install dependencies
npm install

# Run development server
npm run dev
# Opens at http://localhost:8080/

# Build for production
npm run build

# Lint code
npm run lint
```

## Environment

- **Node Version**: Recommended Node v20
- **No API keys required**
- **No backend** - Static site

## Configuration

### Vue Config (vue.config.js)
- `homepage`: Set to `/portfolio/` for GitHub Pages deployment

### Element Plus
The project uses Element Plus components throughout. Key components:
- Cards for project showcase
- Buttons for navigation
- Forms for contact (if applicable)
- Timeline for experience

## Deployment

### GitHub Pages
```bash
npm run build
# Deploy the dist/ folder to GitHub Pages
```

The `homepage` field in `package.json` is set to `/portfolio/` for GitHub Pages deployment.

## Dependencies

### Production
- vue: ^3.2.13
- vue-router: ^4.2.5
- element-plus: ^2.4.4
- core-js: ^3.8.3

### Development
- @vue/cli-service: ^5.0.8
- sass: ^1.77.0
- eslint: ^7.32.0

## Important Files

- `src/App.vue` - Root component with layout
- `src/main.js` - Application entry point
- `src/router/index.js` - Route definitions
- `vue.config.js` - Build configuration

## Customization

To use as your own portfolio:

1. Update content in components
2. Modify `src/assets/` with your images
3. Update personal information
4. Adjust colors/theme via Element Plus overrides
5. Build and deploy

## Notes for AI Agents

- This is a static Vue 3 SPA - no backend required
- Uses Element Plus for UI components
- SCSS for custom styling
- Simple project structure - easy to modify
- Can be deployed to any static hosting (Netlify, Vercel, GitHub Pages)
- The `docs-md/` folder may contain additional documentation
- Designed to be easily customizable for different portfolios
