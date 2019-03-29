<template>
    <div class="everything">
        <div class="card tarjeta">
            <ul class="list-group list-group-flush"><li style="font-weight: bold" class="list-group-item">Offer #{{ offerID }}</li></ul>
            <div class="card-body cuerpoTarjeta">
                <div class="leftContent">
                    <div class="details">
                    <p class="card-text"><span style="font-weight: bold;">Date: </span>{{ date }}</p>
                    <p class="card-text"><span style="font-weight: bold;">Duration: </span>{{ startingHour }} {{ endingHour }}h</p>
                    <p class="card-text"><span style="font-weight: bold;">Price: </span>${{ price }}</p>
                    <p class="card-text"><span style="font-weight: bold;">Address: </span>{{ address }}</p>
                    </div>
                    <div class="description">
                    <p class="card-text"><span style="font-weight: bold;">Description: </span></p>
                    <p class="card-text">{{ description }}</p>
                    </div>
                </div>
                
            </div>
            <div class="bothButtons">
                <div class="cancelButtonDiv"><router-link v-bind:to="cancelURI" class="btn btn-primary cancelButton"><span class="continueText">CANCEL</span></router-link></div>
                <div class="confirmButtonDiv"><div @click="accept()" class="btn btn-primary confirmButton"><span class="continueText">CONFIRM</span></div></div>
            </div>
        </div>
    </div>
</template>

<script>
    import endpoints from '@/utils/endpoints.js';
    import GAxios from '../utils/GAxios.js'
    import GSecurity from '@/security/GSecurity.js';

    export default {
        name: 'extendedOffer',
        data() {
            return {
                gsecurity: GSecurity,
                gaxios: GAxios,
                id: Number,
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
            startingHour: {
                type: String,
                default: '',
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
                default: 'offers'
            },
            confirmURI: {
                type: String,
                default: '/acceptedOffer/'
            }
        },
        methods: {
            accept() {
                var authorizedGAxios = GAxios;
                var GAxiosToken = this.gsecurity.getToken();
                authorizedGAxios.defaults.headers.common['Authorization'] = 'Token ' + GAxiosToken;
                console.log(this.$route.params['offerId'] + ' Hi');
                
                authorizedGAxios.put(endpoints.offer + this.$route.params['offerId'] + '/', 
                {
                    "status": "REJECTED",
                })
                this.$router.push({path: '/offers/'})
                    .then(response => {
                        console.log(response);
                }).catch(ex => {
                    console.log(ex);
                });
                },
            },
    }   
</script>

<style scoped>
    * {
        font-family: "Archivo"
    }

    .tarjeta {
        width: 100%;
    }

    .list-group-item {
        font-size: 36px;
        text-align: left;
    }
    
    .leftContent {
        text-align: left;
    }

    .cancelButtonDiv, .confirmButtonDiv {
        margin-left: 5%;
        margin-right: 5%;
    }

    .bothButtons {
        display: flex;
        justify-content: center;
        padding-bottom: 20px;
    }

    .confirmButton, .cancelButton {
        font-size: 18px;
        border: none;
        border-radius: 30px;
        font-weight: bold;
    }

    .confirmButton {
        margin-left: 3%;
        background-image: linear-gradient(to right, #00fb82, #187fe6);
    }

    .cancelButton {
        margin-right: 3%;        
        background-image: linear-gradient(to right, #a2a2a2, #474747);
    }

    .confirmButton:hover {
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
        background-image: linear-gradient(to right, #14Ca9f, #1648d0) !important;
    }

    .cancelButton:hover {
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
        background-image: linear-gradient(to right, #515151, #232323) !important;
    }

    @media (min-width:768px)  {

        .tarjeta {
            min-width: 335px;
            width: 70%;
            max-width: 900px;

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
            margin-top:5%;
        }

        .details {
            float: left;
            margin-right: 3%;
            flex-basis: 50%;
            flex-grow: 0;
        }

        .description {
            max-width: 250 px;
            flex-basis: 50%;
            flex-grow: 0;
            margin-left: 3%;
        }

        .leftContent {
            display: inline-flex;
            align-items: center;
        }
    }

</style>

<style>

    p.card-text {
        word-break: break-word;
    }

</style>
