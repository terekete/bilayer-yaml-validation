

# Bucket Resource Definition


### Purpose

* Save data for production workflows downstream such as models
* Archive data that is not needing consumption in Big Query
* Share data between teams in raw format
* Write data from business owned processes to GCP for downstream usage (requires Privacy Approval)

### Naming Convention:

* Bucket names are based on `<resource_name>` but the bucket produced will be prefixed with the project id automatically to ensure uniqueness.
* Example: The a resource name of `my_resource_name` results in a bucket called `<project_id>_my_resource_name`.


### Definitions
|Name| Description | Type |
| ----- | ----- | ----- |
| **kind** | [REQUIRED] Resource type | string |
| **version** | [REQUIRED] Version of the manifest | parent |
| **metadata** | [REQUIRED] Parent definition for metadata | parent |
| dep      | [REQUIRED] Reference to the DEP/PIA number or BDS prime. Child of metadata. | string |
| **resource_name** | [REQUIRED] Partial name of the bucket; see above for bucket naming | string |
| **storage_class** | [REQUIRED] Storage class of the bucket | string |
| **lifecycle_age_days** | [OPTIONAL] Set retention time on the data in the bucket. Default value: 365 days. | int |
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


### Example

```
kind: bucket
version: v1
metadata:
  dep: "12"
resource_name: 'bucket_2'
storage_class: 'STANDARD'
lifecycle_age_days: 90
iam_binding:
    users:
      subscribers:
        - principal: user:dong.yang@telus.com
          expiry: datetime(2020,10,25)
        - principal: user:mark.gates@telus.com
          expiry: datetime(2022,12,25)
      publishers:
        - principal: user:mark.gates@telus.com
          expiry: datetime(2022,12,25)
        - principal: user:dong.yang@telus.com
          expiry: datetime(2022,12,25)
    service_accounts:
      subscribers:
      publishers: 
```
