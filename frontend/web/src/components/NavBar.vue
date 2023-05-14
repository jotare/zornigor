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
                <router-link class="navbar-item" :to="{ 'name': 'projects' }">Projects</router-link>
            </div>

        </div>

    </nav>

</template>

<script>
 export default {
     name: "NavBar",
 }
</script>

<style type="text/css" media="screen">
 .iconicon {
     display: flex;
     justify-content: center;
     align-items: flex-end;
 }
</style>
