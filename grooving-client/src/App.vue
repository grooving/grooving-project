<template>
  <div id="app">
    <div class="content">
    <div class="Header"><Header @isArtist="setIsArtist" @authenticated="setAuthenticated" v-bind:authenticated="authenticated" v-bind:isArtist="isArtist"/></div>
    <div class="RightMenu"><RightMenu v-bind:isArtist="isArtist"/></div>
    <div class="LeftMenu"><LeftMenu v-bind:authenticated="authenticated" v-bind:isArtist="isArtist"/></div>
    <router-view/>
    </div>
    <footer><Footer/></footer>
  </div>
</template>

<script>
import Header from "./components/menus/Header.vue"
import RightMenu from "./components/RightMenu.vue"
import LeftMenu from "./components/LeftMenu.vue"
import Footer from "./components/Footer.vue"

export default {
  data() {
    return {
      authenticated: false,
      isArtist: true,
      customerAccount: {
        username: "pug",
        password: "pug",
      },
      artistAccount: {
        username: "rosalia",
        password: "rosalia",
      }
    }
  },

  components:{
    Header, RightMenu, LeftMenu, Footer
  },

  mounted() {
    if(!this.authenticated) {
      this.$router.replace({name: "#"});
    }
  },
  
  methods: {
    setAuthenticated(status) {
      if (status == "false") {
        this.authenticated = false;
      }
      if (status == "true") {
        this.authenticated = true;
      }
    },
    logout() {
      this.authenticated = false;
    },
    setIsArtist(status) {
      if (status == "false") {
        this.isArtist = false;
      }
      if (status == "true") {
        this.isArtist = true;
      }
    }
  }
}

</script>

<style>

html{ height:100%; }
body{ min-height:100%; padding:0; margin:0; position:relative; }


body::after {
  content: '';
  display: block;
  height: 100px; /* Set same as footer's height */
}

footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 100px;
}

.content{
  height: auto;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  display: table;
  height: 100%;
  width: 100%;

}

@media (max-width: 768px) {

  body::after {
    content: '';
    display: block;
    height: 10px; /* Set same as footer's height */
  }

  footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 0px;
    display: none;
  }
}
</style>
