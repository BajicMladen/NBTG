<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { fetchGame } from '../api/index'
import boardGame from '../assets/board-games.png'

const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

let game = ref([])

async function getGames(id: string) {
  const data = await fetchGame(id)
  game.value = data.data
}

onMounted(() => {
  getGames(props.id)
})

const test =
  'Description: The ultimate home entertainment center starts with PlayStation. Whether you are into gaming, HD movies, television, music'
</script>

<template>
  <div class="mt-5">
    <div class="flex flex-row">
      <div class="max-w-lg max-h-96">
        <img :src="game.image ?? boardGame" alt="game_image.png" class="max-h-full" />
      </div>
      <div class="flex flex-col ml-8">
        <div class="text-3xl mb-4">{{ game.name }}</div>
        <hr />
        <div class="mt-2 text-xl">Reviews: {{ game.num_of_reviews }}</div>
        <hr />
        <div class="mt-2 text-2xl">Price: {{ game.price }}$</div>
        <hr />
        <div class="mt-2 text-md">{{ test }}</div>
      </div>
    </div>
  </div>
</template>
