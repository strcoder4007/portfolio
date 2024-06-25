const { defineConfig } = require("@vue/cli-service")
module.exports = defineConfig({
  outputDir: 'docs',
  transpileDependencies: true,
  "publicPath": "/graphic-designer-portfolio/"
});
