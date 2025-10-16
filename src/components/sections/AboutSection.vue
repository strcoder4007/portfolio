<template>
  <div class="container" id="about-section">
    <el-row class="about-section">
      <el-col :span="24">
        <span class="header">Hi! I’m Shubham</span>
        <span class="text" v-html="intro"></span>
        <span class="header">Work Experience</span>
        <span class="text" v-html="workExperience"></span>
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
      <p>I’m a Senior AI/ML Engineer with 7 years of experience — 2 years on GenAI, agentic systems, RAG, and LLMs; 4 years as an ML engineer; and 1 year in software engineering.</p>

      <p>I work end to end: data, modeling, evaluation, and production. I focus on RAG systems, autonomous agents, and getting models fast and efficient for real‑time use with quantization, pruning, and distillation. Over the last two years, I’ve gone deep on agent architectures (including RL‑trained agents) and the real‑world pitfalls teams hit when taking agents to production.</p>

      <p>I’ve shipped AI into government intelligence, healthcare diagnostics, education, and cultural heritage. Recently I built MCP‑style architectures to improve reasoning and cut inference latency by ~80% for interactive systems.</p>

      <p>I’ve also solved 800+ problems on Codeforces, which keeps my algorithms and problem‑solving sharp.</p>`

      const workExperience = `
      <h2><strong>Senior AI/ML Engineer</strong> @ Tagbin (December 2024 - Present)</h2>
      <p>Tagbin is a company focused on creating immersive and interactive experiences.</p>

      <h4>Key Projects:</h4>
      <ul>
        <li><b>AI-Powered Interactive Holobox Systems</b>
          <ul>
            <li>Architected end-to-end ML pipeline for interactive human-sized holographic displays featuring Indian leaders deployed across 7 cities in national museums and memorials</li>
            <li>Optimized latency from 9-10s to 1.5-2s by engineering efficient pipeline using FasterWhisper, Qwen2.5 14B AWQ, Kokoro TTS, Audio2Face, and Unreal Engine 5</li>
            <li>Key technologies: Large Language Models, Speech-to-Text, Text-to-Speech, Audio-to-Face Animation, Real-time Rendering</li>
          </ul>
        </li>
        <li><b>Government AI Solutions</b>
          <ul>
            <li>BIPARD AI: Developed generative AI platform for Bihar government enabling natural language (text/audio) queries to extract insights from government datasets</li>
            <li>Nandurba AI: Built advanced AI system for Maharashtra government integrating PostgreSQL GIS for geospatial intelligence and analytics (e.g., "List villages with no hospitals within 10km radius")</li>
            <li>Key technologies: GenAI, LLMs, PostgreSQL GIS, Spatial Analytics, NLP</li>
            <li>Law Enforcement AI: Implemented similar AI analytics solutions for Delhi Police and Goa Police</li>
          </ul>
        </li>
        <li><b>Purnia AI Education Platform</b>
          <ul>
            <li>Led development of comprehensive AI education platform for Bihar government featuring live classes and AI-powered learning. Implemented multimodal AI enabling students to query NCERT syllabus content and lecture videos</li>
            <li>Key technologies: Computer Vision, Speech-to-Text, Text-to-Speech, GenAI, LLMs</li>
          </ul>
        </li>
        <li><b>Healthcare AI Innovation</b>
          <ul>
            <li>Partnered with AIIMS Delhi to develop computer vision system for leucocoria detection using YOLO architecture</li>
            <li>Key technologies: Computer Vision, YOLO, Medical Image Processing</li>
          </ul>
        </li>
        <li><b>Cultural Heritage Preservation</b>
          <ul>
            <li>Kaithi to Hindi Conversion: Trained ML model on manually annotated data to convert historical property, cultural, and irrigation scriptures from Kaithi script to modern Hindi</li>
            <li>Indian Government Manuscript OCR: Contributed to 50 lakh manuscript digitization project, creating searchable database of Brahminic language texts with deep research capabilities</li>
          </ul>
        </li>
      </ul>
      <br>
      <h2><strong>Software Engineer</strong> @ DoctorPlan (2019 - 2024)</h2>
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

      const deeplearninginterests = `<ul>
        <li>ML Modeling</li>
        <li>Data Engineering</li>
        <li>Computer Vision</li>
        <li>Recommendation Systems</li>
        <li>LLMs, RAG, Agents</li>
        <li>Multimodal Models</li>
        </ul>`

      const interests = `<p style="font-size: 17px">I enjoy working with GPUs, building PCs, running home servers, and reading about psychology and psychoanalysis.</p>`
    return {
      intro,
      workExperience,
      deeplearninginterests,
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
