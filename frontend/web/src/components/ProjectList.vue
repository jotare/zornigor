<template>
    <h1 class="title">Project List:</h1>

    <ul class="container">
        <li class="box" v-for="project in projects" :key="project.id">
            <router-link
                style="text-decoration: none; color: inherit;"
                :to="{ name: 'project', params: { id: project.id } }"
            >
                <h4 class="subtitle">{{ project.name }}</h4>
                <p>{{ project.description }}</p>
            </router-link>
        </li>
    </ul>
</template>

<script>

 import { use_projects_store } from "../stores/project"

 export default {
     name: "ProjectList",

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
         projects() {
             return this.stores.projects.projects;
         },
     },
 }
</script>
