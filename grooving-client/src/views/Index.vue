<template>
<div>
  <img class="d-block w-100 banner" src="@/assets/img/banner.png" alt="First slide" style="box-shadow: 0px 0px 8px 0px rgba(0, 0, 0, .2) !important;">
  <ArtistsList :showFilters="false" />
  </div>

</template>

<script>
  
import ArtistsList from './ArtistsList.vue';

export default {
  name: 'index',
  components: {
    ArtistsList
  }
}
</script>