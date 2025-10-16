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
          images: [],
          tags: ["ml", "Agent", "LLM", "Automation"],
          code: "https://github.com/strcoder4007/browser-agent",
          blog: false,
          description:
            "An AI browser automation agent that plans and executes multi‑step tasks using LLM reasoning and tool control.",
        },
        {
          id: "a2c9e1d4-6b3f-45e2-9f7a-0c8b9d3e4f56",
          name: "S2S Lipsync Unreal Avatar Backend",
          images: [],
          tags: ["ml", "Speech", "TTS", "STT", "Unreal Engine", "Realtime"],
          code: "https://github.com/strcoder4007/S2S-Lipsync-UnrealAvatar-Backend",
          blog: false,
          description:
            "Speech‑to‑speech backend powering real‑time lip‑sync for an Unreal Engine avatar, integrating STT, response generation, TTS, and viseme timing.",
        },
        {
          id: "c5d7f9a1-83b2-4e9d-bc4f-2e7a6c9d0f12",
          name: "Unreal WebSocket Bridge",
          images: [],
          tags: ["ml", "Unreal Engine", "WebSocket", "Realtime"],
          code: "https://github.com/strcoder4007/unreal-websocket",
          blog: false,
          description:
            "WebSocket bridge for Unreal Engine to receive AI‑driven commands, audio, and visemes from backend services for live character animation.",
        },
        {
          id: "e17a5c2b-4f6d-49c0-9b21-83f1c4a9d7e3",
          name: "Insta Sponsor Fetch",
          images: [],
          tags: ["ml", "Data", "ETL", "Instagram", "Analytics"],
          code: "https://github.com/strcoder4007/insta-sponsor-fetch",
          blog: false,
          description:
            "Data pipeline to fetch and normalize Instagram sponsorship/collaboration metadata for analytics and reporting.",
        },
        {
          id: "85b39e2d-f5a0-67c7-ae2d-06297acbe963",
          name: "Multi Agent AI System",
          images: ["https://github.com/strcoder4007/Multi-Agent-AI-System/blob/main/image.jpg?raw=true"],
          tags: ["ml", "Gen AI", "Crew AI", "Langchain", "Agent", "2024"],
          code: "https://github.com/strcoder4007/Multi-Agent-AI-System",
          blog: false,
          description:
            "Multi-agent AI system designed to automate tasks with specialized AI Agents using CrewAI, Langchain and Llama3.1:8B, a team of agents that can work together to complete tasks using AI prompting techniques from creating tasks to generating keynote speeches.",
        },
        {
          id: "85b39e2d-f5a0-47c7-ae2d-06297acbe963",
          name: "NFS Self Driving Simulation",
          images: ["https://github.com/strcoder4007/Need-For-Speed-Self-driving/blob/main/images/nfsmw1.gif?raw=true"],
          tags: ["ml", "Tensorflow 2", "InceptionResNetV2", "Vision", "OpenCV", "Python", "2024"],
          code: "https://github.com/strcoder4007/Need-For-Speed-Self-driving",
          blog: true,
          description:
            "Training a ConvNet to play Need for Speed Most Wanted only by looking at the game, just like humans learn. Using InceptionResNetV2, OpenCV, Tensorflow 2",
        },
        {
          id: "a3b859f2-f5ea-49a2-ae91-c5be0ddf3e86",
          name: "Training Layer Visualization",
          images: ["https://github.com/strcoder4007/Training-Visualization/blob/main/images/layers.gif?raw=true"],
          tags: ["ml", "PyTorch", "OpenCV", "Python", "2024"],
          code: "https://github.com/strcoder4007/Training-Visualization",
          blog: true,
          description:
            "A tool to visualize the hidden layers of the model in real-time using PyTorch.",
        },
        {
          id: "eb66bcbb-9ff3-4bcc-a42f-1b944cfb33ed",
          name: "Codeforces Submissions (C++)",
          images: ["codeforces.png"],
          tags: ["algo", "2014-2017", "C++", "Math", "Number theory", "Bitmask", "Graph Theory", "Dynamic Programming"],
          code: "https://github.com/strcoder4007/Codeforces-Solutions",
          live: "https://codeforces.com/profile/__STR",
          description:
            "My 800+ solved Codeforces problems on Algorithms and Data Structures using C++",
        },
        {
          id: "4e8a86ee-5a59-4c24-b0c1-d78cd165f771",
          name: "Mario Reinforcement Learning",
          images: ["https://github.com/strcoder4007/Mario-Reinforcement-Learning/blob/main/images/mario_ppo.gif?raw=true"],
          tags: ["ml", "Tensorflow 2", "Reinforcement Learning", "OpenAI Gym", "PPO Algorithm", "Python", "2024"],
          code: "https://github.com/strcoder4007/Mario-Reinforcement-Learning",
          blog: true,
          description:
            "Training a Mario reinforcement learning agent on Level 1-1 using Open AI Gym and Stable Baselines 3 PPO algorithm.",
        },
        {
          id: "9c19724b-bd93-4d52-aeb0-63adca6cfce9",
          name: "Detecting Covid-19 using X-Ray Images",
          images: ["covid_19.png"],
          tags: ["2020", "ml", "Tensorflow v1", "Vision", "AlexNet", "OpenCV", "Python"],
          code: "https://github.com/strcoder4007/COVID-19-Deep-Learning",
          blog: true,
          description:
            "Detecting COVID-19 using X-ray Images, CT Scans and Deep Learning",
        },
        {
          id: "d4d3bcde-6b2a-46e2-aef0-be0f7ec87589",
          name: "Medical MRI segmentation using UNet",
          images: ["unet.png"],
          tags: ["ml", "Tensorflow 2", "UNet", "Python", "2024"],
          code: "https://github.com/strcoder4007/U-Net-Image-Segmentation",
          description: "MRI Image Segmentation using U-Net implementation in Tensorflow 2",
        },
        {
          id: "1c8c2951-fbd9-41ab-8bae-ccd0a437a7b2",
          name: "YOLO V1 Implementation",
          images: ["yolo_v1.png"],
          tags: ["ml", "Tensorflow v1", "DarkNet-19", "Vision", "Python", "2021"],
          code: "https://github.com/strcoder4007/YOLO-V1-TF1",
          description:
            "YOLO V1 implementation in Tensorflow 1 using Darknet-19 as backbone",
        },
        {
          id: "f5a8f22a-65bc-47ea-a9ac-aa52848b12eb",
          name: "ML Algos from Scratch to Frameworks",
          images: ["ml_dl_implementation.png"],
          tags: ["2020-2024", "ml", "Python", "Tensorflow v1&2, PyTorch"],
          code: "https://github.com/strcoder4007/Machine-Learning-Deep-Learning-Practice",
          blog: true,
          description:
            "My Code repo for all my implementations while learning ML. Implementation of Linear/Logistic Reg, K-NN, SVM, Clustering, K-Means, ConvNet, ResNet, MobileNet, RNN, LSTM, Reinforcement Learning etc. using Pandas, Matplotlib, NumPy PyTorch & TensorFlow v1&2",
        },



        {
          id: "bcd2eeab-bbef-4f5b-ad7a-c7db4edf89cb",
          name: "Instacode Online Judge",
          images: ["instacode.jpeg"],
          tags: ["2016", "web_dev", "Javascript", "PHP"],
          code: "https://github.com/strcoder4007/Instacode-Online-Judge",
          description: "An online coding platform similar to HackerRank I made for College Practicals that evaluates code submissions in 14 different programming languages and ranks participants on a leaderboard.",
        },
        {
          id: "6c5ec8e8-cfe9-41df-bf90-d3d0d0efcded",
          name: "Real Time Gaze Tracking",
          images: ["face_detection.png"],
          tags: ["ml", "web_dev", "OpenCV", "Python", "Javascript"],
          code: "https://github.com/strcoder4007/tensorflow-face-detection",
          live: "https://strcoder4007.github.io/eye-tracking/",
          description: "Tracking Eyeball and face mesh rendering in real time using OpenCV and MediaPipeFaceMesh.",
        },
        {
          id: "3a98e5fc-0c4a-4c5f-a2ea-dd06a4a615b8",
          name: "Memory Sequence",
          images: ["memseq.jpeg"],
          tags: ["2017", "web_dev", "Javascript", "Angular 4", "Typescript 2"],
          code: "https://github.com/strcoder4007/memorySequence",
          description:
            "A web app for blogging with everything written from scratch. Made this to teach myself Angular 4 + Typescript back in 2017. Currently updated to Angular 7.",
        },
        {
          id: "c7bf5bc0-44dd-4b4d-a4c4-28ab2bb8ff8b",
          name: "Graphic Designer Portfolio Website",
          images: ["graphic_designer_portfolio.png"],
          tags: ["2024", "web_dev", "Javascript", "Vue 3", "Element UI"],
          code: "https://github.com/strcoder4007/graphic-designer-portfolio",
          live: "https://strcoder4007.github.io/graphic-designer-portfolio/",
          description:
            "Graphic Designer Portfolio Website written in Vue 3 and Element Plus UI",
        },
        {
          id: "bf07d3ca-ee63-4fcc-a061-ceabbe0b6b23",
          name: "Town Center (old portfolio website)",
          images: ["town_center.jpeg"],
          tags: ["2017", "web_dev", "Javascript", "Angular 7", "Typescript 3"],
          code: "https://github.com/strcoder4007/theTownCenter",
          description: "My 2018 Portfolio website to showcase all projects and code",
        },
        {
          id: "7e5d83ac-ae1e-47ed-abeb-d39c2e28cbbe",
          name: "ML Engineer Portfolio Website",
          images: ["mle.png"],
          tags: ["2024", "web_dev", "Javascript", "Vue 3", "Element UI"],
          code: "https://github.com/strcoder4007/portfolio",
          live: "https://strcoder4007.github.io/portfolio/",
          description:
            "Machine Learning Engineer Portfolio website with blogs written in Vue 3",
        },
        {
          id: "9a3efbda-4a9e-498e-ad2c-d4b9c5f5d167",
          name: "TimeMyShow",
          images: ["tms.jpeg"],
          tags: ["2017", "web_dev", "Javascript", "Angular 7", "Typescript 3"],
          code: "https://github.com/strcoder4007/timeMyShow",
          description:
            "A progressive web app to search and subscribe to tv shows for new episodes of all subscribed shows sorted, written in Angular 7 & Typescript 3",
        },
        {
          id: "fd0a94dc-b5dd-4df8-aeba-c6d55425ceea",
          name: "BAJASAE India Website",
          images: [""],
          tags: ["2016", "web_dev", "Javascript"],
          code: "https://github.com/strcoder4007/SAE-KIET-Website",
          description: "Official website of the Mechanical BAJA SAE India",
        },
        {
          id: "27a5e908-a946-4bdb-8dca-f2c7ad93abde",
          name: "Code Hour",
          images: [""],
          tags: ["2014", "web_dev", "Javascript"],
          code: "https://github.com/strcoder4007/Code_Hour",
          description:
            "Code_Hour is an open-source web application which allows you to keep track of competitive programming contests across all websites. Code_Hour keeps you updated so you never miss a contest!",
        },


        {
          id: "936ba873-6d1a-4edd-acf0-ffa5e1aa2c24",
          name: "Sphere Online Judge Submissions (C++)",
          images: ["spoj.png"],
          tags: ["algo", "2014-2017", "C++", "Math", "Number theory", "Bitmask", "Graph Theory"],
          code: "https://github.com/strcoder4007/spoj",
          live: "https://www.spoj.com/users/strcoder4007/",
          description:
            "180+ solved SPOJ problems on Algorithms and Data Structures using C++",
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
