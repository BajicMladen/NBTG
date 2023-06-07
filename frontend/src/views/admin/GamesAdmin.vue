<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { useUserStore } from '@/store/userStore'
import {
  fetchGames,
  fetchCategories,
  fetchBrands,
  addGame,
  patchGame,
  deleteGame
} from '../../api/index'
import { useToast } from 'vue-toastification'
import { debounce, cloneDeep } from 'lodash'
import deleteModal from '@/components/modals/deleteModal.vue'

const toast = useToast()

const user = useUserStore()
let items = ref([])
let pages = ref()
let currentPage = ref(1)
let search = ref('')

let editingGame = ref({
  editing: false,
  game: null
})

let game = ref({
  name: '',
  min_age: 0,
  description: '',
  rating: 0,
  count_in_stock: 0,
  price: 0,
  stripe_code: '',
  image: []
})

let categories = ref({
  value: null,
  options: []
})

let brands = ref({
  value: null,
  options: []
})

let columns = [
  { key: 'id' },
  { key: 'name' },
  { key: 'created_at' },
  { key: 'count_in_stock' },
  { key: 'price' },
  { key: 'rating' },
  { key: 'actions', width: 80 },
  { key: 'more_info', width: 80 }
]

watch(currentPage, () => {
  getGames({ page: currentPage.value })
})

watch(
  search,
  debounce(() => {
    console.log(search.value)
    getGames({ search: search.value })
  }, 500)
)

async function getGames(params: object = {}) {
  const data = await fetchGames(params)
  pages.value = Math.floor(data.data.count / 5)
  items.value = data.data.results
}

const getCategories = async () => {
  const { data, error } = await fetchCategories()

  if (error) {
    return
  }

  let results = data.results.map((x) => {
    return { text: x.name, value: x.id }
  })

  categories.value.options = results
  categories.value.value = results[0]
}

const getBrands = async () => {
  const { data, error } = await fetchBrands()

  if (error) {
    return
  }

  let results = data.results.map((x) => {
    return { text: x.name, value: x.id }
  })

  brands.value.options = results
  brands.value.value = results[0]
}

const addNewGame = async () => {
  const payload = {
    category: categories.value.value.value,
    brand: brands.value.value.value,
    user: user.id,
    ...game.value,
    image: game.value.image[0]
  }

  console.log(payload)

  const { error } = await addGame(payload)

  if (error) {
    toast.error('Something went wrong when adding new address.', {
      timeout: 2000
    })
    return
  }

  toast.success('New Game Added.', {
    timeout: 2000
  })
  await getGames()
}

const removeGame = async (id) => {
  const { error } = await deleteGame(id)

  if (error) {
    toast.error('Something went wrong when deleting the game.', {
      timeout: 2000
    })
    return
  }

  toast.success('Game Deleted', {
    timeout: 2000
  })
  await getGames({ page: currentPage.value })
}

const updateGame = async () => {
  const payload = {
    category: categories.value.value.value ?? undefined,
    brand: brands?.value?.value?.value ?? undefined,
    user: user.id,
    ...game.value,
    image:
      game?.value?.image && game?.value?.image[0] instanceof File
        ? game?.value?.image[0]
        : undefined
  }
  const { error } = await patchGame(editingGame.value.game, payload)

  if (error) {
    toast.error('Something went wrong when adding new address.', {
      timeout: 2000
    })
    return
  }

  toast.success('New Game Added.', {
    timeout: 2000
  })
  await getGames({ page: currentPage.value })
}

const resetDataToDefault = () => {
  game.value = {
    name: '',
    min_age: '',
    description: '',
    rating: 0,
    count_in_stock: 0,
    price: 0,
    stripe_code: '',
    image: []
  }
  editingGame.value.editing = false
  editingGame.value.game = null
}

const editGame = (id) => {
  let test = cloneDeep(items)
  const game1 = test.value.find((x) => x.id === id)
  game.value = {
    name: game1.name,
    min_age: game1.min_age,
    description: game1.description,
    rating: game1.rating,
    count_in_stock: game1.count_in_stock,
    price: game1.price,
    stripe_code: game1.stripe_code
  }
  let cats = cloneDeep(categories.value)
  categories.value.value = cats.options.find((x) => x.value === game1.category)

  let brns = cloneDeep(brands.value)
  brands.value.value = brns.options.find((x) => x.value === game1.brand)

  editingGame.value.editing = true
  editingGame.value.game = game1.id
}

onMounted(async () => {
  await getGames()
  await getCategories()
  await getBrands()
})
</script>

