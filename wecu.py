#!/usr/bin/python

import sys
import argparse

parser = argparse.ArgumentParser(description='Wee CommonCrawl Utlity (WECU) is a CLI tool which allows...')
parser.add_argument('command', 
                    metavar='command',
                    type=str,
                    help='The command to be exectured',
                    choices=['setup', 'list'])

if(len(sys.argv) < 2):
    parser.print_help()
    sys.exit(0)

args = parser.parse_args()

if args.command == 'setup':
    print('Beginning setup')