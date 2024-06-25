<template>
  <div class="container" id="work-section">
    <el-row>
      <el-col class="work-section">
        <div class="greetings">Projects</div>
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
  background: #343a40;
  overflow-y: scroll;
}
.work-section {
  overflow-y: scroll;
  height: 100%;
  background: transparent;
  backdrop-filter: blur(2px);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;

  .greetings {
    margin-top: 20px;
    color: #fff;
    font-family: Brandon;
    font-size: 40px;
    font-style: normal;
    font-weight: 600;
    line-height: 72px;
    letter-spacing: -1.77px;
  }

  .description {
    color: #fff;
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
      margin-top: 20px;
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