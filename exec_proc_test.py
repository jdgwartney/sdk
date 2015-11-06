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
from exec_proc import ExecProc

class TestExecProc(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testConstructor(self):
        e = ExecProc()
        self.assertTrue(e != None,"Instance is None")
        
    def testMissingCommand(self):
        try:
            e = ExecProc()
            output = e.execute()
        except ValueError as v:
            self.assertEqual(type(v),ValueError)
        
    def testMissingPath(self):
        try:
            e = ExecProc()
            e.setCommand(["-l"])
            output = e.execute()
        except ValueError as v:
            self.assertEqual(type(v),ValueError)
        
    def testArgsType(self):
        try:
            e = ExecProc()
            e.setCommand("-l")
        except ValueError as v:
            self.assertEqual(type(v),ValueError)
            
    def testExec(self):
        e = ExecProc()
        e.setCommand("ls -l src/test/resources/test-exec")
        output = e.execute()
        self.assertEquals(output,"total 0\n-rw-r--r--  1 davidg  staff  0 Aug 25 12:20 goodbye.txt\n-rw-r--r--  1 davidg  staff  0 Aug 25 12:20 hello.txt\n-rw-r--r--  1 davidg  staff  0 Aug 25 12:20 myDir\n")

if __name__ == '__main__':
    unittest.main()