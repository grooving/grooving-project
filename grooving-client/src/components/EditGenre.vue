<template>
    <div>
    <div class="cancelButtonDiv"><router-link v-bind:to="cancelURI" class="btn btn-primary cancelButton">
        <span class="continueText">CANCEL</span></router-link></div>
        <b-button v-for="(selected,index) in selectedGenres" v-bind:key="selected" @click="deleteGenre(index)" class="btt">{{selected.title}}</b-button>
        
        <template v-if="add">
            <b-button v-bind:key="selected" @click="displaySelect" class="bttn">+</b-button>
        </template>

        <template v-if="select">
            <b-form>
                <b-form-select :select-size="1" v-model="newGenre" class="hi dropdown">
                <template slot="first">
                    <option disabled>-- Please select an option --</option>
                    <option v-for="genre in genres" v-bind:key="genre.id" :value="genre">{{genre.title}}</option>
                </template>
                
                </b-form-select>
                <b-button class="btt" type="button" variant="primary" v-bind:key="index" 
                    v-model="newGenre" @click="addGenre(index)">Submit</b-button>
            </b-form>
        </template>
  </div>
</template>

<script>
export default {
    mounted() {
            for (let i = 0; i < this.genres.length; i++) {
                for(let x = 0; x < this.selectedGenres.length; x++)
                if(this.genres[i].title == this.selectedGenres[x].title) {
                    this.genres.splice(i,1);                    
                }
            }
        },
  data() {
    return {
        select:  false,
        add: true,
        genres:[ 
      {
        id: 1,
        title: 'Art Punk',
      },
      {
        id: 2,
        title: 'Crust Punk',
      },
      {
        id: 3,
        title: 'College Rock'
      },
      {
        id: 4,
        title: 'Britpunk',
      },
      {
        id: 5,
        title: 'Alternative Rock',
      },
      {
        id: 6,
        title: 'Jazz'
      },
      {
        id: 7,
        title: 'Punk',
      },
      {
        id: 10,
        title: 'Rock',
      },
      {
        id:11,
        title: 'Pop'
      },
      {
        id: 12,
        title: 'Alternative',
      },
      {
        id: 8,
        title: 'Crust',
      },
      {
        id: 9,
        title: "Opera"
      },
     ],
        selectedGenres: [
                  {
        id: 8,
        title: 'Crust',
      },
      {
        id: 9,
        title: "Opera"
      },
        ],
        newGenre: null,
	}
  },
  methods: {
      deleteGenre(index) {
          this.genres.push(this.selectedGenres[index]);
          this.selectedGenres.splice(index,1);
      },
      addGenre(index){
          if(!this.selectedGenres.includes(this.newGenre)) {
              this.selectedGenres.push(this.newGenre);
          }
          for (let i = 0; i < this.genres.length; i++) {
              if (this.genres[i].title == this.newGenre.title) {
                  this.genres.splice(i,1);
              }              
          }
              this.select = false;   
              this.add = true;   
      },
      displaySelect() {
          this.select = true;
          this.add = false;
      },
  }
}

</script>

<style scoped>

.hi {
    width: fit-content;
    font-size: 18px;    
}

.btt, .bttn {
    background-color: #a2a2a2;
    border-radius: 7px;
    color: white;
    font-weight: bold;
    font-size: 18px;
    outline: none;
    border-color: transparent;
    margin: 4px;
}

.bttn {
    border-radius: 50%;
}

select:hover{
    border-color: #187fe6;
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .5) !important;
}

select:focus{
    border-color: #00fb82;
    font-weight: semibold;
    color:black;
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
}

.cancelButton {
    font-size: 18px;
    border: none;
    border-radius: 30px;
    font-weight: bold;
}

.cancelButton {
    margin-right: 3%;        
    background-image: linear-gradient(to right, #a2a2a2, #474747);
}

.cancelButton:hover {
    box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
    background-image: linear-gradient(to right, #515151, #232323) !important;
}

</style>


