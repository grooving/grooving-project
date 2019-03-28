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
                        <router-link to="personalInfo"><img class="card-img-top foto" :src="userIcon"></router-link>
                        <h3 class="fotoText">{{userName}}</h3>
                    </div>
                </div>
                <div class="collapse" v-bind:id="noHashtag()">
                    <div class="form-group">
                        <label for="rejectionReason">Please, confirm your rejection:</label>
                        <textarea class="form-control" id="rejectionReason" rows="3" placeholder="You can explain the reason why you are rejecting this offer. It will be shown to the person that contacted you."></textarea>
                    </div>
                    <div class="row container">
                        <div class="right-div right-text2"><a v-bind:href="hashtag()" v-on:click="enableOfferButtons()" class="btn btn-primary cancelButton" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseExample"><span class="continueText">CANCEL</span></a></div>
                        <div v-if="offerStatus === 'pending' && gsecurity.hasRole('ARTIST')" class="right-div right-text2"><router-link v-bind:to="offerURI" class="btn btn-primary confirmButton" v-on:click="rejectOffer()"><span class="continueText">CONFIRM</span></router-link></div>
                        <div v-if="offerStatus === 'pending' && gsecurity.hasRole('CUSTOMER')" class="right-div right-text2"><router-link v-bind:to="offerURI" class="btn btn-primary confirmButton" v-on:click="withdrawnOffer()"><span class="continueText">CONFIRM</span></router-link></div>
                        <div v-if="offerStatus === 'accepted'" class="right-div right-text2"><router-link v-bind:to="offerURI" class="btn btn-primary confirmButton" v-on:click="cancelOffer()"><span class="continueText">CONFIRM</span></router-link></div>
                    </div>
                </div>
                <div v-if="offerStatus === 'pending' || offerStatus === 'accepted'" class="row container" v-bind:id="buttonsId()">
                    <div class="right-div right-text2"><a v-bind:href="hashtag()" v-on:click="disableOfferButtons()" class="btn btn-primary rejectButton" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseExample"><span class="continueText">REJECT</span></a></div>
                    <div v-if="offerStatus === 'pending' && gsecurity.hasRole('ARTIST')" class="right-div right-text2"><router-link v-bind:to="confirmURI" class="btn btn-primary confirmButton"><span class="continueText">ACCEPT</span></router-link></div>
                </div>
                <div v-else class="row container" v-bind:id="buttonsId()">
                    <div class="right-div right-text2"><a v-bind:href="hashtag()" class="btn btn-primary rejectButton"><span class="continueText">REJECT</span></a></div>
                    <div class="right-div right-text2"><router-link v-bind:to="confirmURI" class="btn btn-primary confirmButton"><span class="continueText">ACCEPT</span></router-link></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    import GAxios from '../utils/GAxios.js'
    import GSecurity from '@/security/GSecurity.js';

    export default {
        name: 'Offer',

        data: function() {
            return {
                gsecurity: GSecurity,
                gaxios: GAxios,
            }
        },
        
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
                type: String,
                default: '#'
            },
            offerStatus: {
                type: String,
                default: 'pending',
            },
            offerURI: {
                type: String,
                default: 'offers'
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
            },

            rejectOffer() {

            },
            cancelOffer() {

            },
            withdrawnOffer() {

            },
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
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
    }

    .rejectButton:hover {
        background-image: linear-gradient(to right, #ED7F00, #A20101) !important;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;

    }

    @media (min-width:600px)  {
        .cancelButton:hover {
            background-image: linear-gradient(to right, #515151, #232323) !important;
        }

        .everything {
            margin: 0 auto;
        }
    }

    @media (min-width:768px)  {

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

</style>
