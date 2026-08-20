<template>
  <div class="app-container" id="app-container">
    <div class="layout-grid">
      <!-- Left rail: intro -->
      <aside class="rail rail-intro">
        <IntroSection></IntroSection>
      </aside>

      <!-- Right rail: dynamic section -->
      <main class="rail rail-content">
        <section class="content-frame">
          <component :is="currentSection"></component>
        </section>
      </main>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import IntroSection from "./sections/IntroSection.vue";
import ProjectsSection from "./sections/ProjectsSection.vue";
import BlogsSection from "./sections/BlogsSection.vue";
import GithubSection from "./sections/GithubSection.vue";
import AboutSection from "./sections/AboutSection.vue";

const route = useRoute();

const sectionsMap = {
  '/': ProjectsSection,
  '/projects': ProjectsSection,
  '/blogs': BlogsSection,
  '/github': GithubSection,
  '/about': AboutSection
};

const currentSection = computed(() => sectionsMap[route.path] || ProjectsSection);
</script>

<style scoped>
.app-container {
  padding-top: 64px;
}


.layout-grid {
  display: grid;
  grid-template-columns: 425px 1fr;
  min-height: calc(100vh - 64px);
  background-color: var(--color-bg);
  background-image:
    linear-gradient(to right,  var(--grid-color) 1px, transparent 1px),
    linear-gradient(to bottom, var(--grid-color) 1px, transparent 1px);
  background-size: var(--grid-size) var(--grid-size);
  background-position: 0 0;
}

.rail-intro {
  border-right: 1px solid var(--color-border);
  background-color: var(--color-bg-alt);
  position: sticky;
  top: 64px;
  height: calc(100vh - 64px);
  overflow-y: auto;
}

.rail-content {
  min-height: calc(100vh - 64px);
  overflow-y: auto;
}

.content-frame {
  min-height: 100%;
}

@media (max-width: 1023px) {
  .layout-grid {
    grid-template-columns: 1fr;
  }
  .rail-intro {
    position: static;
    height: auto;
    border-right: none;
    border-bottom: 1px solid var(--color-border);
  }
}
</style>