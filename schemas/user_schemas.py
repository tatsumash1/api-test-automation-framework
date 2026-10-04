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