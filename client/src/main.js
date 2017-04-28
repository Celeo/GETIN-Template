import Vue from 'vue'
import decode from 'jwt-decode'
import Buefy from 'buefy'

import store from './data'
import router from './router'
import App from './App'


Vue.use(Buefy, {
  defaultIconPack: 'fa'
})

Vue.config.productionTip = false
let url = ''
if (process.env.NODE_ENV === 'development') {
  url = 'http://localhost:5000/'
} else {
  url = window.location.origin + '/api/'
}
Vue.config.SERVER_URL = url
console.log(`Server url: ${url}`)

const token = window.sessionStorage.getItem('token')
if (token) {
  const tokenData = decode(token)
  if (typeof tokenData.name !== 'undefined') {
    store.commit('LOG_IN', { token, tokenData })
  } else {
    window.sessionStorage.removeItem('token')
  }
} else {
  window.sessionStorage.removeItem('token')
}

new Vue({
  router,
  store,
  el: '#app',
  render: h => h(App)
})
