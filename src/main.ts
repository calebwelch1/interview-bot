import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import jQuery from "jquery";

import './assets/main.css'

const app = createApp(App)
app.use(router)
// window.$ = window.jQuery;
app.use(jQuery);

app.mount('#app')
