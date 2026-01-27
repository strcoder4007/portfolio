<template>
  <div class="project-landing-page">
    <el-row>
      <el-col :md="12" :lg="8" :xl="6" v-for="project in projectList" :key="project.id" class="project-container">
        <div class="cvfy-container">
          <div class="cvfy-card">
            <div class="card-header">
              <div class="window-controls">
                <span class="control red"></span>
                <span class="control yellow"></span>
                <span class="control green"></span>
              </div>
            </div>
            <div class="card-body image-container">
              <div class="overlay" @click="openModal(project.images[0])">
                 <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="maximize-icon">
                  <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7" />
                 </svg>
              </div>
              <template v-for="image in project.images" :key="image">
                <img :src="resolveImage(image)" />
              </template>
              
            </div>
          </div>
          <div class="project-name">{{  project.name }}</div>
          <div class="project-description">
            {{ project.description }}
          </div>
          <div class="tags-section">
            <span :key="tag" v-for="tag in filterTags(project.tags)">{{ tag }}</span>
          </div>
          <div class="links-container">
            <div v-if="project.hasOwnProperty('live')" class="live" @click="goToLink(project.live)">
              Live 
              <img src="../../../assets/icons/right-arrow.png" alt="Arrow Right Icon" />
            </div>

            <div v-if="project.hasOwnProperty('code')" class="code" @click="goToLink(project.code)">
              Code 
              <img src="../../../assets/icons/right-arrow.png" alt="Arrow Right Icon" />
            </div>

            <div v-if="project.hasOwnProperty('blog') && project.blog" class="blog" @click="goToLink(project.blog)">
                Blog 
                <img src="../../../assets/icons/right-arrow.png" alt="Arrow Right Icon" />
            </div>
          </div>
        </div>
      </el-col>
    </el-row>

    <Teleport to="body">
      <div v-if="showModal" class="modal-overlay" @click="closeModal">
        <div class="modal-content" @click.stop>
          <img :src="modalImage" class="modal-image" />
          <button class="modal-close" @click="closeModal">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import nfsSelfDriving from '../../../assets/projects/nfs_self_driving.png';
import codeforces from '../../../assets/projects/codeforces.png';
import marioRl from '../../../assets/projects/mario_rl.gif';
import layerVisualization from '../../../assets/projects/layer_visualization.gif';
import covid19 from '../../../assets/projects/covid_19.png';
import unet from '../../../assets/projects/unet.png';
import yoloV1 from '../../../assets/projects/yolo_v1.png';
import mlDlImplementation from '../../../assets/projects/ml_dl_implementation.png';
import instacode from '../../../assets/projects/instacode.jpeg';
import graphicDesignerPortfolio from '../../../assets/projects/graphic_designer_portfolio.png';
import spoj from '../../../assets/projects/spoj.png';
import mle from '../../../assets/projects/mle.png';
import faceDetection from '../../../assets/projects/face_detection.png';
import townCenter from '../../../assets/projects/town_center.jpeg';
import memseq from '../../../assets/projects/memseq.jpeg';
import tms from '../../../assets/projects/tms.jpeg';
import ecommerce from '../../../assets/projects/ecommerce.png';
import qwenEdit from '../../../assets/projects/qwen_edit.png';
import tinyDeepAgents from '../../../assets/projects/tiny_deep_agents.png';

import { ref } from 'vue';

