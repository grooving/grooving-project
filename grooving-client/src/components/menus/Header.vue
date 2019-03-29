<template>
  <div>
    <nav class="navbar navbar-light bg-light">
      <div class="navbar-brand vertical-center">
        <button class="d-inline d-md-none navbar-toggler no-border" role="button" data-toggle="collapse" data-target="#sidebarleft"
          @click="sideMenus()">
          <span class="navbar-toggler-icon"></span>
        </button>
        <router-link class="ml-2 vertical-center" to="/"><img src="@/assets/logos/logo_name.png" width="100px"/></router-link>
      </div>
      <div class="d-none d-md-block mr-auto">
        <ul class="navbar-nav row-alignment right-float">
          <li v-for="item in userVisibleLinks" class="nav-item mx-2" v-bind:class="{active: item.selected}">
            <router-link class="nav-link font" :to="item.link">{{item.text}}</router-link> 
          </li>
        </ul>
      </div>
      <div class="ml-auto align-middle">
        <ul class="navbar-nav row-alignment">
          <li class="nav-item active mx-2 right-float">
            <div class="d-md-none serch">
              <a class="nav-link" href="#" @click="toggleSearchPanel()"><i class="material-icons align-middle">search</i></a>
            </div>
            <div class="d-none d-md-inline nav-item">
              <form class="form-inline serch">
                <input v-model="searchQuery" class="form-control mr-sm-2" style="border-radius:100px;" type="search" placeholder="Search" aria-label="Search">
                <button class="btn" type="button" @click="search()"><i class="material-icons align-middle ">search</i></button>
              </form>
            </div>
          </li>
          <li v-if="gsecurity.isAuthenticated()" class="nav-item mx-2 right-float vertical-center" >
            <button role="button" class="collaps" data-toggle="collapse" data-target="#sidebar" @click="sideMenus()">
              <a class="nav-link vertical-center" href="#">
                <img v-if="gsecurity.hasRole('ARTIST')" v-bind:src="artistImage" class="profileImage" alt="Profile Image">
                <img v-else v-bind:src="customerImage" class="profileImage" alt="Profile Image">
              </a>
            </button>
          </li>
          <li v-else>
            <b-dropdown :disabled="loginDisabled" id="ddown-form" ref="ddown" class="m-2" right>
              <template slot="button-content"><i class="material-icons align-middle">account_circle</i></template>
              
              <b-dropdown-form class="loginDropdown">
                <b-form-group class="loginLabel" label="Log In" label-for="ddown-form-email">
                  <b-form-input class="loginInput" v-model="input.username" size="sm" placeholder="Username" id="ddown-form-email"></b-form-input>
                </b-form-group>

                <b-form-group>
                  <b-form-input class="loginInput" v-model="input.password" type="password" size="sm" placeholder="Password" id="ddown-form-passwd"></b-form-input>
                </b-form-group>
                <b-button class="continueButton" variant="primary" size="sm" v-on:click="login()">SIGN IN</b-button>
              </b-dropdown-form>
              <b-dropdown-divider />
              <b-dropdown-item-button class="dropdownButton1">New around here? <span class="signUp">Sign up</span></b-dropdown-item-button>
              <b-dropdown-item-button class="dropdownButton2">Forgot Password?</b-dropdown-item-button>
            </b-dropdown>
          </li>
        </ul>
      </div>
    </nav>
    <Search v-if="showSearchMenu" @closeSearch="toggleSearchPanel()" />
  </div>
</template>

<script>
import Search from "./Search.vue";
import GSecurity from '@/security/GSecurity.js';

