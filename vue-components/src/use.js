import VueRouter from 'vue-router';

const OPTIONS = {};

export default {
  async install(Vue, options = {}) {
    // Get our own custom vuetify
    Vue.use(VueRouter);

    // Configue the root view option
    OPTIONS.router = new VueRouter(options);
  },
  getOptions() {
    return OPTIONS;
  },
};
