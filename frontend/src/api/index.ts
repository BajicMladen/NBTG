import { api } from '../../axios/instance/api'

export const fetchGames = async () => {
  return api.get('api/game')
}

export const fetchGame = (id) => {
  return api.get(`api/game/${id}`)
}
