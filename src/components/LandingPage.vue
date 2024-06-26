<template>
  <div>
    <el-row class="app-container">
      <el-col :sm="24" :md="7">
        <IntroSection></IntroSection>
      </el-col>
      <el-col :sm="24" :md="17">
        <div class="floating-card">
          <WorkSection></WorkSection>
        </div>
      </el-col>
    </el-row>
    
    <!-- 
    <ToolsSection></ToolsSection>
    <FreelanceSection></FreelanceSection>
    <span class="designed-by-me">
      <img src="../assets/icons/heart.png" alt="Heart Icon" />
      Designed by me
    </span> -->
  </div>
</template>

<script>
import IntroSection from "./sections/IntroSection.vue";
import WorkSection from "./sections/WorkSection.vue";
// import FreelanceSection from "./sections/FreelanceSection.vue";
// import ToolsSection from "./sections/ToolsSection.vue";
export default {
  name: "LandingPage",
  props: {
    msg: String,
  },
  components: {
    IntroSection,
    WorkSection,
    // FreelanceSection,
    // ToolsSection
  },
};
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
}
</style>
