<template>
  <div>
    <el-row>
      <el-col :sm="24" :md="8">
        <IntroSection></IntroSection>
      </el-col>
      <el-col :sm="24" :md="16">
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
    <FooterSection></FooterSection>
  </div>
</template>

<script>
import IntroSection from "./sections/IntroSection.vue";
import WorkSection from "./sections/WorkSection.vue";
// import FreelanceSection from "./sections/FreelanceSection.vue";
// import ToolsSection from "./sections/ToolsSection.vue";
import FooterSection from "./sections/FooterSection.vue";
export default {
  name: "LandingPage",
  props: {
    msg: String,
  },
  components: {
    IntroSection,
    WorkSection,
    // FreelanceSection,
    // ToolsSection,
    FooterSection
  },
};
</script>

<style scoped>
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
  height: calc(100vh - 60px - 50px - 80px);
  width: 94%;
  margin: 40px;
  background-color: white;
  border-radius: 20px;
  overflow-y: scroll;
}
@media (max-width: 768px) {
}
</style>
