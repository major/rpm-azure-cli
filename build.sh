#!/bin/bash

SPEC=python-azure.spec
rpmdev-spectool -R -g $SPEC
rpmbuild -bs $SPEC | tee /tmp/srpm-name.txt
SRPM_NAME=$(grep Wrote /tmp/srpm-name.txt | awk '{print $2}')
sudo mock -r /etc/mock/fedora-rawhide-x86_64.cfg --with=check $SRPM_NAME
