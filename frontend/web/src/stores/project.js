import { defineStore } from "pinia"

import { get_project, list_projects } from "@/api/projects"


const state = () => {
    return {
        _error: "",
        _current_project: null,
        _projects: {},          // { project_id: project }
        ongoing_fetches: {
            project_list: false,
            project: false,
        }
    }
}


const getters = {
    error() {
        return this._error;
    },

    current_project() {
        return this._current_project;
    },

    projects() {
        return Object.keys(this._projects).map((key) => this._projects[key]);
    },

    project_by_id() {
        return (project_id) => {
            return this._projects[project_id]
        }
    },
}


// Utils

function has_loaded_projects(store) {
    return Object.keys(store._projects).length > 0;
}


const actions = {
    set_current_project(project_id) {
        this._current_project = null;
        if (project_id in this._projects) {
            this._current_project = this._projects[project_id]
        }
    },

    fetch_projects(force = false) {
        if (this.ongoing_fetches.project_list) {
            return;
        }

        if (has_loaded_projects(this) && !force) {
            return;
        }

        this.ongoing_fetches.project_list = true;
        list_projects()
            .then((projects) => {
                for (const project of projects) {
                    this._projects[project.id] = project;
                }
            })
            .catch((error) => {
                this._error = error.message;
            })
            .finally(() => {
                this.ongoing_fetches.project_list = false;
            })
    },

    fetch_project(project_id) {
        if (this.ongoing_fetches.project) {
            return;
        }
        this.ongoing_fetches.project = true;
        get_project(project_id)
            .then((project) => {
                this._projects[project_id] = project;
            })
            .catch((error) => {
                this._error = error.message;
            })
            .finally(() => {
                this.ongoing_fetches.project = false;
            })
    },
};


export const use_projects_store = defineStore({
    id: "project-store",
    state,
    getters,
    actions,
});
