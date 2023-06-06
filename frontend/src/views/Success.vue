<script setup lang="ts">
import { onMounted } from 'vue'
import { createOrder } from '../api/index'

onMounted(async () => {
  const checkoutAddress = JSON.parse(localStorage.getItem('checkoutAddress'))
  const items = JSON.parse(localStorage.getItem('cart'))
  if (items && checkoutAddress) {
    let price = items.reduce((acc, obj) => {
      return acc + parseInt(obj.price)
    }, 0)
    await createOrder({ address: checkoutAddress.value, price: price, items: [...items] })
  }

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
