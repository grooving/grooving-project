<template>
  <div class="home">
    <!--<img alt="Vue logo" src="../assets/logo.png">-->
    <Index/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Index from '@/views/Index.vue'

export default {
  name: 'home',
  components: {
    HelloWorld, Index
  }
}
</script>

<style scoped>

</style>

