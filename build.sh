#!/bin/bash
set -euxo pipefail

SPEC=$1
rpmdev-spectool -R -g $SPEC
rpmbuild -bs $SPEC | tee /tmp/srpm-name.txt
SRPM_NAME=$(grep Wrote /tmp/srpm-name.txt | awk '{print $2}')

# sudo mock -r /etc/mock/fedora-rawhide-x86_64.cfg \
#     -a https://download.copr.fedorainfracloud.org/results/mhayden/azure-cli/fedora-rawhide-x86_64/ \
#     --postinstall \
#     $SRPM_NAME

sudo mock -r /etc/mock/fedora-rawhide-x86_64.cfg --postinstall $SRPM_NAME

rpmlint /var/lib/mock/fedora-rawhide-x86_64/result/*.rpm

# sudo mock -r /etc/mock/centos-stream-8-x86_64.cfg --with=check \
#     --postinstall \
#     $SRPM_NAME
# rpmlint /var/lib/mock/centos-stream-8-x86_64/result/*.rpm

# copr build --nowait azure-cli $SRPM_NAME
