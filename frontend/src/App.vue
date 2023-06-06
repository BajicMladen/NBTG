<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from './components/layout/Header.vue'
import TradeMark from './components/layout/TradeMark.vue'

import { useUserStore } from '@/store/userStore'

const user = useUserStore()

const userData = JSON.parse(localStorage.getItem('userData'))

if (userData) {
  user.setUser({
    id: userData.id,
    firstName: userData.first_name,
    lastName: userData.last_name,
    email: userData.email,
    username: userData.username
  })
}
</script>

<template>
  <div class="flex flex-col h-screen bg-white">
    <Header></Header>
    <RouterView class="flex-1 px-32" />
    <TradeMark class="mt-14" />
  </div>
</template>
