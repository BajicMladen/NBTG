<script setup lang="ts">
import CartItem from '@/components/CartItem.vue'
import { onMounted, ref } from 'vue'

let items = ref([])

onMounted(() => {
  let cart = localStorage.getItem('cart')
  items.value = JSON.parse(cart)
})

function deleteItem(id: string) {
  items.value = items.value.filter((x) => x.id !== id)
  localStorage.setItem('cart', JSON.stringify(items.value))
}
</script>

<template>
  <div class="flex flex-row justify-between">
    <div>
      <div class="text-3xl">YOUR CART</div>
      <div>
        <CartItem
          v-for="item in items"
          :key="item.id"
          :item="item"
          @delete-from-cart="deleteItem"
        ></CartItem>
      </div>
    </div>
    <div class="flex flex-col justify-between p-6 border-2 border-black w-96 h-96">
      <div>
        <div class="text-2xl">Number of items: {{ items.length }}</div>
        <div class="mt-4 text-xl">Initial Price: $667</div>
        <div class="mt-4 text-xl">Discount: $667</div>
        <div class="mt-4 text-xl">Final Sum: $667</div>
      </div>
      <hr />
      <div class="flex justify-center">
        <button type="button" class="rounded-lg bg-gray-500 p-2">Proceed to checkout</button>
      </div>
    </div>
  </div>
</template>
