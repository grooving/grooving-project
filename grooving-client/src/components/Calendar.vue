<template>
    <div>
        <div>{{ availableDates }}</div>
        <div><vuejs-datepicker v-model="model.date" :disabledDates="disabledDates"  :full-month-name="true" :inline="true"></vuejs-datepicker></div>
    </div>
</template>

<script>

var yesterday = new Date();
yesterday.setDate(yesterday.getDate()-1);

export default {
    name: "Calendar",

    data () {
        return {
            model: {
                date: "",
            },
            currentDate: new Date(),
            disabledDates: {},
        }
    },

    props: {
        availableDates: Array,
        stringToDates: Array,
    },

    components: {
        vuejsDatepicker
    },

    created: function() {
        var res = Array();

        for (var i = 0; i < this.availableDates.length; i++) { 
            res.push(new Date(this.availableDates[i]));
        }

        this.stringToDates = res;

        this.disabledDates = {
            to: yesterday,
            dates: this.stringToDates,
        }
    }
}
</script>

<style>

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

