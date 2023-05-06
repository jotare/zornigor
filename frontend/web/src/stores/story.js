import { defineStore } from "pinia"

import { list_stories } from "@/api/stories"


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
        list_stories(project_id)
            .then((stories) => {
                this._stories = stories;
            })
            .catch((error) => {
                this._error = error.message;
            })
    }
}

export const use_stories_store = defineStore({
    id: "story-store",
    state,
    getters,
    actions,
});
