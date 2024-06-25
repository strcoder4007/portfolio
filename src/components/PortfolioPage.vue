<template>
  <div class="portfolio-page">
    <div class="greetings">Projects</div>
    <LandingComponent></LandingComponent>
    <FooterSection></FooterSection>
  </div>
</template>

<script>
import FooterSection from "./sections/FooterSection.vue";
import LandingComponent from "./sections/project/LandingComponent.vue"
export default {
  name: "PortfolioPage",
  mounted() {
  },
  components: {
    FooterSection,
    LandingComponent
  },
};
</script>

<style scoped>
.portfolio-page {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  height: auto;
  overflow: scroll;
  background-color: transparent;
}
.greetings {
  margin-top: 100px;
  color: var(--Black, #261F22);
  font-family: Brandon;
  font-size: 59px;
  font-style: normal;
  font-weight: 700;
  line-height: 80px;
  letter-spacing: -1.77px;
  letter-spacing: .5px;
  background: linear-gradient(to right, #FE572E, #FC3A79);
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-fill-color: transparent;
}
</style>
  