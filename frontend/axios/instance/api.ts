import axios from 'axios'
import { NBTG_BASE_URL } from '../../src/environment'
import { useTokenInterceptors } from '../inteceptors'

const base = axios.create({
  baseURL: 'http://127.0.0.1:8000/'
})

useTokenInterceptors(base)

const AXIOS_METHODS = ['request', 'get', 'delete', 'head', 'options', 'post', 'put', 'patch']

const useResponse = (axiosFn, defaultData) => {
  const promise = axiosFn instanceof Promise ? axiosFn : axiosFn()

  return Promise.resolve(promise)
    .then((response) => {
      const data = response.data ?? defaultData ?? {}
      return { data, response, error: null }
    })
    .catch((error) => {
      return { data: defaultData ?? {}, response: {}, error }
    })
}

const api = AXIOS_METHODS.reduce((acc, axiosMethod) => {
  const fn = (...args) => useResponse(base[axiosMethod](...args))

  return { ...acc, ...{ [axiosMethod]: fn } }
}, {})

export { base, useResponse, api }
