#!/bin/bash
set -euxo pipefail

CLONE_URL=https://github.com/major/rpm-azure-cli

SPECS=$(ls -1 specs/*.spec)
for SPEC in $SPECS; do
    SPEC_BARE=$(basename ${SPEC})
    PKG_NAME=${SPEC_BARE%.*}

    copr-cli add-package-scm \
        --clone ${CLONE_URL} \
        --commit main \
        --subdir specs \
        --spec $SPEC_BARE \
        --name $PKG_NAME \
        --webhook-rebuild off \
        azure-cli
done
