<script setup lang="ts">
import CartItem from '@/components/CartItem.vue'
import { onMounted, ref } from 'vue'
import { useUserStore } from '@/store/userStore'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { fetchAddress } from '../api/index'
import useStripe from './../components/stripe/useStripe.js'
import { watch } from 'vue'

const toast = useToast()

const user = useUserStore()
const router = useRouter()

const stripe = useStripe()

const checkout = () => {
  let checkoutItems = items.value.map((x) => {
    return { price: x.stripe_code, quantity: x.qty }
  })
  console.log(checkoutItems)
  stripe.checkout(checkoutItems)
}

let items = ref([])
let price = ref(1)
let discount = ref(0)

let addresses = ref({
  value: null,
  options: []
})

onMounted(async () => {
  let cart = localStorage.getItem('cart')
  items.value = JSON.parse(cart)
  if (items?.value?.length) {
    calculatePrice()
  }
  await getAddress()
})

watch(
  () => items.value,
  () => {
    calculatePrice()
  },
  { deep: true }
)

const getAddress = async () => {
  const { data, error } = await fetchAddress()

  if (error) {
    return
  }

  let results = data.results.map((x) => {
    return { text: `${x.address} | ${x.city} | ${x.country}`, value: x.id }
  })

  addresses.value.options = results
  addresses.value.value = results[0]

  console.log(data)
}

const deleteItem = (id: string) => {
  items.value = items.value.filter((x) => x.id !== id)
  localStorage.setItem('cart', JSON.stringify(items.value))
  toast.info('Item deleted from cart!', {
    timeout: 2000
  })
}

const calculatePrice = () => {
  let test = 0
  if (items?.value?.length) {
    items.value.forEach((x) => {
      test = test + parseInt(x.price)
    })
    price.value = test
  }
}

const goToLogIn = () => {
  router.push({ name: 'login' })
}
</script>

<template>
  <div class="flex flex-row justify-between">
    <div>
      <div class="text-3xl mb-10">YOUR CART</div>
      <div v-if="items?.length">
        <CartItem
          v-for="item in items"
          :key="item.id"
          :item="item"
          @delete-from-cart="deleteItem"
        ></CartItem>
      </div>
      <div v-else class="mt-10 flex flex-row">
        <div class="text-xl">YOUR CART IS EMPTY! &nbsp;</div>
        <RouterLink class="text-xl" to="/"> CLICK HERE TO ADD SOMETHING!</RouterLink>
      </div>
    </div>
    <div class="flex flex-col justify-between p-6 border-2 border-black w-96">
      <div class="flex flex-col justify-between">
        <div class="text-xl font-semibold bg-blue-300 rounded-lg text-center mt-1 mb-2">
          Number of items: {{ items?.length ?? 0 }}
        </div>
        <hr />
        <div class="text-xl bg-blue-300 rounded-lg text-center mt-1">
          Initial Price: ${{ price }}
        </div>
        <div class="text-xl bg-blue-300 rounded-lg text-center mt-1">Discount: ${{ discount }}</div>
        <hr />
        <div class="text-xl font-semibold bg-blue-300 rounded-lg text-center mt-2">
          Final Sum: ${{ price - discount }}
        </div>
      </div>
      <div class="flex flex-col justify-between">
        <div>Select Address:</div>
        <va-select v-model="addresses.value" :options="addresses.options" />
      </div>
      <hr />
      <div class="flex justify-center" v-if="user.isLoggedIn">
        <!-- <Checkout :disabled="!items?.length"></Checkout> -->
        <button
          :disabled="!items?.length"
          class="rounded-lg bg-blue-700 text-white p-2 disabled:opacity-70"
          @click="checkout"
        >
          Go to checkout
        </button>
      </div>
      <div class="flex justify-center" v-else>
        <button type="button" class="rounded-lg bg-gray-500 p-2" @click="goToLogIn()">
          Login to continue
        </button>
      </div>
    </div>
  </div>
</template>
