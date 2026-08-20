<template>
  <div class="project-landing-page">
    <el-row :gutter="40">
      <el-col
        :xs="24"
        :sm="12"
        :md="8"
        :xl="6"
        v-for="project in projectList"
        :key="project.id"
        class="project-container"
      >
        <div class="cvfy-container">
          <div class="cvfy-card" @click="openModal(resolveImage(project.images[0]))">
            <div class="card-header">
              <div class="window-controls">
                <span class="control red"></span>
                <span class="control yellow"></span>
                <span class="control green"></span>
              </div>
              <span class="card-filename mono-meta">{{ project.name }}</span>
            </div>
            <div class="card-body image-container">
              <img :src="resolveImage(project.images[0])" :alt="project.name" />
              <div class="overlay">
                <svg class="maximize-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>
              </div>
            </div>
          </div>
          <div class="project-name">{{ project.name }}</div>
          <div class="project-description">
            {{ project.description }}
          </div>
          <div class="tags-section">
            <span :key="tag" v-for="tag in filterTags(project.tags)">{{ tag }}</span>
          </div>
          <div class="links-container">
            <button
              v-if="project.hasOwnProperty('live')"
              class="link-pill live"
              type="button"
              @click="goToLink(project.live)"
            >
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>
              Live
            </button>
            <button
              v-if="project.hasOwnProperty('code')"
              class="link-pill code"
              type="button"
              @click="goToLink(project.code)"
            >
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
              Code
            </button>
            <button
              v-if="project.hasOwnProperty('blog') && project.blog"
              class="link-pill blog"
              type="button"
              @click="goToLink(project.blog)"
            >
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
              Blog
            </button>
          </div>
        </div>
      </el-col>
    </el-row>

    <Teleport to="body">
      <div
        v-if="showModal"
        class="modal-overlay"
        role="dialog"
        aria-modal="true"
        :aria-label="modalAlt || 'Project preview'"
        @click.self="closeModal"
      >
        <button
          class="modal-close"
          type="button"
          aria-label="Close preview"
          @click="closeModal"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2.2"
            stroke-linecap="round"
            stroke-linejoin="round"
            aria-hidden="true"
          >
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
        <div class="modal-content" @click.stop>
          <img
            v-if="!isVideo"
            :src="modalImage"
            :alt="modalAlt"
            class="modal-media"
          />
          <video
            v-else
            :src="modalImage"
            class="modal-media"
            controls
            autoplay
            loop
            playsinline
          ></video>
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

import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue';

export default {
  name: 'ProjectLandingPage',

  setup() {
    const router = useRouter();
    const showModal = ref(false);
    const modalImage = ref('');
    const modalAlt = ref('');

    const goToLink = (url) => {
      if (typeof url === 'boolean') {
        router.push('/blogs');
      } else {
        window.open(url, '_blank');
      }
    };

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
    };

    const resolveImage = (imageName) => {
      if (imageSources[imageName]) {
        return imageSources[imageName];
      }
      return imageName;
    };

    const isVideo = computed(() => {
      const src = modalImage.value;
      if (!src) return false;
      const cleaned = String(src).split('?')[0].split('#')[0].toLowerCase();
      return /\.(mp4|webm|ogg|mov|m4v)(\s|$)/.test(cleaned);
    });

    const openModal = (image, alt) => {
      modalImage.value = resolveImage(image);
      modalAlt.value = alt || '';
      showModal.value = true;
    };

    const closeModal = () => {
      showModal.value = false;
      modalImage.value = '';
      modalAlt.value = '';
    };

    const onKeydown = (e) => {
      if (e.key === 'Escape' && showModal.value) {
        closeModal();
      }
    };

    onMounted(() => {
      window.addEventListener('keydown', onKeydown);
    });
    onBeforeUnmount(() => {
      window.removeEventListener('keydown', onKeydown);
      document.body.style.overflow = '';
    });

    watch(showModal, (open) => {
      document.body.style.overflow = open ? 'hidden' : '';
    });

    return {
      imageSources,
      goToLink,
      showModal,
      modalImage,
      modalAlt,
      isVideo,
      openModal,
      closeModal,
      resolveImage
    };
  },
  props: {
    projectList: {
      type: Array,
      required: true
    }
  },
  data() {
    return {};
  },
  methods: {
    filterTags(projectTags) {
      let tabs = ['show_all', 'ml', 'web_dev', 'algo'];
      return projectTags.filter(tag => !tabs.includes(tag));
    }
  }
};
</script>

