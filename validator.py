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
            "✅\t Schema Validation Successful for kind: {kind} - {manifest_path}".format(
                kind=manifest["kind"], manifest_path=manifest_path
            )
        )
        return
    else:
        logging.error(
            "*\t Schema Validation Failed for kind: {kind} - {resource}".format(
                kind=manifest["kind"], resource=manifest["resource_name"].lower()
            )
        )
        logging.error("Filename: {manifest_path}".format(
            manifest_path=manifest_path))
        print(json.dumps(validator.errors, indent=2))
        sys.exit(1)


# Function to validate if the manifest is null
def validate_manifest_null(manifest: str, manifest_path: str):
    if manifest is None:
        logging.error(
            "*\t Error: YAML Resource is Empty or Does Not Exist  - {manifest_path}"
            .format(manifest_path=manifest_path)
        )
        sys.exit(1)


def process(manifest_path):
    with open(str(manifest_path)) as yaml_file:
        file_handler = yaml.load(yaml_file, Loader=yaml.FullLoader)
    validate_manifest_null(file_handler, manifest_path)
    if file_handler["kind"] == 'dataset':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/dataset.py'
        )
    elif file_handler["kind"] == 'table':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/table.py'
        )
    elif file_handler["kind"] == 'view':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/view.py'
        )
    elif file_handler["kind"] == 'materialized_view':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/mat_view.py'
        )
    elif file_handler["kind"] == 'stored_procedure':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/stored_procedure.py'
        )
    elif file_handler["kind"] == 'spark_job':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/spark_job.py'
        )
    elif file_handler["kind"] == 'vertex_pipeline':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/vertex_pipeline.py'
        )
    elif file_handler["kind"] == 'bucket':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/bucket.py'
        )
    elif file_handler["kind"] == 'ext_table':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/ext_table.py'
        )
    elif file_handler["kind"] == 'scheduled_query':
        validate_manifest(
            file_handler,
            manifest_path,
            os.getcwd() + 'main/schemas/scheduled_query.py'
        )
    else:
        logging.error(
            "*\t Error: Unknown manifest kind: {manifest_path}"
            .format(manifest_path=manifest_path)
        )


def get_paths(path):
    tp_list = [
        root + "/" + file
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
    for path in get_paths(resource_path):
        if path:
            process(path)
        else:
            logging.error(
                "*\t Eror: Unidentified resource path - {path}".format(path=path))


if __name__ == "__main__":
    main()
