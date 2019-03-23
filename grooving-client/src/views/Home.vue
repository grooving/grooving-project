<template>
  <div class="home">
    <hr class="separator"/>
    <TabbedSubMenu />
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import TabbedSubMenu from '@/components/menus/TabbedSubMenu.vue'

export default {
  name: 'home',
  components: {
    HelloWorld,
    TabbedSubMenu
  }
}
</script>

<style scoped>

  .separator{
    margin: 0px;
  }

</style>

