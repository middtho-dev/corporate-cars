export default {
  server: {
    proxy: {
      '/api': 'http://backend:8000'
    }
  }
}
