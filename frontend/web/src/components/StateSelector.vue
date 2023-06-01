<template>
    <div class="select">
        <select v-model="selected">
            <option v-for="state in states"
                    :key="state.id"
                    :value="state.id"
                    @click="select_state(state.id)"
            >
                {{ state.name }}
            </option>
        </select>
    </div>
</template>

<script>

 export default {
     name: "StateSelector",

     props: ["states", "default"],

     emits: ["selection"],

     data() {
         return {
             is_active: false,
             selected: this.default || (this.states.length > 0 ? this.states[0].id : null),
         }
     },

     computed: {
         selected_text() {
             if (this.selected == null) {
                 return "Select an state";
             }
             return this.selected;
         },
     },

     methods: {
         toggle() {
             this.is_active = !this.is_active;
         },

         select_state(state) {
             this.selected = state;
             this.$emit("selection", state);
         }
     },
 }

</script>
