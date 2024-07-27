<template>
  <div>
    <el-row class="app-container" id="app-container">
      <el-col :sm="24" :md="7">
        <IntroSection></IntroSection>
      </el-col>
      <el-col :sm="24" :md="17">
        <div class="floating-card">
          <!-- Dynamically render the section based on the current route -->
          <component :is="currentSection"></component>
        </div>
      </el-col>
    </el-row>
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
import ResumeSection from "./sections/ResumeSection.vue";

const route = useRoute();

// Define a reactive section to watch for changes in the current path
const sectionsMap = {
  '/': ProjectsSection,
  '/projects': ProjectsSection,
  '/blogs': BlogsSection,
  '/github': GithubSection,
  '/about': AboutSection,
  '/resume': ResumeSection
};
const currentSection = computed(() => sectionsMap[route.path] || ProjectsSection);

</script>

<style scoped>
.app-container {
  padding-top: 60px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.floating-card {
  height: calc(100vh - 60px - 20px);
  width: 96.5%;
  margin: 0 20px 20px 20px;
  background-color: white;
  overflow-y: scroll;
}
@media (max-width: 768px) {
  .floating-card {
    height: auto;
    width: 100vw;
    background-color: white;
    overflow-y: scroll;
    margin: 0;
  }
}
</style>
