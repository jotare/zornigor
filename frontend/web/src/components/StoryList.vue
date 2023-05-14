<template>
    <div class="container">
        <ul class="columns is-mobile">
            <li
                class="column border"
                v-for="state in project.states" :key="state.id"
            >
                <h3 class="subtitle has-text-weight-semibold">{{ state.name }}</h3>
                <!-- <p>{{ state.description }}</p> -->

                <hr class="border" />

                <ul>
                    <li v-for="story in state.stories" :key="story.id">
                        <StoryItem :story="story"/>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</template>

<script>
 import StoryItem from "./StoryItem.vue"

 export default {
     name: "StoryList",

     props: ["project"],

     components: {
         StoryItem,
     },

     computed: {
         states() {
             return this.project.states || [];
         },

         stories() {
             return this.project.stories || [];
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
