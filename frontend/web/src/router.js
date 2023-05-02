import { createRouter, createWebHistory } from "vue-router"

import ProjectList from "@/components/ProjectList.vue"
import ProjectStoriesView from "@/components/ProjectStoriesView.vue"



const routes = [
    {
        name: "home",
        path: "/",
        redirect: { name: "projects" }
    },
    {
        name: "projects",
        path: "/projects",
        component: ProjectList,
    },
    {
        name: "project",
        path: "/project/:id",
        component: ProjectStoriesView,
        props: true,
    },
]


const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
