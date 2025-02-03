schema_get_single_resource = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "color": {
          "type": "string"
        },
        "pantone_value": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "year",
        "color",
        "pantone_value"
      ]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "data",
    "support"
  ]
}

schema_create_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "createdAt"
  ]
}

schema_update_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "updatedAt"
  ]
}

schema_post_unsuccessful_login = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}