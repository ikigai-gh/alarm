#!/bin/sh
#
# Builds a docker image

set -xe

docker build . -t alarm:0.1.0
