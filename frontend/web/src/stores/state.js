import { defineStore } from "pinia"

import { list_states } from "@/api/states"


const state = () => {
    return {
        _error: "",
        _states: [],
    }
}

const getters = {
    error() {
        return this._error;
    },

    states() {
        return this._states;
    },
}

const actions = {
    fetch_states(project_id) {
        list_states(project_id)
            .then((states) => {
                this._states = states;
            })
            .catch((error) => {
                this._error = error.message;
            })
    }
}

export const use_states_store = defineStore({
    id: "state-store",
    state,
    getters,
    actions,
});
