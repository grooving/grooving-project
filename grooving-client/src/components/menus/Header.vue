<template>
    <div>
    <nav class="navbar navbar-light bg-light">
      <div class="navbar-brand vertical-center">
        <button class="d-inline d-md-none navbar-toggler no-border">
          <span class="navbar-toggler-icon"></span>
        </button>
        <a class="ml-2 vertical-center" href="#"><img src="@/assets/logos/logo_name.png" width="100px"/></a>
      </div>
      <div class="d-none d-md-block mr-auto">
        <ul class="navbar-nav row-alignment right-float">
          <li v-for="item in menu_links" class="nav-item mx-2" v-bind:class="{active: item.selected}">
            <router-link class="nav-link" :to="item.link">{{item.text}}</router-link> 
          </li>
        </ul>
      </div>
      <div class="ml-auto align-middle">
        <ul class="navbar-nav row-alignment">
          <li class="nav-item active mx-2 right-float">
            <div class="d-md-none">
            <a class="nav-link" href="#" @click="alerta()"><i class="material-icons align-middle">search</i></a>
            </div>
            <div class="d-none d-md-inline nav-item">
              <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" style="border-radius:100px;" type="search" placeholder="Search" aria-label="Search">
                <button class="btn" type="submit"><i class="material-icons align-middle">search</i></button>
              </form>
            </div>
          </li>
          <li class="nav-item mx-2 right-float vertical-center">
            <a class="nav-link vertical-center" href="#"><i class="material-icons align-middle">account_circle</i></a>
          </li>
        </ul>
      </div>
    </nav>
    </div>
</template>

<script>
export default {
    name: 'Header',
    data: function(){
      return{
          menu_links: [
            {text:"Top Artists", link:"#", selected: true},
            {text:"My Offers", link:"#", selected: false},
            {text:"FAQ", link:"#", selected: false}
          ]
      }
    }
}
</script>

<style scoped>

  .no-border{
    border:none;
  }

  .row-alignment{
    flex-direction: row;
  }

  .right-float{
    float: right;
  }

  @media (min-width: 900px){
    input:focus{
      width: 350px;
      box-shadow: 2px 2px 8px 0px rgba(0,0,0,.2)
    }
  }

  input:focus{
    box-shadow: 2px 2px 8px 0px rgba(0,0,0,.2)
  }

  .vertical-center{
    display: flex; 
    align-items: center;  /*Aligns vertically center */
    justify-content: center; /*Aligns horizontally center */
  }

</style>


