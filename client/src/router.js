import Vue from 'vue'
import VueRouter from 'vue-router'

import store from './data'

import Landing from './pages/Landing'
import Login from './pages/Login'
import Logout from './pages/Logout'


Vue.use(VueRouter)

const routes = [
  { path: '/', component: Landing, name: 'Landing' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/logout', component: Logout, name: 'Logout' }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

/*
  State and permission-based routing
*/
router.beforeEach((to, from, next) => {
  /*
    If the user is not logged in and not in the process of doing so or just
    looking at the landing page, redirect them away from their detination
    to the landing page.
  */
  if (to.name !== 'Login' && to.name !== 'Logout' && to.name !== 'Landing') {
    if (!store.getters.isLoggedIn) {
      next({ name: 'Landing' })
      return
    }
  }
  next()
})


// export created and configured router
export default router
