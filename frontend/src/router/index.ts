import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/Signup.vue')
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
    }
  ]
})

export default router
