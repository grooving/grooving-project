<template>
  <div class="LeftMenu">
   
     <div class="collapse navbar-collapse width px-2 bg-light" id="sidebarleft">
         <p>
         <div class="navContent">
         <h2 class="title">Menu</h2>
            <ul class="navbar-nav mr-auto p-2 col align-self-center justify-content-center">
                <li class="nav-item section">
                    <router-link class="nav-link" to="artist_search" data-toggle="collapse" data-target="#sidebarleft" >Top Artists</router-link> 
                    <b-dropdown-divider class="divider"/>
                </li>
                <li v-if="gsecurity.isAuthenticated()" class="nav-item section">
                    <router-link class="nav-link" to="offers" data-toggle="collapse" 
                    data-target="#sidebarleft" >My Offers</router-link>
                    <b-dropdown-divider class="divider"/>
                </li>
                <li v-if="gsecurity.hasRole('ARTIST')" class="nav-item section">
                    <a class="nav-link" href="#" data-toggle="collapse" data-target="#sidebarleft">QR Scan</a>
                    <b-dropdown-divider class="divider"/>
                </li>
                
                <li class="nav-item section">
                    <a class="nav-link" href="#" data-toggle="collapse" data-target="#sidebarleft">FAQ</a>
                </li>
            </ul>
        </div>
        </div>
  </div>
</template>


<!-- Script -->
 
<script>
import GSecurity from '@/security/GSecurity.js';

export default {
  name: 'LeftMenu',
    props: {
        blur: {
            type: Boolean,
        }  
    },
    data: function(){
        return{
            gsecurity: GSecurity,
        }
    }
}

$(window).bind('scroll', function () {
    if ($(window).scrollTop() > 60) {
        $('#sidebarleft').addClass('fixed');
    } else {
        $('#sidebarleft').removeClass('fixed');
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
    margin-left: 5px;
}

.navContent {
    margin-left: 15px;
}

.section {
    font-size: 18px;
}

#sidebarleft.collapse {
    text-align: left;
    position: fixed;
    z-index: 2001;
    transition: all .3s ease;
    left: -130%; /* -width of sidebar */
    width: 100%;
    height: fit-content !important;
    display: block;
    overflow: auto
}

#sidebarleft.collapsing {
    text-align: left;
    transition: all .18s ease-in;
    position: fixed;
    z-index: 2001;
    left: -130%;  /* -width of sidebar */
    width: 100%;  /* width of sidebar */
    height: fit-content !important;
    display: block;
    overflow: auto
}

#sidebarleft.collapse.show {
    text-align: left;
    left: 0;
    width: 100%;  /* width of sidebar */
}
#sidebarleft {
    width: auto;
    position: relative;
    left: 0;
    box-shadow: 2px 2px 8px 0px rgba(0, 0, 0, .3);
}


@media (min-width: 768px) {
    
    .title {
        font-weight: bold;
        margin-left: 5px;
    }

    .navContent {
        margin-left: 20px;
    }

    .section {
        font-size: 18px;
    }

    #sidebarleft.collapse {
        display: none;
        z-index: 2001;
    }

    #sidebarleft.collapsing {
        display: none;
        z-index: 2001;
    }

    #sidebarleft.collapse.show {
        display: none;
    }
    #sidesidebarleftbar {
        display: none;

    }
   
}

</style>
