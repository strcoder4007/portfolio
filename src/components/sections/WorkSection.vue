<template>
  <div class="container" id="work-section">
    <el-row>
      <el-col class="work-section">
        <div class="greetings">My work</div>
        <div class="description">I specialize in website design,<br>but I’ve also designed successful iOS and Android apps.</div>
        <LandingComponent></LandingComponent>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import LandingComponent from "./project/LandingComponent.vue"

export default {
  name: "WorkSection",
  components: {
    LandingComponent
  },
};
</script>

<style lang="scss" scoped>

.container {
  background: transparent;
}
.work-section {
  min-height: 100vh;
  height: auto;
  background: transparent;
  backdrop-filter: blur(2px);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;

  .greetings {
    color: var(--Black, #261F22);
    font-family: Brandon;
    font-size: 59px;
    font-style: normal;
    font-weight: 700;
    line-height: 72px; /* 122.034% */
    letter-spacing: -1.77px;
  }

  .description {
    color: var(--Black, #261F22);
    text-align: center;
    font-family: Bricolage;
    font-size: 21px;
    font-style: normal;
    font-weight: 400;
    line-height: 30px;
    margin-top: 20px;
  }
}
@media (max-width: 768px) {
  .work-section {

    .greetings {
      font-size: 40px;
      font-weight: 700;
    }

    .description {
      padding: 0 20px;
      font-size: 15px;
      line-height: 20px;
    }
  }
}
</style>