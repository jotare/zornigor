<template>

    <template v-if="project == null">
        <div class="container load-spinner-container">
            <div class="loader is-active load-spinner" ></div>
        </div>
    </template>

    <template v-else>
    <div class="container pl-5 pr-5 is-flex is-justify-content-space-between">
        <h1 class="title">{{ project.name }}</h1>

        <router-link class="button" :to="{ 'name': 'story_create' }">
            <p>
                <font-awesome-icon class="pr-1" icon="fa-solid fa-plus"></font-awesome-icon>
                New Story
            </p>
        </router-link>
    </div>
    <!-- <h1 class="title">{{ project.name }}</h1> -->

        <hr style="border: 4px double red" />
        <StoryList :project="project" v-if="project != null"/>
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

     created() {
         this.$watch(
             () => this.$route.params,
             () => {
                 this.store.fetch_project(this.$route.params.id)
                     .then(() => {
                         this.store.select_project(this.$route.params.id);
                     })
             },
             { immediate: true }
         )
     },

     computed: {
         project() {
             return this.store.selected_project
         },
     },
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
