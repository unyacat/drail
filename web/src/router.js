import Vue from "vue";
import VueRouter from "vue-router";
import home from "@/components/home";
import map from "@/components/mapView";

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: '/',
      component: home,
    },
    {
      path: '/draw',
      component: map
    }
  ]
});
export default router;