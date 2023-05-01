<script setup lang="ts">
import { ref, onMounted } from 'vue'
import boardGame from '../assets/board-games.png'
import deleteIcon from '../assets/delete-icon.png'

let qty = ref(1)

const props = defineProps({
  item: {
    type: Object,
    default: () => ({})
  }
})

onMounted(() => {
  console.log(props.item.qty)
  qty.value = props.item.qty
})
</script>

<template>
  <div class="flex flex-row items-center mt-5 mb-1">
    <img :src="item.image ?? boardGame" alt="cart_item.jpg" class="h-20 w-28 mr-10" />
    <div class="text-lg w-28 mr-10">{{ item.name }}</div>
    <div class="text-lg w-20 mr-10">{{ item.price }}$</div>
    <input
      type="number"
      id="qty"
      min="0"
      :max="item.count_in_stock"
      v-model="qty"
      class="w-20 mr-10 text-center border-2 border-black"
    />
    <div class="text-lg w-20 mr-10">{{ item.price * qty }}$</div>
    <img
      :src="deleteIcon"
      alt="cart_item.jpg"
      class="h-4"
      @click="$emit('deleteFromCart', item.id)"
    />
  </div>
  <hr />
</template>
