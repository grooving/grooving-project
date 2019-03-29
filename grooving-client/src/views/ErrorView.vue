<template>
  <div class="error">
    <h1 class="oops">Oops! ☹</h1>
    <h4>Something went wrong!</h4>
    <h4>{{message}}</h4>
  </div>
</template>

<script>
export default {
  name: 'ErrorView',
  props: {
    message:{
      type: String,
      default: "Try again later."
    }
  },
}
</script>

<style>
  .error{
    padding-top: 50px;
  }

  .oops{
    font-size: 100px !important;
    font-weight: bold;
  }
</style>