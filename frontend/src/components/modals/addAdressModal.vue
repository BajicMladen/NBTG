<script setup lang="ts">
import { ref } from 'vue'
import { useForm } from 'vuestic-ui'
import { addAddress } from '../../api/index'
import { useToast } from 'vue-toastification'

const toast = useToast()

const { validate } = useForm('adressForm')

let showAddressModal = ref(false)
const emit = defineEmits(['newAddress'])

const props = defineProps({
  userId: {
    type: Number,
    default: 0
  }
})

let newAddress = ref({
  address: '',
  city: '',
  postal_code: '',
  country: ''
})

const saveNewAddress = async () => {
  if (validate()) {
    const { error } = await addAddress({ created_by: props.userId, ...newAddress.value })

    if (error) {
      toast.error('Something went wrong when adding new address.', {
        timeout: 2000
      })
    }
    toast.success('New shipping address added', {
      timeout: 2000
    })
    emit('newAddress')
    showAddressModal.value = false
  }
}
</script>

<template>
  <va-button @click="showAddressModal = !showAddressModal"> + </va-button>
  <va-modal v-model="showAddressModal">
    <template #content="{ saveAddress }">
      <va-card-title> Add Address </va-card-title>
      <va-card-content class="w-96">
        <va-form ref="adressForm" stateful class="mb-2 flex flex-col gap-2">
          <va-input
            v-model="newAddress.address"
            name="address"
            label="Address"
            :rules="[(v) => Boolean(v) || 'Address is required']"
          />
          <va-input
            v-model="newAddress.city"
            name="city"
            label="City"
            :rules="[(v) => Boolean(v) || 'City is required']"
          />
          <va-input
            v-model="newAddress.postal_code"
            name="postal_code"
            label="Postal Code"
            :rules="[(v) => Boolean(v) || 'Postal Code is required']"
          />
          <va-input
            v-model="newAddress.country"
            name="country"
            label="Country"
            :rules="[(v) => Boolean(v) || 'Country is required']"
          />
        </va-form>
      </va-card-content>
      <va-card-actions>
        <va-button color="primary" @click="saveNewAddress"> Save </va-button>
        <va-button color="secondary" @click="showAddressModal = !showAddressModal">
          Cancel
        </va-button>
      </va-card-actions>
    </template>
  </va-modal>
</template>
