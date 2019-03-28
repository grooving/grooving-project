<template>
    <div class="content">
        <form>
            <div class="form-row">
                <div class="form-group col-12">
                    <h5 class="card-title" style="font-weight:bold;font-size:30px;">Profile</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Basic info of your Grooving account, like your name and email.</h6>
                    <div style="width:100%;margin-top:25px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">FULL NAME</p>
                        <p class="card-text" style="float:right;">John Pug (Pug)</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">EMAIL</p>
                        <p class="card-text" style="float:right;">johnpug@pugsftw.com</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">PASSWORD</p>
                        <p class="card-text" style="float:right;">&#8226;&#8226;&#8226;&#8226;&#8226;&#8226;&#8226;&#8226;</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">COUNTRY</p>
                        <p class="card-text" style="float:right;">Spain</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">BIRTH DATE</p>
                        <p class="card-text" style="float:right;">09/09/2000</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">STATE</p>
                        <p class="card-text" style="float:right;">Andalucia</p>
                    </div>
                    <hr style="margin-top:0px;margin-bottom:0px;"/>
                    <div style="width:100%;margin-top:16px;margin-bottom:0px;">
                        <p class="card-text" style="font-weight:bold;display:inline-block;">CITY</p>
                        <p class="card-text" style="float:right;">Sevilla</p>
                    </div>
                </div>  
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "profileInfo",
    props: {
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
