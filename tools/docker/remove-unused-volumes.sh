#!/usr/bin/env bash

echo "Removing unused volumes"
docker system prune --volumes --force