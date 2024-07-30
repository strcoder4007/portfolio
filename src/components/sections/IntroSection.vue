<template>
  <div class="container" id="intro-section">
    <el-row>
      <el-col class="intro-section">
        <div class="intro-text">
          <span class="profile-text">Machine Learning Engineer</span>
          <br><br>
          <p
            class="phone"
            @click="copyToClipboard('+918126062707', 'Phone Number')"
          >
            (+91) 8126062707
            <img src="../../assets/icons/copy.png" title="Copy Phone" />
          </p>
          <p
            class="email"
            @click="copyToClipboard('mynameshubham23@gmail.com', 'Email')"
          >
            mynameshubham23@gmail.com
            <img src="../../assets/icons/copy.png" title="Copy Email" />
          </p>
          <section class="about">
            <p>
              Passionate about leveraging<mark> Deep learning models </mark
              >to solve problems deemed impossible in the recent past.<br /><br />
              With<mark>
                6 years of experience as a Software Engineer (JS) </mark
              >and a solid background in<mark>
                Algorithms and Data Structures (C++)</mark
              >, I bring a robust skill set to the table.<br /><br />
              I'm on the lookout for Machine Learning opportunities starting August 2024! Please reach out if you think I would be a good fit for your team.
            </p>
          </section>

          <a href="https://drive.google.com/file/d/1TrqF77gH4cCIGAFalZLai0uDGSspymMp/view?usp=sharing" target="_blank" class="btn"
            >Resume
            <img src="../../assets/icons/right-arrow.png" alt="Arrow Icon"
          /></a>

          <div class="social-section">
            <a
              href="https://www.linkedin.com/in/shubham-singh-96b159267"
              target="_blank"
              ><img
                src="../../assets/icons/linkedin.png"
                alt="LinkedIn Icon"
                class="social-icon"
            /></a>
            <a href="https://github.com/strcoder4007" target="_blank"
              ><img
                src="../../assets/icons/github.png"
                alt="Github Icon"
                class="social-icon"
            /></a>
          </div>

          <span class="source-code">
            Written in Vue 3.
            <a href="https://github.com/strcoder4007/portfolio" target="_blank"
              >Code</a
            >
          </span>

          <span class="policy-and-terms-section">
            © 2024 Shubham Singh. All rights reserved.
          </span>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  mounted() {
    setTimeout(() => {
      document
        .querySelectorAll("mark")
        .forEach((e) => (e.style.color = "black"));
    }, 2000);
  },
  methods: {
    copyToClipboard(text, textType) {
      navigator.permissions
        .query({ name: "clipboard-write" })
        .then((result) => {
          if (result.state == "granted" || result.state == "prompt") {
            navigator.clipboard
              .writeText(text)
              .then(() =>
                this.$message({
                  message: textType + " Copied",
                  type: "success",
                })
              )
              .catch(() => console.log("failure"));
          }
        });
    },
    scrollToWork() {
      document.getElementById("projects-section").scrollIntoView();
    },
    download() {
      const link = document.createElement("a");
      link.href = "https://strcoder4007.github.io/portfolio/resume.pdf";
      link.download = "Shubham_Resume.pdf";
      link.click();
    },
  },
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
      font-family: Ubuntu;
    }
    .profile-img {
      width: 150px;
      height: 150px;
      border-radius: 50%;
      object-fit: cover;
    }
    .email,
    .phone {
      margin: 8px 0;
      color: #ffffff;
      letter-spacing: 2px;
      img {
        width: 15px;
        height: auto;
        display: none;
        float: right;
        cursor: pointer;
      }
    }
    .email:hover,
    .phone:hover {
      img {
        display: inline;
      }
    }
    .about {
      text-align: left;
      margin: 30px 0;
      font-size: 17px;
      color: #fff;
      word-wrap: break-word;
      line-height: 25px;

      mark {
        transition: color 1.5s ease;
        -webkit-animation: 1.5s highlight 1.5s 1 normal forwards;
        animation: 1.5s highlight 1.5s 1 normal forwards;
        background-color: #111111;
        color: #fff;
        background: linear-gradient(90deg, #1db954 50%, #111111 50%);
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
      background-color: transparent;
      font-family: Bricolage;
      font-size: 15px;
      text-align: left;
      margin-bottom: 10px;
      line-height: 25px;
      img {
        width: 20px;
        height: auto;
        margin-bottom: -5px;
        margin-left: 5px;
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
    .source-code {
      color: #ffffff;
      font-family: Ubuntu, Brandon;
      font-size: 13px;
      font-style: normal;
      font-weight: 400;
      line-height: 50px;
      position: absolute;
      bottom: 20px;
      a {
        text-decoration-color: #1db954;
        color: #1db954;
        cursor: pointer;
      }
    }
    .policy-and-terms-section {
      color: #ffffff;
      font-family: Ubuntu, Brandon;
      font-size: 13px;
      font-style: normal;
      font-weight: 400;
      position: absolute;
      bottom: 15px;
    }
  }

  .profile {
    color: var(--Black, #261f22);
    text-align: center;
    font-family: Bricolage;
    font-size: 119px;
    font-style: normal;
    font-weight: 700;
    line-height: 144px; /* 121.008% */
    letter-spacing: -3.57px;
  }
}

@media (max-width: 1200px) {
  .intro-section {
    padding: 20px 10px 0 10px ;

    .intro-text {
      padding: 10px 10px 0 10px;
      .profile-text {
        font-size: 27px;
        font-weight: 700;
        font-family: Ubuntu;
      }
      .profile-img {
        display: none;
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
      }
    }
  }
}

@media (max-width: 768px) {
  .intro-section {
    height: calc(100vh - 60px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 30px 10px 0 10px ;

    .intro-text {
      padding: 10px 10px 0 10px;
      .profile-text {
        font-size: 25px;
        font-weight: 700;
        font-family: Ubuntu;
      }
      .profile-img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
      }
      .email,
      .phone {
        font-size: 14px;

        img {
          width: 13px;
          height: auto;
          display: inline;
          float: right;
          cursor: pointer;
        }
      }
      .about {
        margin: 30px 0;
        font-size: 15px;
      }
      .btn {
        padding: 5px 10px;
        font-size: 14px;
        margin-bottom: 10px;
        line-height: 25px;
        img {
          width: 18px;
          height: auto;
          margin-bottom: -5px;
          margin-left: 5px;
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
      .source-code {
        display: none;
      }
      .policy-and-terms-section {
        display: none;
      }
    }
  }
}
</style>
