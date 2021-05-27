#!/usr/bin/env python
from pathlib import Path

from jinja2 import Template
import pandas as pd
import requests


def get_extension(pypi_package, pypi_version):
    # """Detect which file extension should be used for the package in PyPi."""
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

# Load our jinja2 template that we used to build the specs.
with open('python-azure-sdk.template.spec', 'r') as fileh:
    template_content = fileh.read()
template = Template(template_content)

# Read the list of packages from a recent `pip freeze` on azure-cli so we
# only package what's necessary for the CLI.
with open('azure-sdk-allowlist.txt', 'r') as fileh:
    allow_list = fileh.read().split('\n')

packages = []

# Iterate over the Azure SDK packages.
for i, data in df.iterrows():

    # Skip any packages that aren't in our pip freeze allow list.
    if data.Package not in allow_list:
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

    # Namespace packages don't have sitelib files.
    if "nspkg" in data.Package:
        del package_data['files']['sitelib']

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

    # The mgmt-datalake-nspkg has a couple of extra things to package.
    if "mgmt-datalake-nspkg" in data.Package:
        package_data["files"]["base_init"] = (
            "%{python3_sitelib}/azure/mgmt/datalake/__init__.py"
        )
        package_data["files"]["base_init_pycache"] = (
            "%{python3_sitelib}/azure/mgmt/datalake/__pycache__/__init__*"
        )


    packages.append(package_data)

with open('python-azure.spec', 'w') as fileh:
    fileh.write(
        template.render(
            packages=packages
        )
    )
