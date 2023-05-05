import { createPinia } from "pinia"
import { createApp } from "vue";

import App from "./App.vue";
import router from "./router"
import setup_icons from "./icons"


const app = createApp(App);
setup_icons(app);
app.use(createPinia());
app.use(router);
app.mount("#app");
