import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

const state = {
  token: null,
  name: null,
  inAlliance: false,
  axios: axios.create()
}

const mutations = {
  LOG_IN(state, payload) {
    const { token, tokenData } = payload
    state.token = token
    state.name = tokenData.name
    state.inAlliance = tokenData.inAlliance
    state.axios = axios.create({ headers: { Authorization: token } })
  },

  LOG_OUT(state) {
    state.token = null
    state.name = null
    state.inAlliance = false
    state.axios = axios.create()
  }
}

const getters = {
  token(state) {
    return state.token
  },

  name(state) {
    return state.name
  },

  isLoggedIn(state) {
    return !!state.name
  },

  inAlliance(state) {
    return state.inAlliance
  },

  axios(state) {
    return state.axios
  }
}


export default new Vuex.Store({
  state,
  mutations,
  getters
})
