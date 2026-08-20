<template>
  <div class="shimmer-image-wrapper">
    <div v-if="!loaded" class="shimmer"></div>
    <img
      :src="src"
      :alt="alt"
      class="shimmer-img"
      :class="{ 'is-loaded': loaded }"
      @load="loaded = true"
      @error="loaded = true"
    />
  </div>
</template>

<script>
export default {
  name: "ShimmerImage",
  props: {
    src: {
      type: String,
      required: true,
    },
    alt: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      loaded: false,
    };
  },
};
</script>

<style lang="scss" scoped>
.shimmer-image-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
}

.shimmer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
    background: linear-gradient(
      100deg,
      var(--color-bg-alt) 30%,
      var(--color-surface) 50%,
      var(--color-bg-alt) 70%
    );
  background-size: 200% 100%;
  animation: shimmer 1.4s infinite linear;
  z-index: 1;
}

@keyframes shimmer {
  0% {
    background-position: 200% 0;
  }
  100% {
    background-position: -200% 0;
  }
}

.shimmer-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  background-color: var(--color-bg-alt);
  opacity: 0;
  transition: opacity 0.4s ease;
  position: relative;
  z-index: 2;
}

.shimmer-img.is-loaded {
  opacity: 1;
}
</style>
