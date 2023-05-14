import axios from "axios"

import * as  validators from "@/api/validators"

import { BASE_URL } from "@/globals"


function create_story(project_id, story) {
    return axios
        .post(BASE_URL + "/project/" + project_id + "/stories", story)
        .then((response) => {
            if (response.status != 201) {
                throw Error(`API error ${response.status}: ${response.data}`);
            }
        })
        .catch((error) => {
            console.log(`Error while POST /project/${project_id}/stories: ${error.message}`);
            throw error;
        })
}

function get_story(project_id, story_id) {
    return axios
        .get(BASE_URL + "/project/" + project_id + "/story/" + story_id)
        .then((response) => {
            if (response.status != 200) {
                throw Error(`API error ${response.status}: ${response.data}`);
            }

            if (!validators.is_valid_story(response.data)) {
                let api_error = validators.is_valid_story.errors[-1];
                throw new Error(`Invalid API data: ${api_error}`);
            }

            let story = response.data;
            return story;
        })
        .catch((error) => {
            console.log(`Error while GET /project/${project_id}/story/${story_id}: ${error.message}`);
            throw error;
        })
}

function list_stories(project_id) {
    return axios
        .get(BASE_URL + "/project/" + project_id + "/stories")
        .then((response) => {
            if (response.status != 200) {
                throw Error(`API error ${response.status}: ${response.data}`);
            }

            if (!validators.is_valid_story_list(response.data)) {
                let api_error = validators.is_valid_story_list.errors[-1];
                throw new Error(`Invalid API data: ${api_error}`);
            }

            let stories = response.data;
            return stories;
        })
        .catch((error) => {
            console.log(`Error while GET /project/${project_id}/stories: ${error.message}`);
            throw error;
        })
}


function update_story(project_id, story_id, update) {
    return axios
        .patch(BASE_URL + "/project/" + project_id + "/story/" + story_id, update)
        .then((response) => {
            if (response.status != 204) {
                throw Error(`API error ${response.status}: ${response.data}`);
            }
        })
        .catch((error) => {
            console.log(`Error while PATCH /project/${project_id}/story/${story_id}: ${error.message}`);
            throw error;
        })
}


export {
    create_story,
    get_story,
    list_stories,
    update_story,
}
