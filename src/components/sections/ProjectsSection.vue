<template>
  <div class="container" id="projects-section">
    <el-row>
      <el-col class="projects-section">
        <div class="greetings">Projects</div>
        <TabsComponent
          :projectList="projectList"
          @tabChange="tabChange">
        </TabsComponent>

        <LandingComponent 
          :projectList="projectList">
        </LandingComponent>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import TabsComponent from "./project/TabsComponent.vue";
import LandingComponent from "./project/LandingComponent.vue";


const allProjects = [
        {
          id: "f0b5a7b2-2a4d-4f1e-9c51-7a8b3e50b1a1",
          name: "Browser Agent",
          images: ["https://github.com/strcoder4007/browser-agent/blob/main/1.gif?raw=true"],
          tags: ["2025", "ml", "Autonomous Agent", "LLM", "Automation"],
          code: "https://github.com/strcoder4007/browser-agent",
          blog: false,
          description:
            "A browser automation agent that plans multi‑step tasks, reasons with an LLM, and controls tools end‑to‑end to crawl any website and extract structured data.",
        },
        {
          id: "a2c9e1d4-6b3f-45e2-9f7a-0c8b9d3e4f56",
          name: "S2S Lipsync Unreal Avatar Backend",
          images: ["https://github.com/strcoder4007/S2S-Lipsync-UnrealAvatar-Backend/blob/main/images/2.gif?raw=true"],
          tags: ["2025", "ml", "Speech", "TTS", "STT", "Unreal Engine", "Realtime"],
          code: "https://github.com/strcoder4007/S2S-Lipsync-UnrealAvatar-Backend",
          blog: false,
          description:
            "Speech‑to‑speech backend for a real‑time Unreal Engine avatar — STT in, LLM response, TTS out, plus viseme timing for accurate lip‑sync.",
        },
        {
          id: "a3b859f2-f5ea-49a2-ae91-c5be0ddf3e86",
          name: "Training Layer Visualization",
          images: ["https://github.com/strcoder4007/Training-Visualization/blob/main/images/layers.gif?raw=true"],
          tags: ["2024", "ml", "PyTorch", "OpenCV", "Python"],
          code: "https://github.com/strcoder4007/Training-Visualization",
          blog: true,
          description:
            "A real‑time view into a model’s hidden layers using PyTorch and OpenCV.",
        },
        {
          id: "e17a5c2b-4f6d-49c0-9b21-83f1c4a9d7e3",
          name: "Customer Call Sentiment Analysis",
          images: ["https://github.com/strcoder4007/voice-sentiment-analysis/blob/main/images/4.gif?raw=true"],
          tags: ["2025", "ml", "Data", "multimodal model", "Analytics"],
          code: "https://github.com/strcoder4007/voice-sentiment-analysis",
          blog: false,
          description:
            "Customer call analysis app with: Speech-to-Text + speaker diarization. Takes into account not only the text but tone, rythym etc.",
        },
        {
          id: "85b39e2d-f5a0-67c7-ae2d-06297acbe963",
          name: "Multi Agent AI System",
          images: ["https://github.com/strcoder4007/Multi-Agent-AI-System/blob/main/image.jpg?raw=true"],
          tags: ["2024", "ml", "Gen AI", "Crew AI", "Langchain", "Agent"],
          code: "https://github.com/strcoder4007/Multi-Agent-AI-System",
          blog: false,
          description:
            "A multi‑agent system built with CrewAI, LangChain, and Llama 3.1 (8B). Agents coordinate to complete tasks — from planning to generating keynote‑style content.",
        },
        {
          id: "85b39e2d-f5a0-47c7-ae2d-06297acbe963",
          name: "NFS Self Driving Simulation",
          images: ["https://github.com/strcoder4007/Need-For-Speed-Self-driving/blob/main/images/nfsmw1.gif?raw=true"],
          tags: ["2024", "ml", "Tensorflow 2", "InceptionResNetV2", "Vision", "OpenCV", "Python"],
          code: "https://github.com/strcoder4007/Need-For-Speed-Self-driving",
          blog: true,
          description:
            "I trained a ConvNet to play Need for Speed: Most Wanted purely from pixels, using InceptionResNetV2, OpenCV, and TensorFlow 2.",
        },
        {
          id: "c5d7f9a1-83b2-4e9d-bc4f-2e7a6c9d0f12",
          name: "Unreal WebSocket Bridge",
          images: ["https://github.com/strcoder4007/unreal-websocket/blob/main/images/3.gif?raw=true"],
          tags: ["2025", "ml", "Unreal Engine", "WebSocket", "Realtime"],
          code: "https://github.com/strcoder4007/unreal-websocket",
          blog: false,
          description:
            "A lightweight WebSocket bridge that streams AI‑driven commands, audio, and visemes into Unreal Engine for live character animation.",
        },
        {
          id: "eb66bcbb-9ff3-4bcc-a42f-1b944cfb33ed",
          name: "Codeforces Submissions (C++)",
          images: ["codeforces.png"],
          tags: ["2014-2017", "Algorithms", "C++", "Math", "Number theory", "Bitmask", "Graph Theory", "Dynamic Programming"],
          code: "https://github.com/strcoder4007/Codeforces-Solutions",
          live: "https://codeforces.com/profile/__STR",
          description:
            "800+ Codeforces problems solved in C++ — algorithms and data structures.",
        },
        {
          id: "4e8a86ee-5a59-4c24-b0c1-d78cd165f771",
          name: "Mario Reinforcement Learning",
          images: ["https://github.com/strcoder4007/Mario-Reinforcement-Learning/blob/main/images/mario_ppo.gif?raw=true"],
          tags: ["2024", "ml", "Tensorflow 2", "Reinforcement Learning", "OpenAI Gym", "PPO Algorithm", "Python"],
          code: "https://github.com/strcoder4007/Mario-Reinforcement-Learning",
          blog: true,
          description:
            "Trained a Mario agent on Level 1‑1 with Stable Baselines 3 (PPO), TensorFlow 2, and OpenAI Gym.",
        },
        {
          id: "9c19724b-bd93-4d52-aeb0-63adca6cfce9",
          name: "Detecting Covid-19 using X-Ray Images",
          images: ["covid_19.png"],
          tags: ["2020", "ml", "Tensorflow v1", "Vision", "AlexNet", "OpenCV", "Python"],
          code: "https://github.com/strcoder4007/COVID-19-Deep-Learning",
          blog: true,
          description:
            "Built a COVID‑19 classifier on X‑ray and CT images using AlexNet, OpenCV, and TensorFlow (v1).",
        },
        {
          id: "d4d3bcde-6b2a-46e2-aef0-be0f7ec87589",
          name: "Medical MRI segmentation using UNet",
          images: ["unet.png"],
          tags: ["2024", "ml", "Tensorflow 2", "UNet", "Python"],
          code: "https://github.com/strcoder4007/U-Net-Image-Segmentation",
          description: "MRI image segmentation with a U‑Net in TensorFlow 2.",
        },
        {
          id: "1c8c2951-fbd9-41ab-8bae-ccd0a437a7b2",
          name: "YOLO V1 Implementation",
          images: ["yolo_v1.png"],
          tags: ["2021", "ml", "Tensorflow v1", "DarkNet-19", "Vision", "Python"],
          code: "https://github.com/strcoder4007/YOLO-V1-TF1",
          description:
            "A TensorFlow 1 re‑implementation of YOLOv1 using Darknet‑19 as the backbone.",
        },
        {
          id: "f5a8f22a-65bc-47ea-a9ac-aa52848b12eb",
          name: "ML Algos from Scratch to Frameworks",
          images: ["ml_dl_implementation.png"],
          tags: ["2020-2024", "ml", "Python", "Tensorflow v1&2, PyTorch"],
          code: "https://github.com/strcoder4007/Machine-Learning-Deep-Learning-Practice",
          blog: true,
          description:
            "My ML practice repo: from algorithms (Linear/Logistic Reg, K‑NN, SVM, clustering, K‑Means) to deep learning (ConvNets, ResNet, MobileNet, RNN/LSTM, RL) using NumPy, Pandas, Matplotlib, TensorFlow v1/v2, and PyTorch.",
        },



        {
          id: "bcd2eeab-bbef-4f5b-ad7a-c7db4edf89cb",
          name: "Instacode Online Judge",
          images: ["instacode.jpeg"],
          tags: ["2016", "web_dev", "Javascript", "PHP"],
          code: "https://github.com/strcoder4007/Instacode-Online-Judge",
          description: "An online judge I built for college practicals — evaluates submissions in 14 languages and ranks users on a leaderboard.",
        },
        {
          id: "6c5ec8e8-cfe9-41df-bf90-d3d0d0efcded",
          name: "Real Time Gaze Tracking",
          images: ["face_detection.png"],
          tags: ["2023", "ml", "web_dev", "OpenCV", "Python", "Javascript"],
          code: "https://github.com/strcoder4007/tensorflow-face-detection",
          live: "https://strcoder4007.github.io/eye-tracking/",
          description: "Real‑time eye tracking and face mesh rendering with OpenCV and MediaPipe FaceMesh. Live demo included.",
        },
        {
          id: "3a98e5fc-0c4a-4c5f-a2ea-dd06a4a615b8",
          name: "Memory Sequence",
          images: ["memseq.jpeg"],
          tags: ["2017", "web_dev", "Javascript", "Angular 4", "Typescript 2"],
          code: "https://github.com/strcoder4007/memorySequence",
          description:
            "A from‑scratch blogging app I wrote to learn Angular 4 + TypeScript 2 (later updated to Angular 7).",
        },
        {
          id: "c7bf5bc0-44dd-4b4d-a4c4-28ab2bb8ff8b",
          name: "Graphic Designer Portfolio Website",
          images: ["graphic_designer_portfolio.png"],
          tags: ["2024", "web_dev", "Javascript", "Vue 3", "Element UI"],
          code: "https://github.com/strcoder4007/graphic-designer-portfolio",
          live: "https://strcoder4007.github.io/graphic-designer-portfolio/",
          description:
            "A portfolio site for a graphic designer, built with Vue 3 and Element Plus.",
        },
        {
          id: "bf07d3ca-ee63-4fcc-a061-ceabbe0b6b23",
          name: "Town Center (old portfolio website)",
          images: ["town_center.jpeg"],
          tags: ["2017", "web_dev", "Javascript", "Angular 7", "Typescript 3"],
          code: "https://github.com/strcoder4007/theTownCenter",
          description: "My 2018 portfolio site showcasing projects and code (Angular 7 + TypeScript 3).",
        },
        {
          id: "7e5d83ac-ae1e-47ed-abeb-d39c2e28cbbe",
          name: "AI/ML Engineer Portfolio Website",
          images: ["mle.png"],
          tags: ["2024", "web_dev", "Javascript", "Vue 3", "Element UI"],
          code: "https://github.com/strcoder4007/portfolio",
          live: "https://strcoder4007.github.io/portfolio/",
          description:
            "My current portfolio with blogs, built with Vue 3 and Element Plus.",
        },
        {
          id: "9a3efbda-4a9e-498e-ad2c-d4b9c5f5d167",
          name: "TimeMyShow",
          images: ["tms.jpeg"],
          tags: ["2017", "web_dev", "Javascript", "Angular 7", "Typescript 3"],
          code: "https://github.com/strcoder4007/timeMyShow",
          description:
            "A PWA to follow TV shows and get new‑episode alerts; built with Angular 7 and TypeScript 3.",
        },
        {
          id: "fd0a94dc-b5dd-4df8-aeba-c6d55425ceea",
          name: "BAJASAE India Website",
          images: [""],
          tags: ["2016", "web_dev", "Javascript"],
          code: "https://github.com/strcoder4007/SAE-KIET-Website",
          description: "Official website for BAJA SAE India (mechanical team site).",
        },
        {
          id: "27a5e908-a946-4bdb-8dca-f2c7ad93abde",
          name: "Code Hour",
          images: [""],
          tags: ["2014", "web_dev", "Javascript"],
          code: "https://github.com/strcoder4007/Code_Hour",
          description:
            "Open‑source tool that tracks competitive programming contests across sites so you never miss one.",
        },


        {
          id: "936ba873-6d1a-4edd-acf0-ffa5e1aa2c24",
          name: "Sphere Online Judge Submissions (C++)",
          images: ["spoj.png"],
          tags: ["algo", "2014-2017", "C++", "Math", "Number theory", "Bitmask", "Graph Theory"],
          code: "https://github.com/strcoder4007/spoj",
          live: "https://www.spoj.com/users/strcoder4007/",
          description:
            "180+ SPOJ problems solved in C++ — algorithms and data structures.",
        },
      ]

export default {
  name: "ProjectsSection",
  data() {
    return {
      activeTab: 'show_all',
      projectList: allProjects
    };
  },
  methods: {
    tabChange(tab) {
      this.projectList = JSON.parse(JSON.stringify(allProjects))
      this.activeTab = tab
      if (tab != 'show_all')
        this.projectList = this.projectList.filter(proj => proj.tags.includes(tab))
    }
  },
  components: {
    TabsComponent,
    LandingComponent,
  },
};
</script>

<style lang="scss" scoped>
.container {
  background: #222222;
  overflow-y: hidden;
}
.projects-section {
  overflow-y: scroll;
  height: calc(100vh - 80px);
  background: transparent;
  backdrop-filter: blur(2px);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;

  .greetings {
    margin-top: 20px;
    color: #fff;
    font-family: Bricolage;
    font-size: 40px;
    font-style: normal;
    font-weight: 600;
    line-height: 72px;
    letter-spacing: -1px;
  }
}
@media (max-width: 768px) {
  .container {
    padding-top: 60px;
  }
  .projects-section {
    height: auto;
    width: 100vw;
    .greetings {
      float: left;
      text-align: left;
      margin-top: 20px;
      font-size: 30px;
      font-weight: 700;
    }
  }
}
</style>
