#!/usr/bin/python

import sys
from collections import defaultdict

counters = defaultdict(int)

for line in sys.stdin:
    try:
        line = line.strip().split('\t')
        k = line[0] 
        v = line[1]
    except:
        continue

    counters[k] += int(v)

for k in counters:
    print("{}\t{}".format(k, counters[k]))
