import Ajv from "ajv";

const ajv = new Ajv();

const state_schema = {
    $id: "state",
    type: "object",
    properties: {
        id: {type: "string"},
        name: {type: "string"},
        description: {type: "string"},
    },
    additionalProperties: false,
}

const state_list_schema = {
    type: "array",
    items: { $ref: "state" },
}

const validate_state = ajv.compile(state_schema);
const validate_state_list = ajv.compile(state_list_schema);

export {
    validate_state,
    validate_state_list,
};
