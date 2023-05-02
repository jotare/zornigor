<template>
    <ProjectStories v-if="project" :project="project"/>
</template>

<script>
 import { use_projects_store } from "../stores/project"

 import ProjectStories from "./ProjectStories.vue"


 export default {
     name: "ProjectStoriesView",

     props: ["id"],

     components: {
         ProjectStories,
     },

     setup() {
         const stores = {
             projects: use_projects_store(),
         }

         return { stores }
     },

     data() {
         return {
             project: null
         }
     },

     created() {
         this.stores.projects.fetch_project(this.id);
         this.project = this.stores.projects.project_by_id(this.id);
     },

     watch: {
         "$route.params": {
             handler: function(value) {
                 this.project = this.stores.projects.project_by_id(value.id);
             },
             deep: true
         },
         "stores.projects.projects": {
             handler: function() {
                 this.project = this.stores.projects.project_by_id(this.id)
             },
             deep: true,
         },
     },
 }
</script>
