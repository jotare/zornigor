import { createRouter, createWebHistory } from "vue-router"

import { use_projects_store } from "@/stores/projects"

import ZornigorHome from "@/components/ZornigorHome.vue"
import ProjectList from "@/components/ProjectList.vue"
import ProjectView from "@/components/ProjectView.vue"
import ProjectCreate from "@/components/ProjectCreate.vue"
import StoryCreate from "@/components/StoryCreate.vue"


const routes = [
    {
        name: "home",
        path: "/",
        component: ZornigorHome,
    },
    {
        name: "projects",
        path: "/projects",
        component: ProjectList,
    },
    {
        name: "project_create",
        path: "/projects/new",
        component: ProjectCreate,
    },
    {
        name: "project",
        path: "/project/:id/stories",
        component: ProjectView,
        props: true,
    },
    {
        name: "story_create",
        path: "/project/:id/stories/new",
        component: StoryCreate,
    },
]


const router = createRouter({
    history: createWebHistory(),
    routes,
});


router.beforeEach((to) => {
    let matches = to.fullPath.match(/^\/project\/([^/]+)\/.*/);
    let has_project_selected = matches != null;

    if (has_project_selected) {
        let selected_project = matches[1];

        const store = use_projects_store();
        store.fetch_project(selected_project)
             .then(() => {
                 store.select_project(selected_project);
             });
    }

});



export default router
