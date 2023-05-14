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
            //     states: [
            //         *state_metadata,
            //         stories: [
            //             {
            //                 story
            //             },
            //             ...
            //         ],
            //         ...
            //     ],
            // }
        },

        _selected_project: null,

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

    selected_project() {
        return this._projects[this._selected_project];
    },

    states() {
        if (this._projects.chores == undefined) {
            return [];
        } else {
            return this._projects["chores"].states;
        }
        // return (project_id) => {
        //     return this._projects[project_id].states;
        // }
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

            if (!(stories && states)) {
                console.warn("Not stories or states");
                return {}
            }

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
    set_error(error) {
        this._error = error;
    },

    project_count() {
        return Object.keys(this._projects).length;
    },

    select_project(project_id) {
        this._selected_project = project_id;
    },

    fetch_project_list() {
        return list_projects()
            .then((projects) => {
                for (const project of projects) {
                    this._projects[project.id] = project;
                }
            })
            .catch((error) => { this._error = error.message });
    },

    fetch_project(project_id) {
        return Promise
            .all([
                get_project(project_id),
                list_states(project_id),
                list_stories(project_id),
            ])
            .then((result) => {
                let [project, states, stories] = result;
                project.states = states;

                let state_ids = states.map(state => state.id)

                for (let story of stories) {
                    let state_index = state_ids.indexOf(story.state);

                    if (state_index == -1) {
                        throw Error(`API returned story ${story.id} with an unexistent state ${story.state}`);
                    }

                    if (project.states[state_index].stories == null) {
                        project.states[state_index].stories = [];
                    }
                    project.states[state_index].stories.push(story);
                }

                this._projects[project_id] = project;
            })
            .catch((error) => {
                this._error = error.message;
                throw error
            })
    },
}

export const use_projects_store = defineStore({
    id: "projects-store",
    state,
    getters,
    actions,
});
