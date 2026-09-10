export default {
  base: './',
  define: {
    'process.env.NODE_ENV': JSON.stringify('production'),
    __VUE_OPTIONS_API__: 'true',
    __VUE_PROD_DEVTOOLS__: 'false',
    __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false',
  },
  build: {
    lib: {
      entry: './src/use.js',
      name: 'trame_router',
      formats: ['umd'],
      fileName: 'trame-router',
    },
    rollupOptions: {
      external: ['vue'],
      output: {
        globals: {
          vue: 'Vue',
        },
      },
    },
    outDir: '../src/trame_router/module/vue3',
    assetsDir: '.',
    // sourcemap: true,
  },
};
