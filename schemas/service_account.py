{
    'kind': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': '^service_account$'
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
        'regex': '^[a-z](?:[-a-z0-9]{4,28}[a-z0-9])$'
    },
    'kubernetes_service_accounts': {
        'required': True,
        'type': 'list',
        'nullable': False
    }
}
