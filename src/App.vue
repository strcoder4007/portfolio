<template>
  <NavBar></NavBar>
  <router-view></router-view>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar
  },
};
</script>

<style>
/* ============================================================
   PrismML Design System — Global Foundation
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

@font-face {
  font-family: 'Bricolage';
  src: url('./assets/fonts/BricolageGrotesque.ttf');
}
@font-face {
  font-family: 'Brandon';
  src: url('./assets/fonts/Brandon_reg.otf');
}

:root {
  /* Core palette */
  --color-bg:        #E9E4E0;
  --color-bg-alt:    #E2DDD8;
  --color-text:      #262C35;
  --color-text-dim:  #5A606B;
  --color-border:    #262C35;
  --color-accent:    #CFBEBE;
  --color-accent-dim:#B8A8A8;
  --color-surface:   #FFFFFF;

  /* Typography */
  --font-heading: 'Space Grotesk', 'Bricolage', Brandon, sans-serif;
  --font-body:    'Bricolage', 'Space Grotesk', sans-serif;
  --font-mono:    'JetBrains Mono', 'Space Grotesk', monospace;

  /* Grid */
  --grid-color: rgba(38, 44, 53, 0.10);
  --grid-size: 24px;

  /* Angular CTA clip-path */
  --clip-arrow: polygon(0 0, 88% 0, 100% 50%, 88% 100%, 0 100%, 12% 50%);
  --clip-arrow-sm: polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%, 15% 50%);
}


/* Override Element Plus theme to match PrismML */
:root {
  --el-color-primary: var(--color-text);
  --el-color-primary-light-3: var(--color-accent);
  --el-color-primary-light-5: var(--color-accent);
  --el-color-primary-light-7: var(--color-accent);
  --el-color-primary-light-8: var(--color-accent);
  --el-color-primary-light-9: var(--color-accent);
  --el-bg-color: var(--color-surface);
  --el-bg-color-overlay: var(--color-surface);
  --el-text-color-primary: var(--color-text);
  --el-text-color-regular: var(--color-text-dim);
  --el-border-color: var(--color-border);
  --el-border-color-light: var(--color-border);
  --el-border-radius: 0px;
}
/* Visible structural grid on warm paper */
body {
  margin: 0;
  background-color: var(--color-bg);
  background-image:
    linear-gradient(to right,  var(--grid-color) 1px, transparent 1px),
    linear-gradient(to bottom, var(--grid-color) 1px, transparent 1px);
  background-size: var(--grid-size) var(--grid-size);
  background-position: 0 0;
  color: var(--color-text);
  font-family: var(--font-body);
  font-size: 17px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

/* Angular CTA base class */
.btn-angular {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  position: relative;
  padding: 12px 22px;
  background: var(--color-text);
  color: var(--color-bg);
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 14px;
  letter-spacing: 0.4px;
  text-transform: uppercase;
  border: none;
  clip-path: var(--clip-arrow);
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease;
}
.btn-angular:hover {
  background: var(--color-accent);
  color: var(--color-text);
}
.btn-angular:active {
  transform: translateY(2px);
}

/* Angular ghost CTA */
.btn-angular-ghost {
  background: transparent;
  color: var(--color-text);
  border: 1px solid var(--color-text);
}
.btn-angular-ghost:hover {
  background: var(--color-text);
  color: var(--color-bg);
}

/* Structural border utility */
.border-structural {
  border: 1px solid var(--color-border);
}

/* Mono metadata utility */
.mono-meta {
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  color: var(--color-text-dim);
}

/* Oversized heading */
.heading-display {
  font-family: var(--font-heading);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 0.95;
  text-transform: uppercase;
}

/* Remove Element Plus default dark theme interference */
.el-message__content {
  font-family: var(--font-body);
}

/* Scrollbar */
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: var(--color-bg); }
::-webkit-scrollbar-thumb {
  background: var(--color-border);
  border: 2px solid var(--color-bg);
}
::-webkit-scrollbar-thumb:hover { background: var(--color-accent); }
</style>