<template>
  <div class="container" id="about-section">
    <el-row class="about-section">
      <el-col :span="24">
        <span class="header">Hi! I’m Shubham</span>
        <span class="text" v-html="intro"></span>
        <span class="header">Work Experience</span>
        <span class="text" v-html="workExperience"></span>
        <span class="header">Things I can help you with</span>
        <span class="text" v-html="thingsICanHelpWith"></span>
        <span class="header">Deep Learning interests</span>
        <span class="text" v-html="deeplearninginterests"></span>
        <span class="header">Other interests</span>
        <span class="text" v-html="interests"></span>
      </el-col>
    </el-row>
  </div>
</template>

<script>

export default {
  name: "AboutPage",
  mounted() {
    document.getElementById("about-section").scrollIntoView()
  },
  setup() {
    const intro = `
      I am a Machine Learning Engineer with over 5 years of experience in developing and deploying AI-driven solutions across multiple domains, with a strong focus on computer vision and natural language processing. Additionally, I have one year of experience as a Software Engineer.
      <br><br>
      I am proficient in machine learning, statistical analysis, and predictive modeling, with hands-on experience in data acquisition, analysis, and building predictive models using techniques like logistic regression, decision trees, and deep neural networks. I have developed solutions for industries such as finance and healthcare, including models that predict patient outcomes to improve proactive care and resource management.
      <br><br>
      Since then, I've worked full-time at a Swiss Fintech startup for a year, where I contributed in building fintech solutions and for 5 years at a healthcare startup, where I played a key role in developing patient and doctor-centric applications that improved healthcare delivery and accessibility.
      <br><br>
      As a competitive programmer, I have solved over 800 problems on Codeforces, showcasing my strong problem-solving skills and adaptability.`

      const workExperience = `
      
      <h3><strong>Machine Learning Engineer</strong> @ DoctorPlan (2019 - 2024)</h3>
      Skills: <b>Python · Tensorflow · SQL · ML Modeling · Data Analysis · HIPAA Compliance</b>
      <p>DoctorPlan is a Silicon Valley-based healthcare startup revolutionizing patient care through data-driven personalization.</p>
      <h4>Key Responsibilities:</h4>
      <ul>
        <li>Designed and implemented generation of Doctor's chart notes utilizing large language models (LLMs) to enhance operational efficiency of hospitals saving Doctor's time.</li>
        <li>Utilized advanced technologies like retrieval-augmented generation, optimizing LLM responses with extensive prompt engineering and improving user interaction.</li>
        <li>Engineered robust data processing pipelines for sensitive patient medical data (EMR), ensuring HIPAA compliance and data integrity and utilized natural language processing (NLP) to extract meaningful insights from Patient data.</li>
        <li>Led a performance optimization initiative by refactoring and redesigning schema leading to 11x decrease in platform load time.</li>
        <li>Played a pivotal role in development and maintenance of our three major platforms: Hospital app, Patient web app and internal admin dashboard, serving over 100k patients.</li>
        <li>Facilitated seamless collaboration between cross-functional teams across international boundaries, driving product innovation and timely delivery.</li>
      </ul>
      <br>
      <h3><strong>Software Engineer</strong> @ ALLPS Digital GmbH (2018 - 2019)</h3>
      Skills: <b>Python · SQL · Javascript · ReactJS · Computer Vision · Machine Learning</b>
      <p>ALLPS is a Swiss fintech startup partnering with banks to revolutionize invoice processing through digitization.</p>

      <h4>Key Contributions:</h4>
      <ul>
        <li>Implemented advanced computer vision techniques (AlexNet) to enhance invoice processing accuracy by 40%, streamlining information extraction from receipts and cheques.</li>
        <li>Architected and developed robust dashboards and a secure payment gateway for Generali, a major partner bank, facilitating seamless financial transactions for over 100,000 customers.</li>
        <li>Optimized in-house OCR algorithm, improving character recognition accuracy by 25% through refined machine learning models and optimized data inputs.</li>
      </ul>
      <br>
      <h3>Cartesian (3 Months in 2018 • Internship)</h3>
      <strong>Software Engineering Intern</strong>
      <br>
      Skills: <b>Javascript · AWS · C++ · FFmpeg · Python</b>
      <ul>
        <li>Developed a scalable live streaming service utilizing AWS, FFmpeg, and Python, capable of handling concurrent streams for over 10,000 users.</li>
        <li>Gained hands-on experience in cloud computing, real-time video processing, and large-scale system design, laying the foundation for future roles in high-performance computing.</li>
      </ul>
      <br>
      <h3>Wallfruit Technologies (4 Months in 2017 • Internship)</h3>
      <strong>Software Engineer</strong>
      <br>
      Skills: <b>Python · Software Engineering · SQL · CI/CD</b>

      <h4>Notable Accomplishments:</h4>
      <ul>
        <li>Led the development and maintenance of the company's proprietary content management system, reducing critical bugs by 70% and implementing key features that improved system functionality and user experience.</li>
        <li>Redesigned and optimized CI/CD pipelines, resulting in a 50% reduction in rollbacks and a 30% increase in deployment frequency, significantly enhancing product release efficiency and reliability.</li>
      </ul>
`

      const thingsICanHelpWith = `  <ul>
        <li>
          I can help build ML Models for Fraud detection and Recommendation systems to production.
        </li>
        <li>
          I can help with designing, implementing, and optimizing deep learning models using frameworks like TensorFlow and PyTorch. I can tackle a wide range of tasks, from data engineering to hyperparameter tuning and performance optimization.
        </li>
        <li>
          I can successfully develop and deploy neural networks for various applications, including computer vision, natural language processing, and time series analysis, ensuring high performance and accuracy.
        </li>
        <li>
          I can set up and manage scalable ML pipelines, ensuring efficient data flow from ingestion to model training and deployment experience in configuring and managing CI/CD systems for ML.
        </li>
        <li>
          I can help with optimizing model performance through techniques like pruning, quantization, and knowledge distillation, ensuring models run efficiently on both cloud and edge devices.
        </li>
      </ul>`

      const deeplearninginterests = `<ul>
        <li>ML Modeling</li>
        <li>Data Engineering</li>
        <li>Computer Vision</li>
        <li>Recommendation Systems</li>
        <li>LLMs, RAG, Agents</li>
        <li>Multimodal Models</li>
        </ul>`

      const interests = `<ul style="font-size: 17px">
                          <li>GPUs</li>
                          <li>PC Building</li>
                          <li>Home Servers</li>
                          <li>Psychology & Psychoanalytics</li>
                        </ul>`
    return {
      intro,
      workExperience,
      deeplearninginterests,
      thingsICanHelpWith,
      interests
    }
  },
  components: {},
};
</script>

<style lang="scss" scoped>
.container {
  overflow-y: hidden;
}
.about-section {
  overflow-y: scroll;
  height: calc(100vh - 80px);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: baseline;
  padding: 200px 100px 50px 100px;
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
  .about-section {
    overflow-y: scroll;
    height: calc(100vh - 60px);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: baseline;
    padding: 60px 10px;
    width: 100%;
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
