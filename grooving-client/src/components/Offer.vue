<template>
    <div class="everything">
        <div class="card tarjeta">
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
            <div class="container-fluid">
                <div class="container">
                    <div class="right-div right-text" style="width: 100px; text-align: left; vertical-align: top;margin-bottom: 20px;">
                        <div class="priceCard"><h1>{{price}}€</h1><br>
                        </div>
                        <div  style="padding-top: 20px;">
                        <div class="cardTextDate"><i class="material-icons iconOffer">event_note</i><p><span style="margin-bottom: 1px;">{{date}}</span></p>
                        </div>
                        <br>
                        <div class="cardTextLocation"><i class="material-icons iconOffer">location_on</i><p> {{place}}</p>
                        </div>
                        <br>
                        <div class="cardTextId"><i class="material-icons iconOffer">error_outline</i><p style="word-break: break-all">ID:{{offerID}}</p>
                        </div>
                        </div>
                    </div>
                    <div class="right-div right-text">
                        <img class="card-img-top foto" :src="userIcon">
                        <h3 class="fotoText">{{userName}}</h3>
                    </div>
                </div>
                <hr>
                <div class="row container" >
                <div class="right-div right-text2"><router-link v-bind:to="rejectURI" class="btn btn-primary rejectButton"><span class="continueText">REJECT</span></router-link></div>
                <div class="right-div right-text2"><router-link v-bind:to="confirmURI" class="btn btn-primary confirmButton"><span class="continueText">ACCEPT</span></router-link></div>
            </div>
            </div>
        </div>
    </div>
    </div>
</template>

<script>

    export default {
        name: 'Offer',
        
        props: {
            offerID: {
                type: Number,
                default: 3
            },
            date: {
                type: String,
                default: 'March 19, 2019',
            },
            price: {
                type: Number,
                default: 61.00
            },
            place: {
                type: String,
                default: 'Pontevedra',
            },
            rejectURI: {
                type: String,
                default: '#'
            },
            confirmURI: {
                type: String,
                default: '#'
            },
            userIcon: {
                type: String,
                default: '#'
            },
            userName: {
                tyoe: String,
                default: '#'
            }
        },
    }   

</script>

<style scoped>

    .material-icons:hover {
        background: -webkit-linear-gradient(left, #000000, #000000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .iconOffer{
        color:black !important;
    }

    .priceCard{
        background-image: linear-gradient(#ffc107, #ff9800);
        text-align: center;
        border-radius: 10px;
        color: white;
        font-weight: bolder;
        font-family: "Archivo";
        display: table;
        width: 100%;
        padding: 5px;
        vertical-align: middle !important;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .3);
        
        
    }

    .titleCard{
        text-align: left;
        color: black;
        font-weight: semibold;
        font-family: "Archivo";
        display: table;
        width: 100%;
        padding: 5px;
        vertical-align: middle !important;
    }

    .titleCard h3{
        margin-bottom: 0px;
        height: 100%;
        vertical-align: middle;
        display: table-cell;
        vertical-align: middle;
        font-weight: bold;

        font-size: 1vh;
        
    }

    .priceCard h1{
        margin-bottom: 0px;
        height: 100%;
        vertical-align: middle;
        display: table-cell;
        vertical-align: middle;
        font-weight: bold;
        font-size: 2.25vh;
    }

    .cardTextDate{
        display: inline-flex;
        vertical-align: middle;
    }

    .cardTextLocation{
        display: inline-flex;
        vertical-align: middle;
    }

    .cardTextId{
        display: inline-flex;
        vertical-align: middle;
    }

    

    .row .container{
        margin: 0px !important;
    }

    .container{
        width: 100% !important;
        padding: 0px !important;
    }

    .foto{
        object-fit: cover;
        border-radius: 100px;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .3);
        height: 8rem;
        width: 8rem;
    }

    .fotoText{
        margin-top: 10%;
        font-weight: semibold;
    }

    .right-div{
        display: inline-block;
        text-align: center;
        width: 50% !important;
        padding: 20px !important;
    }
    
    .right-div2{
        padding: 0px !important;
    }

    .right-div2{
        padding: 10px !important;
    }

    .right-div .right-text{
        width: 200px;
    }

    * {
        font-family: "Archivo"
    }

    .botonera{
        
        display:flex;
        align-content: center;
    }

    .subtitle{
        color: #187FE6;
    }
    .texto-izq{
        text-align:left;
    }

    .texto-dcha{
        text-align:right;
    }

    .card-title{
        font-size: 1.25rem;
        
    }

    .card-title h2{
        font-weight: bold !important;
    }

    .tarjeta {
        width: 100%;
        box-shadow: 2px 2px 8px 0px rgba(0, 0, 0, .2);
    }
    
    .leftContent {
        text-align: left;
    }

    .rejectButtonDiv, .confirmButtonDiv {
        padding: 5px;
    }
    
    

    .bothButtons {
        display: flex;
        justify-content: center;
        padding-bottom: 20px;
        width: 100% !important;
    }

    .confirmButton, .rejectButton {
        font-size: 21px;
        font-weight:bold;
        width: 100%;
        border: none;
        border-radius: 30px;
    }

    .confirmButton {
        background-image: linear-gradient(to right, #00fb82, #187fe6);
    }

    .rejectButton {        
        background-image: linear-gradient(to right, #FB8600, #FF0000);
    }

    .confirmButton:hover {
        background-image: linear-gradient(to right, #14Ca9f, #1648d0) !important;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
    }

    .rejectButton:hover {
        background-image: linear-gradient(to right, #ED7F00, #A20101) !important;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;

    }

    @media (min-width:600px)  {

        .tarjeta {
            min-width: 335px;
            box-shadow: 2px 2px 8px 0px rgba(0, 0, 0, .2);
        }


        .priceCard h1{
        margin-bottom: 0px;
        height: 100%;
        vertical-align: middle;
        display: table-cell;
        vertical-align: middle;
        font-weight: bold;
        font-size: 2.25vh;
    }
    .titleCard h3{
        margin-bottom: 0px;
        height: 100%;
        vertical-align: middle;
        display: table-cell;
        vertical-align: middle;
        font-weight: semibold;
        
        
        
    }

    

   
      
    }

    .everything {
        margin: 0 auto;
    }

</style>
