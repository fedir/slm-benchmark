<template>
  <div
    v-if="![1, $slidev.nav.total].includes($slidev.nav.currentPage)"
    class="corner-accent"
  />
</template>
