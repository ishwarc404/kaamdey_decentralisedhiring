import HomePage from "../components/homePage.vue";
import searchPage from "../components/searchPage.vue";
import previewPage from "../components/previewPage.vue"
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
    path: "/preview*",
    component: previewPage,
  },
  {
    path: "/*",
    component: HomePage,
  },
];

export default definedRoutes;
