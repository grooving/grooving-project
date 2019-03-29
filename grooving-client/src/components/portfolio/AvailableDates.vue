<template>
    
    <div class="container-fluid">
      <div class="owl-wrapper horizontal-center">
          <div class="row" style="padding-bottom: 15px">
            <div class="col-sm-12 col-md-8 horizontal-center">
              <h3 class="titleCalendar" style="text-align: left;"><strong>Available Dates</strong></h3>
            </div>
          </div>
          <div class="row contentCalendar">
              <div class="col-sm-12 col-md-8 horizontal-center">
                  <div><vuejs-datepicker :disabledDates="disabledDates" :value="currentDate" :full-month-name="true" :inline="true"></vuejs-datepicker></div>
              </div>
          </div>
      </div>
  </div>
</template>

<script>



var yesterday = new Date();
yesterday.setDate(yesterday.getDate()-1);

var rejectedDates = [];




export default {
    name: "Calendar",
    props: {
    },
    components: {
        vuejsDatepicker
    },
    data () {
        return {
            currentDate: new Date(),
            disabledDates: {
                to: yesterday,
                dates: rejectedDates
            }
        }
    },

    methods: {
        addRejectedDate: function (event) {
            alert("HOLA!!");

            var fecha = document.getElementById("inputFecha").value;
            alert(fecha);
            var fecha2 = new Date(fecha);

            alert(fecha2);
            rejectedDates.push(fecha2);
        }
  }
}
</script>

<style>

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
        margin: 0 auto !important;
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
    .vdp-datepicker__calendar .cell:not(.blank):not(.disabled).day:hover, .vdp-datepicker__calendar .cell:not(.blank):not(.disabled).month:hover, .vdp-datepicker__calendar .cell:not(.blank):not(.disabled).year:hover {
        border: none !important;
    }
    .vdp-datepicker__calendar .cell.selected {
        background-image: linear-gradient(to right, #00fb82, #187fe6);
        
        border: none;
        border-radius: 30px;
        color: #ffffff;
    }
    .vdp-datepicker__calendar .cell.selected:hover {
        background-image: linear-gradient(to right, #00fb82, #187fe6);
    }

    
</style>

<style scoped>
    * {
        color: #000000;
    }
</style>