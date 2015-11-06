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
from metric import Metric

class TestMetric(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAttributes(self):
        metric = Metric()
        metric.setName("foo")
        metric.setValue(10)
        metric.setSource("localhost")
        self.assertEqual(metric.getName(), "foo", "Name does not match")
        self.assertEqual(metric.getValue(),10, "Values does nto match")
        self.assertEqual(metric.getSource(), "localhost", "Source does not match")
        
    def testString(self):
        metric = Metric()
        metric.setName("bar")
        metric.setValue(100)
        metric.setSource("snafu")
        print(str(self))
        self.assertEqual(str(metric), "bar 100 snafu", "String does not match")

if __name__ == '__main__':
    unittest.main()