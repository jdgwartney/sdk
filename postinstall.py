#!/usr/bin/env python
from sys import stderr
import fnmatch
import os

stderr.write("Running post install...")
dir="scripts"
for file in os.listdir(dir):
  if fnmatch.fnmatch(file,"*"):
    file = os.path.join(dir,file)
    os.chmod(file, 0755)

stderr.write("done\n")

exit(0)