<style scoped>
.project-landing-page {
  margin: 0 auto;
  padding: 0 48px 64px;
  max-width: 1400px;
  width: 100%;
}
.project-container {
  margin-bottom: 40px;
}
.image-container {
  width: 100%;
  aspect-ratio: 16 / 11;
  background-color: var(--color-bg-alt);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  border: 1px solid var(--color-border);
}
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(38, 44, 53, 0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.2s ease;
  z-index: 10;
  cursor: pointer;
}
.image-container:hover .overlay {
  opacity: 1;
}
.maximize-icon {
  width: 22px;
  height: 22px;
  stroke: var(--color-bg);
  transition: transform 0.2s ease;
}
.overlay:hover .maximize-icon {
  transform: scale(1.15);
}
.image-container img {
  max-width: 100%;
  max-height: 100%;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  background-color: var(--color-bg-alt);
  transition: transform 0.35s ease;
}
.image-container:hover img {
  transform: scale(1.05);
}
.tags-section {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 10px;
  margin-bottom: 12px;
  margin-top: 14px;
}
.tags-section span {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  color: var(--color-text-dim);
  border: 1px solid var(--color-border);
  padding: 3px 8px;
  background: transparent;
}
.cvfy-container {
  max-width: 100%;
  width: 100%;
  margin: 0;
}
.cvfy-card {
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.cvfy-card:hover {
  transform: translateY(-2px);
  box-shadow: 4px 4px 0 var(--color-border);
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 14px;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
}
.window-controls {
  display: flex;
  gap: 6px;
}
.control {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: 1px solid var(--color-border);
}
.control.red { background-color: #E55C5C; }
.control.yellow { background-color: #E5C15C; }
.control.green { background-color: #5CE55C; }
.card-filename {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--color-text-dim);
  letter-spacing: 0.3px;
}
.project-name {
  font-family: var(--font-heading);
  font-size: 20px;
  font-weight: 700;
  text-align: left;
  color: var(--color-text);
  margin-top: 14px;
  letter-spacing: -0.01em;
  line-height: 1.2;
}
.project-description {
  font-family: var(--font-body);
  font-size: 14px;
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0.2px;
  text-align: left;
  margin: 8px 0 0;
  color: var(--color-text-dim);
  display: block;
}
.links-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
  justify-content: flex-start;
}
.links-container .link-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-height: 36px;
  padding: 8px 14px;
  background: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text);
  font-family: var(--font-heading);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.4px;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
}
.links-container .link-pill svg {
  width: 12px;
  height: 12px;
  transition: transform 0.15s ease;
}
.links-container .link-pill:hover {
  background: var(--color-text);
  color: var(--color-bg);
  border-color: var(--color-text);
}
.links-container .link-pill:hover svg {
  transform: translateX(2px);
}
.links-container .link-pill:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
.modal-overlay {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(38, 44, 53, 0.94);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  padding: 72px 20px 20px;
  animation: modal-fade-in 0.18s ease-out;
  overflow: auto;
}
@keyframes modal-fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}
.modal-content {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 100%;
  max-height: 100%;
}
.modal-media {
  display: block;
  max-width: 100%;
  max-height: calc(100vh - 92px);
  width: auto;
  height: auto;
  object-fit: contain;
  border: 1px solid var(--color-border);
  box-shadow: 8px 8px 0 var(--color-border);
  background-color: var(--color-surface);
}
video.modal-media {
  width: auto;
  max-width: min(1200px, 100%);
}
.modal-close {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 44px;
  height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  background: #1a1f26;
  color: #ffffff;
  border: 1px solid #1a1f26;
  border-radius: 50%;
  cursor: pointer;
  z-index: 10000;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
  transition: background 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
}
.modal-close:hover {
  background: #000000;
  transform: scale(1.06);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.45);
}
.modal-close:active {
  transform: scale(0.96);
}
.modal-close:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 3px;
}
.modal-close svg {
  width: 22px;
  height: 22px;
  display: block;
}
@media (max-width: 767px) {
  .modal-overlay {
    padding: 64px 12px 12px;
  }
  .modal-media {
    max-height: calc(100vh - 76px);
  }
  .modal-close {
    top: 12px;
    right: 12px;
    width: 38px;
    height: 38px;
  }
  .modal-close svg {
    width: 18px;
    height: 18px;
  }
}
@media (max-width: 380px) {
  .modal-close {
    top: 8px;
    right: 8px;
    width: 34px;
    height: 34px;
  }
  .modal-close svg {
    width: 16px;
    height: 16px;
  }
  .modal-overlay {
    padding: 56px 8px 8px;
  }
  .modal-media {
    max-height: calc(100vh - 64px);
  }
}
@media (max-width: 1023px) {
  .project-container {
    margin-bottom: 32px;
  }
}
@media (max-width: 767px) {
  .project-landing-page {
    padding: 0 16px 48px;
  }
  .project-container {
    margin-bottom: 28px;
  }
  .image-container {
    aspect-ratio: 16 / 10;
  }
  .project-name {
    font-size: 18px;
  }
  .project-description {
    font-size: 13px;
  }
  .tags-section span {
    font-size: 10px;
    padding: 2px 6px;
  }
  .links-container .link-pill {
    padding: 6px 10px;
    font-size: 11px;
  }
}
</style>