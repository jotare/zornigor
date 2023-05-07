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
                    :class="{'is-active': menus.project_list.is_active}"
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

                        <hr class="navbar-divider">

                        <router-link
                            class="navbar-item"
                            :to="{ name: 'project_create'}"
                        >
                            <p>
                                <font-awesome-icon icon="fa-solid fa-plus"></font-awesome-icon>
                                New Project
                            </p>
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
             menus: {
                 project_list: {
                     is_active: false,
                 },
             },
             modals: {
                 new_project: {
                     is_active: false,
                 },
             },
         }
     },

     computed: {
         projects() {
             return this.store.projects;
         },
     },

     methods: {
         toggle_projects_menu() {
             this.menus.project_list.is_active = !this.menus.project_list.is_active;
         },
     },
 }
</script>

<style type="text/css" media="screen">
.iconicon {
    display: flex;
    justify-content: center;
    align-items: flex-end;
}
</style>
