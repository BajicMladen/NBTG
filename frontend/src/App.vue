<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from './components/layout/Header.vue'
import TradeMark from './components/layout/TradeMark.vue'
</script>

<template>
  <div class="flex flex-col h-screen bg-white">
    <Header></Header>
    <RouterView class="flex-1 px-32" />
    <TradeMark class="mt-14" />
  </div>
</template>
