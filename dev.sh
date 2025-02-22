#!/bin/sh
#
# Run a DEV container

set -xe

docker run --rm -e ENV=DEV --name alarm_dev alarm:0.1.0
