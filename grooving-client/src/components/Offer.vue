<template>
    <div class="everything">
        <div class="card tarjeta">
            <div class="container-fluid">
                <div class="container">
                    <div class="right-div right-text offerInfo">
                        <span class="card-title"><h2>Offer #{{ offerID }} - {{price}}€</h2></span><br>
                        <p>{{date}}</p>
                        <p>  In {{place}}</p>
                    </div>
                    <div class="right-div right-text">
                        <img class="foto" src="https://img.europapress.es/fotoweb/fotonoticia_20181107115306_1920.jpg">
                        <h3 class="fotoText">PEPITO MENGANITO</h3>
                    </div>
                </div>
                <div class="collapse" v-bind:id="noHashtag()">
                    <div class="form-group">
                        <label for="rejectionReason">Please, confirm your rejection:</label>
                        <textarea class="form-control" id="rejectionReason" rows="3" placeholder="You can explain the reason why you are rejecting this offer. It will be shown to the person that contacted you."></textarea>
                    </div>
                    <div class="row container">
                        <div class="right-div right-text2"><a v-bind:href="hashtag()" v-on:click="enableOfferButtons()" class="btn btn-primary cancelButton" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseExample"><span class="continueText">CANCEL</span></a></div>
                        <div class="right-div right-text2"><router-link v-bind:to="confirmURI" class="btn btn-primary confirmButton"><span class="continueText">CONFIRM</span></router-link></div>
                    </div>
                </div>
                <div v-if="offerStatus === 'pending' || offerStatus === 'accepted'" class="row container" v-bind:id="buttonsId()">
                    <div class="right-div right-text2"><a v-bind:href="hashtag()" v-on:click="disableOfferButtons()" class="btn btn-primary rejectButton" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseExample"><span class="continueText">REJECT</span></a></div>
                    <div class="right-div right-text2"><router-link v-bind:to="confirmURI" class="btn btn-primary confirmButton"><span class="continueText">ACCEPT</span></router-link></div>
                </div>
                <div v-else class="row container" v-bind:id="buttonsId()">
                    <div class="right-div right-text2"><a v-bind:href="hashtag()" class="btn btn-primary rejectButton"><span class="continueText">REJECT</span></a></div>
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
            offerStatus: {
                type: String,
                default: 'pending',
            }
        },

        methods: {
            hashtag() {
                return "#offer" + this.offerID;
            },
            noHashtag() {
                return "offer" + this.offerID;
            },
            buttonsId() {
                return "offerButtons" + this.offerID;
            },
            disableOfferButtons() {
                document.getElementById(this.buttonsId()).style.display='none';
                return false;
            },
            enableOfferButtons() {
                document.getElementById(this.buttonsId()).style.display='inline-block';
                return false;
            }
        }
    }   

</script>

<style>

    .form-group {
        text-align: left;
    }

</style>


<style scoped>
    * {
        font-family: "Archivo"
    }

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

    .offerInfo {
        width: 100px !important;
        text-align: left !important;
        vertical-align: top !important;
    }

    .right-div{
        display: inline-block;
        text-align: center;
        width: 50% !important;
        padding: 20px !important;
    }

    .right-div .right-text{
        width: 200px;
    }

    label {
        font-weight: bold;
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
    .confirmButton, .rejectButton, .cancelButton {
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

    .cancelButton {
        background-image: linear-gradient(to right, #a2a2a2, #474747);
    }

    .confirmButton:hover {
        background-image: linear-gradient(to right, #14Ca9f, #1648d0) !important;
    }

    .rejectButton:hover {
        background-image: linear-gradient(to right, #ED7F00, #A20101) !important;
    }

    .cancelButton:hover {
        background-image: linear-gradient(to right, #515151, #232323) !important;
    }

    .everything {
        margin: 0 auto;
    }

    @media (min-width:768px)  {

        .tarjeta {
            min-width: 335px;
            box-shadow: 2px 2px 8px 0px rgba(0, 0, 0, .2);
        }
      
    }

</style>
