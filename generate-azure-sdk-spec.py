#!/usr/bin/env python
from pathlib import Path

from jinja2 import Template
import pandas as pd
import requests


def get_extension(pypi_package, pypi_version):
    # """Detect which file extension should be used for the package in PyPi."""
    print(f"Checking for file extension for {pypi_package}")
    pypi_url = f"https://pypi.org/pypi/{pypi_package}/json"
    resp = requests.get(pypi_url).json()

    filename = next(x['filename'] for x in resp['releases'][pypi_version] if x['packagetype'] == 'sdist')

    if Path(filename).suffix == '.zip':
        return "zip"

    return "tar.gz"

# Get the CSV of the latest SDK releases from Microsoft's jekyll site.
sdk_csv = (
    "https://raw.githubusercontent.com/Azure/azure-sdk/master/_data/releases/"
    "latest/python-packages.csv"
)

# We only care about these colums from the CSV.
filtered_columns = [
    'Package',
    'VersionGA',
    'DisplayName',
    'ServiceName'
]

# Read the CSV, keep the coulumns we care about, and drop any rows without a
# GA version.
df = pd.read_csv(sdk_csv).filter(items=filtered_columns).dropna()
df = df.sort_values(by=['Package'])

# Drop any duplicate packages.
df = df.drop_duplicates(subset=['Package'])

# Load our jinja2 template that we used to build the specs.
with open('python-azure-sdk.template.spec', 'r') as fileh:
    template_content = fileh.read()
template = Template(template_content)

# List of packages to skip because they have no source in pypi. 😞
skip_list = [
    "azure",  # deprecated
    "azure-ai-formrecognizer",  # has no files 🤷🏻‍♂️
    "azure-eventhub-checkpointstoreblob",  # not needed
    "azure-eventhub-checkpointstoreblob-aio",  # not needed
    "azure-cognitiveservices-speech",  # only pre-compiled wheel available
    "azure-devtools",  # not needed
    "azure-mgmt",  # deprecated
    "azure-mgmt-documentdb",  # can't build wheel
    "azure-monitor",  # can't build wheel
    "azure-servicemanagement-legacy",  # not needed
    "azure-storage",  # deprecated
    "azureml-sdk",  # only pre-compiled wheel available
    "doc-warden",  # only needed for docs
    "msrest",  # already packaged
    "msrestazure",  # already packaged
    "tox-monorepo",  # only used for testing
    "uamqp",  # not needed
]

packages = []

# Iterate over the Azure SDK packages.
for i, data in df.iterrows():

    # Skip any packages that aren't in our pip freeze allow list.
    # if data.Package not in allow_list:
    #     continue

    # Skip any packages in the skip_list.
    if data.Package in skip_list:
        continue

    # Set up data for the package.
    package_data = {
        "summary": f"Microsoft Azure Python SDK - {data.DisplayName}",
        "version": data.VersionGA,
        "name": data.Package,
        "short_name": data.Package.replace("azure-", ""),
        "slashed_name": data.Package.replace('-', '/'),
        "underscored_name": data.Package.replace("-", "_"),
        "extension": get_extension(data.Package, data.VersionGA),
    }

    # Set the default set of files that should appear in the package.
    package_data['files'] = {
        "sitelib": (
            "%{python3_sitelib}/"
            f"{package_data['slashed_name']}"
        ),
        "distinfo": (
            "%{python3_sitelib}/"
            f"{package_data['underscored_name']}-*.dist-info/"
        )
    }

    # Namespace packages don't have any sitelib files to package.
    if "nspkg" in data.Package:
        del package_data['files']['sitelib']

    # Extras: azure-data-nspkg
    if data.Package == "azure-data-nspkg":
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/data/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/data/__pycache__/__init__*"
        )

    # Extras: azure-datalake-store
    if data.Package == "azure-datalake-store":
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/datalake/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/datalake/__pycache__/__init__*"
        )

    # Extras: azure-digitaltwins-nspkg
    if data.Package == "azure-digitaltwins-nspkg":
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/digitaltwins/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/digitaltwins/__pycache__/__init__*"
        )

    # Extras: azure-kusto-data
    if data.Package == "azure-kusto-data":
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/kusto/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/kusto/__pycache__/__init__*"
        )
        package_data["files"]["pth_file"] = (
            "%{python3_sitelib}/azure_kusto_data-*.pth"
        )

    # Extras: azure-mgmt-datalake-analytics
    if data.Package == "azure-mgmt-datalake-analytics":
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/mgmt/datalake/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/mgmt/datalake/__pycache__/__init__*"
        )

    # Extras: azure-common
    if data.Package == "azure-common":
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/profiles/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/profiles/__pycache__/__init__*"
        )
        package_data["files"]["base_init_multiapiclient"] = (
            "%{python3_sitelib}/azure/profiles/multiapiclient.py"
        )
        package_data["files"]["base_init_pycache_multiapiclient"] = (
            "%{python3_sitelib}/azure/profiles/__pycache__/multiapiclient*.pyc"
        )

    # Extras: azure-storage-nspkg
    if data.Package == "azure-storage-nspkg":
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/storage/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/storage/__pycache__/__init__*"
        )

    # The databoxedge package oddly has files under mgmt/datab/. 🤷🏻‍♂️
    if "databoxedge" in data.Package:
        package_data["files"]["sitelib_datab"] = (
            "%{python3_sitelib}/azure/mgmt/datab"
        )

    # The core package needs a few extra things from the base azure directory.
    if "mgmt-core" in data.Package:
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/__pycache__/__init__*"
        )
        package_data["files"]["base_mgmt_init"] = (
            "%{python3_sitelib}/azure/mgmt/__init__.py"
        )
        package_data["files"]["base_mgmt_init_pycache"] = (
            "%{python3_sitelib}/azure/mgmt/__pycache__/__init__*"
        )

    # mgmt-cosmosdb extras
    if data.Package == "azure-mgmt-cosmosdb":
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/cosmosdb/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/cosmosdb/__pycache__/__init__*"
        )

    # azure-storage-file-datalake has weird paths. 🤦🏻‍♂️
    if "storage-file-datalake" in data.Package:
        package_data["files"]["sitelib"] = (
            "%{python3_sitelib}/azure/storage/filedatalake"
        )

    # azure-storage-file-share has weird paths. 🤦🏻‍♂️
    if "storage-file-share" in data.Package:
        package_data["files"]["sitelib"] = (
            "%{python3_sitelib}/azure/storage/fileshare"
        )

    packages.append(package_data)

with open('python-azure.spec', 'w') as fileh:
    fileh.write(
        template.render(
            packages=packages
        )
    )
