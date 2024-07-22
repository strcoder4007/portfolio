<template>
  <div>
    <div class="about-page">
      <el-row>
        <el-col :span="24">
          <span class="header">Hi! I’m Shubham</span>
          <span class="description" v-html="description"></span>
          <!-- <el-row class="image-section">
            <el-col :md="12"><img src="../../assets/portrait/one.png"></el-col>
            <el-col :md="12"><img src="../../assets/portrait/two.png"></el-col>
          </el-row> -->
        </el-col>
      </el-row>
    </div>
    <!-- <ToolsSection></ToolsSection> -->
  </div>

</template>

<script>
// import ToolsSection from '../sections/ToolsSection.vue';

export default {
  name: "AboutPage",
  mounted() {
    
  },
  setup() {
    const description = `I'm an enthusiastic Deep Learning and Computer Vision Engineer with a keen interest in
all three pillars of Deep learning i.e Vision, NLP and Reinforcement Learning, but particularly focused on computer vision. With extensive experience in Python, C++ and Javascript, I have been at the cutting edge of developing advanced technologies that enable machines to perceive and interpret visual data more effectively.
<br><br>
Throughout my career, I've had the privilege of working on impactful projects across various sectors including Fintech, Healthcare, and consumer-facing apps. 
My expertise in translating theoretical knowledge into practical, scalable solutions has improved the existing systems in my past Startups.
<br><br>
Using PyTorch and TensorFlow as foundational tools, I've developed robust neural networks capable of processing enormous
volumes of visual data with impressive accuracy. These tools along with Numpy, Pandas, Matplotlib, OpenCV have allowed me to 
experiment quickly, iterate effectively, and make interesting side projects.`;
    return {
      description
    }
  },
  components: {
    // ToolsSection
},
};
</script>

<style lang="scss" scoped>
.container {
  background: #222222;
  overflow-y: scroll;
}
.about-page {
  height: auto;
  min-height: calc(100vh - 60px - 50px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: baseline;
  margin: 20px 100px 50px 100px;
  text-align: left;
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
  color: #333333;
  font-family: Ubuntu, Brandon;
  font-size: 18px;
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
    color: #333333;
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
    color: #333333;
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
