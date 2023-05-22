<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router'
import cart from '../..//assets/cart.png'
import userImg from '../..//assets/user.png'
import { useUserStore } from '@/store/userStore'

const user = useUserStore()

const router = useRouter()

const goToHomePage = () => {
  router.push({ name: 'home' })
}
const goToProfile = () => {
  router.push({ name: 'profile' })
}

const logout = () => {
  localStorage.removeItem('tokens')
  localStorage.removeItem('userData')
  localStorage.removeItem('cart')
  user.resetUser()
  goToHomePage()
}
</script>

<template>
  <div class="flex flex-row items-center justify-between px-32 mb-10 py-6 bg-blue-900 h-14">
    <div class="text-2xl text-white cursor-pointer" @click="goToHomePage">NBTG</div>
    <div class="flex flex-row text-white text-lg">
      <div class="flex flex-row">
        <img :src="cart" alt="login_icon" class="mr-2 w-5 h-5 mt-1" />
        <RouterLink to="/cart" class="mr-8">Cart</RouterLink>
      </div>
      <div class="flex flex-row" v-if="!user.isLoggedIn">
        <img :src="userImg" alt="login_icon" class="mr-2 w-5 h-5 mt-1" />
        <RouterLink to="/login">Login</RouterLink>
      </div>
      <div v-else>
        <va-dropdown class="bg-transparent">
          <template #anchor>
            <div class="bg-transparent cursor-pointer">{{ user.username }}</div>
          </template>

          <va-dropdown-content class="z-10 flex flex-col justify-center items-center w-28 gap-1">
            <div @click="goToProfile" class="cursor-pointer">Profile</div>
            <div @click="logout" class="cursor-pointer">Logout</div>
          </va-dropdown-content>
        </va-dropdown>
      </div>
    </div>
  </div>
</template>
