<script setup lang="ts">
import { useRouter } from 'vue-router'
import boardGame from '../assets/board-games.png'

const router = useRouter()
const props = defineProps({
  item: {
    type: Object,
    default: () => ({})
  }
})

function goToSingleItemPage() {
  router.push({ name: 'singleGamePage', params: { id: props.item.id } })
}
</script>

<template>
  <div
    class="flex flex-col p-4 w-60 h-auto border-2 border-gray-400 cursor-pointer"
    @click="goToSingleItemPage"
  >
    <div class="w-52 h-36 border-2 border-b-gray-400">
      <img :src="item.image ?? boardGame" alt="item_img.png" class="max-h-full" />
    </div>
    <div class="flex flex-row justify-between">
      <div class="mt-2 text-lg">{{ item.name }}</div>
      <div class="mt-3 bg-red-400 w-24 text-white h-6 rounded-md text-center">
        {{ item.category }}
      </div>
    </div>
    <div class="mt-2">
      <div>Rating {{ item.rating }}</div>
      <div>{{ item.num_of_reviews }} reviews</div>
    </div>
    <div class="flex flex-row justify-between">
      <div class="mt-2 text-xl">{{ item.price }}$</div>
      <div class="mt-3 bg-gray-500 w-24 text-white rounded-md text-center">
        {{ item.count_in_stock > 0 ? item.count_in_stock : 0 }} in stock
      </div>
    </div>
  </div>
</template>
