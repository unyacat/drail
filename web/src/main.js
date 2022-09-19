import Vue from "vue";
import App from "./App.vue";
import axios from "axios";
import router from './router'

import { Icon } from "leaflet";
import "leaflet/dist/leaflet.css";
import vuetify from "./plugins/vuetify";

// this part resolve an issue where the markers would not appear
delete Icon.Default.prototype._getIconUrl;

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;

new Vue({
  vuetify,
  router: router,
  render: h => h(App)
}).$mount("#app");
