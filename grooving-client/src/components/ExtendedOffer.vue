<template>
    <div class="everything">
        <div class="card tarjeta">
            <ul class="list-group list-group-flush"><li class="list-group-item">Offer #{{ offerID }}</li></ul>
            <div class="card-body cuerpoTarjeta">
                <div class="leftContent">
                    <p class="card-text"><span style="font-weight: bold;">Date: </span>{{ date }}</p>
                    <p class="card-text"><span style="font-weight: bold;">Duration: </span>{{ startingHour }}h - {{ endingHour }}h</p>
                    <p class="card-text"><span style="font-weight: bold;">Price: </span>${{ price }}</p>
                    <p class="card-text"><span style="font-weight: bold;">Address: </span>{{ address }}</p>
                    <p class="card-text"><span style="font-weight: bold;">Description: </span></p>
                    <p class="card-text">{{ description }}</p>
                </div>
                
            </div>
            <div class="bothButtons">
                <div class="cancelButtonDiv"><a v-bind:href="cancelURI" class="btn btn-primary cancelButton"><span class="continueText">CANCEL</span></a></div>
                <div class="confirmButtonDiv"><a v-bind:href="confirmURI" class="btn btn-primary confirmButton"><span class="continueText">CONFIRM</span></a></div>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'extendedOffer',
        
        props: {
            offerID: {
                type: Number,
                default: 3
            },
            date: {
                type: String,
                default: 'March 19, 2019',
            },
            startingHour: {
                type: String,
                default: '19:30',
            },
            endingHour: {
                type: String,
                default: '23:00',
            },
            price: {
                type: Number,
                default: 61.00
            },
            address: {
                type: String,
                default: 'Plaza de España s/n',
            },
            description: {
                type: String,
                default: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            },
            cancelURI: {
                type: String,
                default: '#'
            },
            confirmURI: {
                type: String,
                default: '#'
            }
        },
    }   

</script>

<style scoped>
    * {
        font-family: "Archivo"
    }

    .tarjeta {
        width: 100%;
        box-shadow: 2px 2px 8px 0px rgba(0, 0, 0, .2);
    }

    .list-group-item {
        font-size: 36px;
        text-align: left;
    }
    
    .leftContent {
        text-align: left;
    }

    .cancelButtonDiv, .confirmButtonDiv {
        padding: 5px;
    }

    .bothButtons {
        display: flex;
        justify-content: center;
        padding-bottom: 20px;
    }

    .confirmButton, .cancelButton {
        font-size: 21px;
        font-weight:bold;
        
        border: none;
        border-radius: 30px;
    }

    .confirmButton {
        background-image: linear-gradient(to right, #00fb82, #187fe6);
    }

    .cancelButton {        
        background-image: linear-gradient(to right, #a2a2a2, #474747);
    }

    .confirmButton:hover {
        background-image: linear-gradient(to right, #14Ca9f, #1648d0) !important;
    }

    .cancelButton:hover {
        background-image: linear-gradient(to right, #515151, #232323) !important;
    }

    @media (min-width:768px)  {

        .tarjeta {
            min-width: 335px;
            width: 25%;

            box-shadow: 2px 2px 8px 0px rgba(0, 0, 0, .2);
        }
      
        .everything {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 5%;
            text-align: center;
            padding: 15px;
            margin-left: 10%;
            margin-right: 10%;
            margin-top:0%;
        }
    }

</style>
