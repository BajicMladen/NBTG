import { loadStripe } from '@stripe/stripe-js'

export default function useStripe() {
  const stripePromise = loadStripe(
    'pk_test_51NAcJdEZXmWenCaRUfok9MaSdVYid5pPR1Qy5PiwOtUluOsi8uuMkRmtoAwPEHqi83DiUqAWlFgu28T34QEtnG8G00LRQM2CfR'
  )
  const checkout = async (items) => {
    try {
      const stripe = await stripePromise
      const { error } = await stripe.redirectToCheckout({
        mode: 'payment',
        lineItems: [...items],
        successUrl: 'http://localhost:5173/success',
        cancelUrl: 'http://localhost:5173/cart'
      })

      if (error) {
        console.error(error)
      }
    } catch (error) {
      console.error(error)
    }
  }

  return {
    checkout
  }
}
