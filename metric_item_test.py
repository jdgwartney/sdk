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

import unittest
from metric_item import MetricItem

class TestMetricItem(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        m = MetricItem();

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testConstructor(self):
        m = MetricItem()
        
    def testName(self):
        m = MetricItem();
        m.setName("foo")
        self.assertEquals(m.getName(),"foo","Names not equal")
        
    def testNameType(self):
        m = MetricItem();
        m.setName("foo")
        self.assertTrue(type(m.getName()) == str,"Name is not a string")
        
    def testPollInterval(self):
        m = MetricItem();
        m.setPollingInterval(100)
        self.assertEquals(m.getPollingInterval(),100,"Poll intervals not equal")
        
    def testPollIntervalType(self):
        m = MetricItem();
        m.setPollingInterval(1000)
        self.assertTrue(type(m.getPollingInterval()) == int)
        
    def testPollInterval(self):
        m = MetricItem();
        m.setDebug(True)
        self.assertEquals(m.getDebug(),True,"Debug not equal")
        
    def testCommand(self):
        m = MetricItem()
        m.setCommand("snafu")
        self.assertEquals(m.getCommand(),"snafu","Commands not equal")

if __name__ == '__main__':
    unittest.main()