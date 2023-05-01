<script setup lang="ts">
import { useRouter } from 'vue-router'

defineProps({
  item: {
    type: Object,
    default: () => ({})
  }
})
</script>

<template>
  <div class="flex flex-col text-gray-500 w-1/2">
    <div class="text-md">{{ item.user }}</div>
    <div class="mt-1">Rating: {{ item.rating }}</div>
    <div class="mt-1">Date: {{ item.created_at }}</div>
    <div class="mt-3">
      {{ item.comment }}
    </div>
    <hr />
  </div>
</template>
