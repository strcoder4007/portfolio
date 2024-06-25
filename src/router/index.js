import { createWebHistory, createRouter } from "vue-router";
import Home from "@/components/LandingPage.vue";
import About from "@/components/AboutPage.vue";
import Portfolio from "@/components/PortfolioPage.vue";
import Contact from "@/components/ContactPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/work",
    name: "work",
    component: Portfolio,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  }
];

const router = createRouter({
  history: createWebHistory('/graphic-designer-portfolio/'),
  routes,
});

export default router;