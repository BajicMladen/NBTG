import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/store/userStore'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
      beforeEnter: (to, from) => {
        const user = useUserStore()
        if (user.isLoggedIn) return from
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/Signup.vue'),
      beforeEnter: (to, from) => {
        const user = useUserStore()
        if (user.isLoggedIn) return from
      }
    },
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/game/:id',
      name: 'singleGamePage',
      component: () => import('../views/SingleGameView.vue'),
      props: true
    },
    {
      path: '/cart',
      name: 'cart',
      component: () => import('../views/Cart.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/Profile.vue'),
      beforeEnter: (to, from) => {
        const user = useUserStore()
        if (!user.isLoggedIn) return from
      }
    },
    {
      path: '/success',
      name: 'success',
      component: () => import('../views/Success.vue'),
      beforeEnter: (to, from) => {
        const user = useUserStore()
        if (!user.isLoggedIn) return from
      }
    }
  ]
})

export default router
