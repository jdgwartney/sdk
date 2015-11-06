#!/bin/bash

if [ $# -ne 2 ]
then
  echo "usage: $(basename $0) <e-mail> <api-token>"
  exit 1
fi

typeset -r EMAIL=$1
typeset -r API_TOKEN=$2

curl -X PUT -u "$EMAIL:$API_TOKEN" "https://premium-api.boundary.com/v1/plugins/private/boundary_plugin_shell/boundary/boundary-plugin-shell"
