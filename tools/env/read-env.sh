#!/bin/bash

. "$(dirname "${BASH_SOURCE[0]}")/../bash/helpers.sh"

FILE=$1

if [ -z "${FILE}" ]; then
  echo 'Usage: read-env <file>'
  exit 1;
fi

read_env_file "$FILE"
