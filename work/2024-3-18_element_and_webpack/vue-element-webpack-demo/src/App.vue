<template>
  <div id="app">
    <container-view></container-view>
  </div>
</template>

<script>
import ContainerView from "./views/ContainerView.vue";
export default {
  components: { ContainerView },
  data() {
    return {

    }
  }
}
</script>

<style>
#app {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
