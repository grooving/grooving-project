<template>
  <div>
    <ArtistInfo :artistBanner="portfolioBanner" :artistName="portfolioName" :artistGenres="portfolioGenres" />
    <ImageCarousel class="imageCarousel" />
    <VideoCarousel class="videoCarousel" :videosInfo="d_portfolioVideos" :key="updateVideosKey"/>
    <Calendar class="availableDates" :availableDates="this.datos[0].availableDates"/>
  </div>
</template>

<script>

import ArtistInfo from '@/components/portfolio/ArtistInfo.vue';
import ImageCarousel from '@/components/portfolio/ImageCarousel.vue';
import VideoCarousel from '@/components/portfolio/VideoCarousel.vue';
import GAxios from '@/utils/GAxios.js';
import endpoints from '@/utils/endpoints.js';
import GSecurity from '@/security/GSecurity.js';
import Calendar from '@/components/Calendar.vue';

var portfolioDays = [];

export default {
  name: 'Portfolio',
  components: {
    ArtistInfo,
    ImageCarousel,
    VideoCarousel,
    Calendar,
  },  
  props: {
    portfolioBanner: {
      type: String
    },
    portfolioIcon: {
      type: String
    },
    portfolioName: {
      type: String
    },
    portfolioBiography: {
      type: String
    },
    portfolioImages: {
      type: Array,
      default: function() {return []}
    },
    portfolioVideos: {
      type: Array,
      default: function() {return []}
    },
    portfolioVideos: {
      type: Array,
      default: function() {return []}
    },
    portfolioGenres: {
      type: Array,
      default: function() {return[]}
    }
  },

  data: function(){
    
    return{
      gsecurity: GSecurity,
      updateVideosKey: 0,
      d_portfolioBanner: '',
      d_portfolioIcon: '',
      d_portfolioName:'',
      d_portfolioBiography: '',
      d_portfolioImages: Array(),
      d_portfolioVideos: Array(),
      datos: Array(),
    }
  },
  
  mounted: function(){
    
    var authorizedGAxios = GAxios;
    authorizedGAxios.get(endpoints.portfolio+this.$route.params['artistId']+"/")
      .then(response => {

          var portfolio = response.data;

          this.d_portfolioBanner = portfolio.banner;
          this.d_portfolioName = portfolio.artisticName;
          var media = portfolio.portfoliomodule_set;
          var genres = portfolio.artisticGender;

          for(var i = 0; i < genres.length; i++){
            var genre = genres[i];
            this.portfolioGenres.push(genre['name']);
          }
          var imgCounter = 0;
          var vidCounter = 0;

          for(var i = 0; i < media.length; i++){

            var elementMedia = media[i];
            
            if(elementMedia['type'] == 'VIDEO'){
              this.d_portfolioVideos.push({id:vidCounter, videoURL:elementMedia['link']});
              vidCounter += 1;
            }
            if(elementMedia['type'] == 'PHOTO'){
              this.d_portfolioImages.push(elementMedia['link'])
            }
          }

          this.updateVideosKey += 1;
                
    });


      var authorizedGAxios = GAxios;
      var GAxiosToken = this.gsecurity.getToken();
      authorizedGAxios.defaults.headers.common['Authorization'] = 'Token ' + GAxiosToken;

      authorizedGAxios.get('/artist' + endpoints.calendar + this.$route.params['artistId'] + '/')
        .then(response => {
            var calendar = response.data;
            console.log(calendar[0].days)

            this.datos.push({
                availableDates: calendar[0].days,
            })

        }).catch(ex => {
            console.log(ex);
        });

  }

}
</script>

<style scoped>

  .imageCarousel{
    padding-top: 20px;
  }

  .videoCarousel{
    padding-top: 30px;
  }

  .availableDates{
    padding-top: 30px;
    margin-bottom: 35px;
  }

</style>

