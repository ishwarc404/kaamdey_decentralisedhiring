import HomePage from "../components/homePage.vue";
import searchPage from "../components/searchPage.vue";

const definedRoutes = [
  {
    path: "/home",
    component: HomePage,
  },
  {
    path: "/search",
    component: searchPage,
  },
  {
    path: "/reviews",
    component: HomePage,
  },
  {
    path: "/*",
    component: HomePage,
  },
];

export default definedRoutes;
