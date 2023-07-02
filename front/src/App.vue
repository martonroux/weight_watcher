<script setup>
import Banner from "./components/Banner.vue"
import Background from "./components/Background.vue";
</script>

<template>
  <main>
    <div class="app">
      <Background style="position:fixed; height: 100%; width: 100%"/>
      <div class="container-div">
        <router-view></router-view>
      </div>
      <Banner style="width: 100vw; margin: 0; padding: 0; position:fixed;" />
    </div>
  </main>
</template>

<script>
export default {
}
</script>

<style scoped>

.container-div {
  position: absolute;
  display: flex;
  flex-direction: column;
  width: 100vw;
  padding-top: 90px;
}

</style>
