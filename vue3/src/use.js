import { createRouter, createWebHashHistory } from 'vue-router';

export default {
  async install(Vue) {
    const router = createRouter({
      history: createWebHashHistory(),
      routes: [],
    });

    window.trame.utils.router = router;

    Vue.use(router);
  },
};
