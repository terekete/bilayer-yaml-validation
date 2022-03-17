

# External Table Resource Definition


### Naming Convention:
* bq_`<resource_name>
* Example: `bq_my_data`



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
| **source_format** | [REQUIRED] source format of the source data. Possible values: "CSV", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET" | string |
| **autodetect** | [REQUIRED] if autodetect source uris schema | boolean |
| **source_uris_staging** | [REQUIRED] list of source uris in staging, wildcard expression can be used | list |
| **source_uris_serving** | [REQUIRED] list of source uris in serving, wildcard expression can be used | list |
| **schema** | [OPTIONAL] schema of the source uris | string |
| **csv_options** | [OPTIONAL] options if source uris are in CSV | parent |
| quote      | [OPTIONAL] The value that is used to quote data sections in a CSV file. If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allow_quoted_newlines property to true. The API-side default is ", specified in the provider escaped as \". Due to limitations with default values, this value is required to be explicitly set. | string |
| allow_jagged_rows      | [OPTIONAL] Indicates if BigQuery should accept rows that are missing trailing optional columns. | boolean |
| allow_quoted_newlines      | [OPTIONAL] Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false. | boolean |
| encoding      | [OPTIONAL] The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. | string |
| field_delimiter      | [OPTIONAL] The separator for fields in a CSV file. | string |
| skip_leading_rows      | [OPTIONAL] Reference to the DEP/PIA number or BDS prime. Child of metadata. | integer |
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
kind: ext_table
version: v1
metadata:
  dep: "144"
description: "ext table"
resource_name: bq_exttable_1
dataset_id: pdc_2
expiration_datetime_staging: datetime(2022,12,25)
expiration_datetime_serving:
source_format: "CSV"
autodetect: True
source_uris_staging: 
  # - "gs://dse-cicd-test-lab-4c0841-jobs-scripts/userdata1.avro"
  - "gs://dse-cicd-test-lab-4c0841-jobs-scripts/loan*"
source_uris_serving: 
  - "gs://dse-cicd-test-lab-4c0841-jobs-scripts/loan*"
schema: 
csv_options:
    quote: ""
    allow_jagged_rows: True 
    allow_quoted_newlines: False
    encoding: "UTF-8"
    field_delimiter: ","
    skip_leading_rows: 1
iam_binding:
    users:
      subscribers:
        - principal: user:dong.yang@telus.com
          expiry: datetime(2020,10,25)
        - principal: user:mark.gates@telus.com
          expiry: datetime(2022,12,25)
    service_accounts:
      subscribers:
        - principal: serviceAccount:sspark@dse-cicd-test-lab-4c0841.iam.gserviceaccount.com
  ```
