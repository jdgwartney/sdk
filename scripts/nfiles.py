#!/usr/bin/env python
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

import sys
import fnmatch
import os
import socket

class FileCount:
    
  def __init__(self):
    self.nfiles = 0
    self.dir = None
    
  def usage(self):
    sys.stderr.write("usage: {} <directory>\n".format(os.path.basename(sys.argv[0])))
    sys.stderr.write("\n")
    sys.stderr.write("where:\n")
    sys.stderr.write("   directory - Path of directory to count files\n")

  # We require the path to the directory
  # to count the number of files
  def checkArgs(self,args):
    if len(args) != 2:
      self.usage()
      sys.exit(1)
    self.dir = args[1]

  ### Collect the metric
  def countFiles(self):
    # List the directory, count the number of files
    self.nfiles = 0
    for file in os.listdir(self.dir):
      if fnmatch.fnmatch(file,"*"):
        path = os.path.join(self.dir,file)
        if os.path.isfile(path) or os.path.isdir(path):
          self.nfiles = self.nfiles + 1

  ### Write the metric standard out
  def printMetric(self):
    sys.stdout.write("BOUNDARY_FILE_COUNT {0} {1}\n".format(self.nfiles,socket.gethostname()))

  def execute(self):
    self.checkArgs(sys.argv)
    self.countFiles()
    self.printMetric()

if __name__ == "__main__":
  f = FileCount()
  f.execute()

