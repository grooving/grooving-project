<template>
    <div class="everything">
        <div class="card tarjeta">
            <div class="container-fluid">
                <div class="container">
                    <div class="right-div right-text" style="width: 100px; text-align: left; vertical-align: top;s">
                        <span class="card-title"><h2>Offer #{{ offerID }} - {{price}}€</h2></span><br>
                        
                        <p>{{date}}</p>
                        <p>  In {{place}}</p>
                    </div>
                    <div class="right-div right-text">
                        <img class="foto" src="https://img.europapress.es/fotoweb/fotonoticia_20181107115306_1920.jpg">
                        <h3 class="fotoText">PEPITO MENGANITO</h3>
                    </div>
                </div>
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
            }
        },
    }   

</script>

<style scoped>

    .row .container{
        margin: 0px !important;
    }

    .foto{
        width: 100%;
        border-radius: 10px;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .3);
    }

    .fotoText{
        margin-top: 10%;
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
    }

    .rejectButton:hover {
        background-image: linear-gradient(to right, #ED7F00, #A20101) !important;
    }

    @media (min-width:768px)  {

        .tarjeta {
            min-width: 335px;
            box-shadow: 2px 2px 8px 0px rgba(0, 0, 0, .2);
        }
      
    }

    .everything {
        margin: 0 auto;
    }

</style>
