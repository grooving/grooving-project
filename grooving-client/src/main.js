import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import GSecurity from './security/GSecurity.js'


Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.prototype.$gsecurity = GSecurity;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

export default Vue