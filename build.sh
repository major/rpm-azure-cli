#!/bin/bash
set -euxo pipefail

SPEC=$1
rpmdev-spectool -R -g $SPEC
rpmbuild -bs $SPEC | tee /tmp/srpm-name.txt
SRPM_NAME=$(grep Wrote /tmp/srpm-name.txt | awk '{print $2}')
sudo mock -r /etc/mock/fedora-rawhide-x86_64.cfg --with=check \
    -a https://download.copr.fedorainfracloud.org/results/mhayden/azure-cli/fedora-rawhide-x86_64/ \
    --postinstall \
    $SRPM_NAME
rpmlint /var/lib/mock/fedora-rawhide-x86_64/result/*.rpm
