from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

import json


def storage_bucket_no_public_read_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "gcp:storage/bucketACL:BucketACL" and "predefinedAcl" in args.props:
        acl = args.props["predefinedAcl"]
        if acl == "public-read" or acl == "public-read-write":
            report_violation("Storage buckets acl cannot be set to public-read or public-read-write.")

storage_bucket_no_public_read = ResourceValidationPolicy(
    name="storage-bucket-no-public-read",
    description="Prohibits setting the publicRead or publicReadWrite permission on GCP Storage buckets.",
    validate=storage_bucket_no_public_read_validator,
)

def location_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if "location" in args.props:
        location = args.props["location"]
        if location != "northamerica-northeast1":
            report_violation("Resource location must be set to northamerica-northeast1")

location = ResourceValidationPolicy(
    name="location-must-be-northamerica-northeast1",
    description="Prohibits setting the location to other than northamerica-northeast1",
    validate=location_validator,
)

json_data = json.load(open("allowed_resources.json"))

def resources_types_allow_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type not in json_data["allow_list"]:
        report_violation("resource type not allowed")

resources_types_allow = ResourceValidationPolicy(
    name="resources-types-allow",
    description="Only allow build of certain types of resources",
    validate=resources_types_allow_validator,
)


def bq_datatset_role_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "gcp:bigquery/datasetIamMember:DatasetIamMember":
        role = args.props["role"]
        if role != "roles/bigquery.dataViewer":
            report_violation("Dataset binding can only set role: roles/bigquery.dataViewer")

bq_datatset_role = ResourceValidationPolicy(
    name="bq_datatset_role",
    description="Dataset binding can only set role: roles/bigquery.dataViewer",
    validate=bq_datatset_role_validator,
)

def bq_table_role_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type in ['google-native:bigquery/v2:TableIamMember', 'gcp:bigquery/iamMember:IamMember']:
        role = args.props["role"]
        if role not in ["roles/bigquery.dataViewer", "roles/bigquery.dataOwner"]:
            report_violation("Table binding can only set role: roles/bigquery.dataViewer, roles/bigquery.dataOwner")

bq_table_role = ResourceValidationPolicy(
    name="bq_table_role",
    description="Table binding can only set role: roles/bigquery.dataViewer, roles/bigquery.dataOwner",
    validate=bq_table_role_validator,
)

def bq_resources_names_policy_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type in ["google-native:bigquery/v2:Table","gcp:bigquery/table:Table"]:
        if "tableReference" in args.props:
            if "tableId" in args.props["tableReference"]:
                bq_object_nm = str(args.props["tableReference"]["tableId"])
                if not str(bq_object_nm).startswith("bq_"):
                    report_violation("BigQuery Object (Table/View) Name must start with ** bq_ ** keyword")

bq_resources_names_policy = ResourceValidationPolicy(
    name="bq-resources-names-policy",
    description="Ensuring that BigQuery Object (Table/View) Name starts with ** bq_ ** keyword",
    validate=bq_resources_names_policy_validator,
)

PolicyPack(
    name="gcp-python",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        storage_bucket_no_public_read,
        location,
        resources_types_allow,
        bq_datatset_role,
        bq_table_role,
        bq_resources_names_policy
    ],
)