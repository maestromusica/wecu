#!/usr/bin/python
import os
import sys
import re

is_regex = sys.argv[3] == 'true'
search_terms = sys.argv[4:]
search_terms_counters = dict()

# Initialise
for term in search_terms:
    search_terms_counters[term] = 0

if not is_regex:
    for line in sys.stdin:
        for term in search_terms_counters:
            search_terms_counters[term] += line.count(term)
else:
    for line in sys.stdin:
        for term_regex in search_terms_counters:
            search_terms_counters[term_regex] += len(re.findall(term_regex, line))


for term in search_terms_counters:
    print("{}\t{}".format(term, search_terms_counters[term]))