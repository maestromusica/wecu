#!/bin/python

import urllib2

def get_list_of_crawls():
  response = urllib2.urlopen('https://commoncrawl.org/the-data/get-started/')
  html = response.read()



