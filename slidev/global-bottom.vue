<template>
  <div
    v-if="$slidev.nav.currentPage > 1"
    class="abs-br m-10 text-xs select-none slm-page-number"
  >
    {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
  </div>
</template>
