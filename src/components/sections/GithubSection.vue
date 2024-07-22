<template>
  <div class="container" id="github-section">
    <el-row>
      <el-col class="github-section">
        <div class="greetings">Github</div>
        <!-- <span>![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=strcoder4007&exclude_repo=github-readme-stats,anuraghazra.github.io)</span> -->
      </el-col>
    </el-row>
  </div>
</template>

<script>

export default {
  name: "GithubSection",
  components: {
  },
};
</script>

<style lang="scss" scoped>

.container {
  background: #222222;
  overflow-y: scroll;
}
.github-section {
  overflow-y: scroll;
  height: calc(100vh - 80px);
  background: transparent;
  backdrop-filter: blur(2px);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;

  .greetings {
    margin-top: 20px;
    color: #fff;
    font-family: Bricolage;
    font-size: 40px;
    font-style: normal;
    font-weight: 600;
    line-height: 72px;
    letter-spacing: -1px;
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
  .github-section {

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