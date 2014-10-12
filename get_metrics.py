#!/usr/bin/env python

'''
Sets creates or updates a metric from a JSON file
'''

import json
import os
from pprint import pprint
from string import split
import sys
import argparse
import logging
import re

import requests


class GetMetrics():

  def __init__(self):
    '''
    Initialize the instance
    '''
    self.metrics = None
    # Get credentials and end point information TODO: Split out into another class
    self.email = os.environ['BOUNDARY_PREMIUM_EMAIL']
    self.key = os.environ['BOUNDARY_PREMIUM_API_TOKEN']
    self.apihost = os.environ['BOUNDARY_PREMIUM_API_HOST']
    self.parser = argparse.ArgumentParser(description='Export metric definitions')
    self.filter_expression = None
    
  def initialize(self):
    '''
    Initialization operations
    '''
    self.parseArgs()
    if self.args.debug == True:
      level = logging.DEBUG
    else:
      level = logging.ERROR
    if self.args.patterns:
      self.filter_expression = re.compile(self.args.patterns)
    else:
      self.filter_expression = None

  def parseArgs(self):
    self.parser.add_argument('-d','--debug',dest='debug',action='store_true',help='Enables debugging')
    self.parser.add_argument('-e','--email',dest='email',action='store',help='e-mail uses to create the account')
    self.parser.add_argument('-p', '--pattern',metavar='pattern',dest='patterns', action='store',
                    help='text pattern to use search the name of the metric')
    self.parser.add_argument('-t','--api-key',dest='apikey',required=False,action='store')
    self.parser.add_argument('-v', dest='verbose', action='store_true',help='verbose mode')

    self.args = self.parser.parse_args()

    # Output the collected arguments
    logging.debug(self.args.debug)
    logging.debug(self.args.email)
    logging.debug(self.args.patterns)
    logging.debug(self.args.apikey)
    logging.debug(self.args.verbose)
    

  def fetch(self):
    '''
    Make an API call to get all the metrics associated with the account
    '''
    project = split(self.key, '-')[-1]
    url = "https://{0}/project/{1}/metricsEdit".format(self.apihost, project)
    headers = {'content-type': 'application/json'}
    r = requests.get(url, auth=(self.email, self.key))
    if r.status_code != 200:
      print(url)
      print(headers)
      print(r)
    self.metrics = json.loads(r.text)
    logging.debug(r.text)

  def get(self):
    '''
    Read the JSON file and parse into a dictionary
    '''
    self.fetch()
    self.filter()
    self.output()
    
  def filter(self):
    '''
    Apply the criteria to filter out on the metrics required
    '''
    metrics = self.metrics['result']
    new_metrics = []
    for m in metrics:
      if self.filter_expression != None:
        if self.filter_expression.match(m['name']):
          new_metrics.append(m)
    self.metrics['result'] = new_metrics
      
  def output(self):
    out = json.dumps(self.metrics,sort_keys=True,indent=4,separators=(',', ': '))
    print(out)
        
if __name__ == "__main__":
  p = GetMetrics()
  p.initialize()
  p.get()
