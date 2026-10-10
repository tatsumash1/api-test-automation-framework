USER_SCHEMA = {
    "type": "object",
    "required": [
        "id",
        "email",
        "first_name",
        "last_name",
        "avatar",
    ],
    "properties": {
        "id": {
            "type": "integer",        
        },
        "email": {
            "type": "string",
        },
        "first_name": {
            "type": "string",
        },
        "last_name": {
            "type": "string",
        },
        "avatar": {
            "type": "string",
        },
    },
}

USER_LIST_SCHEMA = {
    "type": "array",
    "minItems": 1,
    "items": USER_SCHEMA,
}

USER_PUT_SCHEMA = {
    "type": "object",
    "required": [
        "name",
        "job",
        "updatedAt",
    ],
    "properties":{
        "name": {
            "type": "string",
        },
        "job": {
            "type": "string",
        },
        "updatedAt": {
            "type": "string",
        },
    },
}

USER_PATCH_NAME_SCHEMA = {
    "type": "object",
    "required": [
        "name",
        "updatedAt",
    ],
    "properties":{
        "name": {
            "type": "string",
        },
        "updatedAt": {
            "type": "string",
        },
    },
}

USER_PATCH_JOB_SCHEMA = {
    "type": "object",
    "required": [
        "job",
        "updatedAt"
    ],
    "properties": {
        "job": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        },
    },
}

USER_PATCH_NAME_AND_JOB_SCHEMA = {
    "type": "object",
    "required": [
        "name",
        "job",
        "updatedAt"
    ],
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        },
    },
}