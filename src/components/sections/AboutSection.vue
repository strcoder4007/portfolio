<template>
  <div>
    <div class="about-page">
      <el-row>
        <el-col :span="24">
          <span class="header">Hi! I’m Shubham</span>
          <span class="text" v-html="intro"></span>
          <span class="header">Work Experience</span>
          <span class="text" v-html="workExperience"></span>
          <span class="header">Things I can help you with</span>
          <span class="text" v-html="thingsICanHelpWith"></span>
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
    const intro = `
      I am a Machine Learning Engineer with 1.5 years of experience in creating and optimizing models, preprocessing data, setting up production pipelines, and fine-tuning. Additionally, I have 4.5 years of experience in Software Engineering, building high-performance web applications for hospitals and banks.
      <br><br>
      In 2014, during my first year of college, I delved into competitive programming with C++ which required programming optimized code implementations of Algorithmic problems under time, runtime and memory constraints. The leaderboard challenge captivated me, and I pursued it for 3 years before transitioning to Web Development (JavaScript, React, Vue) in 2017.
      <br><br>
      Since then, I've had the privilege of building software for a Swiss Fintech startup (1 year) and a Silicon Valley based healthcare startup (5 years), both focused on consumer-facing applications.`

      const workExperience = `
      <h3>DoctorPlan (2019 - 2024)</h3>
      Worked at this US healthcare startup as a Software Engineer. Later transitioned into Machine Learning role within the company. I worked extensively on the primary products i.e the Doctor's/Hospital's app and the Patient web app. Along with other internal apps.
      <ul>
        <li>
          Preprocessed large amounts of sensitive patient data according to HIPAA guidelines using Python, Numpy and Pandas.
        </li>
        <li>
          Wrote the code for batch processing all patient data which ran once every night along with setting up the ML pipeline. Using Sagemaker, Inferencia and MLFlow.
        </li>
        <li>
          Led the development and maintenance of a critical app used by doctors and patients, focusing on enhancing user experience and functionality. Managed all frontend tasks across the entire product lifecycle, utilizing Vue 2.
        </li>
        <li>
          Collaborated closely with cross-functional teams in the US, including developers, designers, and product managers, to ensure seamless integration and delivery.
        </li>
        <li>
        </li>
      </ul>
      <h3>ALLPS Digital GmBH (2018 - 2019)</h3>
      <ul>
        <li>
          Contributed to a Swiss Fintech startup by improving invoice processing and information extraction through advanced computer vision techniques.
        </li>
        <li>
          Developed dashboards and a payment gateway for our partner bank, Generali. 
        </li>
        <li>
          Enhanced the efficiency of a character recognition algorithm by optimizing data inputs and refining machine learning models.
        </li>
      </ul>
      <h3>Cartesian (3 Months in 2018)</h3>
        Completed an internship focused on developing a live streaming service using AWS, FFmpeg, and Python. Gained hands-on experience in cloud computing and real-time video processing technologies.
      <br><br>`

      const thingsICanHelpWith = `  <ul>
    <li>
      I can help with designing, implementing, and optimizing deep learning models using frameworks like TensorFlow and PyTorch. I can tackle a wide range of tasks, from data engineering to hyperparameter tuning and performance optimization.
    </li>
    <li>
      I can successfully develope and deploy neural networks for various applications, including computer vision, natural language processing, and time series analysis, ensuring high performance and accuracy.
    </li>
    <li>
      I can set up and manage scalable ML pipelines, ensuring efficient data flow from ingestion to model training and deployment experience in configuring and managing CI/CD systems for ML.
    </li>
    <li>
      I can help with optimizing model performance through techniques like pruning, quantization, and knowledge distillation, ensuring models run efficiently on both cloud and edge devices.
    </li>
  </ul>`
    return {
      intro,
      workExperience,
      thingsICanHelpWith
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
  margin: 200px 100px 50px 100px;
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
  font-size: 45px;
  font-style: normal;
  font-weight: 700;
  line-height: 62px;
  margin-bottom: 40px;
}
.text {
  display: block;
  color: #333333;
  font-family: Ubuntu, Brandon;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: 25px;
  width: auto;
  min-width: 400px;
  margin-bottom: 80px;
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