<template>

    <div class="container is-fluid pt-5">

        <div class="field has-text-left">
            <label class="label">Project name:</label>
            <div class="control">
                <input class="input is-primary" v-model="name" type="text" placeholder="How you are going to name it?">
            </div>
            <p class="help is-info">Project slug will be: {{ slug }}</p>
        </div>

        <div class="field has-text-left">
            <label class="label">Description:</label>
            <div class="control">
                <textarea class="textarea is-primary" v-model="description" placeholder="What is the project going to be about?"></textarea>
            </div>
        </div>

        <div class="field is-grouped">
            <div class="control">
                <button class="button is-link" @click="create_project">Create project</button>
            </div>
            <div class="control">
                <button class="button is-link is-light" @click="$router.back()">Cancel</button>
            </div>
        </div>

        <div v-if="error" class="field has-text-left">
            <p class="has-text-danger">An error ocurred, please try again later</p>
        </div>

    </div>

</template>

<script>

 import { create_project as api_create_project } from "@/api/projects"
 import { slugify } from "@/utils"


 export default {
     name: "ProjectCreate",

     data() {
         return {
             name: "",
             description: "",

             error: null,
         }
     },

     computed: {
         slug() {
             return slugify(this.name)
         },
     },

     methods: {
         create_project() {
             console.log("Creating project");
             const payload = {
                 slug: this.slug,
                 name: this.name,
                 description: this.description,
             };
             api_create_project(payload)
                 .then(() => {
                     this.$router.push({
                         name: "project",
                         params: {
                             id: this.slug,
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
