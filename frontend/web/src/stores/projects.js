import { defineStore } from "pinia"
import { get_project, list_projects } from "@/api/projects"
import { list_states } from "@/api/states"
import { list_stories } from "@/api/stories"


const state = () => {
    return {
        _error: null,

        _projects: {
            // project_id: {
            //     *project_metadata,
            //     states: [],
            //     stories: {
            //         state_id: [story_list]
            //     }
            // }
        },
        // ongoing_operations: {
        //     fetch: {
        //         project: false,
        //         project_list: false,
        //     }
        // }
    }
}


const getters = {
    error() {
        return this._error;
    },

    projects() {
        return Object.keys(this._projects).map((key) => this._projects[key]);
    },

    project() {
        return (id) => {
            return this._projects[id]
        }
    },

    states() {
        return (project_id) => {
            return this._projects[project_id].states;
        }
    },

    stories() {
       return (project_id) => {
           return this._projects[project_id].stories;
       }
    },

    stories_by_state() {
        return (project_id) => {
            let states = this._projects[project_id].states;
            let stories = this._projects[project_id].stories;

            let grouped = {}
            for (let state of states) {
                for (let story of stories) {
                    if (story.state == state.id) {
                        if (grouped[state.id] == null) {
                            grouped[state.id] = [];
                        }
                        grouped[state.id].push(story);
                    }
                }
            }
            return grouped;
        }
    },
}

const actions = {
    project_count() {
        return Object.keys(this._projects).length;
    },

    fetch_projects() {
        list_projects()
            .then((projects) => {
                for (const project of projects) {
                    this._projects[project.id] = project;
                }
            })
            .catch((error) => { this._error = error.message });
    },

    fetch_project(project_id) {
        get_project(project_id)
            .then((project) => {
                this._projects[project_id] = project;
            })
            .catch((error) => { this._error = error.message });
    },

    fetch_states(project_id) {
        list_states(project_id)
            .then((states) => {
                this._projects[project_id].states = states;
            })
            .catch((error) => { this._error = error.message });
    },

    fetch_stories(project_id) {
        list_stories(project_id)
            .then((stories) => {
                this._projects[project_id].stories = stories;
            })
            .catch((error) => { this._error = error.message });
    },
}

export const use_projects_store = defineStore({
    id: "projects-store",
    state,
    getters,
    actions,
});
