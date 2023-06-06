import { api } from '../../axios/instance/api'

export const fetchGames = async (params) => {
  return api.get('api/game', { params })
}

export const fetchGame = (id: string) => {
  return api.get(`api/game/${id}`)
}

export const fetchReviews = (id: string) => {
  return api.get(`api/review?game__id=${id}`)
}

export const fetchAddress = () => {
  return api.get('api/shipping-address')
}

export const createOrder = async (data) => {
  return api.post('api/order/create_order', data)
}

export const getOrdersHistory = async () => {
  return api.get('api/order')
}

export const addReview = async (data) => {
  return api.post('api/review', data)
}

export const addAddress = async (data) => {
  return api.post('api/shipping-address', data)
}
