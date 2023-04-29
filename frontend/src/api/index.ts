import { api } from '../../axios/instance/api'

export const fetchGames = async () => {
  return api.get('api/game')
}
