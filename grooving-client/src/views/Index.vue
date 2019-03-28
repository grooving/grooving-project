<template>
<div>
  <div class="banners">
  <div class="banner2"><img class="d-block w-100 banner2" src="@/assets/img/banner2.png" alt="First slide" style="box-shadow: 0px 0px 8px 0px rgba(0, 0, 0, .2) !important;"></div>
  <div class="banner1"><img class="d-block w-100 banner1" src="@/assets/img/banner1.png" alt="First slide" style="box-shadow: 0px 0px 8px 0px rgba(0, 0, 0, .2) !important;"></div>
  </div>
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

<style>

.banners{
  padding-bottom: 3%;
}
  @media(min-width: 720px) {
    .banner2{display:block;}
    .banner1{display:none;}
  }

  @media(max-width: 720px) {
    .banner2{display:none;}
    .banner1{display:block;}
  } 
</style>
