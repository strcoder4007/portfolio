<template>
  <div class="project-landing-page">
    <el-row>
      <el-col :md="12" :xl="8" v-for="project in projectList" :key="project.id" class="project-container">
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
              <!-- <img v-if="project.image === 'dashboard_design'" src="../../../assets/projects/dashboard_design.png" />
              <img v-if="project.image === 'illustration'" src="../../../assets/projects/illustration.png" />
              <img v-if="project.image === 'website_design'" src="../../../assets/projects/website_design.png" />
              <img v-if="project.image === 'mobile_app_design'" src="../../../assets/projects/mobile_app_design.png" />
              <img v-if="project.image === 'ui_ux_design'" src="../../../assets/projects/ui_ux_design.png" /> -->
            </div>
          </div>
          <div class="project-name">{{  project.name }}</div>
          <div class="project-description">
            {{ project.description }}
          </div>
          <div class="links-container">
            <div v-if="project.hasOwnProperty('live')" class="live" @click="goToLink(project.live)">Live <img src="../../../assets/icons/right-arrow.png" alt="Arrow Right Icon" /></div>
            <div v-if="project.hasOwnProperty('code')" class="code" @click="goToLink(project.code)">Code <img src="../../../assets/icons/right-arrow.png" alt="Arrow Right Icon" /></div>
            <div v-if="project.hasOwnProperty('blog')" class="blog" @click="goToLink(project.blog)">Blog <img src="../../../assets/icons/right-arrow.png" alt="Arrow Right Icon" /></div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "ProjectLandingPage",

  setup() {
    const goToLink = (url) => {
      window.open(url, '_blank');
    }
    return {
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
  mounted() {
    
  },
  components: {
  },
};
</script>

<style lang="scss" scoped>
.project-landing-page {
  margin: 0 20px;
}
.image-container {
    width: 350px;
    height: 200px;
    background-color: #f0f0f0; 
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    overflow: hidden; 
}
.image-container.centered {
    display: flex;
    justify-content: center;
    align-items: center;
}



.cvfy-container {
  max-width: 350px;
  margin: 30px auto;
}

.cvfy-card {
  background-color: white;
  border-radius: 5px;
  overflow: hidden;
  margin-bottom: 40px;
  cursor: pointer;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px 10px 10px;
  border-bottom: 1px solid #ebeef5;
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

.control.red { background-color: #cccccc; }
.control.yellow { background-color: #cccccc; }
.control.green { background-color: #cccccc; }

.project-name {
  font-size: 25px;
  font-weight: 600;
  font-family: Ubuntu, Bricolage;
  display: flex;
  color: #fff;
  margin-top: -20px;
}

.project-description {
  font-size: 15px;
  font-family: Bricolage;
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
    font-family: ubuntu-medium, Brandon;
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