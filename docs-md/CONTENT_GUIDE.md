# Content Guide

Projects

- File: `src/components/sections/ProjectsSection.vue`
- Add entries to the `allProjects` array with fields:
  - `id`: stable string identifier (UUID or unique string)
  - `name`: project title
  - `images`: array of image URLs or asset names placed under `src/assets/projects`
  - `tags`: array of tags (used for filtering)
  - `code`: repository URL
  - `live`: optional live URL
  - `blog`: optional boolean flag
  - `description`: short description

Example:

```js
{
  id: "123e4567-e89b-12d3-a456-426614174000",
  name: "My Project",
  images: ["my_project.png"],
  tags: ["2024", "web_dev", "Vue 3"],
  code: "https://github.com/user/my-project",
  live: "https://user.github.io/my-project/",
  blog: false,
  description: "One-line summary of what it does.",
}
```

Blogs

- File: `src/assets/blogs/blogs.json`
- Add an object to the JSON array with:
  - `title`: string
  - `content`: HTML string (rendered with `v-html`)
  - `time`: string in format `DD Month YYYY` (e.g., `15 August 2024`)
  - `tags`: array (e.g., `["ml", "genai"]`)
- The UI sorts blogs by the `time` field (day, month name, year).

Optional lazy-loaded full content

- Instead of embedding the full HTML in `content`, you can provide:
  - `contentSource`: relative path under `public/` (e.g., `blogs/external/my-post.html`)
  - On first expand, the app fetches and injects that HTML into the post.
- Place the HTML file at `public/blogs/...`. It will be served at `BASE_URL/blogs/...`.

Content example:

```json
{
  "title": "New Feature X",
  "content": "<p>Short HTML summary...</p>",
  "time": "11 October 2024",
  "tags": ["update"]
}
```

About Page

- File: `src/components/sections/AboutSection.vue`
- Edit the `intro`, `workExperience`, and `interests` HTML strings in `setup()`.
- Keep content simple and valid HTML; it is injected using `v-html`.

Assets

- Place images under the appropriate directory:
  - Projects: `src/assets/projects/`
  - Tools: `src/assets/tools/`
  - Icons: `src/assets/icons/`
  - Portraits: `src/assets/portrait/`
- Reference local assets by filename in components (e.g., `"mle.png"`), or by full URLs when hosted externally.

Navigation

- File: `src/components/NavBar.vue` controls section switching and scrolling.
- To add a new section, update the menu and add a route in `src/router/index.js`.
