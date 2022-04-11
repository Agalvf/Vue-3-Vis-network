import { createRouter, createWebHistory } from "vue-router";
import App from "../App.vue";
import Shark from "../components/Shark.vue";
import Grafos from "../components/Grafos.vue";

const routes = [
  {
    path: "/",
    name: "App",
    component: App,
  },
  {
    path: "/shark",
    name: "Shark",
    component: Shark,
  },
  {
    path: "/grafos",
    name: "Grafos",
    component: Grafos,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
