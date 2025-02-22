#!/bin/sh
#
# Run a PROD container

set -xe

docker run -d --name alarm alarm:0.1.0
