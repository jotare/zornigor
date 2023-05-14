<template>
    <div class="container pl-5 pr-5 is-flex is-justify-content-space-between">
        <h1 class="title">Projects</h1>

        <router-link class="button" :to="{ 'name': 'project_create' }">
            <p>
                <font-awesome-icon class="pr-1" icon="fa-solid fa-plus"></font-awesome-icon>
                New Project
            </p>
        </router-link>
    </div>

    <ul class="container border pb-5">
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

 import { use_projects_store } from "@/stores/projects"

 export default {
     name: "ProjectList",

     setup() {
         const store = use_projects_store();
         return { store }
     },

     created() {
         this.store.fetch_project_list();
     },

     computed: {
         projects() {
             return this.store.projects;
         },
     },
 }
</script>
