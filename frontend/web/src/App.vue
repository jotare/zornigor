<template>
    <NavBar/>

    <main class="pt-4 container">
        <router-view></router-view>
    </main>
</template>

<script>
 import { use_projects_store } from "@/stores/project"

 import NavBar from "./components/NavBar.vue"

 export default {
     name: "App",

     components: {
         NavBar,
     },

     setup() {
         const stores = {
             projects: use_projects_store(),
         }

         return { stores }
     },

     created() {
         this.stores.projects.fetch_projects();
     },

     computed: {
         current_project() {
             return this.stores.projects.current_project;
         },
     },
 }
</script>

<style lang="scss">
 @import "~bulma/css/bulma.min.css";

 #app {
     font-family: Avenir, Helvetica, Arial, sans-serif;
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
     text-align: center;
     color: #2c3e50;
     margin-top: 60px;
 }
</style>
