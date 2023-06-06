<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useUserStore } from '@/store/userStore'
import { getOrdersHistory } from '../api/index'
import { updateProfile } from '../api/auth'
import { useToast } from 'vue-toastification'

const toast = useToast()

const user = useUserStore()
let items = ref([])
let profileChange = ref(false)

let password = ref({
  current: '',
  new: ''
})
let passwordChange = ref(false)

let columns = [
  { key: 'id' },
  { key: 'created_at' },
  { key: 'total_price' },
  { key: 'paid' },
  { key: 'delivered' },
  { key: 'actions', width: 80 }
]

async function getOrders() {
  const data = await getOrdersHistory()
  items.value = data.data.results
}

async function updatePassword() {}

async function updateProfileData() {
  const { data, error } = await updateProfile(user)

  if (error) {
    toast.error('Somethin went wrong, please try again.', {
      timeout: 2000
    })
    return
  }

  localStorage.setItem('userData', JSON.stringify(data))
  user.setUser({
    id: userData.id,
    firstName: data.first_name,
    lastName: data.last_name,
    email: data.email,
    username: data.username
  })

  toast.success('Information changed successively', {
    timeout: 2000
  })

  profileChange.value = false
}

onMounted(async () => {
  await getOrders()
})
</script>

<template>
  <div class="flex flex-row justify-between">
    <div class="w-2/3">
      <div class="text-3xl mb-10">Purchase History</div>
      <va-data-table :items="items" :columns="columns">
        <template #cell(actions)="{ row, isExpanded }">
          <va-button
            @click="row.toggleRowDetails()"
            :icon="isExpanded ? 'va-arrow-up' : 'va-arrow-down'"
            preset="secondary"
            class="w-full"
          >
            {{ isExpanded ? 'Hide' : 'More info' }}
          </va-button>
        </template>

        <template #expandableRow="{ rowData }">
          <div
            class="flex gap-1 mb-4 divide-y w-full"
            v-for="item in rowData.order_items"
            :key="item.id"
          >
            <va-avatar :src="`http://127.0.0.1:8000${item?.game.image}`" />
            <div class="pl-2">
              <div class="flex">
                <div class="flex flex-row">
                  <va-icon size="small" name="sports_esports" color="secondary" class="mr-2 mt-1" />
                  <span class="va-link">Name:&nbsp</span>
                  <span class="va-link">{{ item.game.name }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="category" color="secondary" class="mr-2" />
                  <span class="va-link">Category:&nbsp</span>
                  <span class="va-link">{{ item.game.category }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="branding_watermark" color="secondary" class="mr-2" />
                  <span class="va-link">Brand:&nbsp</span>
                  <span class="va-link">{{ item.game.brand }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="star_half" color="secondary" class="mr-2" />
                  <span class="va-link">Rating:&nbsp</span>
                  <span class="va-link">{{ item.game.rating }}</span>
                </div>
              </div>
              <div class="flex">
                <div class="flex flex-row">
                  <va-icon size="small" name="payments" color="secondary" class="mr-2 mt-1" />
                  <span class="va-link">Price:&nbsp</span>
                  <span class="va-link">{{ item.game.price }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="numbers" color="secondary" class="mr-2" />
                  <span class="va-link">Quantity:&nbsp</span>
                  <span class="va-link">{{ item.quantity }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="shopping_cart" color="secondary" class="mr-2" />
                  <span class="va-link">Total Price:&nbsp</span>
                  <span class="va-link">{{ item.price }}</span>
                </div>
              </div>
            </div>
          </div>
        </template>
      </va-data-table>
    </div>
    <div class="w-3/12">
      <va-form class="flex flex-col justify-center rounded-2xl" tag="form" ref="formRef">
        <div class="mb-6 text-center font-semibold text-2xl">Profile Information</div>
        <va-input
          v-model="user.firstName"
          label="First Name"
          class="mb-6"
          :disabled="!profileChange"
          :rules="[(v) => Boolean(v) || 'Username is required']"
        />
        <va-input
          v-model="user.lastName"
          label="Last Name"
          class="mb-6"
          :disabled="!profileChange"
          :rules="[(v) => Boolean(v) || 'Username is required']"
        />
        <va-input
          v-model="user.username"
          label="Username"
          class="mb-6"
          :disabled="!profileChange"
          :rules="[(v) => Boolean(v) || 'Username is required']"
        />
        <va-button class="" v-if="profileChange" @click="updateProfileData"> Save </va-button>
        <va-button class="" v-else @click="profileChange = true"> Change </va-button>
      </va-form>
      <va-form class="flex flex-col justify-center rounded-2xl mt-10" tag="form" ref="formRef">
        <div class="mb-6 text-center font-semibold text-2xl">Password</div>
        <va-input
          v-model="password.current"
          label="Current Password"
          class="mb-6"
          :disabled="!passwordChange"
          :rules="[
            (v) => Boolean(v) || 'Password is required',
            (v) => v.length > 6 || 'Password must be a least 6 symbols'
          ]"
        />
        <va-input
          v-model="password.new"
          label="New Password"
          class="mb-6"
          :disabled="!passwordChange"
          :rules="[
            (v) => Boolean(v) || 'Password is required',
            (v) => v.length > 6 || 'Password must be a least 6 symbols'
          ]"
        />
        <va-button class="" v-if="passwordChange" @click="updatePassword"> Save </va-button>
        <va-button class="" v-else @click="passwordChange = true"> Change </va-button>
      </va-form>
    </div>
  </div>
</template>
