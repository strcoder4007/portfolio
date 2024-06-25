<template>
  <div class="container">
    <el-row>
      <el-col class="intro-section">
        <div class="resume-container">
          <el-button class="action-btn" @click="scrollToWork()">
            See my work
            <img src="../../assets/icons/arrow-down.png" alt="Arrow Right Icon" />
          </el-button>
          <el-button class="action-btn" @click="download()">
            Download CV
            <img src="../../assets/icons/download.png" alt="Arrow Right Icon" />
          </el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
// import { ref } from 'vue';

export default {
  setup() {

    return {
    };
  },
  methods: {
    scrollToWork() {
      document.getElementById('work-section').scrollIntoView()
    },
    download() {
      const link = document.createElement('a')
      link.href = 'https://strcoder4007.github.io/portfolio/resume.pdf'
      link.download = 'Shubham_Resume.pdf'
      link.click();
    }
  }
};
</script>

<style lang="scss" scoped>

.container {
  background: transparent;
}
.intro-section {
  height: calc(100vh - 60px - 80px);
  background: transparent;
  backdrop-filter: blur(2px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  .greetings {
    text-align: center;
    font-family: Brandon;
    font-size: 59px;
    font-style: normal;
    font-weight: 330;
    line-height: 72px;
    background: var(--brand-gradient, linear-gradient(90deg, #FE572E 0%, #FC3A79 100%));
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .profile {
    color: var(--Black, #261F22);
    text-align: center;
    font-family: Bricolage;
    font-size: 119px;
    font-style: normal;
    font-weight: 700;
    line-height: 144px; /* 121.008% */
    letter-spacing: -3.57px;
  }

  .description {
    color: var(--black75, rgba(38, 31, 34, 0.75));
    text-align: center;
    font-family: Bricolage;
    font-size: 21px;
    font-style: normal;
    font-weight: 400;
    line-height: 30px; /* 142.857% */
  }

  .resume-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
  }
  .action-btn {
    margin-bottom: 20px;
    color: #FFF;
    font-family: Bricolage;
    font-size: 21px;
    font-style: normal;
    font-weight: 700;
    line-height: 30px;
    border-radius: 100px;
    padding: 36px 48px;
    background: var(--brand-gradient, linear-gradient(90deg, #FE572E 0%, #FC3A79 100%));
    box-shadow: 0px 2.76726px 2.21381px 0px rgba(0, 0, 0, 0.02), 0px 6.6501px 5.32008px 0px rgba(0, 0, 0, 0.03), 0px 12.52155px 10.01724px 0px rgba(0, 0, 0, 0.04), 0px 22.33631px 17.86905px 0px rgba(0, 0, 0, 0.04);
    img {
      width: 20px;
      height: 20px;
      margin-left: 15px;
    }
  }
}
@media (max-width: 768px) {
  .intro-section {
    height: 70vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .greetings {
      font-weight: 400;
      font-size: 30px;
    }
    .profile {
      font-size: 50px;
      line-height: 60px;
    }

    .description {
      font-size: 15px;
      line-height: 20px;
      padding: 0 20px;
      margin-top: 20px;
    }

    .action-btn {
      font-size: 15px;
      line-height: 20px;
      padding: 20px 25px;
      img {
        width: 15px;
        height: 15px;
        margin-left: 10px;
      }
    }
  }
}
</style>