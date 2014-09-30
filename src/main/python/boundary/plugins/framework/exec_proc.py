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

from subprocess import Popen,PIPE
import shlex
import logging
from string import replace

class ExecProc:
    
    def __init__(self):
        self.command = None
        self.debug = False
        
    def setDebug(self,debug):
        self.debug = debug
        
    def setCommand(self,command):
        if type(command) != str:
            raise ValueError
        self.command = command
        
    def execute(self):
        if self.command == None:
            raise ValueError
        args = shlex.split(self.command)
        if self.debug == True:
            logging.info("command=\"%s\"",args)
        p = Popen(args,stdout=PIPE)
        o,e = p.communicate()
        if self.debug == True:
            logging.info("before: " + ':'.join(x.encode('hex') for x in o))
        # Remove carriage returns from output
        o = replace(o,"\r","")
        if self.debug == True:
            logging.info("after: " + ':'.join(x.encode('hex') for x in o))
        if self.debug == True:
            logging.info("output=\"%s\"",o)
            logging.info(':'.join(x.encode('hex') for x in o))
        return o

