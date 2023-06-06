import { defineStore } from 'pinia'

export const useUserStore = defineStore('userStore', {
  state: () => ({
    isLoggedIn: false,
    id: null,
    firstName: '',
    lastName: '',
    username: '',
    email: ''
  }),
  actions: {
    setUser(data: UserInfo) {
      ;(this.isLoggedIn = true),
        (this.id = data.id),
        (this.firstName = data.firstName),
        (this.lastName = data.lastName),
        (this.username = data.username),
        (this.email = data.email)
    },
    resetUser() {
      ;(this.isLoggedIn = false),
        (this.id = null),
        (this.firstName = ''),
        (this.lastName = ''),
        (this.username = ''),
        (this.email = '')
    }
  }
})

interface UserInfo {
  isLoggedIn: boolean
  firstName: string
  lastName: string
  username: string
  email: string
}