<template>
  <div class="container">
    <el-row>
      <el-col class="intro-section">

        <div class="intro-text">
          <span class="profile-text">Machine Learning Engineer</span>
          <p class="phone">(+91) 8126062707</p>
          <p class="email">mynameshubham23@gmail.com</p>
          <section class="about">
              <p>
                Passionate about leveraging Computer Vision and Deep learning to solve 
                problems deemed impossible in the recent past.<br><br>
                I have background in Web Dev (Javascript/Vue/React) and Competitive programming (C++). <br><br>
                Explore my work and see how I can contribute to your team's success.
              </p>
          </section>
          
          <a href="#" class="btn">Resume</a>
          
          <div class="social-icons">
            <a href="#" title="GitHub">&#xf09b;</a>
            <a href="#" title="Facebook">&#xf09a;</a>
            <a href="#" title="Instagram">&#xf16d;</a>
          </div>
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
  height: calc(100vh - 60px);
  background: transparent;
  backdrop-filter: blur(2px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 20px 0 30px;

  .intro-text {
    text-align: left;
    .profile-text {
      font-size: 50px;
      font-weight: 700;
    }
    .profile-img {
      width: 150px;
      height: 150px;
      border-radius: 50%;
      object-fit: cover;
    }
    .email, .phone {
        color: #ffffff;
        letter-spacing: 2px;
    }
    .about {
        text-align: left;
        margin: 30px 0;
        font-size: 20px;
        color: #fff;
        word-wrap: break-word;
        line-height: 25px;
    }
    .btn {
      display: grid;
      padding: 10px 20px;
      border: 1px solid #fff;
      text-decoration: none;
      color: #fff;
      margin-bottom: 30px;
    }
    .social-icons {
      display: flex;
      justify-content: start;
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
    background: #0c0f11 ;
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
    background: #0c0f11 ;
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
    padding: 0 10px;

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