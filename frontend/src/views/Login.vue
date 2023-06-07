<script setup lang="ts">
import { ref } from 'vue'
import { logIn, getCurrentUser } from '@/api/auth'
import { useForm } from 'vuestic-ui'
import { RouterLink, useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { useUserStore } from '@/store/userStore'

const user = useUserStore()

const toast = useToast()
const router = useRouter()

let formData = ref({
  username: '',
  password: ''
})

const handleSubmit = async () => {
  const { data, error } = await logIn(formData.value)

  if (error) {
    toast.error('Something went wrong, please try again', {
      timeout: 2000
    })
    return
  }
  localStorage.setItem('tokens', JSON.stringify(data))

  await getUserData()

  router.push({ name: 'home' })
}

const getUserData = async () => {
  const { data, error } = await getCurrentUser()
  if (error) {
    toast.error('Something went wrong, please try again', {
      timeout: 2000
    })
    return
  }
  localStorage.setItem('userData', JSON.stringify(data))
  user.setUser({
    id: data.id,
    isAdmin: data.is_admin,
    image: data.image,
    firstName: data.first_name,
    lastName: data.last_name,
    email: data.email,
    username: data.username
  })
}

const { isValid, validate } = useForm('formRef')

let isPasswordVisible = ref(false)
</script>

<template>
  <div class="flex h-96 items-center justify-center">
    <va-form class="flex flex-col justify-center w-3/12 rounded-2xl" tag="form" ref="formRef">
      <div class="mb-8 mt-4 text-center font-semibold text-2xl">Log In</div>
      <va-input
        v-model="formData.username"
        label="Username"
        class="mb-6"
        :rules="[(v) => Boolean(v) || 'Username is required']"
      />

      <va-input
        v-model="formData.password"
        :type="isPasswordVisible ? 'text' : 'password'"
        label="Password"
        :rules="[
          (v) => Boolean(v) || 'Password is required',
          (v) => v.length > 6 || 'Password must be a least 6 symbols'
        ]"
      >
        <template #appendInner>
          <va-icon
            v-if="formData.password"
            :name="isPasswordVisible ? 'visibility_off' : 'visibility'"
            size="small"
            color="--va-primary"
            @click="isPasswordVisible = !isPasswordVisible"
          />
        </template>
      </va-input>
      <div class="flex flex-row mt-1">
        <div class="text-xs">You don't have and account?</div>
        <RouterLink to="/signup" class="text-xs ml-1 text-blue-500 underline">Signup</RouterLink>
      </div>

      <va-button class="mt-6" :disabled="!isValid" @click="validate() && handleSubmit()">
        Login
      </va-button>
    </va-form>
  </div>
</template>
