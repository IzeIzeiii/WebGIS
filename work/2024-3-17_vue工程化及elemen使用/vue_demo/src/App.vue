<template>
  <div id="app">
    <!-- {{ msg }}
    <xu-view></xu-view>
    <element-view></element-view> -->
    <container-view></container-view>
  </div>
</template>

<script>
import XuView from "./views/XuView.vue";
import ElementView from "./views/ElementView.vue";
import ContainerView from "./views/ContainerView.vue";
export default ({
  components:{XuView,ElementView,ContainerView},
  data(){
    return{
      msg:"hello vuuee"
    }
  }
})
</script>

<style>

</style>
