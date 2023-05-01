import { api } from '../../axios/instance/api'

export const fetchGames = async () => {
  return api.get('api/game')
}

export const fetchGame = (id: string) => {
  return api.get(`api/game/${id}`)
}

export const fetchReviews = (id: string) => {
  return api.get(`api/review?game__id=${id}`)
}
