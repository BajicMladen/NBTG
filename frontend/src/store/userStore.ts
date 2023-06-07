import { defineStore } from 'pinia'

export const useUserStore = defineStore('userStore', {
  state: () => ({
    isLoggedIn: false,
    id: null,
    isAdmin: false,
    firstName: '',
    lastName: '',
    username: '',
    email: '',
    image: ''
  }),
  actions: {
    setUser(data: UserInfo) {
      ;(this.isLoggedIn = true),
        (this.id = data.id),
        (this.isAdmin = data.isAdmin),
        (this.image = data.image),
        (this.firstName = data.firstName),
        (this.lastName = data.lastName),
        (this.username = data.username),
        (this.email = data.email)
    },
    resetUser() {
      ;(this.isLoggedIn = false),
        (this.id = null),
        (this.isAdmin = false),
        (this.firstName = ''),
        (this.lastName = ''),
        (this.username = ''),
        (this.email = ''),
        (this.image = '')
    }
  }
})

interface UserInfo {
  id: number | null
  is_admin: boolean
  image: string
  isLoggedIn: boolean
  firstName: string
  lastName: string
  username: string
  email: string
}
