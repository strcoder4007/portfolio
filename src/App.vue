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

#app {
  font-family: Bricolage, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  opacity: 0; /* Start invisible */
  animation: fade-in 1s ease-in-out forwards;
}
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
body {
  margin: 0;
  background: linear-gradient(to bottom, #ffffff 0%, #FF745B 100%);
  background-position: 0 0;
  background-size: 200% 100%;
  animation: background-move 10s linear infinite;
}
@keyframes background-move {
  from { background-position: 0 0; }
  to { background-position: -200% 0; }
}
button:hover {
  cursor: pointer;
  transform: scale(1.05); /* Slightly enlarge on hover */
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
