<template>
  <div class="container" id="github-section">
    <el-row>
      <el-col class="github-section">
        <div class="greetings">Github</div>
        <el-row class="container">
          <img src="https://streak-stats.demolab.com?user=strcoder4007&theme=&background=111111&border=111111&stroke=1DB954&ring=1DB954&fire=1DB954&currStreakNum=1DB954&sideNums=1DB954&currStreakLabel=1DB954&sideLabels=1DB954&dates=1DB954&card_width=600&border_radius=2" alt="GitHub Streak" />
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "GithubSection",

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
  background: #222;
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

  .container {
    margin-top: 40px;
  }
}
@media (max-width: 768px) {
  .github-section {
    .greetings {
      margin-top: 20px;
      font-size: 40px;
      font-weight: 700;
    }

  }
}
</style>