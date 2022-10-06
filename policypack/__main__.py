from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)


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

PolicyPack(
    name="gcp-python",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        storage_bucket_no_public_read,
        location
    ],
)

