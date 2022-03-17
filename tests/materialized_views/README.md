

# Materialized View Resource Definition


### Purpose
- Materialized views serve as teh final aggregation layer that can be best utilized for serving summarized data to other platforms. The can scheduled updates that are cached.
- Considerations: Materialized Views have limitations on how they can be used when joining to other tables. Please refer to the Google Docs [here](https://cloud.google.com/bigquery/docs/materialized-views-create#query_limitations).


### Naming Convention:
* bq_`<resource_name>`_view
* Example: `bq_my_mat_view`

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
| **enable_refresh** | [OPTIONAL] Specifies whether to use BigQuery’s automatic refresh for this materialized view when the base table is updated. The default value is true.| bool |
| **refresh_interval_ms** | [OPTIONAL] The maximum frequency at which this materialized view will be refreshed. The default value is 1800000| int |
| **iam_binding** | [REQUIRED] Parent definition for IAM | parent |
| users | [REQUIRED] Child of iam_binding. Parent definition for user IAM | parent |
| subscribers | [OPTIONAL] Users that have read permissions. | list |
| principal | [OPTIONAL] Users definition. Format of users: `user:user@telus.com`  | string |
| expiry | [OPTIONAL] Expiry datetime of the user binding. Python datetime format in string. E.g `datetime(2021,10,25)` | string |
| **service_accounts** | [REQUIRED] Child of iam_binding. Parent definition for service accounts IAM | parent |
| subscribers | [OPTIONAL] Service accounts that have read permissions. Child of service_accounts. | list |
| principal | [OPTIONAL] Service accounts definition. Format of service accounts: `serviceAccount:prod-dev-example@appspot.gserviceaccount.com` | string |


### Example: 
```
kind: materialized_view
version: v1
metadata:
  dep: "144"
description: "Mat. View for Testing"
resource_name: bq_material_run_view
dataset_id: mat_view_1
expiration_datetime_staging: datetime(2022,12,25)
expiration_datetime_serving:
params:
  query: "select * from `source_data.data`"
  refresh: true
  refresh_ms: 60000
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
