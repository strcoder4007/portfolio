<template>
  <div class="container" id="github-section">
    <el-row>
      <el-col class="github-section">
        <div class="greetings">GitHub</div>
        <div class="github-cards">
          <div
            v-for="(card, i) in cards"
            :key="card.label"
            :class="['card', { 'card-wide': i === cards.length - 1 }]"
          >
            <span class="card-label">{{ card.label }}</span>
            <img
              v-if="!failed[i]"
              :src="card.src"
              :alt="card.label"
              @error="onError($event, i)"
            />
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
  name: "GithubSection",
  data() {
    return {
      failed: {},
      usedFallback: {},
      cards: [
        {
          label: "Contribution Streak",
          src: "https://streak-stats.demolab.com?user=strcoder4007&theme=&background=111111&border=111111&stroke=1DB954&ring=1DB954&fire=1DB954&currStreakNum=1DB954&sideNums=1DB954&currStreakLabel=1DB954&sideLabels=1DB954&dates=1DB954&card_width=600&border_radius=2",
          fallback: "",
          link: "https://github.com/strcoder4007"
        },
        {
          label: "GitHub Stats",
          src: "https://github-readme-stats-sigma-five.vercel.app/api?username=strcoder4007&show_icons=true&theme=dark&bg_color=111111&hide_border=true&title_color=1DB954&icon_color=1DB954&text_color=ffffff",
          fallback: "",
          link: "https://github.com/strcoder4007"
        },
        {
          label: "Top Languages",
          src: "https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=strcoder4007&layout=compact&theme=dark&bg_color=111111&hide_border=true&title_color=1DB954&text_color=ffffff",
          fallback: "",
          link: "https://github.com/strcoder4007"
        },
        {
          label: "Contribution Graph",
          src: "https://github-readme-activity-graph.vercel.app/graph?username=strcoder4007&theme=github-compact&bg_color=111111&color=1DB954&line=1DB954&point=ffffff&hide_border=true",
          fallback: "https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=strcoder4007&theme=github_dark",
          link: "https://github.com/strcoder4007/contributions"
        }
      ]
    };
  },
  methods: {
    onError(e, i) {
      const card = this.cards[i];
      if (card.fallback && !this.usedFallback[i]) {
        this.usedFallback[i] = true;
        e.target.src = card.fallback;
        return;
      }
      this.failed[i] = true;
    }
  },
  mounted() {
    document.getElementById("github-section").scrollIntoView();
  }
};
</script>

<style lang="scss" scoped>

.container {
  background-color: #222222;
  background-image: var(--bg-texture-dark);
  height: 100%;
  overflow-y: hidden;
}
.github-section {
  overflow-y: scroll;
  height: calc(100vh - 60px);
  background: #222;
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

  .github-cards {
    width: min(1100px, 92%);
    margin-top: 40px;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 24px;
    padding-bottom: 60px;

    .card {
      background: #111111;
      border: 1px solid #2a2a2a;
      border-radius: 8px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
      box-shadow: 2px 2px 14px rgba(0, 0, 0, 0.3);
    }

    .card-wide {
      grid-column: 1 / -1;
    }

    .card-label {
      color: #1db954;
      font-family: 'Space Grotesk', Bricolage;
      font-size: 14px;
      font-weight: 600;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      align-self: flex-start;
    }

    .card-link {
      color: #1db954;
      font-family: 'Space Grotesk', Bricolage;
      font-size: 15px;
      font-weight: 600;
      text-decoration: none;
      padding: 28px 0;

      &:hover {
        text-decoration: underline;
      }
    }

    img {
      max-width: 100%;
      width: 100%;
      height: auto;
      border-radius: 4px;
    }
  }

  @media (max-width: 768px) {
    .github-cards {
      grid-template-columns: 1fr;
      gap: 16px;
      margin-top: 20px;

      .card {
        padding: 12px;
      }
    }
  }
}

@media (max-width: 768px) {
  .container {
    padding-top: 60px;
    overflow-y: visible;
  }
  .github-section {
    height: auto;
    min-height: calc(100vh - 60px);
    overflow-y: visible;

    .greetings {
      margin-top: 20px;
      font-size: 30px;
      font-weight: 700;
    }
  }
}
</style>
