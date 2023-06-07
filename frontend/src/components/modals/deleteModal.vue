<script setup lang="ts">
import { ref } from 'vue'

let showDeleteModal = ref(false)
const emit = defineEmits(['deleteItem'])

const props = defineProps({
  itemId: {
    type: Number,
    default: 0
  }
})

const deleteItem = async () => {
  emit('deleteItem', props.itemId)
}
</script>

<template>
  <va-button
    preset="plain"
    icon="delete"
    class="ml-3"
    @click="showDeleteModal = !showDeleteModal"
  />
  <va-modal v-model="showDeleteModal">
    <template #content="{}">
      <va-card-title> Delete </va-card-title>
      <va-card-content> Are you sure you want to delete {{}} </va-card-content>
      <va-card-actions>
        <va-button color="primary" @click="deleteItem"> Yes </va-button>
        <va-button color="secondary" @click="showDeleteModal = !showDeleteModal">
          Cancel
        </va-button>
      </va-card-actions>
    </template>
  </va-modal>
</template>
