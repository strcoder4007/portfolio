<template>
  <div>
    <div class="image-container">
      <img :src="getImageSrc()" />
    </div>
    <div class="project-name">{{ name }}</div>
    <div class="project-description">{{ description }}</div>
    <div class="links-container">
      <div class="live">Live</div>
      <div class="code">Code</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProjectComponent",
  props: {
    name: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    image: {
      type: String,
      required: true
    }
  },
  data() {
    return {}
  },
  mounted() {

  },
  methods: {
    getImageSrc() {
      try {
        const imageUrl = new URL(`./images/${this.image}.png`, import.meta.url).href;
        return imageUrl;
      } catch (error) {
        console.error(error);
      }
    }
  },
  components: {},
};
</script>

<style lang="scss" scoped>
@media (max-width: 768px) {

}
</style>