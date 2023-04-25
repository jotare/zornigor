import Ajv from "ajv";

const ajv = new Ajv();

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

const validate_story = ajv.compile(story_schema);
const validate_story_list = ajv.compile(story_list_schema);

export {
    validate_story,
    validate_story_list,
};
