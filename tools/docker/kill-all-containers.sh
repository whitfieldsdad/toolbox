#!/usr/bin/env bash

#: Get all running containers.
CONTAINERS=$(docker ps -q)

#: Kill 'em.
if [[ -n ${CONTAINERS} ]]; then
  docker kill "${CONTAINERS}"
fi
