<script setup lang="ts">
import ItemCard from '@/components/ItemCard.vue'
import { reactive, onMounted, ref } from 'vue'
import { fetchGames } from '../api/index'

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
  <div class="px-24">
    <div class="mb-5">Curosel</div>
    <div class="flex flex-col justify-center items-center">
      <div class="text-3xl mb-10">List of Games</div>
      <div class="flex flex-row flex-wrap">
        <ItemCard
          v-for="game in games"
          :item="game"
          v-bind:key="game.id"
          class="mr-5 mb-4"
        ></ItemCard>
      </div>
    </div>
  </div>
</template>
