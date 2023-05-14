<template>
    <NavBar/>

    <main class="pt-4 container">
        <ErrorView v-if="error" :error="error"/>
        <router-view v-else></router-view>
    </main>

</template>

<script>

 import { use_projects_store } from "@/stores/projects"

 import NavBar from "@/components/NavBar.vue"
 import ErrorView from "@/components/ErrorView.vue"

 export default {
     name: "App",

     setup() {
         const store = use_projects_store();
         return { store };
     },

     components: {
         NavBar,
         ErrorView,
     },

     computed: {
         error() {
             return this.store.error;
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
