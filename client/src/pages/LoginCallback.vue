<template lang="pug">
  section.section
    div.container
      div.heading
        h1.title(v-if="!error && processing") Finishing login ...
        template
          div(v-if="error")
            h1.title.red An error occurred with your login
            h2.subtitle
              router-link(to="{ name: 'Login' }") Please log in again
          div(v-if="!error && !processing && name")
            h1.title Login successful, redirecting you <strong>{{ name }}</strong>
</template>

<script>
import Vue from 'vue'
import decode from 'jwt-decode'


export default {
  data() {
    return {
      processing: true,
      error: false,
      name: ''
    }
  },
  async created() {
    try {
      const code = window.location.href.match(/code=([0-9a-zA-Z_-]*)/)[1]
      const response = await this.$store.getters.axios.post(`${Vue.config.SERVER_URL}eve/sso`, { code })
      const { token } = response.data
      const tokenData = decode(token)
      window.sessionStorage.setItem('token', token)
      this.$store.commit('LOG_IN', { token, tokenData })
      this.$router.push({ name: 'Landing' })
      this.processing = false
      this.error = false
    } catch (err) {
      console.error(err)
      this.error = true
    }
  }
}
</script>

<style lang="stylus" scoped>
.red
  color $red
</style>
