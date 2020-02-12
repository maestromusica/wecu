#!/usr/bin/python

import sys

request_counter = 0
response_counter = 0

for line in sys.stdin:
    line = line.strip().split('\t')
    if line[0] == 'request_counter':
        request_counter += int(line[1])
    elif line[0] == 'response_counter':
        response_counter += int(line[1])
    else:
        print(line[0])
        print('error')
        sys.exit(1)

print(request_counter)
print(response_counter)