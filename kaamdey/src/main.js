

import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import VueRouter from "vue-router";

import store from "./store/index"


import definedRoutes from "./router/index";


import "./css/homepage.css"
import "./css/searchpage.css"

Vue.config.productionTip = false;
Vue.use(VueRouter); //enabling routing
// Register it globally

const router = new VueRouter({
  routes: definedRoutes,
  mode: "history"
});
new Vue({
  store,
  vuetify,
  router,
  render: h => h(App)
}).$mount("#app");
