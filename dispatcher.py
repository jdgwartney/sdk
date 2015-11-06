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

import random
from time import sleep
import platform
from sys import stdout
from threading import Thread, Lock
from exec_proc import ExecProc
from metric_thread import MetricThread
import logging

class Dispatcher:
    
    def __init__(self):
        pass
    
    def setConfig(self,config):
        self.config = config
    
    def printMetric(self,metric):
        print(metric + " " + str(random.randrange(0,99)) + " " + platform.node())
    
    def printOutput(self):
        self.printMetric("LOAD_1_MINUTE")
        self.printMetric("LOAD_5_MINUTE")
        self.printMetric("LOAD_15_MINUTE")
        
    def run(self):
        stdoutmutex = Lock() # same as thread.allocate_lock()
        threads = []
        items = self.config.getItems()
        for i in items:
#           print(i.getName())
            thread = MetricThread(i,stdoutmutex) # make/ start 10 threads
            thread.start() # starts run method in a thread
            threads.append(thread)
        for thread in threads:
            thread.join() # wait for thread exits
            
    def execute(self,executeProcess,inputs):
        pool = Pool(processes=len(inputs))
        print(type(executeProcess))
        print(type(inputs))
        print(type(len(inputs)))
        results = pool.map(executeProcess,inputs)
        pool.close()
        return all(results)
