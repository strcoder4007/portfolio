<template>
  <div class="container" id="projects-section">
    <el-row>
      <el-col class="projects-section">
        <div class="greetings">Projects</div>
        <TabsComponent
          :projectList="projectList"
          @tabChange="tabChange"
        ></TabsComponent>
        <LandingComponent :projectList="projectList"></LandingComponent>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import TabsComponent from "./project/TabsComponent.vue";
import LandingComponent from "./project/LandingComponent.vue";


const allProjects = [
        {
          name: "NFS Self Driving Car",
          images: ["nfs_self_driving.png"],
          tags: ["ml", "Tensorflow 2", "InceptionResNetV2", "Vision", "OpenCV", "Python"],
          code: "https://github.com/strcoder4007/Need-For-Speed-Self-driving",
          description:
            "Training a ConvNet to play Need for Speed Most Wanted only by looking at the game, just like humans learn. Using InceptionResNetV2, OpenCV, Tensorflow 2",
        },
        {
          name: "Mario Reinforcement Learning",
          image: ["mario_rl.png"],
          tags: ["ml", "Tensorflow 2", "Reinforcement Learning", "OpenAI Gym", "PPO Algorithm", "Python"],
          code: "https://github.com/strcoder4007/Mario-Reinforcement-Learning",
          description:
            "Training a Mario reinforcement learning agent using Open AI Gym and Stable Baselines 3 PPO algorithm.",
        },
        {
          name: "Training Layer Visualization",
          image: ["layer_visualization.png"],
          tags: ["ml", "PyTorch", "OpenCV", "Python"],
          code: "https://github.com/strcoder4007/Training-Visualization",
          description:
            "A tool to visualize the hidden layers of the model in real-time using PyTorch.",
        },
        {
          name: "Detecting Covid-19 using X-Ray Images",
          image: ["covid_19.png"],
          tags: ["ml", "Tensorflow v1", "Vision", "AlexNet", "OpenCV", "Python"],
          code: "https://github.com/strcoder4007/COVID-19-Deep-Learning",
          description:
            "Detecting COVID-19 using X-ray Images, CT Scans and Deep Learning",
        },
        {
          name: "Medical MRI segmentation using UNet",
          image: ["unet_mri.png"],
          tags: ["ml", "Tensorflow 2", "UNet", "Python"],
          code: "https://github.com/strcoder4007/U-Net-Image-Segmentation",
          description: "MRI Image Segmentation using U-Net implementation in Tensorflow 2",
        },
        {
          name: "YOLO V1 Implementation",
          image: ["yolo_v1.png"],
          tags: ["ml", "Tensorflow v1", "DarkNet-19", "Vision", "Python"],
          code: "https://github.com/strcoder4007/YOLO-V1-TF1",
          description:
            "YOLO V1 implementation in Tensorflow 1 using Darknet-19 as backbone",
        },
        {
          name: "ML Algos from Scratch to Frameworks",
          image: [""],
          tags: ["ml", "Python", "Tensorflow v1&2, PyTorch"],
          code: "https://github.com/strcoder4007/Machine-Learning-Deep-Learning-Practice",
          description:
            "My Code repo for all my implementations while learning ML. Implementation of Linear/Logistic Reg, K-NN, SVM, Clustering, K-Means, ConvNet, ResNet, MobileNet, RNN, LSTM, Reinforcement Learning etc. using Pandas, Matplotlib, NumPy PyTorch & TensorFlow v1&2",
        },
        {
          name: "Real Time Eyeball Tracking",
          image: ["eye_tracking.png"],
          tags: ["ml", "web_dev", "OpenCV", "Python", "Javascript"],
          code: "https://github.com/strcoder4007/eye-tracking",
          live: "https://strcoder4007.github.io/eye-tracking/",
          description: "Tracking Eyeball and face mesh in real time using OpenCV.",
        },



        {
          name: "Town Center (old portfolio website)",
          images: ["town_center.png"],
          tags: ["web_dev", "Javascript", "Angular 7", "Typescript 3"],
          code: "https://github.com/strcoder4007/theTownCenter",
          description: "My 2018 Portfolio website to showcase all projects and code",
        },
        {
          name: "Memory Sequence",
          image: ["memseq.png"],
          tags: ["web_dev", "Javascript", "Angular 4", "Typescript 2"],
          code: "https://github.com/strcoder4007/memorySequence",
          description:
            "A web app for blogging with everything written from scratch. Made this to teach myself Angular 4 + Typescript back in 2017. Currently updated to Angular 7.",
        },
        {
          name: "ML Engineer Portfolio Website",
          image: ["portfolio.png"],
          tags: ["web_dev", "Javascript", "Vue 3", "Element UI"],
          code: "https://github.com/strcoder4007/portfolio",
          live: "https://strcoder4007.github.io/portfolio/",
          description:
            "Machine Learning Engineer Portfolio website with blogs written in Vue 3",
        },
        {
          name: "Tensorflow.js Face Detection",
          image: ["face_detection.png"],
          tags: ["web_dev", "Javascript", "Tensorflow.JS"],
          code: "https://github.com/strcoder4007/tensorflow-face-detection",
          live: "https://strcoder4007.github.io/eye-tracking/",
          description:
            "Face mesh render by detecting face using tensorflow.js and MediaPipeFaceMesh",
        },
        {
          name: "Graphic Designer Portfolio Website",
          image: ["graphic_designer_portfolio.png"],
          tags: ["web_dev", "Javascript", "Vue 3", "Element UI"],
          code: "https://github.com/strcoder4007/graphic-designer-portfolio",
          live: "https://strcoder4007.github.io/graphic-designer-portfolio/",
          description:
            "Graphic Designer Portfolio Website written in Vue 3 and Element Plus UI",
        },
        {
          name: "TimeMyShow",
          image: ["time_my_show.png"],
          tags: ["web_dev", "Javascript", "Angular 7", "Typescript 3"],
          code: "https://github.com/strcoder4007/timeMyShow",
          description:
            "A progressive web app to search and subscribe to tv shows for new episodes of all subscribed shows sorted, written in Angular 7 & Typescript 3",
        },
        {
          name: "BAJASAE India Website",
          image: ["baja.png"],
          tags: ["web_dev", "Javascript"],
          code: "https://github.com/strcoder4007/SAE-KIET-Website",
          description: "Official website of the Mechanical BAJA SAE India",
        },
        {
          name: "Code Hour",
          image: ["code_hour.png"],
          tags: ["web_dev", "Javascript"],
          code: "https://github.com/strcoder4007/Code_Hour",
          description:
            "Code_Hour is an open-source web application which allows you to keep track of competitive programming contests across all websites. Code_Hour keeps you updated so you never miss a contest!",
        },


        {
          name: "Codeforces Submissions (C++)",
          image: ["codeforces.png"],
          tags: ["algo", "C++", "Math", "Number theory", "Bitmask", "Graph Theory", "Dynamic Programming"],
          code: "https://github.com/strcoder4007/Codeforces-Solutions",
          live: "https://codeforces.com/profile/__STR",
          description:
            "My 800+ solved Codeforces problems on Algorithms and Data Structures using C++",
        },
        {
          name: "Sphere Online Judge Submissions (C++)",
          image: ["spoj.png"],
          tags: ["algo", "C++", "Math", "Number theory", "Bitmask", "Graph Theory"],
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
  overflow-y: scroll;
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

  .description {
    color: #fff;
    text-align: center;
    font-family: Bricolage;
    font-size: 21px;
    font-style: normal;
    font-weight: 400;
    line-height: 30px;
    margin-top: 20px;
  }
}
@media (max-width: 768px) {
  .projects-section {
    .greetings {
      margin-top: 20px;
      font-size: 40px;
      font-weight: 700;
    }

    .description {
      padding: 0 20px;
      font-size: 15px;
      line-height: 20px;
    }
  }
}
</style>
