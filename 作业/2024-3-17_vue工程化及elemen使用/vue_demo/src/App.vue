<template>
  <div id="app">
    {{ msg }}
    <xu-view></xu-view>
    <element-view></element-view>
  </div>
</template>

<script>
import XuView from "./views/XuView.vue";
import ElementView from "./views/ElementView.vue";
export default ({
  components:{XuView,ElementView},
  data(){
    return{
      msg:"hello vuuee"
    }
  }
})
</script>

<style>

</style>
