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

const validate_project = ajv.compile(project_schema)
const validate_project_list = ajv.compile(project_list_schema)

export {
    validate_project,
    validate_project_list,
};
