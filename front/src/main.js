import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import { routes } from './js_components/router.js'
import App from "@/App.vue";
import './assets/main.css'

const api_link = "http://2.4.115.102:8000";

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App)
app.use(router)

app.mount('#app')
