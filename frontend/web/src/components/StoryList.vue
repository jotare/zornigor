<template>
    <div v-if="stories_error">
        {{ stories_error }}
    </div>

    <div v-else-if="states_error">
        {{ states_error }}
    </div>

    <div v-else class="container">
        <ul class="columns is-mobile">
            <li class="column" v-for="state in states" :key="state.id" style="border: 4px double green">
                <h3 class="subtitle has-text-weight-semibold">{{ state.name }}</h3>
                <!-- <p>{{ state.description }}</p> -->

                <hr style="border: 4px double green" />

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
 // import { mapState } from "pinia"
 import { use_stories_store } from "../stores/story"
 import { use_states_store } from "../stores/state"

 import StoryItem from "./StoryItem.vue"

 export default {
     name: "StoryList",

     props: ["project"],

     components: {
         StoryItem,
     },

     setup() {
         const stores = {
             stories: use_stories_store(),
             states: use_states_store(),
         }

         return { stores }
     },

     created() {
         this.stores.states.fetch_states(this.project.id);
         this.stores.stories.fetch_stories(this.project.id);
     },

     computed: {
         states() {
             return this.stores.states.states;
         },

         states_error() {
             return this.stores.states.error;
         },

         stories() {
             let stories = {}
             for (let state of this.states) {
                 for (let story of this.stores.stories.stories) {
                     if (story.state == state.id) {
                         if (stories[state.id] == null) {
                             stories[state.id] = [];
                         }
                         stories[state.id].push(story);
                     }
                 }
             }
             return stories;
         },

         stories_error() {
             return this.stores.stories.error;
         },
     },
 }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
</style>
