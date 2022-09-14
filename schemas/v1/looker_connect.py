{
    'kind': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': '^looker_connect$'
    },
    'version': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': '^v1$',
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
    'location': {
        'required': False,
        'type': 'string',
        'nullable': True,
        'default': None
    },
    'pdt_dataset_id': {
        'required': False,
        'type': 'string',
        'nullable': True,
        'default': 'pdt_looker',
        'regex': '([a-z])([a-z0-9_])+'
    },
    'pub_dataset_id': {
        'required': False,
        'type': 'string',
        'nullable': True,
        'default': None,
        'regex': '([a-z])([a-z0-9_])+'
    },
    'pub_partition_expiration_ms': {
        'required': False,
        'type': 'number',
        'nullable': True,
        'default': None
    },
    'pub_table_expiration_ms': {
        'required': False,
        'type': 'number',
        'nullable': True,
        'default': None
    },
    'pdt_partition_expiration_ms': {
        'required': False,
        'type': 'number',
        'nullable': True,
        'default': None
    },
    'pdt_table_expiration_ms': {
        'required': False,
        'type': 'number',
        'nullable': True,
        'default': None
    },
    'p4sa_service_accounts': {
        'required': True,
        'type': 'list',
        'nullable': False
    }
}