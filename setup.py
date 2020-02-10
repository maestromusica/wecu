#!/bin/bash

import os
import sys
import re

AUTHORISED_HOSTS_FILE_PATH = '/home/cc/.ssh/authorized_keys'

with open(AUTHORISED_HOSTS_FILE_PATH, 'r') as auth_file:
    hosts = auth_file.readlines()
    print(hosts) 
