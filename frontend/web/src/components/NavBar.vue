<template>
    <nav class="navbar is-info is-fixed-top has-navbar-fixed-top" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <router-link class="navbar-item" :to="{ name: 'home'}">
                <h1 class="title">Z</h1>
                <!-- <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28"> -->
            </router-link>

            <!-- Navbar burger is only visible touch devices and it needs three
                 empty span tags in order to visualize the three hamburguer
                 lines or cross (when active) -->
            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar_menu">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbar_menu" class="navbar-menu">
            <div class="navbar-start">
                <div
                    class="navbar-item has-dropdown"
                    :class="{'is-active': is_menu_active}"
                    @click="toggle_projects_menu"
                >
                    <a class="navbar-link">
                        Projects
                    </a>

                    <div class="navbar-dropdown">
                        <router-link
                            class="navbar-item"
                            v-for="project in projects" :key="project.id"
                            :to="{ name: 'project', params: { id: project.id } }"
                        >
                            {{ project.name }}
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>

</template>

<script>
 import { use_projects_store } from "@/stores/projects"

 export default {
     name: "NavBar",

     setup() {
         const store = use_projects_store();
         return { store }
     },

     created() {
         this.store.fetch_projects();
     },

     data() {
         return {
             is_menu_active: false,
         }
     },

     computed: {
         projects() {
             return this.store.projects;
         },
     },

     methods: {
         toggle_projects_menu() {
            this.is_menu_active = !this.is_menu_active;
         },
     }

 }
</script>
