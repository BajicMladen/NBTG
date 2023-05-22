<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { StripeCheckout } from '@vue-stripe/vue-stripe'

const props = defineProps({
  disabled: {
    type: Boolean,
    required: false
  }
})

const publishableKey = ref(
  'pk_test_51NAcJdEZXmWenCaRUfok9MaSdVYid5pPR1Qy5PiwOtUluOsi8uuMkRmtoAwPEHqi83DiUqAWlFgu28T34QEtnG8G00LRQM2CfR'
)
const checkoutRef = ref(null)
const successURL = ref('http://localhost:5173/game/9')
const cancelURL = ref('http://localhost:5173/')
let loading = ref(false)

let lineItems = ref([
  {
    price: 'price_1NAcYgEZXmWenCaRJKYPaP2z',
    quantity: 1
  },
  {
    price: 'price_1NAd2aEZXmWenCaRMHBNkQd6',
    quantity: 1
  }
])

const pay = () => {
  checkoutRef.value.redirectToCheckout()
}
</script>

<template>
  <div>
    <StripeCheckout
      ref="checkoutRef"
      mode="payment"
      :pk="publishableKey"
      :line-items="lineItems"
      :success-url="successURL"
      :cancel-url="cancelURL"
      @loading="(v) => (loading = v)"
    />
    <button
      :disabled="props.disabled"
      class="rounded-lg bg-blue-700 text-white p-2 disabled:opacity-70"
      @click="pay"
    >
      Pay now!
    </button>
  </div>
</template>
