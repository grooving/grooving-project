<template>
    <div class="content">
        <form>
            <div class="form-row">
                <div class="form-group col-12">
                    <h5 class="card-title" style="font-weight:bold;font-size:30px;">Profile</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Basic info of your Grooving account, like your name and email.</h6>
                    <div style="width:100%;margin-top:25px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">NAME</p>
                        <p class="card-text" style="float:right;">{{name}}</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:25px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">SURNAMES</p>
                        <p class="card-text" style="float:right;">{{surnames}}</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">EMAIL</p>
                        <p class="card-text" style="float:right;">{{email}}</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">PHONE</p>
                        <p class="card-text" style="float:right;">{{phoneNumber}}</p>
                    </div>
                    <!--
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">COUNTRY</p>
                        <p class="card-text" style="float:right;">{{userCountry}}</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">BIRTH DATE</p>
                        <p class="card-text" style="float:right;">{{userBirthday}}</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">STATE</p>
                        <p class="card-text" style="float:right;">{{userState}}</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;margin-bottom:0px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">CITY</p>
                        <p class="card-text" style="float:right;">{{userCity}}</p>
                    </div>-->
                </div>  
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "profileInfo",
    props: {
        name: {
            type: String,
            //default: 'John'
        },
        surnames: {
            type: String,
            //default: 'Pug Retriever'
        },
        email: {
            type: String,
            //default: 'johnpug@pugsftw.com'
        },
        phoneNumber: {
            type: String,
            //default: '633017787'
        },
        userBirthday: {
            type: String,
            default: '09/09/2000'
        },
        userState: {
            type: String,
            default: 'Andalucia'
        },
        userCity: {
            type: String,
            default: 'Pilas'
        },

        location: {
            type: String,
            default: 'Monday night party at the campus.'
        },
        continueURI: {
            type: String,
            default: 'paymentSelector'
        } 
    },
}
</script>

<style scoped>

    .continueButton {
        font-size: 18px;
        padding-left: 4%;
        padding-right: 4%;
        border: none;
        border-radius: 30px;
        width: fit-content;
        font-weight: bold;
    
        background-image: linear-gradient(to right, #00fb82, #187fe6);
    }

    .continueButton:hover{
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
        background-image: linear-gradient(to right, #14Ca9f, #1648d0) !important;
    }
    
    .content {
        padding: 10px;
    }

    .form-group.col-12 {
        margin-bottom: 0px;
    }

    @media (max-width:767px)  {
        .content{
            padding-top: 5%;
            margin-right: 3%;
            margin-left: 3%;
        }
    }

    @media (min-width:768px)  {

        .continueButton{
            
            margin-right: 25%;
            margin-left: 25%;
        }
        
        form{
            margin-top:5px;
            width: 320px;
            margin-right: 4%;
            margin-left: 4%;
            margin-bottom: 0;
        }

        .content{
            margin-top: 10% !important;
            margin-left: 3%;
            border-radius: 10px;
            display: flex;
            align-items: center;
            box-shadow: 0px 2px 8px 2px rgba(0, 0, 0, .3);
        }
    }

</style>
