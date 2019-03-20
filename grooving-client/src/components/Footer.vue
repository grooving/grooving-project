<template>
    <div>
        <footer>
            <div class="info">
                <a v-bind:href="aboutUsURI" class="link">About Us</a> | 
                <a v-bind:href="FAQsURI" class="link">FAQs</a> | 
                <a v-bind:href="termsURI" class="link">Terms of Use</a> | 
                <span>Contact Us:</span> grupogrooving@gmail.com 
            </div>

            <div>Copyright © 2019:
                <a v-bind:href="groovingURI">Grooving</a>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    name: "Footer",
    props: {
        aboutUsURI: {
            type: String,
            default: '#'
        },

        FAQsURI: {
            type: String,
            default: '#'
        },

        termsURI: {
            type: String,
            default: '#'
        },

        groovingURI: {
            type: String,
            default: '#'
        }
    }
}
</script>

<style scoped>
    * {
        font-family: "Archivo"
    }

    footer {
        background-color: #f5f5f5;
        padding: 30px;
    }

    .info {
        padding: 10px;
        color: #606060;
    }

    .link {
        color: #606060;
    }

    span {         
        font-weight: bold;
    }

</style>