export default {
  name: 'Header',

  data: function() {
    return {
        menu_links: [
          {text: "Top Artists", link: "artist_search", selected: true, requiedRoles: []},
          {text: "My Offers", link: "offers", selected: false, requiedRoles: ['CUSTOMER', 'ARTIST']},
          {text: "QR Scan", link: "receivePayment", selected: false, requiedRoles: ['ARTIST']},
          {text: "FAQs", link: "#", selected: false, requiedRoles: []}
        ],
        showSearchMenu: false,
        sideMenu: false,
        searchQuery: '',
        input: {
          username: "",
          password: "",
        },
        gsecurity: GSecurity,
        loginDisabled: false,
    }
  },

  components: {
    Search
  },

  methods: {
    toggleSearchPanel: function() {
      this.showSearchMenu = !this.showSearchMenu;

      if(this.showSearchMenu){
        $(document.body).css("overflow", "hidden")
      } else {
        $(document.body).css("overflow", "")
      }

    },
    sideMenus: function() {
      this.sideMenu = !this.sideMenu;
      this.loginDisabled = !this.loginDisabled;

      if(this.sideMenu){
        $(document.body).css("overflow", "hidden")

      } else {
        $(document.body).css("overflow", "")
      }
    },
    search: function() {
      this.$router.push({ path: '/artist_search', query: { query : this.searchQuery } })
    },
    login() {
      if(this.gsecurity.authenticate(this.input.username, this.input.password)){
          this.$router.push({ path: "/" });
      }
    }
  },

  props: {
    customerImage: {
      type: String,
      default: 'http://i65.tinypic.com/35mpp1h.jpg'
    },
    artistImage: {
      type: String,
      default: 'https://img.europapress.es/fotoweb/fotonoticia_20181107115306_1920.jpg'
    },
  },

  mounted: function() {
    $("button").removeClass("dropdown-toggle");
  },

  computed: {
    userVisibleLinks: function(){
      return this.menu_links.filter(item => (item.requiedRoles.length == 0 || item.requiedRoles.includes(this.gsecurity.getRole())))
    }
  }
}
</script>

<style>
  .material-icons:hover {
    background: -webkit-linear-gradient(left, #00fb82, #187fe6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .navbar {
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .3) !important;
  }

  .btn-secondary {
    color: #212529;
    background-color: transparent;
    border-color: transparent;
  }

  .btn-secondary:hover {
    color: #212529;
    background-color: transparent;
    border-color: transparent;
  }

  .btn-secondary:not(:disabled):not(.disabled).active, .btn-secondary:not(:disabled):not(.disabled):active, .show>.btn-secondary.dropdown-toggle {
    color: #000000;
    background-color: transparent;
    border-color: transparent;
  }
  
  .btn-secondary.disabled, .btn-secondary:disabled{
    color: #000000;
    background-color: transparent;
    border-color: transparent;
  }

  .dropdown-toggle::after{
    display: none
  }

</style>


<style scoped>

  .font { font-family: "Archivo" }

  .collaps {
    border: 0ch;
    background: transparent;
  }

  nav { height:75px; }

  .no-border { border:none; }

  .row-alignment{ flex-direction: row; }

  .right-float{ float: right; }

  .profileImage {
    width: 45px;
    height: 45px;
    object-fit: cover;
    border-radius: 25px;
    margin-bottom: 5px;
  }

  .profileImage:hover {
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .5) !important;
  }

  input:hover{
    border-color: #187fe6;
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .3) !important;
  }

  select:hover{
    border-color: #187fe6;
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .5) !important;
  }
  
  input:focus{
    border-color: #00fb82;
    font-weight: semibold;
    color:black;
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;    
  }

  select:focus{
    border-color: #00fb82;
    font-weight: semibold;
    color:black;
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;      
  }

  .loginDropdown {
    padding: 20px;
    text-align:center;
  }

  .loginLabel {
    text-align:center;
    font-weight:bold;
    font-size:30px;
  }

  .loginInput {
    border-radius:25px;
  }

  .signUp {
    font-weight:bold
  }

  .dropdownButton1:hover {
    background-color: #b5ffdb;
  }

  .dropdownButton2:hover {
    background-color: #a8c9ea;
  }

  .continueButton {
    font-size: 18px;
    padding-left: 4%;
    padding-right: 4%;
    border: none;
    border-radius: 30px;
    width: 80%;
    font-weight: bold;
    background-image: linear-gradient(to right, #00fb82, #187fe6);
  }
   
  .continueButton:hover{
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
    background-image: linear-gradient(to right, #14Ca9f, #1648d0) !important;
  }

  .dropdownButton1, .dropdownButton2 {
    color: gray;
    text-align:center;
  }

  input:focus{
    box-shadow: 2px 2px 8px 0px rgba(0,0,0,.2)
  }

  .vertical-center{
    display: flex; 
    align-items: center;  /*Aligns vertically center */
    justify-content: center; /*Aligns horizontally center */
  }

  .serch {
    padding-top: 8px;
    vertical-align: auto;
  }

  @media (min-width: 900px){
    .searchBar:focus {
      width: 350px;
      box-shadow: 2px 2px 8px 0px rgba(0,0,0,.2)
    }
  }

</style>


