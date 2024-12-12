const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  // Vue 3에서 main.ts를 엔트리 파일로 사용
  chainWebpack: (config) => {
    config.entry('app').clear().add('./src/main.ts');
  },
  configureWebpack: {
    resolve: {
      extensions: ['.ts', '.js', '.vue', '.json'],  // TypeScript 확장자 추가
    },
    module: {
      rules: [
        {
          test: /\.vue$/,
          loader: 'vue-loader',        // Vue 파일 처리
        },
        {
          test: /\.ts$/,
          loader: 'ts-loader',         // TypeScript 파일 처리
          options: {
            appendTsSuffixTo: [/\.vue$/],  // .vue 파일 내 TypeScript 처리
          },
        },
      ],
    },
  },
});
