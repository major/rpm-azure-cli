#!/bin/bash
set -euo pipefail

pip download --no-binary :all: --no-deps $1 > /tmp/files_from_pypi.txt
SOURCE=$(egrep -o "\.*/.*.[tar.gz|zip]" /tmp/files_from_pypi.txt)
echo $SOURCE

if [[ $SOURCE =~ .zip ]]; then
    unzip -l $SOURCE | egrep -i "license|readme"
else
    tar tf $SOURCE | egrep -i "license|readme"
fi
