<template>
    <div>
        <TypeOfHiring v-if="paymentProcess == 0" @hiring="nextStep()" />
        <DateSelection v-if="paymentProcess == 1" @dateSelected="nextStepDateSelected" />
        <TimeSelection v-if="paymentProcess == 2" @timeSelected="nextStep()" />
        <AddressInput v-if="paymentProcess == 3" @addressSelected="nextStepAddress" />
        <EventInput v-if="paymentProcess == 4" @eventData="nextStepDescription" />
        <PaymentSelector v-if="paymentProcess == 5" @paymentSelected="nextStep()" />
        <Payment v-if="paymentProcess == 6" />
    </div>
</template>

<script>

import TypeOfHiring from '@/views/TypeOfHiring.vue'
import DateSelection from '@/views/DateSelection.vue'
import TimeSelection from '@/views/TimeSelection.vue'
import AddressInput from '@/views/AddressInput.vue'
import EventInput from '@/views/EventInput.vue'
import PaymentSelector from '@/views/PaymentSelector.vue'
import Payment from '@/views/Payment.vue'
import endpoints from '@/utils/endpoints.js'
import GAxios from '@/utils/GAxios.js'
import GSecurity from '@/security/GSecurity.js'


export default {
    components:{
        TypeOfHiring,
        DateSelection,
        TimeSelection,
        AddressInput,
        EventInput, 
        PaymentSelector,
        Payment,
    },

    data: function(){
        return {
            paymentProcess: 0,
            hiringType: 1,
            fecha: '',
            duracion: 2,
            zipcode: '',
            address: '',
            street: '',
            description: '',
            gsecurity: GSecurity,
        }
    },

    methods: {
        nextStep: function(){
            this.paymentProcess++;
        },
        nextStepDateSelected: function(){
            this.fecha = arguments[0];
            this.nextStep();
        },
        nextStepAddress: function(){
            this.zipcode = arguments[0];
            this.address = arguments[1];
            this.street = arguments[2];
            this.nextStep();
        },
        nextStepDescription: function(){
            this.description = arguments[0];
            this.createOffers();
        },

        createOffers: function(){

            var authorizedGAxios = GAxios;
            var GAxiosToken = this.gsecurity.getToken();
            authorizedGAxios.defaults.headers.common['Authorization'] = 'Token ' + GAxiosToken;
            console.log(GAxiosToken)
            //Creamos EventLocation
            authorizedGAxios.post(endpoints.offer)
            .then(response => {
                console.log(response);
            }).catch(ex => {
                console.log(ex);
            });

        }
    }
}
</script>

<style scoped>

</style>

