<template>
<div class="prueba">
    <div class="everything">
        <div class="paymentSelect">
          <div class="paymentOptions"><ProfileInfo/></div>
        </div>
    </div>
</div>
</template>

<script>
import ProfileInfo from '@/components/ProfileInfo.vue'

export default {
    name: 'personalInfo',
    components: {
        ProfileInfo
    },
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
