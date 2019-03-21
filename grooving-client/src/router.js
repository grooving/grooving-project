import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/tarjeta',
      name: 'tarjeta',
      component: () => import('./views/DateSelection.vue')
    },
    {
      path: '/acceptnotif',
      name: 'acceptnotif',
      component: () => import('./components/AcceptedNotif.vue')
    },
    {
      path: '/sentnotif',
      name: 'sentnotif',
      component: () => import('./components/SentOfferNotif.vue')
    },
  ]
})
