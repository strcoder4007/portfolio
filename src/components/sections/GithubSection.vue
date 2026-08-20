<template>
  <div class="container" id="github-section">
    <el-row>
      <el-col class="github-section">
        <div class="greetings">GitHub</div>
        <div class="github-cards">
          <div
            v-for="(card, i) in cards"
            :key="card.label"
            :class="['card', { 'card-wide': i === cards.length - 1, 'card-failed': failed[i] }]"
          >
            <span class="card-label">{{ card.label }}</span>
            <div v-if="!failed[i]" class="card-image-wrap">
              <div v-if="!loaded[i]" class="card-skeleton"></div>
              <img
                :src="card.src"
                :alt="card.label"
                @load="onLoad(i)"
                @error="onError($event, i)"
                :class="['card-img', { 'is-loaded': loaded[i] }]"
              />
            </div>
            <a
              v-else
              :href="card.link"
              target="_blank"
              rel="noopener"
              class="card-link"
            >View {{ card.label }} on GitHub &rarr;</a>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'GithubSection',
  data() {
    return {
      failed: {},
      loaded: {},
      usedFallback: {},
      cards: [
        {
          label: 'GitHub Stats',
          src: 'https://github-readme-stats-sigma-five.vercel.app/api?username=strcoder4007&show_icons=true&theme=default&bg_color=E9E4E0&hide_border=true&title_color=262C35&icon_color=262C35&text_color=262C35&border_radius=0',
          fallback: 'https://github-readme-stats.vercel.app/api?username=strcoder4007&show_icons=true&theme=default&bg_color=E9E4E0&hide_border=true&title_color=262C35&icon_color=262C35&text_color=262C35&border_radius=0',
          link: 'https://github.com/strcoder4007'
        },
        {
          label: 'Top Languages',
          src: 'https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=strcoder4007&layout=compact&theme=default&bg_color=E9E4E0&hide_border=true&title_color=262C35&text_color=262C35&border_radius=0',
          fallback: 'https://github-readme-stats.vercel.app/api/top-langs/?username=strcoder4007&layout=compact&theme=default&bg_color=E9E4E0&hide_border=true&title_color=262C35&text_color=262C35&border_radius=0',
          link: 'https://github.com/strcoder4007'
        },
        {
          label: 'Contribution Streak',
          src: 'https://streak-stats.demolab.com?user=strcoder4007&theme=dark&background=E9E4E0&border=262C35&stroke=262C35&ring=CFBEBE&fire=CFBEBE&currStreakNum=262C35&sideNums=262C35&currStreakLabel=262C35&sideLabels=262C35&dates=262C35&card_width=600&border_radius=0',
          fallback: '',
          link: 'https://github.com/strcoder4007'
        },
        {
          label: 'Contribution Graph',
          src: 'https://github-readme-activity-graph.vercel.app/graph?username=strcoder4007&theme=github-light&bg_color=E9E4E0&color=262C35&line=262C35&point=CFBEBE&hide_border=true&radius=0',
          fallback: 'https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=strcoder4007&theme=default',
          link: 'https://github.com/strcoder4007/contributions'
        }
      ]
    };
  },
  mounted() {
    document.getElementById('github-section')?.scrollIntoView();
  },
  methods: {
    onLoad(i) {
      this.loaded[i] = true;
    },
    onError(e, i) {
      const card = this.cards[i];
      if (card.fallback && !this.usedFallback[i]) {
        this.usedFallback[i] = true;
        e.target.src = card.fallback;
        return;
      }
      this.failed[i] = true;
    }
  }
};
</script>

<style scoped>
.container {
  background-color: transparent;
  height: 100%;
}
.github-section {
  overflow-y: visible;
  min-height: calc(100vh - 64px);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 32px 24px 64px;
}
.greetings {
  margin: 8px 0 24px;
  color: var(--color-text);
  font-family: var(--font-heading);
  font-size: 40px;
  font-weight: 700;
  line-height: 0.95;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  align-self: flex-start;
}
.github-cards {
  width: 100%;
  max-width: 1100px;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
  overflow: hidden;
}
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 12px;
  min-width: 0;
}
.card-wide {
  grid-column: 1 / -1;
}
.card-failed {
  min-height: 120px;
  justify-content: center;
}
.card-label {
  color: var(--color-accent);
  font-family: var(--font-heading);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
.card-image-wrap {
  position: relative;
  min-height: 80px;
}
.card-skeleton {
  position: absolute;
  inset: 0;
  background: var(--color-bg-alt);
  animation: shimmer 1.4s infinite linear;
  background: linear-gradient(100deg, var(--color-bg-alt) 30%, var(--color-surface) 50%, var(--color-bg-alt) 70%);
  background-size: 200% 100%;
}
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
.card-img {
  max-width: 100%;
  width: 100%;
  height: auto;
  display: block;
  opacity: 0;
  transition: opacity 0.3s ease;
}
.card-img.is-loaded {
  opacity: 1;
}
.card-link {
  color: var(--color-text);
  font-family: var(--font-heading);
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  padding: 24px 0;
  border: 1px dashed var(--color-border);
  text-align: center;
  transition: color 0.15s ease;
}
.card-link:hover {
  color: var(--color-accent);
}
@media (max-width: 767px) {
  .github-cards {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .greetings {
    font-size: 30px;
  }
  .github-section {
    padding: 24px 12px 48px;
  }
}
</style>