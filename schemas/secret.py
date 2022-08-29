{
    'kind': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': '^secret$'
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
    'resource_name': {
        'required': True,
        'type': 'string',
        'nullable': False,
    },
}