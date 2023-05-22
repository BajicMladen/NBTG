<script setup lang="ts">
import CartItem from '@/components/CartItem.vue'
import { onMounted, ref } from 'vue'
import { useUserStore } from '@/store/userStore'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { fetchAddress } from '../api/index'

const user = useUserStore()

let items = ref([])
</script>

<template>
  <div class="flex flex-row justify-between">
    <div>
      <div class="text-3xl mb-10">YOUR ORDERS</div>
      <div v-if="items?.length">
        <CartItem v-for="item in items" :key="item.id" :item="item"></CartItem>
      </div>
      <div v-else class="mt-10 flex flex-row">
        <div class="text-xl">YOU DONT HAVE ANY COMPLETED ORDERS! &nbsp;</div>
        <RouterLink class="text-xl" to="/"> GO TO SHOPPING!</RouterLink>
      </div>
    </div>
    <div class="flex flex-col justify-between p-6 border-2 border-black w-96 h-72">
      <div class="flex flex-col justify-between">
        <div class="text-2xl font-semibold rounded-lg text-center mt-1 mb-4">Your Profile</div>
        <hr />
        <div class="text-xl bg-blue-300 rounded-lg text-center mt-2">
          First Name: {{ user.firstName }}
        </div>
        <div class="text-xl bg-blue-300 rounded-lg text-center mt-2">
          Last Name: {{ user.lastName }}
        </div>
        <hr />
        <div class="text-xl bg-blue-300 rounded-lg text-center mt-2">
          UserName: {{ user.username }}
        </div>
        <div class="text-xl bg-blue-300 rounded-lg text-center mt-2">Email: {{ user.email }}</div>
      </div>
      <hr />
    </div>
  </div>
</template>
