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
          <!-- <li class="menu-item" :class="{ 'active': activeIndex === 'home' }" @click="handleSelect('Home')">Home</li> -->
          <li class="menu-item" :class="{ 'active': activeIndex === 'home' }" @click="handleSelect('home')">Projects</li>
          <li class="menu-item" :class="{ 'active': activeIndex === 'blogs' }" @click="handleSelect('blogs')">Blogs</li>
          <li class="menu-item" :class="{ 'active': activeIndex === 'work' }" @click="handleSelect('work')">Work</li>
          <li class="menu-item" :class="{ 'active': activeIndex === 'github' }" @click="handleSelect('github')">Github Stats</li>
          <!-- <li v-if="!isMobile" class="menu-item shubhams-portfolio" @click="handleSelect('Home')">Shubham's Portfolio</li> -->
          <li class="menu-item" :class="{ 'active': activeIndex === 'about' }" @click="handleSelect('About')">About me</li>
          <!-- <li class="menu-item" :class="{ 'active': activeIndex === 'contact' }" @click="handleSelect('Contact')">Contact</li> -->
        </ul>
      </div>
    </div>
  </header>
</template>

<script>
import { onMounted, ref, computed } from 'vue';
import { useRouter } from 'vue-router'

export default {
  setup() {
    const router = useRouter();
    const activeIndex = ref('home');
    const isMenuOpen = ref(false);

    onMounted(() => {
    })

    const handleSelect = (name) => {
      activeIndex.value = name.toLowerCase();
      isMenuOpen.value = false; // Close menu after selection
      // Handle navigation or route changes based on selected item
      router.push({name});
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
  background-color: #0c0f11 ;
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
      background-color: #0c0f11 ;
      padding: 1rem;
      box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
      opacity: 1;
      transform: translateY(0);
      transition: all 0.3s ease-in-out;
    }
  }

  .menu-toggle {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    position: absolute;
    top: 40px;
    right: 30px;
    z-index: 100;
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
    top: 85px;
    left: 0;
    z-index: 10;
    width: 100vw;

    background-color: #0c0f11 ;
    box-shadow: 0 4px 5px rgba(0, 0, 0, 0.3);
    transform: translateY(-200%);
    transition: transform 0.6s ease-in-out;

    .menu-item {
      list-style: none;
      font-weight: bold;
      text-decoration: none;
      cursor: pointer;

      font-family: Ubuntu, Brandon, sans-serif;

      border-radius: 4px;
      color: #FFFFFF;
      margin-top: -40px;
      margin-bottom: 15px;
      line-height: 50px;
      height: 50px;
      width: 200px;
      background: #0c0f11 ;


      &.active::after {
        content: '';
        display: none !important;
        width: 5px;
        height: 5px;
        background: #0c0f11 ;
        border-radius: 50%;
        margin: 0 auto;
        margin-top: 5px;
      }
    }
  }

  .menu-items.is-open {
    transform: translateX(0); /* Show menu when isMenuOpen becomes true */
  }
}
</style>