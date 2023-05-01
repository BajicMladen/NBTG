<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router'
import cart from '../..//assets/cart.png'
import user from '../..//assets/user.png'

const router = useRouter()

function goToHomePage() {
  router.push({ name: 'home' })
}
</script>

<template>
  <div class="flex flex-row items-center justify-between px-32 mb-10 bg-slate-600 h-20">
    <div class="text-2xl text-white cursor-pointer" @click="goToHomePage">NBTG</div>
    <div class="flex flex-row text-white text-lg">
      <div class="flex flex-row">
        <img :src="cart" alt="login_icon" class="mr-2 w-5 h-5 mt-1" />
        <RouterLink to="/cart" class="mr-8">Cart</RouterLink>
      </div>
      <div class="flex flex-row">
        <img :src="user" alt="login_icon" class="mr-2 w-5 h-5 mt-1" />
        <RouterLink to="/login">Login</RouterLink>
      </div>
    </div>
  </div>
</template>
