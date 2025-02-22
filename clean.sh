#!/bin/sh

set -x

docker stop alarm alarm_dev
docker rm alarm alarm_dev
docker rmi alarm:0.1.0 alarm_dev:0.1.0
