PRODUCT_SCHEMA = {
    "type": "object",
    "required": [
        "id",
        "name",
        "year",
        "color",
        "pantone_value",
    ],
    "properties": {
        "id": {
            "type": "integer",
        },
        "name": {
            "type": "string",
        },
        "year": {
            "type": "integer",
        },
        "color": {
            "type": "string",
        },
        "pantone_value": {
            "type": "string"
        },
    },
}

PRODUCT_LIST_SCHEMA = {
    "type": "array",
    "minItems": 1,
    "items": PRODUCT_SCHEMA
}