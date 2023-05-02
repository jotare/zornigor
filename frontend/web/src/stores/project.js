import axios from "axios"
import { defineStore } from "pinia"

import { validate_project_list } from "@/models/api/project"


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
        console.log("[store] Project set:", this._current_project);
    },

    fetch_projects(force = false) {
        if (this.ongoing_fetches.project_list) {
            return;
        }

        if (has_loaded_projects(this) && !force) {
            return;
        }

        this.ongoing_fetches.project_list = true;
        axios
            .get("http://localhost:8080/api/v1/projects")
            .then((response) => {
                if (!validate_project_list(response.data)) {
                    this._error = `Invalid data from API: ${validate_project_list.errors[-1]}`;
                    console.error(this._error);
                    return;
                }

                for (const project of response.data) {
                    this._projects[project.id] = project;
                }
                console.log("response", response.data)
                console.log("Projects:", this._projects)
            })
            .catch((error) => {
                console.log("ERROR", error)
                this._error = error.message;
            })
            .finally(() => {
                this.ongoing_fetches.project_list = false;
            });
    },

    fetch_project(project_id) {
        // TODO fetch only this project
        project_id;
        this.fetch_projects();
    },
};


export const use_projects_store = defineStore({
    id: "project-store",
    state,
    getters,
    actions,
});
