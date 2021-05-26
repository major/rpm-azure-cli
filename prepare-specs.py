#!/usr/bin/env python
"""Generate Azure Python SDK RPM spec files."""
from pathlib import Path

from jinja2 import Template
import pandas as pd
import requests

def get_extension(pypi_package, pypi_version):
    """Detect which file extension should be used for the package in PyPi."""
    pypi_url = f"https://pypi.org/pypi/{pypi_package}/json"
    resp = requests.get(pypi_url).json()

    filename = next(x['filename'] for x in resp['releases'][pypi_version] if x['packagetype'] == 'sdist')

    if Path(filename).suffix == 'zip':
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

# Load our jinja2 template that we used to build the specs.
with open('azure-sdk-template.spec', 'r') as fileh:
    template_content = fileh.read()
template = Template(template_content)

# Read the list of packages from a recent `pip freeze` on azure-cli so we
# only package what's necessary for the CLI.
with open('azure-package-allowlist.txt', 'r') as fileh:
    allow_list = fileh.read().split('\n')

# Iterate over the Azure SDK packages.
for i, data in df.iterrows():

    # Skip any packages that aren't in our pip freeze allow list.
    if data.Package not in allow_list:
        continue

    # Render the spec file template with jinja2.
    summary = f"Microsoft Azure Python SDK - {data.DisplayName}"
    output = template.render(
            version = data.VersionGA,
            srcname = data.Package,
            slashed_srcname = data.Package.replace('-', '/'),
            extension = get_extension(data.Package, data.VersionGA),
            summary = summary
    )

    # Write the spec file.
    filename = f"sdk_specs/python-{data.Package}.spec"
    with open(filename, 'w') as fileh:
        fileh.write(output)
