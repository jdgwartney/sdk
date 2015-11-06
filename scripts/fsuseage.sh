#!/bin/bash
# Copyright 2014 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

usage() {
  echo "useage: $(basename $0) <mount point>"
}

OutputMetric() {
  typeset -r metric=$1
  typeset -r value=$2
  typeset -r source=$3

  echo "$metric $value $source"
}

Main() {
  if [ $# -ne 1 ]
  then
    usage
    exit 1
  fi
  typeset -r metric="BOUNDARY_FILE_SPACE_CAPACITY"
  typeset -r mount_point=$1
  typeset -r source=$(hostname)

  used=$(df -kP $mount_point | tail -1 | awk '{print $5}' | tr -d '%')
  used=$(python -c "print(str($used/100.0))")

  OutputMetric $metric $used $source
}

Main $*
