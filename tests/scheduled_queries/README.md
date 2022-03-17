

# Scheduled Query Resource Definition


### Purpose
* This manifest creates a scheduled query and land data into a set Big Query table
* The table schema must match the output of the query output

## Naming Conventions
* Scheduled query name = `bq_data_transfer_<resource_name>`
* Scheduled query table name = bq_`<resource_name>`


### Definitions
|Name| Description | Type |
| ----- | ----- | ----- |
| **kind** | [REQUIRED] Resource type | string |
| **version** | [REQUIRED] Version of the manifest | parent |
| **metadata** | [REQUIRED] Parent definition for metadata | parent |
| dep      | [REQUIRED] Reference to the DEP/PIA number or BDS prime. Child of metadata. | string |
| **resource_name** | [REQUIRED] See above for the naming of the resources, must start with `bq_`  | string |
| **description** | [REQUIRED] Description of the table | string |
| **dataset_id** | [REQUIRED] The dataset ID to create the table in. Changing this forces a new resource to be created. | string |
| **expiration_datetime_staging** | [REQUIRED] In the staging environnmenet, the time when this object expires, in Python datetime format in string E.g `datetime(2021,10,25)`. Expired object will be deleted and their storage reclaimed. | string |
| **expiration_datetime_serving** | [REQUIRED] In the serving environnmenet, the time when this object expires, in Python datetime format in string E.g `datetime(2021,10,25)`. Expired object will be deleted and their storage reclaimed. | string |
| **schema** | [REQUIRED] A JSON schema for the table. | string |
| **query** | [REQUIRED] A query whose result is persisted. | string |
| **query_schedule** | [REQUIRED] Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: the granularity should be at least 8 hours, or less frequent. | string |
| **write_disposition** | [REQUIRED] write_disposition | string |
| **iam_binding** | [REQUIRED] Parent definition for IAM | parent |
| users | [REQUIRED] Child of iam_binding. Parent definition for user IAM | parent |
| subscribers | [OPTIONAL] Users that have read permissions. Child of users.| list |
| principal | [OPTIONAL] Users definition. Format of users: `user:user@telus.com`  | string |
| expiry | [OPTIONAL] Expiry datetime of the user binding. Python datetime format in string. E.g `datetime(2021,10,25)` | string |
| publishers | [OPTIONAl] Users that have write permissions. Child of users. | list |
| principal | [OPTIONAL] Users definition. Format of users: `user:user@telus.com` Format of service accounts: `serviceAccount:prod-dev-example@appspot.gserviceaccount.com` | string |
| expiry | [OPTIONAL] Expiry datetime of the user binding. Python datetime format in string. E.g `datetime(2021,10,25)` | string |
| **service_accounts** | [REQUIRED] Child of iam_binding. Parent definition for service accounts IAM | parent |
| subscribers | [OPTIONAL] Service accounts that have read permissions. Child of service_accounts. | list |
| principal | [OPTIONAL] Service accounts definition. Format of service accounts: `serviceAccount:prod-dev-example@appspot.gserviceaccount.com` | string |
| publishers | [OPTIONAl] Service accounts that have write permissions. Child of service_accounts. Format of service accounts: `serviceAccount:prod-dev-example@appspot.gserviceaccount.com` | list |
| principal | [OPTIONAL] Service accounts definition. Format of service accounts: `serviceAccount:prod-dev-example@appspot.gserviceaccount.com` | string |

### Example:

```
kind: scheduled_query
version: v1
metadata:
  dep: "144"
description: "Table for testing"
resource_name: bq_query_scheduled_1
dataset_id: pdc_2
expiration_datetime_staging: datetime(2022,12,25)
expiration_datetime_serving:
query_schedule: "every 24 hours"
write_disposition: "WRITE_APPEND"
query: >
  select 'ones' as run_id
schema: >
  [
    {
      "name": "run_id",
      "type": "STRING",
      "mode": "NULLABLE",
      "description": "run_id"
    },
    {
      "name": "run_ts",
      "type": "DATETIME",
      "mode": "NULLABLE",
      "description": "run_ts"
    },
    {
        "name": "addresses",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "status",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "address",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "city",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "state",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "zip",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "numberOfYears",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "numberOfMonths",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "numberOfWeeks",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    },
    {
      "name": "run_sa",
      "type": "STRING",
      "mode": "NULLABLE",
      "description": "run_sa"
    },
    {
      "name": "run_status",
      "type": "STRING",
      "mode": "NULLABLE",
      "description": "run_status"
    },
    {
      "name": "run_query",
      "type": "STRING",
      "mode": "NULLABLE",
      "description": "run_query"
    }
  ]
iam_binding:
    users:
      subscribers:
        - principal: user:user1@telus.com
          expiry: datetime(2020,10,25)
        - principal: user:user2@telus.com
          expiry: datetime(2022,12,25)
      publishers:
        - principal: user:user2@telus.com
          expiry: datetime(2022,12,25)
    service_accounts:
      subscribers:
        - principal: serviceAccount:sspark@dse-cicd-test-lab-4c0841.iam.gserviceaccount.com
      publishers:
   ```
  
