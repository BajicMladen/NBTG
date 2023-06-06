<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { fetchGame, fetchReviews, addReview } from '../api/index'
import boardGame from '../assets/board-games.png'
import ReviewCard from '@/components/ReviewCard.vue'
import { useToast } from 'vue-toastification'
import { useUserStore } from '@/store/userStore'

const toast = useToast()

const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

const user = useUserStore()
let game = ref({})
let reviews = ref([])
let qty = ref(1)
let newReview = ref({
  rating: 0,
  title: '',
  comment: ''
})

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

const submitReview = async () => {
  const payload = {
    ...newReview.value,
    game: game.value.id,
    user: user.id
  }
  const { error } = await addReview(payload)

  if (error) {
    toast.error('Something went wrong when adding a review ', {
      timeout: 2000
    })
    return
  }

  getReviews(props.id)
}

function addItemToCart() {
  if (!validateQty()) {
    toast.info('Can not add more items than we there are in stock', {
      timeout: 2000
    })
    return
  }
  let cart = localStorage.getItem('cart')
  if (!cart) {
    localStorage.setItem('cart', JSON.stringify([]))
    cart = localStorage.getItem('cart')
  }
  let cart1 = JSON.parse(cart)
  let itemAlreadyExist = false

  const cart2 = cart1.map((x) => {
    if (x.id == game.value.id) {
      x.qty = x.qty + qty.value
      itemAlreadyExist = true
    }
    return x
  })

  if (itemAlreadyExist) {
    localStorage.setItem('cart', JSON.stringify(cart2))
  } else {
    localStorage.setItem('cart', JSON.stringify([...cart1, { qty: qty.value, ...game.value }]))
  }
  toast.success('Item added to cart!', {
    timeout: 2000
  })
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
          <div>{{ game.price * qty }}$</div>
        </div>
        <div class="flex flex-row justify-between mt-8">
          <div>Status:</div>
          <div>{{ game.count_in_stock > 0 ? 'In Stock' : 'Out of Stock' }}</div>
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
          <button class="w-40 bg-blue-700 text-white rounded-lg p-1 text-md" @click="addItemToCart">
            Add To Cart
          </button>
        </div>
      </div>
    </div>
    <div class="flex flex-row w-full">
      <div class="mt-10 w-5/6">
        <div class="text-3xl">REVIEWS</div>
        <div v-if="reviews?.length > 0">
          <ReviewCard :reviews="reviews" class="mt-6"></ReviewCard>
        </div>
        <div class="text-lg" v-else>No Reviews for this game!</div>
      </div>
      <div class="flex flex-col mt-10 w-1/2 h-1/4" v-if="user.isLoggedIn">
        <div class="text-2xl mb-3">Add comment</div>
        <div class="flex">
          <va-input v-model="newReview.title" class="mr-9" label="Title" placeholder="Add Title" />
          <va-input
            v-model="newReview.rating"
            label="Rating 0-100"
            type="number"
            placeholder="Add Rating"
          />
        </div>
        <va-input
          v-model="newReview.comment"
          class="w-full mt-6"
          type="textarea"
          label="Comment"
          placeholder="Add Comment"
          autosize
        />
        <va-button
          class="w-1/3 mt-2"
          @click="submitReview"
          :disabled="newReview.comment.length < 1 || newReview.title.length < 1"
        >
          Submit
        </va-button>
      </div>
    </div>
  </div>
</template>
