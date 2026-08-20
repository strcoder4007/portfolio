<template>
  <div class="project-tabs-page">
    <div class="tab-card">
      <button
        v-for="tab in tabs"
        :key="tab.id"
        :id="tab.id"
        class="tab"
        :class="{ 'active': activeTab === tab.id }"
        @click="selectTab(tab.id)"
      >
        <span class="tab-label">{{ tab.label }}</span>
        <span class="tab-count">{{ tab.count }}</span>
      </button>
    </div>
  </div>
</template>

<script>
const TAB_IDS = ['show_all', 'ml', 'web_dev', 'algo'];

const TAB_LABELS = {
  show_all: 'All',
  ml: 'AI/ML',
  web_dev: 'Web',
  algo: 'Algo'
};

export default {
  name: "ProjectTabsPage",
  props: {
    allProjects: {
      type: Array,
      required: true
    }
  },
  emits: ['tabChange'],
  data() {
    return {
      activeTab: 'show_all'
    };
  },
  computed: {
    tabs() {
      return TAB_IDS.map(id => ({
        id,
        label: TAB_LABELS[id],
        count: this.getCount(id)
      }));
    }
  },
  methods: {
    getCount(id) {
      if (id === 'show_all') return this.allProjects.length;
      return this.allProjects.filter(p => p.tags && p.tags.includes(id)).length;
    },
    removeAllActiveClasses() {
      for (const id of TAB_IDS) {
        const btn = document.getElementById(id);
        if (btn) btn.classList.remove('active');
      }
    },
    selectTab(tab) {
      this.activeTab = tab;
      this.$emit('tabChange', tab);
    }
  }
};
</script>

<style lang="scss" scoped>
.project-tabs-page {
  display: flex;
  justify-content: center;
  margin: 28px 0 40px;
}

.tab-card {
  display: inline-flex;
  align-items: center;
  gap: 0;
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  padding: 4px;
}

.tab {
  background: transparent;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-family: var(--font-heading);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  color: var(--color-text-dim);
  position: relative;
  transition: color 0.15s ease, background 0.15s ease;
}

.tab:hover {
  color: var(--color-text);
  background: rgba(38, 44, 53, 0.05);
}

.tab.active {
  color: var(--color-bg);
  background: var(--color-text);
}

.tab-count {
  font-family: var(--font-mono);
  font-size: 11px;
  margin-left: 6px;
  opacity: 0.6;
}

@media (max-width: 768px) {
  .tab-card {
    max-width: 100%;
    justify-content: space-between;
    padding: 3px;
  }
  .tab {
    padding: 8px 10px;
    font-size: 11px;
  }
  .tab-label {
    display: inline-block;
  }
  .tab-count {
    display: none;
  }
}
</style>