#!/usr/bin/env bash

IMAGE=$1
if [ -z "${IMAGE}" ]; then
  echo "Usage: export-image <image>"
  exit 1
fi

docker save -o "${IMAGE}".tar "${IMAGE}"
