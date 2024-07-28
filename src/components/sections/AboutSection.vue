<template>
  <div class="container" id="about-section">
    <div class="about-page">
      <el-row>
        <el-col :span="24">
          <span class="header">Hi! I’m Shubham</span>
          <span class="text" v-html="intro"></span>
          <span class="header">Work Experience</span>
          <span class="text" v-html="workExperience"></span>
          <span class="header">Things I can help you with</span>
          <span class="text" v-html="thingsICanHelpWith"></span>
          <span class="header">Other interests</span>
          <span class="text" v-html="interests"></span>
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
    document.getElementById("about-section").scrollIntoView()
  },
  setup() {
    const intro = `
      I'm a seasoned Software Engineer with 6 years of experience architecting and developing high-performance SaaS platforms for healthcare and fintech industries. My expertise spans full-stack development, with a recent focus on cutting-edge Machine Learning projects.
      <br><br>
      In 2014, during my first year of college, I delved into competitive programming with C++. This experience instilled in me a deep appreciation for algorithmic efficiency and optimization under strict constraints. Alos, the leaderboard challenge captivated me, and I pursued it for 3 years before transitioning to Web Development (JavaScript, React, Vue) in 2017 and did couple of internships.
      <br><br>
      Since then, I've worked full-time at a Swiss Fintech startup for a year, where I contributed in building fintech solutions and for 5 years at a healthcare startup, where I played a key role in developing patient and doctor-centric applications that improved healthcare delivery and accessibility.`

      const workExperience = `
      <h3>DoctorPlan (2019 - 2024)</h3>
      <strong>Software Engineer</strong>
      <br>
      Skills: <b>Javascript · VueJS · Data Analysis · HIPAA Compliance</b>
      <p>DoctorPlan is a Silicon Valley-based healthcare startup revolutionizing patient care through data-driven personalization.</p>
      <h4>Key Achievements:</h4>
      <ul>
        <li>Spearheaded development and maintenance of three major platforms: Hospital app, Patient web app, and internal admin dashboard, serving over 100,000 users.</li>
        <li>Engineered robust data processing pipelines for sensitive patient medical data, ensuring HIPAA compliance and data integrity.</li>
        <li>Led a performance optimization initiative, resulting in an 11x decrease in platform load time, significantly enhancing user experience and engagement.</li>
        <li>Facilitated seamless collaboration between cross-functional teams across international boundaries, driving product innovation and timely delivery.</li>
      </ul>
      <br>
      <h3>ALLPS Digital GmbH (2018 - 2019)</h3>
      <strong>Full-Stack Developer & Machine Learning Engineer</strong>
      <br>
      Skills: <b>Python · SQL · Javascript · ReactJS · Computer Vision · Machine Learning</b>
      <p>ALLPS is a Swiss fintech startup partnering with banks to revolutionize invoice processing through digitization.</p>

      <h4>Key Contributions:</h4>
      <ul>
        <li>Implemented advanced computer vision techniques (AlexNet) to enhance invoice processing accuracy by 40%, streamlining information extraction from receipts and cheques.</li>
        <li>Architected and developed robust dashboards and a secure payment gateway for Generali, a major partner bank, facilitating seamless financial transactions for over 100,000 customers.</li>
        <li>Optimized in-house OCR algorithm, improving character recognition accuracy by 25% through refined machine learning models and optimized data inputs.</li>
      </ul>
      <br>
      <h3>Global Voices Ltd (2017 - 2018)</h3>
      <strong>Software Engineer</strong>
      <br>
      Skills: <b>Python · Software Engineering · SQL · CI/CD</b>

      <h4>Notable Accomplishments:</h4>
      <ul>
        <li>Led the development and maintenance of the company's proprietary content management system, reducing critical bugs by 70% and implementing key features that improved system functionality and user experience.</li>
        <li>Redesigned and optimized CI/CD pipelines, resulting in a 50% reduction in rollbacks and a 30% increase in deployment frequency, significantly enhancing product release efficiency and reliability.</li>
      </ul>
      <br>
      <h3>Cartesian (3 Months in 2017 • Internship)</h3>
      <strong>Software Engineering Intern</strong>
      <br>
      Skills: <b>Javascript · AWS · C++ · FFmpeg · Python</b>
      <ul>
        <li>Developed a scalable live streaming service utilizing AWS, FFmpeg, and Python, capable of handling concurrent streams for over 10,000 users.</li>
        <li>Gained hands-on experience in cloud computing, real-time video processing, and large-scale system design, laying the foundation for future roles in high-performance computing.</li>
      </ul>`

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

      const interests = `<ul style="font-size: 17px">
                          <li>GPUs</li>
                          <li>Home Servers</li>
                          <li>Psychology & Psychoanalytics</li>
                          <li>Camping</li>
                        </ul>`
    return {
      intro,
      workExperience,
      thingsICanHelpWith,
      interests
    }
  },
  components: {
    // ToolsSection
},
};
</script>

<style lang="scss" scoped>
.container {
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

@media (max-width: 768px) {
  .container {
    padding-top: 60px;
  }
  .about-page {
    height: auto;
    min-height: calc(100vh - 60px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: baseline;
    margin: 60px 10px;
    width: calc(100vw - 40px);
  }

  .header {
    display: block;
    background-color: #111111 ;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    -moz-text-fill-color: transparent;

    font-family: Ubuntu, Brandon;
    font-size: 26px;
    font-style: normal;
    font-weight: 700;
    line-height: 40px;
    margin-bottom: 20px;
  }
  .text {
    font-size: 15px;
    font-style: normal;
    font-weight: 400;
    line-height: 25px;
    width: auto;
    min-width: calc(100vw - 20px);
    max-width: calc(100vw - 20px);
    margin-bottom: 40px;
    word-break: break-word;
  }
}

</style>
