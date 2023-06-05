import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import { routes } from './js_components/router.js'
import App from "@/App.vue";
import './assets/main.css'

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App)
app.use(router)

app.mount('#app')
