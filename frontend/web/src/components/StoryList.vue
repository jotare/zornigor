<template>
    <div class="stories">
        <h1>Stories</h1>
        <p v-if="stories_error">{{ stories_error }}</p>
        <ul>
            <li v-for="story in stories" :key="story.id">
                <!-- Item -->
                <h3>{{ story.title }}</h3>
                <p>{{ story.description }}</p>
            </li>
        </ul>
    </div>
</template>

<script>
 import { mapState } from "pinia"
 import { use_stories_store } from "../stores/story"

 export default {
     name: 'StoryList',

     setup() {
         const stories_store = use_stories_store();

         return { stories_store }
     },

     created() {
         this.stories_store.fetch_stories()
     },

     computed: {
         ...mapState(use_stories_store, ["stories"]),
         ...mapState(use_stories_store, {
             stories_error: "error",
         }),
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
