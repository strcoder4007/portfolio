<template>
  <header class="navbar">
    <div class="navbar-container">
      <div class="brand" @click="handleSelect('Home')">
        <span class="brand-mark">◆</span>
        <span class="brand-text">SHUBHAM_SINGH</span>
      </div>

      <nav class="navbar-menu" :class="{ 'is-open': isMenuOpen }">
        <button class="menu-toggle" @click="toggleMenu" aria-label="Toggle menu">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <ul class="menu-items">
          <li class="menu-item"
              :class="{ 'active': ['home', 'projects'].includes(activeIndex) }"
              @click="handleSelect('Projects')">Projects</li>
          <li class="menu-item"
              :class="{ 'active': activeIndex === 'about' }"
              @click="handleSelect('About')">About</li>
          <li class="menu-item"
              :class="{ 'active': activeIndex === 'blogs' }"
              @click="handleSelect('Blogs')">Blogs</li>
          <li class="menu-item"
              :class="{ 'active': activeIndex === 'github' }"
              @click="handleSelect('Github')">Github Stats</li>
        </ul>
      </nav>
    </div>
  </header>
</template>
<script>
import { onMounted, ref, computed, watch } from 'vue';
import { useRouter } from 'vue-router'

export default {
  setup() {
    const router = useRouter();
    const activeIndex = ref('home');
    const isMenuOpen = ref(false);

    const getRouteName = () => {
      const r = router.currentRoute.value;
      return r && r.name ? String(r.name).toLowerCase() : 'home';
    };

    onMounted(() => {
      activeIndex.value = getRouteName();
    });

    watch(
      () => router.currentRoute.value && router.currentRoute.value.name,
      (newVal) => {
        if (newVal) activeIndex.value = String(newVal).toLowerCase();
      }
    );

    const handleSelect = (name) => {
      activeIndex.value = name.toLowerCase();
      isMenuOpen.value = false;
      router.push({name});
      setTimeout(() => {
        if (name === 'Home') {
          document.getElementById("app-container").scrollIntoView()
        } else if (document.getElementById("projects-section"))
          document.getElementById("projects-section").scrollIntoView()
      }, 500);
    };

    const toggleMenu = () => {
      isMenuOpen.value = !isMenuOpen.value;
    };

    const isMobile = computed(() => {
      return window.innerWidth <= 768;
    })

    return {
      activeIndex,
      handleSelect,
      isMobile,
      toggleMenu,
      isMenuOpen
    };
  },
};
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

.navbar {
  width: 100%;
  height: 64px;
  padding: 0 2rem;
  background-color: var(--color-bg);
  color: var(--color-text);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  box-sizing: border-box;
  overflow-x: hidden;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  overflow-x: hidden;
  border-bottom: 1px solid var(--color-border);
}

.navbar-container {
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  min-width: 0;
  box-sizing: border-box;
  gap: 16px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  font-family: var(--font-mono);
  font-size: 15px;
  font-weight: 500;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--color-text);
  white-space: nowrap;
  flex-shrink: 0;
}

.brand-mark {
  color: var(--color-accent);
  font-size: 14px;
}

/* Desktop menu */
.navbar-menu {
  display: flex;
  flex-grow: 1;
  min-width: 0;
  justify-content: flex-end;
}

.menu-items {
  display: flex;
  gap: 28px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.menu-item {
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 14px;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  color: var(--color-text-dim);
  cursor: pointer;
  background: none;
  border: none;
  padding: 0;
  position: relative;
  white-space: nowrap;
  flex-shrink: 0;
  transition: color 0.15s ease;
}
.menu-item:hover {
  color: var(--color-text);
}

.menu-item.active {
  color: var(--color-text);
}

.menu-item.active::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -6px;
  width: 100%;
  height: 2px;
  background-color: var(--color-accent);
}

.menu-toggle {
  display: none;
  background: none;
  border: 1px solid var(--color-border);
  padding: 8px 10px;
  cursor: pointer;
  flex-direction: column;
  gap: 4px;
}

.menu-toggle span.icon-bar {
  display: block;
  width: 18px;
  height: 2px;
  background-color: var(--color-text);
  transition: 0.2s;
}

@media (max-width: 1100px) {
  .navbar {
    padding: 0 1.25rem;
  }
  .menu-items {
    gap: 18px;
  }
  .menu-item {
    font-size: 13px;
  }
}

/* Desktop: hide toggle */
@media only screen and (min-width: 769px) {
  .menu-toggle {
    display: none;
  }
}

/* Mobile */
@media only screen and (max-width: 768px) {
  .navbar {
    padding: 0 1rem;
  }

  .menu-toggle {
    display: flex;
    z-index: 101;
  }

  .navbar-menu {
    display: none;
    position: fixed;
    top: 64px;
    left: 0;
    right: 0;
    z-index: 100;
    background-color: var(--color-bg);
    border-bottom: 1px solid var(--color-border);
    padding: 0;
  }

  .navbar-menu.is-open {
    display: block;
  }

  .menu-items {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
    padding: 0;
    margin: 0;
  }

  .menu-item {
    width: 100%;
    padding: 16px 1.5rem;
    border-bottom: 1px solid var(--color-border);
    font-size: 16px;
    color: var(--color-text);
    text-align: left;
    font-family: var(--font-heading);
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }

  .menu-item.active {
    background-color: var(--color-accent);
    color: var(--color-text);
  }

  .menu-item.active::after {
    display: none;
  }
}
</style>