{
    'kind': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': '^scalar_function$'
    },
    'version': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': 'v(\d{1})',
    },
    'metadata': {
        'required': True,
        'type': 'dict',
        'schema': {
            'dep': {
                'required': True,
                'type': 'string',
                'nullable': False
            }
        }
    },
    'description': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'resource_name': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': '[a-z0-9_]+'
    },
    'dataset_id': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'language': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'imported_libraries': {
        'required': False,
        'type': 'list',
        'nullable': True
    },
    'determinism_level': {
        'required': False,
        'type': 'string',
        'nullable': True,
        'allowed': ['DETERMINISM_LEVEL_UNSPECIFIED', 'DETERMINISTIC', 'NOT_DETERMINISTIC']
    },
    'return_type': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'input_parameters': {
        'required': True,
        'type': 'list',
        'nullable': False,
        'schema': {
            'type': 'dict',
            'schema': {
                'name': {
                    'type': 'string'
                },
                'data_type': {
                    'type': 'string'
                }
            }
        }
    },
    'definition_body': {
        'required': True,
        'type': 'string',
        'nullable': False
    }
}
