import { api } from '../../axios/instance/api'

export const fetchGames = async (params: object) => {
  return api.get('api/game', { params })
}

export const addGame = async (data) => {
  return api.post('api/game', data)
}

export const patchGame = async (gameId, data) => {
  return api.patch(`api/game/${gameId}`, data)
}

export const deleteGame = async (gameId) => {
  return api.delete(`api/game/${gameId}`)
}

export const fetchCategories = async () => {
  return api.get('api/category')
}

export const fetchBrands = async () => {
  return api.get('api/brand')
}

export const fetchGame = (id: string) => {
  return api.get(`api/game/${id}`)
}

export const fetchReviews = (id: string) => {
  return api.get(`api/review?game__id=${id}`)
}

export const fetchAddress = (params: object) => {
  return api.get(`api/shipping-address`, { params })
}

export const createOrder = async (data) => {
  return api.post('api/order/create_order', data)
}

export const getOrdersHistory = async (params: object) => {
  return api.get('api/order', { params })
}

export const addReview = async (data) => {
  return api.post('api/review', data)
}

export const addAddress = async (data) => {
  return api.post('api/shipping-address', data)
}
