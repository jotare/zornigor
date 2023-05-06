import axios from "axios"

import * as  validators from "@/api/validators"

import { BASE_URL } from "@/globals"


function list_states(project_id) {
    return axios
        .get(BASE_URL + "/project/" + project_id + "/states")
        .then((response) => {
            if (response.status != 200) {
                throw Error(`API error ${response.status}: ${response.data}`);
            }

            if (!validators.is_valid_state_list(response.data)) {
                let api_error = validators.is_valid_state_list.errors[-1];
                throw new Error(`Invalid API data: ${api_error}`);
            }

            let states = response.data;
            return states;
        })
        .catch((error) => {
            console.log(`Error while GET /project/${project_id}/states: ${error.message}`);
            throw error;
        })
}


export {
    list_states,
}
