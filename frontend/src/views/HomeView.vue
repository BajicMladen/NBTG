<script setup lang="ts">
import ItemCard from '@/components/ItemCard.vue'
import { onMounted, ref } from 'vue'
import { fetchGames } from '../api/index'
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import boardGame from '../assets/board-games.png'

let games = ref([])

async function getGames() {
  const data = await fetchGames()
  games.value = data.data.results
}

onMounted(() => {
  getGames()
})
</script>

<template>
  <div class="mt-2">
    <carousel :items-to-show="5">
      <slide v-for="game in games" class="flex flex-col" :key="games.id">
        <img :src="game.image ?? boardGame" class="w-52 h-40" alt="game_image.png" />
        <div class="text-lg text-black">{{ game.name }}</div>
      </slide>
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
    <div class="flex flex-col justify-center items-center mt-10">
      <div class="text-3xl mb-10">List of Games</div>
      <div class="flex flex-row flex-wrap">
        <ItemCard v-for="game in games" :item="game" :key="game.id" class="mr-5 mb-4"></ItemCard>
      </div>
    </div>
  </div>
</template>
