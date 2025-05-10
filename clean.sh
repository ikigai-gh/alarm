#!/bin/sh

set -x

docker compose -f compose_dev.yaml -f compose.yaml down
