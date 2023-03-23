import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'
import messages from '@intlify/unplugin-vue-i18n/messages'

import App from './App.vue'

import './assets/main.css'

// Vuetify
import { createVuetify } from 'vuetify'

const app = createApp(App)

app.use(createPinia())

const vuetify = createVuetify({
  theme: { defaultTheme: 'dark' }
})

app.use(vuetify)

app.use(
  createI18n({
    locale: 'en',
    messages
  })
)

app.mount('#inject-dashboard-help')
