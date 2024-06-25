<template>
  <div class="container">
    <el-row>
      <el-col class="intro-section">

        <div class="intro-text">
          <p class="email">mynameshubham23@gmail.com</p>
          <section class="about">
              <p>Write a brief description about yourself, your education, current role, and previous experiences here.</p>
          </section>
          
          <a href="#" class="btn">About Me</a>
          
          <div class="social-icons">
            <a href="#" title="GitHub">&#xf09b;</a>
            <a href="#" title="Facebook">&#xf09a;</a>
            <a href="#" title="Instagram">&#xf16d;</a>
          </div>
        </div>
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
  height: calc(100vh - 60px - 50px);
  background: transparent;
  backdrop-filter: blur(2px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 0 15px;

  .intro-text {
    .profile-img {
      width: 150px;
      height: 150px;
      border-radius: 50%;
      object-fit: cover;
    }
    h1 {
        margin-top: 20px;
        font-size: 24px;
        text-transform: uppercase;
    }
    .email {
        color: #ffffff;
        margin-bottom: 30px;
    }
    .about {
        text-align: left;
        margin: 30px;
        color: #fff;
    }
    .btn {
        display: inline-block;
        padding: 10px 20px;
        border: 1px solid #fff;
        text-decoration: none;
        color: #fff;
        margin-bottom: 30px;
    }
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 30px;
    }
    .social-icons a {
        color: #fff;
        text-decoration: none;
        font-size: 24px;
    }
    .footer {
        font-size: 12px;
        color: #fff;
    }
  }

  .greetings {
    text-align: center;
    font-family: Brandon;
    font-size: 59px;
    font-style: normal;
    font-weight: 330;
    line-height: 72px;
    background: #596164;
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
    color: #ffffff;
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
    background: #596164;
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