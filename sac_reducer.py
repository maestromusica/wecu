#!/usr/bin/python

import sys
from collections import defaultdict

if sys.argv[2] == 'by-file':
    # Show results by file
    for line in sys.stdin:
        print(line.strip())
else:
    # Aggregate results
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
