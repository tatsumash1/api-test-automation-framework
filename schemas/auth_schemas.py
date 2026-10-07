REGISTER_SUCCESS_SCHEMA = {
    "type": "object",
    "required": ["id", "token"],
    "properties": {
        "id": {
            "type": "integer",
        },
        "token": {
            "type": "string",
        },
    },
}

LOGIN_SUCCESS_SCHEMA = {
    "type": "object",
    "required": ["token"],
    "properties": {
        "token": {
            "type": "string",
        },
    },
}

AUTH_ERROR_SCHEMA = {
    "type": "object",
    "required": ["error"],
    "properties": {
        "error": {
            "type": "string",
        },
    },
}