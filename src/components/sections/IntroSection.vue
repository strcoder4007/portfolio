<template>
  <div class="container">
    <el-row>
      <el-col class="intro-section" >

        <div class="intro-text">
          <span class="profile-text">Machine Learning Engineer</span>
          <p class="phone">(+91) 8126062707</p>
          <p class="email">mynameshubham23@gmail.com</p>
          <section class="about">
              <p>
                Passionate about leveraging<mark> Computer Vision </mark>and<mark> Deep learning </mark>to solve 
                problems deemed impossible in the recent past.<br><br>
                I have<mark> 6 years of experience as a Software Engineer (Javascript/Vue/React) </mark>and a solid background in<mark> Algorithms and Data Structures (C++)</mark>.<br><br>
                Explore my work and see how I can contribute to your team's success.
              </p>
          </section>
          
          <a href="#" class="btn">Resume <img src="../../assets/icons/right-arrow.png" alt="Arrow Icon"/></a>

          <div class="social-section">
            <a href="https://github.com/strcoder4007" target="_blank"><img src="../../assets/icons/github.png" alt="Github Icon" class="social-icon" /></a>
            <a href="https://www.linkedin.com/in/riny-yadav-a24a90238/" target="_blank"><img src="../../assets/icons/linkedin.png" alt="LinkedIn Icon" class="social-icon" /></a>
          </div>

          <span class="policy-and-terms-section">
            © 2024 Shubham Singh. All rights reserved.
          </span>
        
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
  mounted() {
    setTimeout(() => {
      document.querySelectorAll('mark').forEach(e => e.style.color = "black");
    }, 2000);
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
  padding: 0 70px 0 30px;

  .intro-text {
    text-align: left;
    .profile-text {
      font-size: 40px;
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
        font-size: 18px;
        color: #fff;
        word-wrap: break-word;
        line-height: 25px;

        mark {
          transition: color 1.5s ease;
          -webkit-animation: 1.5s highlight 1.5s 1 normal forwards;
          animation: 1.5s highlight 1.5s 1 normal forwards;
          background-color: #111111;
          color: #fff;
          background: linear-gradient(90deg, #1DB954 50%, #111111 50%);
          background-size: 200% 100%;
          background-position: 100% 0;
        }
        @-webkit-keyframes highlight {
          to {
            background-position: 0 0;
          }
        }
        @keyframes highlight {
          to {
            background-position: 0 0;
          }
        }
    }
    .btn {
      display: block;
      padding: 10px 20px;
      border: 1px solid #fff;
      text-decoration: none;
      color: #fff;
      margin-bottom: 10px;
      line-height: 25px;
      img {
        width: 20px;
        height: auto;
        margin-bottom: -5px;
        margin-left: 5px;
      }
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
    .policy-and-terms-section {
      color: #ffffff;
      font-family: Ubuntu, Brandon;
      font-size: 13px;
      font-style: normal;
      font-weight: 400;
      line-height: 50px;
      position: absolute;
      bottom: 0;
    }
  }

  .greetings {
    text-align: center;
    font-family: Ubuntu, Brandon;
    font-size: 59px;
    font-style: normal;
    font-weight: 330;
    line-height: 72px;
    background: #111111 ;
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
}
.social-section {
  display: flex;
  justify-content: start;
  align-items: start;
  margin: 20px 0;
  gap: 15px;
  img {
      width: 30px;
      height: auto;
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
  }
}
</style>