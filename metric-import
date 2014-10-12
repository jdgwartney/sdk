#!/usr/bin/env python

'''
Sets creates or updates a metric from a JSON file
'''

import argparse
import json
import logging
import os
from pprint import pprint
import sys

import requests

'''

'''
class MetricImport():

  def __init__(self):
    self.metrics = None
    self.parser = argparse.ArgumentParser(description='Import metric definitions')
    self.path = None
    self.email = os.environ['BOUNDARY_PREMIUM_EMAIL']
    self.key = os.environ['BOUNDARY_PREMIUM_API_TOKEN']
    self.apihost = os.environ['BOUNDARY_PREMIUM_API_HOST']
    
  def initialize(self):
      self.parseArgs()
      self.path = self.args.path
      
    
  def parseArgs(self):
    '''
    Configure handling of command line arguments
    '''
    self.parser.add_argument('-d','--debug',dest='debug',action='store_true',help='Enables debugging')
    self.parser.add_argument('-e','--email',dest='email',action='store',help='e-mail used to create the account')
    self.parser.add_argument('-f','--file',dest='path',action='store',required=True,help='Path to JSON file')
    self.parser.add_argument('-t','--api-key',dest='apikey',required=False,action='store',help='Boundary API Key')
    self.parser.add_argument('-v', dest='verbose', action='store_true',help='verbose mode')

    self.args = self.parser.parse_args()

    # Output the collected arguments
    logging.debug(self.args.apikey)
    logging.debug(self.args.debug)
    logging.debug(self.args.email)
    logging.debug(self.args.path)
    logging.debug(self.args.verbose)

  def load(self):
    '''
    Load the metrics file from the given path
    '''
    f = open(self.path,"r")
    self.metrics_json = f.read()

  def parse(self):
      '''
      Parse JSON into a dictionary
      '''
      self.metrics = json.loads(self.metrics_json)

  def put(self):
    '''
    Read the JSON file and parse into a dictionary
    '''
    self.load()
    self.parse()
    metrics = self.metrics['result']
    for m in metrics:
        self.createUpdate(m)

  def createUpdate(self,metric):
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
      m['name'] = metric['name']
      if metric['description'] != None:
          m['description'] = metric['description']
      
      if metric['displayName'] != None:
          m['displayName'] = metric['displayName']
      
      if metric['displayNameShort'] != None:
          m['displayNameShort'] = metric['displayNameShort']
    
      if metric['defaultAggregate'] != None:
          m['defaultAggregate'] = metric['defaultAggregate']
          
      if metric['defaultResolutionMS'] != None:
          m['defaultResolutionMS'] = metric['defaultResolutionMS']

      if metric['isDisabled'] != None:
          m['isDisabled'] = metric['isDisabled']
          
      url = "https://{0}/v1/metrics/{1}".format(self.apihost,metric['name'])

      payload = json.dumps(m)
      headers = {'content-type': 'application/json'}
      r = requests.put(url,data=payload,headers=headers,auth=(self.email,self.key))
      if r.status_code != 200:
        print(url)
        print(headers)
        print(r)
        
if __name__ == "__main__":
  p = MetricImport()
  p.initialize()
  p.put()
