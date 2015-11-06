#!/usr/bin/env python
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
import platform
import random
import sys
from time import sleep
import logging
logging.basicConfig(filename='simple.log',format='%(asctime)s %(message)s',level=logging.DEBUG)

while True:
    s = "SHELL_METRIC" + " " + str(random.randrange(0,99)) + " " + platform.node()
    print(s)
    sys.stdout.flush()
    logging.debug(s)
    sleep(1)
