<template>
    <div class="container">
      <div class="owl-wrapper horizontal-center">
          <div class="col-sm-12 col-md-8 horizontal-center">
              <div class="row">
                <div class="col-8 vertical-c enter">
                  <h3 style="text-align: left; color: black; margin:0"><strong>Available dates</strong></h3>
                </div>
                <div class="col-4 vertical-center" style="padding-left: 10px" >
                    <button class="acceptButton vertical-center" style="height:65px; width:inherit;" v-on:click="changeToggle">
                        <i v-if="toggleAddURL" class="material-icons arrowIcon acceptButton"  style="margin: 0 auto; font-size: 55px">add_circle</i>
                        <i v-else class="material-icons arrowIcon acceptButton"  style="margin: 0 auto; font-size: 55px">cancel</i>
                    </button>
                </div>
              </div>
                <div class="row">
                    <div v-if="toggleAddURL==false" class="contentForm"> 
                        <div class="form-group mx-sm-3 mb-2">
                            <input class="form-control inputFecha" type="text" id="inputFecha" placeholder="YYYY-MM-DD">
                        </div>
                        <button class="btn btn-primary mb-2 continueButton" v-on:click="addRejectedDate">ADD</button>
                    </div>
                </div>
          </div>
          <div class="row contentCalendar">
              <div class="col-sm-12 col-md-8 horizontal-center">
                  <div><vuejs-datepicker id="calendario" @selected="deleteDate" :highlighted="highlighted" :disabledDates="disabledDates" :value="currentDate" :full-month-name="true" :inline="true"></vuejs-datepicker></div>
              </div>
          </div>
      </div>
      
  </div>
</template>

<script>



var yesterday = new Date();
yesterday.setDate(yesterday.getDate()-1);

var availableDates = []
/*availableDates.push(new Date(2019, 2, 29));
availableDates.push(new Date(2019, 2, 30));
availableDates.push(new Date(2019, 2, 28));*/

export default {
    name: "Calendar",
    props: {
        availableDates: {
            type: Array,
            default: [
                new Date(2019, 2, 29),
                new Date(2019, 2, 30),
                new Date(2019, 2, 28)
            ],
        }
    },
    components: {
        vuejsDatepicker
    },
    data () {
        return {
            currentDate: new Date(),
            disabledDates: {
                to: yesterday
            },
            highlighted: {
                dates: this.availableDates
            },

            toggleAddURL: true
        }
    },

    methods: {
        addRejectedDate: function (event) {
            var fecha = document.getElementById("inputFecha").value;
            var fecha2 = new Date(fecha)
            var fecha3 =new Date(fecha2.getFullYear(), fecha2.getMonth(), fecha2.getDate());
            this.availableDates.push(fecha3);
        },
        changeToggle: function(event) {
            if(this.toggleAddURL==false){
                this.toggleAddURL=true;
            }
            else{
                this.toggleAddURL=false;
            }
        },
        deleteDate: function(event){
            //alert(this.availableDates);
            //alert(event);
            var collection = this.availableDates,
                d = new Date(event.getFullYear(), event.getMonth(), event.getDate()),
                idx;

            //alert(collection);
            idx = collection.map(Number).indexOf(+d);
            //alert(idx);
            
            if(idx!=-1){
                var confirmar = confirm("Are you sure you wanna delete this date?");
                if(confirmar == true){
                    this.availableDates.splice(idx, 1);
                }
                
            }
            
        }


  }
}
</script>

<style>

.acceptButton{
    background-color:transparent;
    border: none;
}

.vertical-center{
    display: flex !important; 
    align-items: center !important;  /*Aligns vertically center */
    vertical-align: middle;
  }

.titleCalendar{
    color: green !important;
}

.horizontal-center{
    margin: 0 auto;
  }

  @media (max-width: 576px) {
    .artistImage {
      object-fit: cover;
      height: 12rem;
      width: 100%;
      border-radius: 10px 10px 10px 10px;
    }
  }

  @media (min-width: 576px) {
    .artistImage {
      object-fit: cover;
      height: 15rem;
      width: 100%;
      border-radius: 10px 10px 10px 10px;
    }
  }
    .horizontal-center{
        margin: 0 auto;

    }
    .contentForm{
        padding-top: 10px !important;
        padding-bottom: 10px;
        display:flex;
        align-content: center;
    }

    .form-inline .formulario{
        margin: 0 auto !important;
    }

    .vdp-datepicker__calendar {
        width: 100%;
        border: 0px;
        margin-top: 10px;
    }

    .container-fluid{
        width: 100% !important;
        margin: 0 auto !important;
        padding-left: 10px;
        padding-right: 10px;
        padding-top: 10px;
        padding-bottom: 10px;

    }

    input:hover{
        border-color: #187fe6;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .3) !important;
    }

    input:focus{
        border-color: #00fb82 !important;
        font-weight: semibold;
        color:black;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
        
    }

    .continueButton {
        font-size: 18px;
        border: none;
        border-radius: 30px;
        color: white !important;
        font-weight: bold;
        margin-left: 2%;
        background-image: linear-gradient(to right, #00fb82, #187fe6);
    }

    .continueButton:hover{
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
        background-image: linear-gradient(to right, #14Ca9f, #1648d0) !important;
    }


    .availableDates{
        text-align: left;
        font-weight: semibold;
    }

    @media (min-width: 768px){
        .vdp-datepicker__calendar {
            width: 100% !important;
            border: 0px;
            margin-top: 10px;
            margin: 0 auto !important;
        }

        .availableDates{
            text-align: center;
            margin-bottom: 20px;
            font-weight: semibold;
        }

        .contentCalendar{
            padding-top: 20px !important;
            width: 65% !important;
            
            margin: 0 auto !important;
            padding-left: 10px;
            padding-right: 10px;
            padding-top: 10px;
            padding-bottom: 10px;
            border-radius: 10px;
            box-shadow: 0px 2px 8px 2px rgba(0, 0, 0, .5);

        }
    }

    
    .vdp-datepicker__calendar header span {
        font-weight: bold;
    }
    .vdp-datepicker__calendar .cell.day-header {
        color: #187FE6;
        font-weight: bold;
    }
    .vdp-datepicker__calendar .cell.selected {
        background-image: linear-gradient(to right, #ffffff, #ffffff) !important;
        color: black !important;
    }
    

    .vdp-datepicker__calendar .cell.highlighted{
        background-image: linear-gradient(to right, #92ffca, #8dc4fc) !important;
        border-radius: 25px;
        color: black !important;
        border: solid white;

    }

    .vdp-datepicker__calendar .cell.selected.cell.highlighted {
        background-image: linear-gradient(to right, #00fb82, #187fe6) !important;
        color: white !important;
        font-weight: bolder;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .5) !important;
    }

    .vdp-datepicker__calendar .cell.selected:hover {
        background-image: linear-gradient(to right, #00fb82, #187fe6);
        border-radius: 25px;
    }


    
</style>

<style scoped>
    * {
        color: #000000;
    }
</style>