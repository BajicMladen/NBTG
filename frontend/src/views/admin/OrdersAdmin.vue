<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { getOrdersHistory } from '../../api/index'

let items = ref([])
let columns = [
  { key: 'id' },
  { key: 'user_name' },
  { key: 'created_at' },
  { key: 'total_price' },
  { key: 'payment_method' },
  { key: 'paid' },
  { key: 'delivered' },
  { key: 'details', width: 80 }
]

async function getOrders() {
  const data = await getOrdersHistory()
  items.value = data.data.results
}

onMounted(async () => {
  await getOrders()
})
</script>

<template>
  <div class="flex flex-row justify-between">
    <div class="w-full">
      <div class="text-3xl mb-10">All Orders</div>
      <va-data-table :items="items" :columns="columns">
        <template #cell(details)="{ row, isExpanded }">
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
                  <span class="va-link">{{ item.game.category_name }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="branding_watermark" color="secondary" class="mr-2" />
                  <span class="va-link">Brand:&nbsp</span>
                  <span class="va-link">{{ item.game.brand_name }}</span>
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
  </div>
</template>
