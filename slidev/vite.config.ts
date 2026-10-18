import { defineConfig } from 'vite'

// Node/Vite here resolve "localhost" to IPv6 (::1) only, so the dev server
// was unreachable at http://127.0.0.1:3030 even though ::1/[localhost] worked.
// Binding explicitly fixes that.
export default defineConfig({
  server: {
    host: '0.0.0.0',
  },
})
