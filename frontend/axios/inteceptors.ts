export const useTokenInterceptors = (instance) => {
  instance.interceptors.request.use(
    async (config) => {
      const tokens = JSON.parse(localStorage.getItem('tokens'))
      if (tokens) {
        config.headers.Authorization = `Bearer ${tokens.access}`
      }
      return config
    },
    (error) => Promise.reject(error)
  )
}
