// import { NBTG_API_URL, NBTG_BASE_URL } from '../../src/environment'
// import { baseControllers } from '@/axios/controllers.js'

// export const useTokenInterceptors = (instance) => {
//   instance.instance.request.use(async (config) => {
//     const url = new URL(config.url, config.baseURL).href

//     if (url.includes(NBTG_BASE_URL)) {
//       baseControllers[url] = new AbortController()
//       config.signal = baseControllers[url].signal

//     }
//   })
// }
