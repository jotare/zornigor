<template>
    <div class="select">
        <select>
            <option v-for="project in projects" :key="project.slug"> {{ project.name }}</option>
        </select>
    </div>
</template>

<script>

 import { use_projects_store } from "@/stores/projects"


 export default {
     name: "ProjectSelector",

     setup() {
         const store = use_projects_store();
         return { store };
     },

     data() {
         return {
             is_active: false,
             selected_project: null,
             projects: [],
         }
     },

     created() {
         this.store.fetch_project_list()
             .then(() => {
                 this.projects = this.store.projects;
             })
     },

     computed: {
         selected_project_text() {
             if (this.selected_project == null) {
                 return "Select a project";
             }
             return this.selected_project;
         },
     },

     methods: {
         toggle() {
             console.log("Toggle")
             this.is_active = !this.is_active;
         },

         select_project(project) {
             this.selected_project = project;
         },
     },
 }

</script>
