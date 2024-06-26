<template>
  <div class="contact-page">
      <FreelanceSection class="freelance-section"></FreelanceSection>
      <LinksSection class="links-section"></LinksSection>
  </div>
</template>
  
<script>
  import LinksSection from './sections/LinksSection.vue';
  import FreelanceSection from './sections/FreelanceSection.vue';
  export default {
    name: "ContactPage",
    components: {
      LinksSection,
      FreelanceSection
    },
  };
</script>
  
<style scoped>
.contact-page {
  height: auto;
  min-height: calc(100vh - 60px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 80px auto 0px auto;
}
</style>
  