<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from './components/layout/Header.vue'
import TradeMark from './components/layout/TradeMark.vue'
</script>

<template>
  <div class="flex flex-col justify-between m-0 p-0 h-screen w-full">
    <Header></Header>
    <RouterView />
    <TradeMark />
  </div>
</template>
