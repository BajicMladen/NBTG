<script setup lang="ts">
import { onMounted } from 'vue'

onMounted(() => {
  localStorage.removeItem('cart')
})
</script>

<template>
  <div class="flex flex-col justify-center items-center">
    <div class="text-green-500 text-9xl mb-10">SUCCESS</div>
    <div class="text-2xl">Your order was processed successfully</div>
    <RouterLink class="text-xl underline mt-9" to="profile">Go to your order history!</RouterLink>
  </div>
</template>
