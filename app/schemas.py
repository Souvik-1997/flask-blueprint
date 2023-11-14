# Schemas for logistics transport

transports_schema = {
    "type": {
        "type": "string",
        "required": True,
        "minlength": 2,
        "maxlength": 20,
    },
    "name": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "maxlength": 20,
    },
    "description": {
        "type": "string",
        "required": True,
    },
}
