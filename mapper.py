#!/usr/bin/python

import sys

response_counter = 0
request_counter = 0

for line in sys.stdin:
    if line.startswith('WARC-Type: response'):
        response_counter += 1
    if line.startswith('WARC-Type: request'):
        request_counter += 1
    
print('request_counter\t{}'.format(request_counter))
print('response_counter\t{}'.format(response_counter))

