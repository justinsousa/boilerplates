#!/usr/bin/env bash

TERRAFORM_VERSION=$1
INSTALL=${2:-'yes'}

if [[ -z "${TERRAFORM_VERSION}" ]]; then
    curl -vs https://releases.hashicorp.com/terraform/ 2>&1 | grep terraform/ | cut -f 2 -d '>' | cut -f 1 -d '<'
    echo 'need to pass terraform version as the first arg...pick from one of the current versions shown above'
    exit 1
fi

SYSTEM_TYPE=$(uname | tr '[:upper:]' '[:lower:]')
PROCTYPE=$(uname -m | cut -f 2 -d _)
dl_url="https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_${SYSTEM_TYPE}_amd${PROCTYPE}.zip"

wget ${dl_url}
unzip -o terraform*${TERRAFORM_VERSION}*.zip
[[ "${INSTALL}"  == 'yes' ]] && mv ./terraform /usr/local/bin
