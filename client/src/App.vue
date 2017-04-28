<template lang="pug">
  div
    nav.nav.has-shadow
      div.container
        div.nav-left
          router-link#brand.nav-item(:to="'/'") GETIN
        div.nav-center.nav-menu
          router-link.nav-item.is-tab(
            :to="{ name: 'Landing' }"
            v-bind:class="{ 'is-active': $router.currentRoute.name == 'Landing' }"
          ) Home
          div(v-if="!loggedIn")
            router-link.nav-item.is-tab(
              :to="{ name: 'Login' }"
              v-bind:class="{ 'is-active': $router.currentRoute.name == 'Login' }"
            ) Log in
          div(v-if="loggedIn")
            router-link.nav-item.is-tab(
              :to="{ name: 'Logout' }"
              v-bind:class="{ 'is-active': $router.currentRoute.name == 'Logout' }"
            ) Log out
    transition(name="fade" mode="out-in")
      router-view
</template>

<script>
export default {
  computed: {
    loggedIn() {
      return this.$store.getters.isLoggedIn
    },
    member() {
      return this.$store.getters.inAlliance
    }
  }
}
</script>

<!-- Buefy customization -->
<style lang="scss">
@import "~bulma/sass/utilities/_all";

$primary: $blue;
$primary-invert: findColorInvert($primary);

$colors: (
    "white": ($white, $black),
    "black": ($black, $white),
    "light": ($light, $light-invert),
    "dark": ($dark, $dark-invert),
    "primary": ($primary, $primary-invert),
    "info": ($info, $info-invert),
    "success": ($success, $success-invert),
    "warning": ($warning, $warning-invert),
    "danger": ($danger, $danger-invert)
);

$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>

<!-- App css -->
<style lang="stylus">
#brand
  font-weight 600
  font-size 24px

.fade-enter-active, .fade-leave-active
  transition opacity .2s

.fade-enter, .fade-leave-active
  opacity 0
</style>
