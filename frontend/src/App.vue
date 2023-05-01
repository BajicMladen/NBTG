<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from './components/layout/Header.vue'
import TradeMark from './components/layout/TradeMark.vue'
</script>

<template>
  <div class="flex flex-col justify-between m-0 p-0">
    <Header></Header>
    <RouterView class="h-full px-32" />
    <TradeMark class="mt-14" />
  </div>
</template>
