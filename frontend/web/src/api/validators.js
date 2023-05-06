import Ajv from "ajv";

const ajv = new Ajv();

const project_schema = {
    $id: "project",
    type: "object",
    properties: {
        id: { type: "string" },
        name: { type: "string" },
        description: { type: "string" },
    },
    additionalProperties: false,
}

const project_list_schema = {
    type: "array",
    items: { $ref: "project" }
}

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

const story_schema = {
    $id: "story",
    type: "object",
    properties: {
        id: {type: "integer"},
        title: {type: "string"},
        description: {type: "string"},
        state: {type: "string"},
    },
    additionalProperties: true,
}

const story_list_schema = {
    type: "array",
    items: { $ref: "story" },
}

const is_valid_project = ajv.compile(project_schema)
const is_valid_project_list = ajv.compile(project_list_schema)

const is_valid_state = ajv.compile(state_schema);
const is_valid_state_list = ajv.compile(state_list_schema);

const is_valid_story = ajv.compile(story_schema);
const is_valid_story_list = ajv.compile(story_list_schema);

export {
    is_valid_project,
    is_valid_project_list,
    is_valid_state,
    is_valid_state_list,
    is_valid_story,
    is_valid_story_list,
};
