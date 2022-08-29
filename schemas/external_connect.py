{
    'kind': {
        'required': True,
        'type': 'string',
        'nullable': False,
        'regex': '^extrenal_connectivty$'
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
        'nullable': True
    },
    'resource_name': {
        'required': True,
        'type': 'string',
        'nullable': False,
    },
    'domain': {
        'required': False,
        'type': 'string',
        'nullable': False,
        'excludes': 'ip_list'
    },
    'dns_ip': {
        'required': False,
        'type': 'string',
        'nullable': False,
        'allowed': ["8.8.8.8"]
    },
    'rtype': {
        'required': False,
        'type': 'string',
        'nullable': False,
        'allowed': ["AA"]
    },
    'transport': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'protocol': {'type': 'string','allowed': ["tcp"]},
                'ports': {'type': 'list'}
                    }
                }
            },
    'ip_list': {
        'required': False,
        'type': 'list',
        'nullable': False,
        'excludes': 'domain'
            }
}