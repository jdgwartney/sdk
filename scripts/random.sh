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


RandomNumber() {
  typeset -r floor=$1
  typeset -r range=$2
  typeset -i number=0
  while [ "$number" -le $floor ]
  do
    number=$RANDOM
    # Scales $number down within $range.
    let "number %= $range"
  done
  echo $number
}

Main() {
   if [ $# -ne 2 ]
   then
     echo "usage: $(basename $0) <min> <max>" 
     echo ""
     echo "where:"
     echo "  min is the smallest value to generate"
     echo "  max is the largest value to generate"
     exit 1
   fi
   typeset -r MIN=$1
   typeset -r RANGE=$(($2 - $1))
   typeset -r SOURCE=$(hostname)
   value=$(RandomNumber "$MIN" "$RANGE")
   echo "BOUNDARY_RANDOM_NUMBER $value $SOURCE"
}

Main $*
exit 0
