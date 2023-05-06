import axios from "axios"

import * as  validators from "@/api/validators"

import { BASE_URL } from "@/globals"


function get_project(project_id) {
    return axios
        .get(BASE_URL + "/project/" + project_id)
        .then((response) => {
            if (response.status != 200) {
                throw Error(`API error ${response.status}: ${response.data}`);
            }

            if (!validators.is_valid_project(response.data)) {
                let api_error = validators.is_valid_project.errors[-1];
                throw new Error(`Invalid API data: ${api_error}`);
            }

            let project = response.data;
            return project;
        })
        .catch((error) => {
            console.log(`Error while GET /project/${project_id}: ${error.message}`);
            throw error;
        })
}

function list_projects() {
    return axios
        .get(BASE_URL + "/projects")
        .then((response) => {
            if (response.status != 200) {
                throw Error(`API error ${response.status}: ${response.data}`);
            }

            if (!validators.is_valid_project_list(response.data)) {
                let api_error = validators.is_valid_project_list.errors[-1];
                throw new Error(`Invalid API data: ${api_error}`);
            }

            let projects = response.data;
            return projects;
        })
        .catch((error) => {
            console.log(`Error while GET /projects: ${error.message}`);
            throw error;
        })
}


export {
    get_project,
    list_projects,
}
