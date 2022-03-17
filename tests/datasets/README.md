

# Dataset Resource Definition

### Purpose
- Create a dataset for hosting your tables.
- Considerations: It's recommended to separate your dataset into either data domains or functions of data access. A team might put all data of a domain in one dataset. A team might also classify a single dataset as a place to host shared tables.
- Note: Datasets can be delted if no tables are present. Deleting the YAML definition and running through CICD will remove the dataset.


### Definitions
|Name| Description | Type |
| ----- | ----- | ----- |
| **kind** | [REQUIRED] resource type | string |
| **version** | [REQUIRED] Version of the manifest | parent |
| **metadata** | [REQUIRED] Parent definition for metadata | parent |
| dep      | [REQUIRED] Reference to the DEP/PIA number or BDS prime. Child of metadata. | string |
| **resource_name** | [REQUIRED] Name of the dataset | string |
| **description** | [REQUIRED] Description of the dataset | string |
| **partition_expiration_ms** | [OPTIONAL] The default partition expiration for all partitioned tables in the dataset, in milliseconds. | int |
| **table_expiration_ms** | [OPTIONAL] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). | int |
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
kind: dataset
version: v1
metadata:
  dep: "12"
description: "techub dataset"
resource_name: pdc_2
partition_expiration_ms:
table_expiration_ms:
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
