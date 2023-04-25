<template>
    <a class="box has-background-grey-lighter" @click="open_modal">
        <h3>{{ story.title }}</h3>
    </a>

    <div class="modal" :class="{ 'is-active': show_modal }">
        <div class="modal-background" @click="close_modal"></div>

        <div ref="detail-view" class="modal-content fullsize" tabindex="0" @keyup.esc="close_modal">
            <div class="box" style="height: 100%">
                <h3>{{ story.title }}</h3>
                <hr style="border: 1px green" />
                <div class="columns">
                    <!-- Story content -->
                    <div class="column is-three-quarters">
                        <pre>
                            {{ story.description }}
                        </pre>
                    </div>

                    <!-- Story sidebar -->
                    <div class="column is-one-quarter">
                        <p>State: {{ story.state }}</p>
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

 export default {
     name: "StoryItem",

     props: ["story"],

     data() {
         return {
             show_modal: false,
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
