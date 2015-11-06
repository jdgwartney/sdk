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

class MetricItem:
    
    def __init__(self):
        self.name = ""
        self.pollInterval = 5
        self.command = ""
    
    def setName(self, name):
        if type(name) != str:
            raise ValueError
        self.name = name
        
    def getName(self):
        return self.name
        
    def setPollingInterval(self, pollInterval):
        if type(pollInterval) != int:
            raise ValueError
        self.pollInterval = pollInterval
        
    def getPollingInterval(self):
        return self.pollInterval
    
    def setDebug(self,debug):
        if type(debug) != bool:
            raise ValueError
        self.debug = debug
        
    def getDebug(self):
        return self.debug
        
    def setCommand(self, command):
        if type(command) != str:
            raise ValueError
        self.command = command
        
    def getCommand(self):
        return self.command