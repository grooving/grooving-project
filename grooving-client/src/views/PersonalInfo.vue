<template>
<div class="prueba">
    <div class="everything">
        <div class="paymentSelect">
          <div class="paymentOptions"><ProfileInfo :name="userName" :surnames="userSurnames" :email="userEmail" :phoneNumber="userPhoneNumber" /></div>
        </div>
    </div>
</div>
</template>

<script>
import ProfileInfo from '@/components/ProfileInfo.vue';
import GAxios from '@/utils/GAxios.js';
import endpoints from '@/utils/endpoints.js';
import GSecurity from '@/security/GSecurity.js';

export default {
    name: 'personalInfo',
    components: {
        ProfileInfo
    },
    props: {
        userName:{
            type: String
        },
        userSurnames:{
            type: String
        },
        userEmail: {
            type: String
        },
        userPhoneNumber: {
            type: String
        }
    },
    data: function(){
        gsecurity: undefined

    },

    beforeMount: function(){
        this.gsecurity = GSecurity
        var GAxiosToken = this.gsecurity.getToken();


        var authorizedGAxios = GAxios;
        authorizedGAxios.defaults.headers.common['Authorization'] = 'Token '+GAxiosToken;

        var role = this.gsecurity.getRole();

        
        if(role=='CUSTOMER'){
            //alert(GAxiosToken)
            authorizedGAxios.get(endpoints.customerPersonalInformation)
                .then(response => {
                    var personalInformation = response.data.user;
                    console.log(personalInformation);
                    console.log(response);
                    
                    this.userName=personalInformation['first_name']
                    this.userSurnames = personalInformation['last_name'];
                    this.userEmail=personalInformation['email'];
                    this.userPhoneNumber = response.data.phone;


                
            });
        
        }

        

        if(role=='ARTIST'){
            //alert(GAxiosToken)
            authorizedGAxios.get(endpoints.artistPersonalInformation)
                .then(response => {
                    var personalInformation = response.data.user;
                    console.log(personalInformation);
                    console.log(response);
                    
                    this.userName=personalInformation['first_name']
                    this.userSurnames = personalInformation['last_name'];
                    this.userEmail=personalInformation['email'];
                    this.userPhoneNumber = response.data.phone;


                
            });
        
        }
    }
}
</script>

<style scoped>
    * {
        font-family: "Archivo"
    }

    @media (min-width:768px)  {
      
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
