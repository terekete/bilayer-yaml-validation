

# View Resource Definition


### Purpose
- Views are a way to summarize a query logic without landing data in Big Query Storage. This can help minimize costs but there are minor tradeoffs in speed.
- Considerations: Use a view is highly recommended but note user utlizing views must also have data access to the tables utilized in the view. If this is a challenge consider summarizing data in views and writting final queries that use those views via Scheduled Queries.


### Naming Convention:
* bq_`<resource_name>`_view
* Example: `bq_my_data_view`



### Definitions
|Name| Description | Type |
| ----- | ----- | ----- |
| **kind** | [REQUIRED] resource type | string |
| **version** | [REQUIRED] Version of the manifest | parent |
| **metadata** | [REQUIRED] Parent definition for metadata | parent |
| dep      | [REQUIRED] Reference to the DEP/PIA number or BDS prime. Child of metadata. | string |
| **resource_name** | [REQUIRED] Name of the object, must start with `bq_` and end by `_view` | string |
| **description** | [REQUIRED] Description of the object | string |
| **dataset_id** | [REQUIRED] The dataset ID to create the object in. Changing this forces a new resource to be created. | string |
| **expiration_datetime_staging** | [REQUIRED] In the staging environnmenet, the time when this object expires, in Python datetime format in string E.g `datetime(2021,10,25)`. Expired object will be deleted and their storage reclaimed. | string |
| **expiration_datetime_serving** | [REQUIRED] In the serving environnmenet, the time when this object expires, in Python datetime format in string E.g `datetime(2021,10,25)`. Expired object will be deleted and their storage reclaimed. | string |
| **query** | [REQUIRED] A query whose result is persisted. | string |
| **iam_binding** | [REQUIRED] Parent definition for IAM | parent |
| **users** | [REQUIRED] Child of iam_binding. Parent definition for user IAM | parent |
| subscribers | [OPTIONAL] Users that have read permissions. | list |
| principal | [OPTIONAL] Users definition. Format of users: `user:user@telus.com`  | string |
| expiry | [OPTIONAL] Expiry datetime of the user binding. Python datetime format in string. E.g `datetime(2021,10,25)` | string |
| **service_accounts** | [REQUIRED] Child of iam_binding. Parent definition for service accounts IAM | parent |
| subscribers | [OPTIONAL] Service accounts that have read permissions. Child of service_accounts. | list |
| principal | [OPTIONAL] Service accounts definition. Format of service accounts: `serviceAccount:prod-dev-example@appspot.gserviceaccount.com` | string |

### Example:
```
kind: view
version: v1
metadata:
  dep: "144"
description: "Table for testing pulling data from datahub"
resource_name: bq_test_view
dataset_id: pdc_2
expiration_datetime_staging: datetime(2022,12,25)
expiration_datetime_serving:
query: >
  select * from `source_data.data`
use_legacy_sql: false
iam_binding:
    users:
      subscribers:
        - principal: user:user1@telus.com
          expiry: datetime(2020,10,25)
        - principal: user:user2@telus.com
          expiry: datetime(2022,12,25)
    service_accounts:
      subscribers:
        - principal: serviceAccount:spark-sa@dse-cicd-test-lab-4c0841.iam.gserviceaccount.com
  ```
