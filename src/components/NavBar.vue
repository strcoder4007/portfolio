<template>
  <header class="navbar">
    <div class="navbar-container">
      <div class="terminal" @click="handleSelect('Home')">
          <span class="carret">&gt;</span> Shubham Singh <span class="cursor"></span>
      </div>
      <div class="navbar-menu">
        <button class="menu-toggle" @click="toggleMenu">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <ul class="menu-items" :class="{ 'is-open': isMenuOpen }">
          <li class="menu-item" :class="{ 'active': ['home', 'projects'].includes(activeIndex) }" @click="handleSelect('Projects')">Projects</li>
          <li class="menu-item" :class="{ 'active': activeIndex === 'about' }" @click="handleSelect('About')">About</li>
          <li class="menu-item" :class="{ 'active': activeIndex === 'blogs' }" @click="handleSelect('Blogs')">Blogs</li>
          <li class="menu-item" :class="{ 'active': activeIndex === 'github' }" @click="handleSelect('Github')">Github Stats</li>
        </ul>
      </div>
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

    onMounted(() => {

    });

    watch(
      () => router.currentRoute.value, // Watch the entire current route object
      (newVal) => {
        activeIndex.value = newVal.name.toLowerCase()
      }
    );

    const handleSelect = (name) => {
      activeIndex.value = name.toLowerCase();
      isMenuOpen.value = false; // Close menu after selection
      // Handle navigation or route changes based on selected item
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
.terminal {
  font-family: Ubuntu;
  font-weight: 600;
  font-size: 20px;
  color: #ffffff;
  cursor: pointer;
  .carret {
    font-size: 25px;
    color: #1DB954;
  }
}
.cursor {
  display: inline-block;
  width: 10px;
  height: 20px;
  background-color: #1DB954 ;
  animation: blink 0.7s infinite;
}
@keyframes blink {
    0% { opacity: 0; }
    49% { opacity: 0; }
    50% { opacity: 1; }
    100% { opacity: 1; }
}
button.menu-toggle {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
}

.menu-toggle span.icon-bar {
  display: block;
  width: 20px;
  height: 2px;
  margin: 2px 0;
  background-color: #ffffff;
  transition: 0.3s;
}

.navbar {
  width: calc(100% - 4rem);
  height: 60px;
  padding: 0 2rem;
  background-color: #111111 ;
  color: #ffffff;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: fixed;


  .shubhams-portfolio {
    color: #ffffff;
    font-family: Ubuntu, Brandon, sans-serif;
    font-size: 40px;
    font-style: normal;
    font-weight: 900 !important;
    line-height: 42px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 0px !important;
  }

  .navbar-container {
    display: flex;
    align-items: center;
    width: 100%;

    .brand-section,
    .social-section {
      width: auto;
    }

    .brand-icon {
      width: 30px;
      height: auto;
      cursor: pointer;
    }
    .social-icon {
      width: 15px;
      height: auto;
      cursor: pointer;
      margin-left: 15px;

      &:first-child {
        width: 20px;
        margin-bottom: -3px;
      }

      &:last-child {
        width: 20px;
      }
    }

    .navbar-menu {
      display: flex;
      flex-grow: 1;
      padding: 0px;

      .menu-items {
        display: flex;
        flex-grow: 1;
        justify-content: end;
        gap: 100px;

        .menu-item {
          list-style: none;
          font-weight: bold;
          text-decoration: none;
          cursor: pointer;

          &.active {
            color: #1DB954;
          }

          &.active::after {
            content: '>';
            display: block;
            width: 0px;
            height: 0px;
            background: #1DB954;
            margin-left: -12px;
            margin-top: -20px;
          }
        }
      }
    }
  }
}


/* Desktop styles (screens wider than 768px) */
@media only screen and (min-width: 768px) {
  .menu-toggle {
    display: none; /* Hide menu toggle button on desktop */
  }
}

/* Mobile styles (screens below 768px) */
@media only screen and (max-width: 767px) {

  .social-section {
    display: none; /* Hide social icons on mobile */
  }

  .navbar-menu {
    display: none;
    padding: 0;

    &.is-open {
      display: block;
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      background-color: #111111 ;
      padding: 1rem;
      box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
      opacity: 1;
      transform: translateY(0);
      transition: all 0.03s ease-in-out;
    }
  }

  .menu-toggle {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    position: absolute;
    top: 22px;
    right: 30px;
    z-index: 100;
    cursor: pointer;
  }

  .menu-items {
    display: flex;
    justify-content: center !important;
    flex-direction: column;
    align-items: center !important;
    gap: 0px;
    padding: 0;
    margin: 0;

    position: absolute;
    height: 350px;
    top: 60px;
    left: 0;
    z-index: 10;
    width: 100vw;

    background-color: #111111;
    box-shadow: 0 4px 5px rgba(0, 0, 0, 0.3);
    transform: translateY(-200%);
    transition: transform 0.4s ease-in-out;

    .menu-item {
      list-style: none;
      font-weight: bold;
      text-decoration: none;
      cursor: pointer;

      font-family: Ubuntu, Brandon, sans-serif;

      border-radius: 1px;
      color: #1DB954;
      margin-top: -47px;
      margin-bottom: -26px;
      line-height: 50px;
      height: 50px;
      width: 200px;
      background: transparent;

          &.active::after {
            content: '>';
            display: block;
            width: 0px;
            height: 0px;
            background: #1DB954;
            margin-left: 36px !important;
            margin-top: -51px !important;
          }
    }
  }

  .menu-items.is-open {
    transform: translateX(0); /* Show menu when isMenuOpen becomes true */
  }
}
</style>