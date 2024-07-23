<template>
  <div class="project-landing-page">
    <el-row>
      <el-col :md="12" :lg="12" :xl="8" v-for="project in projectList" :key="project.id" class="project-container">
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
              <template v-for="image in project.images" :key="image">
                <img v-if="image.includes('.png')" :src="imageSources[image]" />
                <img v-else :src="image" />
                
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
import instacode from '../../../assets/projects/instacode.png';
import graphicDesignerPortfolio from '../../../assets/projects/graphic_designer_portfolio.png';
import spoj from '../../../assets/projects/spoj.png';
export default {
  name: "ProjectLandingPage",

  setup() {
    const router = useRouter();
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
      'instacode.png': instacode,
      'graphic_designer_portfolio.png': graphicDesignerPortfolio,
      'spoj.png': spoj,
    }

    return {
      imageSources,
      goToLink
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
    width: 350px;
    height: 200px;
    background-color: #111;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.image-container img {
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
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
  max-width: 350px;
  margin: 30px auto;
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
  font-family: Ubuntu, Bricolage;
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
    font-family: Ubuntu, Brandon;
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

@media (max-width: 768px) {
  .project-landing-page {
    margin: 60px 5px;
  }
}
</style>