export default {
  name: "ProjectLandingPage",

  setup() {
    const router = useRouter();
    const showModal = ref(false);
    const modalImage = ref('');

    const goToLink = (url) => {
      if (typeof url === 'boolean') {
        router.push('/blogs');
      } else window.open(url, '_blank');
    }

    const imageSources = {
      'nfs_self_driving.png': nfsSelfDriving,
      'codeforces.png': codeforces,
      'mario_rl.gif': marioRl,
      'layer_visualization.gif': layerVisualization,
      'covid_19.png': covid19,
      'unet.png': unet,
      'yolo_v1.png': yoloV1,
      'ml_dl_implementation.png': mlDlImplementation,
      'instacode.jpeg': instacode,
      'graphic_designer_portfolio.png': graphicDesignerPortfolio,
      'spoj.png': spoj,
      'mle.png': mle,
      'face_detection.png': faceDetection,
      'town_center.jpeg': townCenter,
      'memseq.jpeg': memseq,
      'tms.jpeg': tms,
      'ecommerce.png': ecommerce,
      'qwen_edit.png': qwenEdit,
      'tiny_deep_agents.png': tinyDeepAgents
    }

    const resolveImage = (imageName) => {
      if (imageSources[imageName]) {
        return imageSources[imageName];
      }
      return imageName;
    };

    const openModal = (image) => {
      modalImage.value = resolveImage(image);
      showModal.value = true;
    };

    const closeModal = () => {
      showModal.value = false;
    };

    return {
      imageSources,
      goToLink,
      showModal,
      modalImage,
      openModal,
      closeModal,
      resolveImage
    }
  },

  props: {
    projectList: {
      type: Array,
      required: true
    },
  },  
  data() {
    return {}
  },
  methods: {
    filterTags(projectTags) {
      let tabs = ['show_all', 'ml', 'web_dev', 'algo']
      return projectTags.filter(tag => !tabs.includes(tag))
    }
  },
  components: {
  },
};
</script>

<style lang="scss" scoped>
.project-landing-page {
  margin: 0 20px;
  width: 96%;
}

.image-container {
    width: 320px;
    height: 200px;
    background-color: #111;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 10;
  cursor: pointer;
}

.image-container:hover .overlay {
  opacity: 1;
}

.maximize-icon {
  width: 24px;
  height: 24px;
  stroke: #fff;
  transition: transform 0.2s ease;
}

.overlay:hover .maximize-icon {
  transform: scale(1.1);
}

.image-container img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    display: block;
    background-color: #000;
    margin: 0 auto;
    position: relative;
}

.tags-section {
  white-space: nowrap;
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 10px;
  span {
    border: 2px solid #fff;
    margin-right: 10px;
    margin-bottom: 5px;
    border-radius: 15px;
    padding: 5px;
    font-size: 12px;
    line-height: 13px;
  }
}


.cvfy-container {
  max-width: 320px;
  margin: 20px auto;
}

.cvfy-card {
  background-color: #111;
  border-radius: 5px;
  overflow: hidden;
  margin-bottom: 40px;
  cursor: pointer;
  box-shadow: 2px 2px 14px rgba(0, 0, 0, 0.3);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px 10px 10px;
  height: 5px;
}

.window-controls {
  display: flex;
  gap: 5px;
}

.control {
  width: 9px;
  height: 9px;
  border-radius: 50%;
}

.control.red { background-color: #666; }
.control.yellow { background-color: #666; }
.control.green { background-color: #666; }

.project-name {
  font-size: 23px;
  font-weight: 600;
  text-align: left;
  font-family: 'Space Grotesk', Bricolage;
  display: flex;
  color: #fff;
  margin-top: -20px;
}

.project-description {
  font-size: 15px;
  font-family: Bricolage;
  font-weight: 300;
  line-height: 19px;
  letter-spacing: 1px;
  display: flex;
  text-align: left;
  margin: 10px 0;
  color: #fff;
}

.links-container {
  display: flex;
  flex-direction: row;
  justify-content: start;
  .live, .code, .blog, .behance, .figma {
    font-size: 18px;
    font-weight: 500;
    font-family: 'Space Grotesk', Brandon;
    margin-right: 30px;
    color: #fff;
    cursor: pointer;
    img {
      height: 20px;
      margin-bottom: -5px;
      margin-left: 2px;
    }
  }
  .live:hover, .code:hover, .blog:hover, .behance:hover, .figma:hover {
    text-decoration: underline;
    text-decoration-color: #1DB954;
    text-decoration-thickness: 3px;
  }
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.modal-content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
}

.modal-image {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 4px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}

.modal-close {
  position: absolute;
  top: -40px;
  right: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  color: white;
  padding: 5px;
}

.modal-close:hover {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
}

@media (min-width: 1200px) and (max-width: 1400px) {
  .image-container {
    width: 280px;
  }
  .cvfy-container {
    max-width: 280px;
  }
  .project-name {
    font-size: 21px;
  }
  .project-description {
    font-size: 13px;
  }
  .links-container .live, .links-container .code, .links-container .blog {
    font-size: 16px;
  }
}

@media (max-width: 768px) {
  .project-landing-page {
    margin: 0;
    width: 100vw;
  }
}
</style>
