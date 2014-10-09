#!/usr/bin/env python

import json
from pprint import pprint

metric_file = "now.json"

with open(metric_file) as f:
  metric_data = json.loads(f.read())

records = metric_data['result']

for r in records:
  pprint(r)
