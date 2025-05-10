#!/bin/sh
#
# Run a DEV container

set -xe

docker compose -f compose_dev.yaml up -d
