<template>
  <div>
    <hr />
    <TabbedSubMenu @selectedTab="setSelectedTab"/>
    <div class="container-fluid" style="padding-top: 20px">
      <div class="container">
          <div id="results" class="col-12 col-lg-9 col-xl-10 results">
            <span v-if="selectedTab == 0">
            <div class="row">
              <div v-for="oferta in pending" :key="oferta.offerID" class="tarjeta col-12 col-md-6 col-xl-6">
                <Offer :offerID="oferta.offerID" :confirmURI="oferta.confirmURI" :date="oferta.date" :price="oferta.price" 
                  :place="oferta.place" :userIcon="oferta.userIcon" :userName="oferta.userName"  :offerStatus="oferta.offerStatus"/>
              </div>
            </div>
            </span>
            <span v-if="selectedTab == 1">
            <div class="row">
              <div v-for="oferta in accepted" :key="oferta.offerID" class="tarjeta col-12 col-md-6 col-xl-6">
                <Offer :offerID="oferta.offerID" :confirmURI="oferta.confirmURI" :date="oferta.date" :price="oferta.price" 
                  :place="oferta.place" :userIcon="oferta.userIcon" :userName="oferta.userName"  :offerStatus="oferta.offerStatus"/>
              </div>
            </div>
            </span>
            <span v-if="selectedTab == 2">
            <div class="row">
              <div v-for="oferta in rejected" :key="oferta.offerID" class="tarjeta col-12 col-md-6 col-xl-6">
                <Offer :offerID="oferta.offerID" :confirmURI="oferta.confirmURI" :date="oferta.date" :price="oferta.price" 
                  :place="oferta.place" :userIcon="oferta.userIcon" :userName="oferta.userName"  :offerStatus="oferta.offerStatus"/>
              </div>
            </div>
            </span>
            
          </div>
        </div>
      </div>
  </div>
</template>

<script>

import Offer from '@/components/Offer.vue';
import TabbedSubMenu from '@/components/menus/TabbedSubMenu.vue';
import GAxios from '@/utils/GAxios.js';
import endpoints from '@/utils/endpoints.js';
import GSecurity from '@/security/GSecurity.js';

var acceptURI = '/offerDetails/';

export default {
  name: 'OffersList',
  components: {
    Offer,
    TabbedSubMenu
  },

  data: function(){
    return {
        gsecurity: GSecurity,
        pending: Array(),
        accepted: Array(),
        rejected: Array(),
        datos_prueba:[
          {
            offerID:  1, 
            date: 'January 1, 2019',
            price: 89.00,
            place: 'Pilas',
            confirmURI: 'offerDetails',
            userIcon: 'https://i.imgur.com/zg5UgRb.jpg',
            userName: 'Laika'
          },
          {
            offerID: 3, 
            date: 'February 19, 2019',
            price: 38.00,
            place: 'La Algaba',
            confirmURI: 'offerDetails',
            userIcon: 'https://i.imgur.com/Y6UhVQF.jpg',
            userName: 'Dobby'
          },
          {
            offerID: 5, 
            date: 'June 28, 2019',
            price: 120.00,
            place: 'Espartinas',
            confirmURI: 'offerDetails',
            userIcon: 'https://i.imgur.com/C0EXLuU.jpg',
            userName: 'Otto'
          },
          {
            offerID: 7, 
            date: 'July 14, 2019',
            price: 3.50,
            place: 'Huelva',
            confirmURI: 'offerDetails',
            userIcon: 'https://i.imgur.com/asPcsKa.jpg',
            userName: 'Alicia'
          },
        ],
        selectedTab: 0, 
      }
    },
    methods: {
      toggleFilterSelectionModal: function (){
        this.showFilterSelectionModal = !this.showFilterSelectionModal;
      },
      updateFilters: function() {
        var selected = Array();

        for(var i = 0; i < arguments[0].length; i++){
          selected.push(arguments[0][i]);
        }

        for(var j = 0; j < this.filter_parameters.length; j++){
          if(selected.includes(this.filter_parameters[j].id)){
            this.filter_parameters[j].selected = true;
          }
        }
      },
      setSelectedTab(status) {
        this.selectedTab = status;
      }
    },
     beforeMount: function(){
      var authorizedGAxios = GAxios;
      var GAxiosToken = this.gsecurity.getToken();
      authorizedGAxios.defaults.headers.common['Authorization'] = 'Token ' + GAxiosToken;

      authorizedGAxios.get(endpoints.offers)
      .then(response => {
        console.log('ok1')
        var offers = response.data.results;
        
        for(var i = 0; i < offers.length; i++){
          if(offers[i].status == 'PENDING') {
          this.pending.push({
            offerID: offers[i].id,
            offerStatus: offers[i].status,
            date: offers[i].date,
            place: offers[i].eventLocation.zone.name,
            userName: offers[i].eventLocation.customer.user.first_name,
            userIcon: offers[i].eventLocation.customer.photo,
            price: offers[i].price,
            confirmURI: acceptURI + offers[i].id,
            // rejectURI: rejectURI + offers[i].id,
          });
        }}
        for(var i = 0; i < offers.length; i++){
          if(offers[i].status == 'REJECTED') {
          this.rejected.push({
            offerID: offers[i].id,
            offerStatus: offers[i].status,
            date: offers[i].date,
            place: offers[i].eventLocation.zone.name,
            userName: offers[i].eventLocation.customer.user.first_name,
            userIcon: offers[i].eventLocation.customer.photo,
            price: offers[i].price,
            confirmURI: acceptURI + offers[i].id,
            // rejectURI: rejectURI + offers[i].id,
          });
        }}
        for(var i = 0; i < offers.length; i++){
          if(offers[i].status == 'CONTRACT_MADE') {
          this.accepted.push({
            offerID: offers[i].id,
            offerStatus: offers[i].status,
            date: offers[i].date,
            place: offers[i].eventLocation.zone.name,
            userName: offers[i].eventLocation.customer.user.first_name,
            userIcon: offers[i].eventLocation.customer.photo,
            price: offers[i].price,
            confirmURI: acceptURI + offers[i].id,
            // rejectURI: rejectURI + offers[i].id,
          });
        }}
      }).catch(ex => {
          console.log(ex);
      });

    },
    
}
</script>

<style scoped>

    .results{
      margin: 0 auto; 
      padding: 0px;
    }    

    .tarjeta{
      padding-bottom: 20px;
    }

    hr {
      margin: 0px;
    }

</style>

