

# Stored Procedure Resource Definition

### Naming Convention:
* bq_`<resource_name>`_stored_procedure
* Example: `bq_my_data_stored_procedure`


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
| **definition body** | [REQUIRED] Contain of the stored procedure | string |
| **query_schedule** | [OPTIONAL] If not null, the stored procedule will be executed with the defined schedule | string |

### Example:
```
kind: stored_procedure
version: v1
metadata:
  dep: "144"
description: "stored_procedures"
resource_name: bq_test_stored_procedure
dataset_id: pdc_2
expiration_datetime_staging: datetime(2022,12,25)
expiration_datetime_serving:
definition_body: >
    BEGIN
    INSERT mango_2.bq_audit_run  (_customer_id) VALUES("io");
    END;
query_schedule: every 24 hours
  ```
