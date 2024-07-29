import { createWebHashHistory, createRouter } from "vue-router";
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
  }
];

const router = createRouter({
  history: createWebHashHistory('/portfolio/'),
  routes,
});

export default router;