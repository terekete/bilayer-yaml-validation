import sys
import os
import json
import yaml
import logging
import argparse

from cerberus import Validator


def validate_manifest(manifest: str, manifest_path: str, schema_path: str):

    schema = eval(open(schema_path).read())
    validator = Validator(schema)
    if validator.validate(manifest):
        logging.info(
            "✅\t#### Schema Validation Successful for kind: {kind} - {resource}".format(
                kind=manifest["kind"], resource=manifest["resource_name"].lower()
            )
        )
        return
    else:
        logging.error(
            "#### Schema Validation Failed for kind: {kind} - {resource}".format(
                kind=manifest["kind"], resource=manifest["resource_name"].lower()
            )
        )
        logging.error("Filename: {manifest_path}".format(
            manifest_path=manifest_path))
        print(json.dumps(validator.errors, indent=2))
        sys.exit(1)


# Function to validate if the manifest is null
def validate_manifest_null(manifest: str):
    if manifest is None:
        logging.error(
            "#### YAML Resource Definition is Incomplete - {manifest}".format(
                manifest)
        )
        sys.exit(1)


def process(manifest_path, schema_path):
    with open(str(manifest_path)) as yaml_file:
        file_handler = yaml.load(yaml_file, Loader=yaml.FullLoader)
    validate_manifest_null(file_handler)
    validate_manifest(
        manifest=file_handler, manifest_path=manifest_path, schema_path=schema_path
    )


def get_paths(path):
    tp_list = [
        (os.path.basename(os.path.normpath(root)), root + "/" + file)
        for root, subdirs, files in os.walk(path)
        for file in files
        if file.endswith(".yaml") or file.endswith(".yml")
    ]
    return tp_list


def main():
    logging.basicConfig(
        level=logging.INFO, format="[%(asctime)s] %(levelname)-6s %(message)s"
    )
    parser = argparse.ArgumentParser(description="action-yaml-check")
    parser.add_argument(
        "resource_path",
        help="Path to YAML file being validated",
    )
    args = parser.parse_args()
    resource_path = args.resource_path
    for type, path in get_paths(resource_path):
        if type == "buckets":
            process(path, os.getcwd() + "/schemas/bucket.py")
        elif type == "datasets":
            process(path, os.getcwd() + "/schemas/dataset.py")
        elif type == "external_tables":
            process(path, os.getcwd() + "/schemas/ext_table.py")
        elif type == "materialized_views":
            process(path, os.getcwd() + "/schemas/mat_view.py")
        elif type == "scheduled_queries":
            process(path, os.getcwd() + "/schemas/scheduled_query.py")
        elif type == "stored_procedures":
            process(path, os.getcwd() + "/schemas/stored_procedure.py")
        elif type == "spark_jobs":
            process(path, os.getcwd() + "/schemas/spark_job.py")
        elif type == "tables":
            process(path, os.getcwd() + "/schemas/table.py")
        elif type == "views":
            process(path, os.getcwd() + "/schemas/view.py")
        else:
            logging.error(
                "Unidentified resource definition - {path}".format(path=path))


if __name__ == "__main__":
    main()
