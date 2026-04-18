<template>
  <NavBar></NavBar>
  <router-view></router-view>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

@font-face {
  font-family: 'Bricolage';
  src: url('./assets/fonts/BricolageGrotesque.ttf');
}
@font-face {
  font-family: 'Brandon';
  src: url('./assets/fonts/Brandon_reg.otf');
}

html {
  scroll-behavior: smooth;
  height: auto;
}
::selection {
  color: #111111;
  background: #1DB954;
}

#app {
  font-family: Bricolage, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  opacity: 0; /* Start invisible */
  animation: fade-in 1s ease-in-out forwards;
}

/* Subtle noise texture overlay — works on both dark and light backgrounds */
#app::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.035;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-size: 200px 200px;
  mix-blend-mode: soft-light;
  -webkit-mix-blend-mode: soft-light;
}
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
body {
  margin: 0;
  background: #111111;
  background-position: 0 0;
  background-size: 200% 100%;
  animation: background-move 10s linear infinite;
  position: relative;
}
@keyframes background-move {
  from { background-position: 0 0; }
  to { background-position: -200% 0; }
}
button:hover {
  cursor: pointer;
  /* transform: scale(1.05); Slightly enlarge on hover */
  transition: transform 0.2s ease-in-out;
}

button:active {
  transform: translateY(2px); /* Slightly sink on press */
  transition: transform 0.1s ease-in-out;
}

input:focus {
  border-color: #f00; /* Change border color on focus */
  transition: border-color 0.2s ease-in-out;
}

.el-message__content {
  font-family: Bricolage;
}
</style>
