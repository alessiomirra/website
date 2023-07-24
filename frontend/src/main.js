import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import store from './store' 

axios.defaults.baseURL = 'http://127.0.0.1:8000'

import '@/assets/bootstrap/bootstrap.min.css'
import '@/assets/bootstrap/bootstrap.min.js'


createApp(App).use(router).use(store).mount('#app')