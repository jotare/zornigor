import axios from "axios"
import { defineStore } from "pinia"

import { validate_story_list } from "@/models/api/story"


const state = () => {
    return {
        _error: "",
        _stories: [],
    }
}

const getters = {
    error() {
        return this._error;
    },

    stories() {
        return this._stories;
    },
}

const actions = {
    fetch_stories(project_id) {
        axios.get(`http://localhost:8080/api/v1/project/${project_id}/stories`).then((response) => {
            if (!validate_story_list(response.data)) {
                this._error = `Invalid data from API: ${validate_story_list.errors[-1]}`;
                console.error(this._error);
                return;
            }

            this._stories = response.data;
        });
    }
}

export const use_stories_store = defineStore({
    id: "story-store",
    state,
    getters,
    actions,
});
