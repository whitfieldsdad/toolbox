#!/usr/bin/env bash

INPUT_FILE=$1
if [ -z "$INPUT_FILE" ]; then
  echo "Usage $0 <path>"
  exit 1
fi

jq < "$1"
