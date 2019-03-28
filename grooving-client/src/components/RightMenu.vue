<template>
  <div class="RightMenu">
   
     <div class="collapse navbar-collapse width px-2 bg-light" id="sidebar">
         <p>
        <div class="navContent">

         <h2>Hello, <span v-if="gsecurity.hasRole('ARTIST')">ROSALÍA</span><span v-else>Pug</span></h2>
            <ul class="navbar-nav mr-auto p-2 col align-self-center justify-content-center">
                <li class="nav-item section">
                    <router-link class="nav-link" to="personalInfo" data-toggle="collapse" data-target="#sidebar">My Account</router-link>
                    <b-dropdown-divider class="divider"/>
                </li>
                <li class="nav-item section" v-if="gsecurity.hasRole('ARTIST')">
                    <router-link class="nav-link" to="showPortfolio" data-toggle="collapse" data-target="#sidebar">My Portfolio</router-link>
                    <b-dropdown-divider class="divider"/>
                </li>
                
                <li class="nav-item section">
                    <a class="nav-link" href="#" data-toggle="collapse" data-target="#sidebar">Messages</a>
                     <b-dropdown-divider class="divider"/>
                </li>
                <li class="nav-item section">
                    <a class="nav-link" href="" v-on:click="logout()">Log Out</a>
                </li>
            </ul>
        </div>
        </div>
  </div>
</template>

<script>
import GSecurity from '@/security/GSecurity.js';

export default {
  name: 'RightMenu',
    props: {
        blur: Boolean,
    },
    data: function(){
        return{
            gsecurity: GSecurity,
        }
    },
    methods: {
    logout() {
      this.gsecurity.deauthenticate();
      this.$router.push({ path: "/" });
    }
  },
}

$(window).bind('scroll', function () {
    if ($(window).scrollTop() > 75) {
        $('#sidebar').offset({top:window.pageYOffset});        
    } else {
        
        $('#sidebar').offset({top:75});
    }
});


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

* {
    font-family: "Archivo"
}

.title {
    font-weight: bold;
    margin-right: 5px;
}

.navContent {
    margin-right: 20px;
}

.section {
    font-size: 18px;
}

#sidebar.collapse {
    text-align: right;
    position: fixed;
    z-index: 2000;
    transition: right .3s ease;
    
    right: -130%; /* -width of sidebar */
    width: 100%;
    height: fit-content !important;
    display: block;
    overflow: auto
}

#sidebar.collapsing {
    text-align: right;
    transition: right .18s ease-in;
    position: fixed;
    z-index: 2000;
    right: -130%;  /* -width of sidebar */
    width: 100%;  /* width of sidebar */
    height: fit-content !important;
    display: block;
    overflow: auto
}

#sidebar.collapse.show {
    text-align: right;
    right: 0;
    width: 100%;  /* width of sidebar */
}
#sidebar {
    width: auto;
    position: relative;
    right: 0;
    box-shadow: 2px 2px 8px 0px rgba(0, 0, 0, .3);
}

.divider {
    width: 100%;
}


@media (min-width: 768px) {

    .title {
        font-weight: bold;
        margin-right: 5px;
    }

    .navContent {
        margin-right: 20px;
    }

    .section {
        font-size: 20px;
    }


    #sidebar.collapse {
        
        text-align: right ;
        z-index: 2000;
        transition: right .3s ease;
        right: -30%; /* -width of sidebar */
        width: 0;
        height: 100% !important;
        display: block;
        overflow: auto
    }

    #sidebar.collapsing {
        text-align: right;
        transition: right .18s ease-in;
        z-index: 2000;
        right: -30%;  /* -width of sidebar */
        width: 25%;  /* width of sidebar */
        height: 100% !important;
        display: block;
        overflow: auto
    }

    #sidebar.collapse.show {
        text-align: right;
        width: 25%;  /* width of sidebar */
    }
    #sidebar {
        width: auto;
        float: right;
    }

}

</style>
