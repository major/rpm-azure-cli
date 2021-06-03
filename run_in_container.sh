#!/bin/bash
set -euxo pipefail

sudo docker buildx build -f Dockerfile -t azure-cli-rawhide-container --build-arg CACHEBUST=$(date +%s) .
sudo docker run --rm -it azure-cli-rawhide-container az version
