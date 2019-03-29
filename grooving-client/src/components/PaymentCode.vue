<template>
    <div class="content">
    <form>
        <div class="form-row">
            <div class="form-group col-12">
                <p class="title">Type the code:</p>
                <input :value="code" type="text" class="form-control" placeholder="XXXX-XXXX-XXXX-XXXX">
            </div>  
        </div>
        <div class="continueButtonDiv"><router-link v-bind:to="continueURI" 
            class="btn btn-primary continueButton"><span class="continueText">CONTINUE</span></router-link></div>

    </form>
    </div>
</template>

<script>
export default {
    name: "paymentCode",
    props: {
        code: {
            type: String,
            default: '1234-5678-9012-3456'
        },
        continueURI: {
            type: String,
            default: 'paymentConfirmation'
        } 
    },
}
</script>

<style scoped>
    
    input:hover{
        border-color: #187fe6;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .3) !important;
    }

    input:focus{
        border-color: #00fb82;
        font-weight: semibold;
        color:black;
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
        
    }

    .continueButton {
        font-size: 18px;
        padding-left: 4%;
        padding-right: 4%;
        border: none;
        border-radius: 30px;
        width: fit-content;
        margin-top: 2%;
        font-weight: bold;
    
        background-image: linear-gradient(to right, #00fb82, #187fe6);
    }

    .continueButton:hover{
        box-shadow: 0px 2px 8px 0px rgba(0, 0, 0, .7) !important;
        background-image: linear-gradient(to right, #14Ca9f, #1648d0) !important;
    }

    .title {
        text-align: center;
        font-size: 30px;
        margin-top: 5%;
        margin-bottom: 5%;
        font-weight: bold;
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
            margin-left: 3%;
            height: 305px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            box-shadow: 0px 2px 8px 2px rgba(0, 0, 0, .3);
            
            
        }
    }


</style>
