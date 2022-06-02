{
    'kind': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': '^expectation$'
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
    'table_id': {
        'required': True,
        'type': 'string',
        'nullable': False
    },
    'expiration_datetime_staging': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': 'datetime\(\d{4},([1-9]|1[0-2]),([1-9]|[12][0-9]|3[01])\)'
    },
    'expiration_datetime_serving': {
        'required': True,
        'type': 'string',
        'nullable': True,
        'regex': 'datetime\(\d{4},([1-9]|1[0-2]),([1-9]|[12][0-9]|3[01])\)'
    },
    'data_validation': {
        'required': True,
        'type': 'dict',
        'schema': {
            'query': {'type': 'string'},
            'schedule': {'type': 'string'},
            'gchat_webhook_list': {'type': 'list'},
            'properties': {'type': 'dict'}
        }
        }
}
