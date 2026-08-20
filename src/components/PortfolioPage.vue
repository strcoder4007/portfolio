<template>
  <div class="portfolio-page">
    <div class="page-header">
      <span class="page-eyebrow mono-meta">// projects</span>
      <h1 class="page-title heading-display">Selected Work</h1>
      <div class="header-line"></div>
    </div>
    <LandingComponent></LandingComponent>
  </div>
</template>

<script>
import LandingComponent from "./sections/project/LandingComponent.vue"
export default {
  name: "PortfolioPage",
  components: {
    LandingComponent
  },
};
</script>

<style scoped>
.portfolio-page {
  padding: 48px 56px 64px;
  max-width: 1400px;
  margin: 0 auto;
}

.page-header {
  margin-bottom: 48px;
}

.page-eyebrow {
  display: block;
  margin-bottom: 12px;
}

.page-title {
  font-size: clamp(48px, 7vw, 96px);
  color: var(--color-text);
  margin: 0 0 24px;
}

.header-line {
  width: 80px;
  height: 3px;
  background-color: var(--color-accent);
}

@media (max-width: 768px) {
  .portfolio-page {
    padding: 32px 16px 48px;
  }
}
</style>