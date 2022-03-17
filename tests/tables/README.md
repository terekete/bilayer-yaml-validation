

# Table Resource Definition


### Purpose
- Table definition is used to create tables that are used for external loading. As such they define the schema and table qualities but there is no job associated to the resource definition itself. If you are looking to define a job please refer to the Pyspark Jobs resource.
- Examples would be to define a table that can be used to load data into from an external process such as data written from on-prem or from another project or pipeline.


### Naming Convention:
* bq_`<resource_name>`
* Example: `bq_my_table`


### Definitions
|Name| Description | Type |
| ----- | ----- | ----- |
| **kind** | [REQUIRED] Resource type | string |
| **version** | [REQUIRED] Version of the manifest | parent |
| **metadata** | [REQUIRED] Parent definition for metadata | parent |
| dep      | [REQUIRED] Reference to the DEP/PIA number or BDS prime. Child of metadata. | string |
| **resource_name** | [REQUIRED] Name of the table; must start with `bq_` | string |
| **description** | [REQUIRED] Description of the table | string |
| **dataset_id** | [REQUIRED] The dataset ID to create the table in. Changing this forces a new resource to be created. | string |
| **expiration_datetime_staging** | [REQUIRED] In the staging environnmenet, the time when this object expires, in Python datetime format in string E.g `datetime(2021,10,25)`. Expired object will be deleted and their storage reclaimed. | string |
| **expiration_datetime_serving** | [REQUIRED] In the serving environnmenet, the time when this object expires, in Python datetime format in string E.g `datetime(2021,10,25)`. Expired object will be deleted and their storage reclaimed. | string |
| **time_partitioning** | [OPTIONAL] time partitioning options | parent |
| type | [REQUIRED] The supported types are DAY, HOUR, MONTH, and YEAR, which will generate one partition per day, hour, month, and year, respectively. | string |
| expiration_ms | [REQUIRED] Number of milliseconds for which to keep the storage for a partition. | integer |
| field | [OPTIONAL] The field used to determine how to create a range-based partition. | string |
| require_partition_filter | [OPTIONAL] If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. | boolean |
| **schema** | [REQUIRED] A JSON schema for the table. | string |
| **iam_binding** | [REQUIRED] Parent definition for IAM | parent |
| **users** | [REQUIRED] Child of iam_binding. Parent definition for user IAM | parent |
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
kind: table
version: v1
metadata:
  dep: "144"
description: "Table for testing "
resource_name: bq_audit_run
dataset_id: pdc_2
expiration_datetime_staging: datetime(2022,12,25)
expiration_datetime_serving:
schema: >
  [
    {
      "name": "run_id",
      "type": "STRING",
      "mode": "REQUIRED",
      "description": "run_id"
    },
    {
      "name": "run_ts",
      "type": "DATETIME",
      "mode": "REQUIRED",
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
      "mode": "REQUIRED",
      "description": "run_sa"
    },
    {
      "name": "run_status",
      "type": "STRING",
      "mode": "REQUIRED",
      "description": "run_status"
    },
    {
      "name": "run_query",
      "type": "STRING",
      "mode": "REQUIRED",
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
        - principal: user:user3@telus.com
          expiry: datetime(2022,12,25)
    service_accounts:
      subscribers:
      publishers:
        - principal: serviceAccount:spark-sa@dse-cicd-test-lab-4c0841.iam.gserviceaccount.com
 ```
