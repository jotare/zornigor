<template>

    <div class="container is-fluid pt-5">

        <div class="field has-text-left">
            <label class="label">Story title:</label>
            <div class="control">
                <input class="input is-primary" v-model="title" type="text" placeholder="How you are going to name it?">
            </div>
        </div>

        <div class="field has-text-left">
            <label class="label">Description:</label>
            <div class="control">
                <textarea class="textarea is-primary" v-model="description" placeholder="What is the project going to be about?"></textarea>
            </div>
        </div>

        <div class="field has-text-left">
            <label class="label">
                State:
            </label>
            <div class="control">
                <StateSelector :states="states" @selection="select_state"/>
            </div>
        </div>

        <div class="field is-grouped">
            <div class="control">
                <button class="button is-link" @click="create_story">Create story</button>
            </div>
            <div class="control">
                <button class="button is-link is-light" @click="$router.back()">Cancel</button>
            </div>
        </div>

        <div v-if="error" class="field has-text-left">
            <p class="has-text-danger">An error ocurred, please try again later</p>
            <p class="has-text-danger">Details:{{ error }}</p>
        </div>

    </div>

</template>

<script>

 import { create_story as api_create_story } from "@/api/stories"
 import { use_projects_store } from "@/stores/projects"

 import StateSelector from "@/components/StateSelector.vue"

 export default {
     name: "StoryCreate",

     components: {
         StateSelector,
     },

     setup() {
         const store = use_projects_store();
         return { store };
     },

     data() {
         return {
             title: "",
             description: "",
             state: "",

             error: null,
         }
     },

     computed: {
         selected_project() {
             return this.store.selected_project;
         },

         project_name() {
             if (this.store.selected_project == null) {
                 return "";
             }
             return this.store.selected_project.name;
         },

         states() {
             if (this.store.selected_project == null) {
                 return [];
             }
             return this.store.selected_project.states
         },
     },

     methods: {
         select_state(state) {
             this.state = state
         },

         create_story() {
             console.log("Creating story");
             const payload = {
                 title: this.title,
                 description: this.description,
                 state: this.state || this.selected_project.states[0].id,
             };
             api_create_story(this.store.selected_project.id, payload)
                 .then(() => {
                     this.$router.push({
                         name: "project",
                         params: {
                             id: this.selected_project.id,
                         }
                     })
                 })
                 .catch((error) => {
                     this.error = error.message;
                 });
         },
     },

 }

</script>
