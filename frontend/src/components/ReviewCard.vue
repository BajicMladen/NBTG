<script setup lang="ts">
defineProps({
  reviews: {
    type: Object,
    default: () => []
  }
})
</script>

<template>
  <va-list>
    <va-list-item v-for="(review, index) in reviews" :key="index" class="list__item mb-8">
      <va-list-item-section avatar>
        <va-avatar>
          <img :src="`http://127.0.0.1:8000${review?.user_image}`" />
        </va-avatar>
      </va-list-item-section>

      <va-list-item-section>
        <div class="flex flex-row">
          <va-list-item-label>{{ review.user_name }} </va-list-item-label>
          <va-list-item-label class="ml-5">
            {{ review.created_at }}
          </va-list-item-label>
          <va-list-item-label class="ml-5"> Rating: {{ review.rating }} </va-list-item-label>
        </div>

        <va-list-item-label caption :lines="index + 1" class="text-lg">
          {{ review.title }}
        </va-list-item-label>

        <va-list-item-label caption :lines="index + 1">
          {{ review.comment }}
        </va-list-item-label>
      </va-list-item-section>
    </va-list-item>
  </va-list>
</template>
