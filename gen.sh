#!/bin/bash

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/openapi.yml \
    -g python-fastapi \
    -o /local/app \
    --package-name customer_api