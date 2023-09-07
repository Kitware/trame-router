export default {
  base: './',
  define: {
    'process.env': {},
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
    outDir: '../trame_router/module/vue3',
    assetsDir: '.',
    // sourcemap: true,
  },
};
