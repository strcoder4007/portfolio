import { createWebHistory, createRouter } from "vue-router";
import Home from "@/components/LandingPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/projects",
    name: "Projects",
    component: Home,
  },
  {
    path: "/blogs",
    name: "Blogs",
    component: Home,
  },
  {
    path: "/github",
    name: "Github",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: Home,
  },
  {
    path: "/resume",
    name: "Resume",
    component: Home,
  },
];

const router = createRouter({
  history: createWebHistory('/portfolio/'),
  routes,
});

export default router;