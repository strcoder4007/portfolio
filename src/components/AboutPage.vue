<template>
  <div>
    <div class="about-page">
      <el-row>
        <el-col :span="24">
          <span class="header">Hi! I’m Shubham Singh. </span>
          <span class="description" v-html="description"></span>
          <el-row class="image-section">
            <el-col :md="12"><img src="../assets/portrait/one.png"></el-col>
            <el-col :md="12"><img src="../assets/portrait/two.png"></el-col>
          </el-row>
        </el-col>
      </el-row>
    </div>
    <ToolsSection></ToolsSection>
    <FreelanceSection class="freelance-section"></FreelanceSection>
  </div>

</template>

<script>
import ToolsSection from './sections/ToolsSection.vue';
import FreelanceSection from './sections/FreelanceSection.vue';

export default {
  name: "AboutPage",
  mounted() {
    
  },
  setup() {
    const description = `An illustrator, designer who brings inclusive, minimal and future oriented user experience to people in need.<br><br>
    I came to graphic design from a background in human resources, which gives me a strong background in communication, It was the best decision I ever made because it showed me what I wanted to do for the rest of my life.<br><br>
    I was driven to designing because it felt exciting and rewarding to learn about people’s goals and desires, help them solve their problems and make their lives easier.<br><br>
    I help businesses all around the world by designing websites and mobile apps.<br><br>
    Right now I’m based in Noida.`;
    return {
      description
    }
  },
  components: {
    FreelanceSection,
    ToolsSection
},
};
</script>

<style lang="scss" scoped>
.about-page {
  height: auto;
  min-height: calc(100vh - 60px - 50px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: baseline;
  margin: 200px 150px 50px 150px;
  text-align: left;
}

.freelance-section {
  margin-top: 80px;
}

.header {
  display: block;
  background-color: #111111 ;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;

  font-family: Ubuntu, Brandon;
  font-size: 84px;
  font-style: normal;
  font-weight: 700;
  line-height: 112px;
  margin-bottom: 40px;
}
.description {
  display: block;
  color: #ffffff;
  font-family: Ubuntu, Brandon;
  font-size: 21px;
  font-style: normal;
  font-weight: 400;
  line-height: 30px;
  width: auto;
  min-width: 400px;
  margin-bottom: 40px;
}

.image-section {
    img {
      width: 100%;
      height: auto;
      object-fit: contain;
      margin-bottom: 40px;
    }
} 

.promises-header {
  color: var(--Black, #261F22);
  font-family: Ubuntu, Brandon;
  font-size: 59px;
  font-style: normal;
  font-weight: 330;
  line-height: 72px; 
  letter-spacing: -1.77px;
  margin: 10px 0 100px 0;
}

.promises {
  padding: 0 40px 40px 0;
  margin-bottom: 50px;
  img {
    width: 64px;
    height: 64px;
  }
  .promise-subheader {
    display: block;
    color: var(--Black, #261F22);
    font-family: Ubuntu, Brandon;
    font-size: 30px;
    font-style: normal;
    font-weight: 450;
    line-height: 40px;
    margin-bottom: 30px;
    margin-top: 10px;
  }
  .promise-description {
    color: #ffffff;
    font-family: Bricolage;
    font-size: 17px;
    font-style: normal;
    font-weight: 400;
    line-height: 30px;
  }
}
@media (max-width: 768px) {
  .about-page {
    height: auto;
    min-height: calc(100vh - 60px - 50px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: baseline;
    margin: 100px 30px 5px 50px;
    text-align: left;
  }

  .freelance-section {
    margin-top: 40px;
  }

  .header {
    display: block;
    background-color: #111111 ;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    -moz-text-fill-color: transparent;

    font-family: Ubuntu, Brandon;
    font-size: 32px;
    font-style: normal;
    font-weight: 700;
    line-height: 40px;
    margin-bottom: 20px;
  }
  .description {
    display: block;
    color: #ffffff;
    font-family: Ubuntu, Brandon;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: 20px;
    width: auto;
    min-width: 100%;
    margin-bottom: 20px;
  }

  .image-section {
      img {
        width: 100%;
        height: auto;
        object-fit: contain;
        margin-bottom: 10px;
      }
  } 

  .promises-header {
    color: var(--Black, #261F22);
    font-family: Ubuntu, Brandon;
    font-size: 30px;
    font-style: normal;
    font-weight: 330;
    line-height: 40px; 
    margin: 30px 0 40px 0;
  }

  .promises {
    padding: 0 10px 10px 0;
    margin-bottom: 40px;
    img {
      width: 40px;
      height: 40px;
    }
    .promise-subheader {
      display: block;
      font-size: 18px;
      font-style: normal;
      font-weight: 600;
      line-height: 25px;
      margin-bottom: 20px;
      margin-top: 10px;
    }
    .promise-description {
      font-size: 13px;
      font-style: normal;
      font-weight: 400;
      line-height: 15px;
    }
  }
}

</style>
