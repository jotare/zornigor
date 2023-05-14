<template>
    <a class="box has-background-link-light" @click="open_modal" >
        <h3>{{ story.title }}</h3>
    </a>

    <div class="modal" :class="{ 'is-active': show_modal }">
        <div class="modal-background" @click="close_modal"></div>

        <div ref="detail-view" class="modal-content fullsize" tabindex="0" @keyup.esc="close_modal">
            <div class="box m-2" style="height: 100%">
                <div class="columns">

                    <!-- Story content -->
                    <div class="column is-three-quarters">

                        <div class="container">
                            <input class="input m-2" type="text" v-model="updates.title" />

                            <!-- <hr style="border: 1px green" /> -->

                            <textarea class="textarea m-2" v-model="updates.description"></textarea>
                        </div>
                    </div>

                    <!-- Story sidebar -->
                    <div class="column is-one-quarter has-text-left">
                        <p>Story ID: {{ story.id }}</p>

                        <hr style="border: 1px green" />

                        <p>State:</p>
                        <StateSelector :states="states" :default="story.state" @selection="update_state"/>

                        <hr style="border: 1px green" />

                    </div>

                </div>

                <div class="container">
                    <div class="field is-grouped">
                        <p class="control">
                            <button class="button is-link" @click="save_story">
                                Save changes
                            </button>
                        </p>
                        <p class="control">
                            <button class="button" @click="close_modal">
                                Cancel
                            </button>
                        </p>
                    </div>
                </div>

            </div>
        </div>

        <!-- modal close button -->
        <button class="modal-close is-large" aria-label="close" @click="close_modal"></button>
    </div>
</template>

<script>
 import { nextTick } from "vue"

 import { update_story as api_update_story } from "@/api/stories"
 import { use_projects_store } from "@/stores/projects"

 import StateSelector from "@/components/StateSelector.vue"

 export default {
     name: "StoryItem",

     components: {
         StateSelector,
     },

     props: ["story"],

     setup() {
         const store = use_projects_store();
         return { store }
     },

     data() {
         return {
             updates: {
                 title: this.story.title,
                 description: this.story.description,
                 state: this.story.state,
             },
             show_modal: false,
         }
     },

     computed: {
         states() {
             return this.store.selected_project.states;
         }
     },

     methods: {
         async open_modal() {
             this.show_modal = true;
             await nextTick();
             this.$refs["detail-view"].focus();
         },

         close_modal() {
             this.show_modal = false;
         },

         update_state(state) {
             console.log("Update state to", state)
             this.updates.state = state;
         },

         save_story() {
             console.log("Updating story");
             const payload = {
                 title: this.updates.title,
                 description: this.updates.description,
                 state: this.updates.state,
             }
             api_update_story(this.story.project, this.story.id, payload)
                 .then(() => {
                     return this.store.fetch_project(this.story.project)
                         .then(() => {
                             this.close_modal();
                         })
                 })
                 .catch((error) => {
                     this.error = error.message;
                 });
         },
     },
 }
</script>

<style scoped lang="scss">
 .fullsize {
     min-height: calc(100vh - 10%);
     min-width: calc(100vw - 10%);
 }

 div:focus {
     outline: none;
 }
</style>
