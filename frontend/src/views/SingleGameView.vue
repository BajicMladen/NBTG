<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { fetchGame, fetchReviews } from '../api/index'
import boardGame from '../assets/board-games.png'
import ReviewCard from '@/components/ReviewCard.vue'

const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

let game = ref({})
let reviews = ref([])
let qty = ref(1)

async function getGames(id: string) {
  const data = await fetchGame(id)
  game.value = data.data
}

async function getReviews(id: string) {
  const data = await fetchReviews(id)
  reviews.value = data.data.results
}

function validateQty() {
  return game.value.count_in_stock > qty.value && qty.value >= 0
}

function addItemToCart() {
  if (!validateQty()) {
    console.log('Can not order more than it is in stock')
    return
  }
  let cart = localStorage.getItem('cart')
  if (!cart) {
    localStorage.setItem('cart', JSON.stringify([]))
    cart = []
  }
  let cart1 = JSON.parse(cart)
  localStorage.setItem('cart', JSON.stringify([...cart1, { qty: qty.value, ...game.value }]))
}
onMounted(() => {
  getGames(props.id)
  getReviews(props.id)
})
</script>

<template>
  <div class="mt-5">
    <div class="flex flex-row justify-between">
      <img :src="game.image ?? boardGame" alt="game_image.png" class="h-[400px] w-[400px]" />
      <div class="flex flex-col mr-10 ml-10">
        <div class="text-3xl mb-4">{{ game.name }}</div>
        <div class="mt-2 text-xl">Reviews: {{ game.num_of_reviews }}</div>
        <div class="mt-2 text-2xl">Price: {{ game.price }}$</div>
        <div class="mt-2 text-md">{{ game.description }}</div>
      </div>
      <div class="border-2 border-black px-5 h-fit text-xl">
        <div class="flex flex-row justify-between mt-4 w-52">
          <div>Price:</div>
          <div>199$</div>
        </div>
        <div class="flex flex-row justify-between mt-8">
          <div>Status:</div>
          <div>In Stock</div>
        </div>
        <div class="flex flex-row justify-between mt-8">
          <div>Quantity:</div>
          <input
            type="number"
            id="qty"
            min="0"
            :max="game.count_in_stock"
            v-model="qty"
            class="w-20 border-2 border-black text-center"
          />
        </div>
        <div class="flex flex-row justify-center mt-10 mb-6">
          <button class="bg-slate-500 rounded-lg p-1" @click="addItemToCart">Add To Cart</button>
        </div>
      </div>
    </div>
    <div class="mt-10">
      <div class="text-3xl">REVIEWS</div>
      <div class="mt-10" v-if="reviews.length > 0">
        <ReviewCard
          v-for="review in reviews"
          :key="review.id"
          :item="review"
          class="mt-5"
        ></ReviewCard>
      </div>
      <div class="mt-10 text-lg" v-else>No Reviews for this game!</div>
    </div>
  </div>
</template>
