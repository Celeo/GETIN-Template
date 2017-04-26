<template lang="pug">
  div.container
    section.section
      div.heading
        h1.title Logging out ...
</template>

<script>
export default {
  async mounted() {
    this.$store.commit('LOG_OUT')
    window.sessionStorage.removeItem('token')
    setInterval(() => {
      window.location.href = '/'
    }, 2000)
  }
}
</script>