<template>
  <div class="flex flex-row justify-between">
    <div class="w-2/3">
      <div class="text-3xl mb-8">Games</div>
      <va-input v-model="search" placeholder="Search..." class="mb-1 w-1/3 mr-10" />
      <va-button @click="resetDataToDefault" class="self-end"> Add New </va-button>
      <va-data-table :items="items" :columns="columns" hoverable>
        <template #cell(actions)="{ rowData }">
          <va-button preset="plain" icon="edit" @click="editGame(rowData.id)" />
          <deleteModal @deleteItem="removeGame" :itemId="rowData.id"></deleteModal>
        </template>
        <template #cell(more_info)="{ row, isExpanded }">
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
          <div class="flex gap-1 mb-4 divide-y w-full">
            <va-avatar :src="rowData.image" />
            <div class="pl-2">
              <div class="flex">
                <div class="flex flex-row">
                  <va-icon size="small" name="sports_esports" color="secondary" class="mr-2 mt-1" />
                  <span class="va-link">Name:&nbsp</span>
                  <span class="va-link">{{ rowData.name }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="category" color="secondary" class="mr-2" />
                  <span class="va-link">Category:&nbsp</span>
                  <span class="va-link">{{ rowData.category_name }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="branding_watermark" color="secondary" class="mr-2" />
                  <span class="va-link">Brand:&nbsp</span>
                  <span class="va-link">{{ rowData.brand_name }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="star_half" color="secondary" class="mr-2" />
                  <span class="va-link">Rating:&nbsp</span>
                  <span class="va-link">{{ rowData.rating }}</span>
                </div>
              </div>
              <div class="flex">
                <div class="flex flex-row">
                  <va-icon size="small" name="payments" color="secondary" class="mr-2 mt-1" />
                  <span class="va-link">Price:&nbsp</span>
                  <span class="va-link">{{ rowData.price }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="numbers" color="secondary" class="mr-2" />
                  <span class="va-link">Quantity:&nbsp</span>
                  <span class="va-link">{{ rowData.count_in_stock }}</span>
                </div>
                <div class="ml-4">
                  <va-icon size="small" name="forum" color="secondary" class="mr-2" />
                  <span class="va-link">No. of reviews:&nbsp</span>
                  <span class="va-link">{{ rowData.num_of_reviews }}</span>
                </div>
              </div>
            </div>
          </div>
        </template>
        <template #bodyAppend>
          <tr>
            <td colspan="6">
              <div class="flex justify-center mt-4">
                <va-pagination v-model="currentPage" :pages="pages" :visible-pages="pages" />
              </div>
            </td>
          </tr>
        </template>
      </va-data-table>
    </div>
    <div class="w-3/12">
      <va-form class="flex flex-col justify-center rounded-2xl" tag="form" ref="formRef">
        <div class="mb-6 text-center font-semibold text-2xl" v-if="!editingGame.editing">
          Add new game
        </div>
        <div class="mb-6 text-center font-semibold text-2xl" v-else>Update Game</div>
        <va-input
          v-model="game.name"
          label="Name"
          class="mb-4"
          :rules="[(v) => Boolean(v) || 'Name is required']"
        />
        <div class="flex flex-row">
          <va-input
            v-model="game.min_age"
            type="number"
            label="Min Age"
            class="mb-4"
            :rules="[(v) => Boolean(v) || 'Min Age is required']"
          />
          <va-input
            v-model="game.rating"
            type="number"
            label="Rating"
            class="mb-4 ml-2"
            :rules="[(v) => Boolean(v) || 'Rating is required']"
          />
          <va-input
            v-model="game.count_in_stock"
            type="number"
            label="In Stock"
            class="mb-4 ml-2"
            :rules="[(v) => Boolean(v) || 'Rating is required']"
          />
        </div>
        <va-select
          v-model="categories.value"
          :options="categories.options"
          class="mb-4"
          label="Category"
          prevent-overflow
        />
        <va-select
          v-model="brands.value"
          :options="brands.options"
          class="mb-4"
          label="Brand"
          prevent-overflow
        />
        <div class="flex flex-row">
          <va-input
            v-model="game.stripe_code"
            label="Stripe Code"
            class="mb-4"
            :rules="[(v) => Boolean(v) || 'Stripe Code is required']"
          />
          <va-input
            v-model="game.price"
            type="number"
            label="Price"
            class="mb-4 ml-2"
            :rules="[(v) => Boolean(v) || 'Price is required']"
          />
        </div>

        <va-input
          v-model="game.description"
          label="description"
          type="textarea"
          class="mb-4"
          :rules="[(v) => Boolean(v) || 'Description is required']"
          autosize
        />
        <va-file-upload v-model="game.image" type="gallery" file-types="image/*" class="" />
        <va-button @click="addNewGame" v-if="!editingGame.editing"> Create </va-button>
        <va-button @click="updateGame" v-else> Update </va-button>
      </va-form>
    </div>
  </div>
</template>
