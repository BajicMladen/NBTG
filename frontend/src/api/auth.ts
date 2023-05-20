import { api } from '../../axios/instance/api'

export const signUp = async (data) => {
  return api.post('sign-in/', data)
}

export const logIn = async (data) => {
  return api.post('token/', data)
}

export const getCurrentUser = async () => {
  return api.get('api/user/current-user/')
}
