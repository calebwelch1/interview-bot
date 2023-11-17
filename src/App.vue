<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!-- <header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header> -->

  <RouterView />
</template>

<style scoped>
.brand-gradient {
  background: rgb(255,27,24);
  background: linear-gradient(342deg, rgba(255,27,24,1) 0%, rgba(255,149,0,1) 100%, rgba(0,212,255,1) 100%);
}
</style>
