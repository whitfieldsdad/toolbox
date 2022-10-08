#!/usr/bin/env bash

echo "Attaching to 'redis' container..."
docker exec -it redis redis-cli
