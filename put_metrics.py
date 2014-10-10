#!/usr/bin/env python

import json
import sys
import os
from pprint import pprint
import requests

'''
Sets creates or updates a metric from a JSON file
'''
class PutMetrics():

  def __init__(self,path):
    self.metrics = None
    self.path = path
    self.email = os.environ['BOUNDARY_PREMIUM_EMAIL']
    self.key = os.environ['BOUNDARY_PREMIUM_API_TOKEN']
    self.apihost = os.environ['BOUNDARY_PREMIUM_API_HOST']

  def getMetricNames():
    return self.manifest['metrics']

  def load(self):
    '''
    Load the metrics file from the given path
    '''
    f = open(self.path,"r")
    self.metrics_json = f.read()

  def parse(self):
      self.metrics = json.loads(self.metrics_json)

  def put(self):
    '''
    Read the JSON file and parse into a dictionary
    '''
    self.load()
    self.parse()
    metrics = self.metrics['result']
    for m in metrics:
        print(m)


# name
# Name of the metric, must be globally unique if creating
# description
# Description of the metric (optional if updating)
# displayName
# Short name to use when referring to the metric (optional if updating)
# displayNameShort
# Terse short name when referring to the metric and space is limited, less than 15 characters preferred. (optional if updating)
# unit
# The units of measurement for the metric, can be percent, number, bytecount, or duration (optional if updating)
# defaultAggregate
# When graphing (or grouping at the 1 second interval) the aggregate function that makes most sense for this metric. Can be sum, avg, max, or min. (optional if updating)
# defaultResolutionMS
# Expected polling time of data in milliseconds. Used to improve rendering of graphs for non-one-second polled metrics. (optional if updating)
# isDisabled
# Is this metric disabled (optional if updating)
  def createUpdate(self,name,
                   description=None,displayName=None,displayNameShort=None,unit=None,defaultAggregate=None,
                   isDisabled=None,defaultResolutionMS=None):
      '''
      name - Name of the metric, must be globally unique if creating
      description - Description of the metric (optional if updating)
      displayName - Short name to use when referring to the metric (optional if updating)
      displayNameShort - Terse short name when referring to the metric and space is limited, less than 15 characters preferred. (optional if updating)
      unit - The units of measurement for the metric, can be percent, number, bytecount, or duration (optional if updating)
      defaultAggregate - When graphing (or grouping at the 1 second interval) the aggregate function that makes most sense for this metric. Can be sum, avg, max, or min. (optional if updating)
      defaultResolutionMS - Expected polling time of data in milliseconds. Used to improve rendering of graphs for non-one-second polled metrics. (optional if updating)
      isDisabled - Is this metric disabled (optional if updating)
      '''
      m = {}
      m['name'] = name
      if description != None:
          m['description'] = description
      
      if displayName != None:
          m['displayName'] = displayName
      
      if displayNameShort != None:
          m['displayNameShort'] = displayNameShort
    
      if defaultAggregate != None:
          m['defaultAggregate'] = defaultAggregate
          
      if defaultResolutionMS != None:
          m['defaultResolutionMS'] = defaultResolutionMS

      if defaultResolutionMS != None:
          m['isDisabled'] = isDisabled
          
      r = requests.post("https://{0}/v1/metrics/{1}".format(self.apihost,name), data=payload)
      print(r)
        
if __name__ == "__main__":

  if len(sys.argv) != 2:
    sys.stderr.write("usage: {0} <path>\n".format(sys.argv[0]))
    sys.exit(1)
    
  p = PutMetrics(sys.argv[1])
  p.put()
