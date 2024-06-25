<template>
  <div>
    <IntroSection></IntroSection>
    <WorkSection></WorkSection>
    <ToolsSection></ToolsSection>
    <FreelanceSection></FreelanceSection>
    <span class="designed-by-me">
      <img src="../assets/icons/heart.png" alt="Heart Icon" />
      Designed by me
    </span>
    <FooterSection></FooterSection>
  </div>
</template>

<script>
import IntroSection from "./sections/IntroSection.vue";
import WorkSection from "./sections/WorkSection.vue";
import FreelanceSection from "./sections/FreelanceSection.vue";
import FooterSection from "./sections/FooterSection.vue";
import ToolsSection from "./sections/ToolsSection.vue";
export default {
  name: "LandingPage",
  props: {
    msg: String,
  },
  components: {
    IntroSection,
    WorkSection,
    FreelanceSection,
    FooterSection,
    ToolsSection
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
.designed-by-me {
  img {
    width: 18px;
    height: 17px;
    margin: 0 7px;
  }
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Bricolage";
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 80px;
  color: black;
}
</style>
