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
