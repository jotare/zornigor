<template>
    <div v-if="error">
        {{ error }}
    </div>

    <div v-else class="container">
        <ul class="columns is-mobile">
            <li
                class="column border"
                v-for="state in states" :key="state.id"
            >
                <h3 class="subtitle has-text-weight-semibold">{{ state.name }}</h3>
                <!-- <p>{{ state.description }}</p> -->

                <hr class="border" />

                <ul>
                    <li v-for="story in stories[state.id]" :key="story.id">
                        <StoryItem :story="story"/>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</template>

<script>
 import { use_projects_store } from "@/stores/projects"

 import StoryItem from "./StoryItem.vue"

 export default {
     name: "StoryList",

     props: ["project"],

     components: {
         StoryItem,
     },

     setup() {
         const store = use_projects_store();
         return { store }
     },

     created() {
         this.store.fetch_states(this.project.id);
         this.store.fetch_stories(this.project.id);
     },

     watch: {
         project(value) {
             this.store.fetch_states(value.id);
             this.store.fetch_stories(value.id);
         },
     },

     computed: {
         states() {
             return this.store.states(this.project.id);
         },

         stories() {
             return this.store.stories_by_state(this.project.id);
         },

         error() {
             return this.store.error;
         },
     },
 }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
 @import "~bulma/bulma.sass";

 h3 {
     margin: 40px 0 0;
 }
 ul {
     list-style-type: none;
     padding: 0;
 }
 li {
     display: inline-block;
     margin: 0 10px;
 }
 a {
     color: #42b983;
 }

 .border {
    border: 4px double $info;
 }
</style>
