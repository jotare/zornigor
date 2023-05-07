<template>

    <template v-if="project == null">
        <div class="container load-spinner-container">
            <div class="loader is-active load-spinner" ></div>
        </div>
    </template>

    <template v-else>
        <h1 class="title">{{ project.name }}</h1>

        <hr style="border: 4px double red" />
        <StoryList :project="project"/>
        <hr style="border: 4px double red" />
    </template>

</template>

<script>
 import { use_projects_store } from "@/stores/projects"

 import StoryList from "@/components/StoryList.vue"

 export default {
     name: "ProjectView",

     components: {
         StoryList,
     },

     props: {
         id: {
             type: String,
             required: true,

             validator(value) {
                 return value != null && value.length > 0;
             },
         }
     },

     setup() {
         const store = use_projects_store();
         return { store };
     },

     data() {
         return {
             project: null,
         }
     },

     watch: {
         "$route.params": {
             handler: function(value) {
                 // async fetch
                 this.fetch_project(value.id);
             },
             deep: true,
             immediate: true,
         },

         "store.projects": {
             handler: function() {
                 // update project when async fetch has finished
                 this.project = this.store.project(this.id)
             }
         }
     },

     methods: {
         fetch_project(project_id) {
             this.store.fetch_project(project_id);
             this.store.fetch_stories(project_id);
         },
     }
 }
</script>

<style scoped>
 .load-spinner-container {
     width: 150px;
     height: 150px;
 }

 .load-spinner{
     width: 100%;
     height: 100%;
 }

</style>
