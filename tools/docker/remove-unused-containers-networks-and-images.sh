#!/usr/bin/env bash

echo "Removing unused containers, networks, and images"
docker system prune --all --force
