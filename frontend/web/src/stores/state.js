import axios from "axios"
import { defineStore } from "pinia"

import { validate_state_list } from "@/models/api/state"


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
        axios.get(`http://localhost:8080/api/v1/project/${project_id}/states`).then((response) => {
            if (!validate_state_list(response.data)) {
                this._error = `Invalid data from API: ${validate_state_list.errors[-1]}`;
                console.error(this._error);
                return;
            }

            this._states = response.data;
        });
    }
}

export const use_states_store = defineStore({
    id: "state-store",
    state,
    getters,
    actions,
});
