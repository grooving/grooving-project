<template>
  <div class="container-fluid">
      <div class="owl-wrapper horizontal-center">
          <div class="row">
              <div class="col-sm-12 col-md-8 horizontal-center">
                  <div class="owl-carousel owl-theme">       
                      <a v-for="photoInfo in photosInfo" :key="photoInfo.id" :href="photoInfo.link">
                        <img :src="photoInfo.imageURL" class="card-img-top artistImage" alt="Artist's Image">
                      </a>
                  </div>
              </div>
          </div>
      </div>
  </div>
</template>

<script>

import 'owl.carousel/dist/assets/owl.carousel.css';
import 'owl.carousel'

/* Makes Slides responsive */
$(window).on('resize', function(){
  var windowWidth = $(window).width();

  /* Substracts some amount to ensure component's width
  is smaller than the window */
  windowWidth -= 100;

  $('.owl-wrapper').css('width', windowWidth);
});

/* Initializes Owl Carousel */
$(document).ready(function(){  
  var windowWidth = $( window ).width();
  windowWidth -= 100;

  $('.owl-wrapper').css('width', windowWidth);

  $('.owl-carousel').owlCarousel({
    loop:true,
    margin: 10,
    autoplay: true,
    nav: false,
    responsive:{
        0:{
            items:1,
        },
        600:{
            items:2,
        },
        992:{
            items:3,
        }
    },

  });

});

export default {
  name: "ImageCarousel",
  props:{
    photosInfo: {
            /* Array of dictionaries of type { id:int, imageURL: String, link: String} */
            type: Array,
            default: [
              {id: 0, imageURL: "https://4c79id2ej5i11apui01ll2wc-wpengine.netdna-ssl.com/wp-content/uploads/2018/09/Charli-XCX-Gallery-1.jpg", link: '#'}
            ]
    },
  }
}
</script>

<style scoped>
  .horizontal-center{
    margin: 0 auto;
  }

  @media (max-width: 576px) {
    .artistImage {
      object-fit: cover;
      height: 12rem;
      width: 100%;
      border-radius: 20px 20px 20px 20px;
    }
  }

  @media (min-width: 576px) {
    .artistImage {
      object-fit: cover;
      height: 15rem;
      width: 100%;
      border-radius: 20px 20px 20px 20px;
    }
  }
</style>


