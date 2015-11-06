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
from configuration import Configuration

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testConstructor(self):
        c = Configuration("src/test/resources/test_param.json")
        
    def testEntryCount(self):
        c = Configuration("src/test/resources/test_param.json")
        c.load()
        self.assertEquals(c.getEntryCount(),2,"Entry count does not match")


    def testItems(self):
        c = Configuration("src/test/resources/test_param.json")
        c.load()
        config = c.getItems()
        self.assertEqual(len(config),2)
        self.assertEquals(config[0].getName(),"Echo foo")
        self.assertEquals(config[0].getPollInterval(),5)
        self.assertEquals(config[0].getCommand(),["echo","$HOME"])
        self.assertEquals(config[1].getName(),"Echo bar")
        self.assertEquals(config[1].getPollInterval(),20)
        self.assertEquals(config[1].getCommand(),["echo","$PATH"])
        
    def testEmptyItems(self):
        c = Configuration("src/test/resources/test_param.json")
        self.assertEquals(len(c.getItems()),0,"Items not equal to zero")

if __name__ == '__main__':
    unittest.main()