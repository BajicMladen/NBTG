<script setup lang="ts">
import ItemCard from '@/components/ItemCard.vue'
import { onMounted, ref, watch } from 'vue'
import { fetchGames } from '../api/index'
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination as Pag, Navigation } from 'vue3-carousel'
import boardGame from '../assets/board-games.png'
import { debounce } from 'lodash'

let games = ref([])
let search = ref('')
let currentPage = ref(1)
let pages = ref()

let curoselData = ref([])

async function getGames(params: object = {}) {
  const data = await fetchGames(params)
  pages.value = Math.floor(data.data.count / 5)
  games.value = data.data.results
}

watch(
  search,
  debounce(() => {
    console.log(search.value)
    getGames({ search: search.value })
  }, 500)
)

watch(currentPage, () => {
  getGames({ page: currentPage.value })
})

onMounted(async () => {
  await getGames()
  curoselData.value = games.value
})
</script>

<template>
  <div class="mt-2">
    <carousel :items-to-show="5">
      <slide v-for="game in curoselData" class="flex flex-col" :key="games.id">
        <img :src="game.image ?? boardGame" class="w-52 h-40" alt="game_image.png" />
        <div class="text-lg text-black">{{ game.name }}</div>
      </slide>
      <template #addons>
        <navigation />
        <Pag />
      </template>
    </carousel>
    <div class="flex flex-col mt-10">
      <div class="text-3xl mb-10">List of Games</div>
      <div class="flex flex-row">
        <div class="mr-3 text-xl">Search:</div>
        <input type="search" class="border-2 border-black mb-4 w-40 h-8" v-model="search" />
      </div>
      <div class="flex flex-row flex-wrap">
        <ItemCard v-for="game in games" :item="game" :key="game.id" class="mr-3 mb-3"></ItemCard>
      </div>
      <va-pagination v-model="currentPage" :pages="pages" :visible-pages="pages" />
    </div>
  </div>
</template>
