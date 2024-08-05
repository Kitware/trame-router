import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router';

export default {
  async install(Vue) {
    const mode = window.trame.state.state.trame__route_mode || "hash";
    const history = mode === "html5" ? createWebHistory() : createWebHashHistory();
    const routes =  window.trame.state.state.trame__routes || [];
    const router = createRouter({ history, routes });

    window.trame.utils.router = router;
    Vue.use(router);
  },
};
