<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/store/userStore'

const user = useUserStore()

const router = useRouter()

const goToHomePage = () => {
  router.push({ name: 'home' })
}
const goToProfile = () => {
  router.push({ name: 'profile' })
}
const goToOrdersPage = () => {
  router.push({ name: 'ordersAdmin' })
}
const goToGamesPage = () => {
  router.push({ name: 'gamesAdmin' })
}
const goToUsersPage = () => {
  router.push({ name: 'usersAdmin' })
}

const logout = () => {
  localStorage.removeItem('tokens')
  localStorage.removeItem('userData')
  localStorage.removeItem('cart')
  localStorage.removeItem('checkoutAddress')
  user.resetUser()
  goToHomePage()
}
</script>

<template>
  <div class="flex flex-row items-center justify-between px-32 mb-10 py-6 bg-blue-900 h-14">
    <div class="text-2xl text-white cursor-pointer" @click="goToHomePage">NBTG</div>
    <div class="flex flex-row text-white text-lg">
      <div class="flex flex-row">
        <va-icon class="mr-1 mt-1" name="shopping_cart" />
        <RouterLink to="/cart" class="mr-8">Cart</RouterLink>
      </div>
      <div class="flex flex-row mr-6" v-if="user.isAdmin">
        <va-icon class="mr-1 mt-1" name="build" />
        <va-dropdown class="bg-transparent">
          <template #anchor>
            <div class="bg-transparent cursor-pointer">Dashboard</div>
          </template>

          <va-dropdown-content class="z-10 flex flex-col justify-center items-center w-28 gap-1">
            <div @click="goToOrdersPage" class="cursor-pointer">Orders</div>
            <div @click="goToGamesPage" class="cursor-pointer">Games</div>
            <div @click="goToUsersPage" class="cursor-pointer">Users</div>
          </va-dropdown-content>
        </va-dropdown>
      </div>
      <div class="flex flex-row" v-if="!user.isLoggedIn">
        <RouterLink to="/login">Login</RouterLink>
      </div>
      <div v-else class="flex flex-row">
        <va-avatar size="small" class="mr-2">
          <img :src="`http://127.0.0.1:8000${user?.image}`" />
        </va-avatar>
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
