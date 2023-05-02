<template>
    <h1 class="title">{{ project.name }}</h1>

    <hr style="border: 4px double red" />
    <StoryList :project="project"/>
    <hr style="border: 4px double red" />
</template>

<script>
 import StoryList from "./StoryList.vue"

 export default {
     name: "ProjectStories",

     props: ["project"],

     components: {
         StoryList,
     },
 }
</script>
