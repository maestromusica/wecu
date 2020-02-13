#!/usr/bin/python

import sys
import argparse

# Top-level parser
parser = argparse.ArgumentParser(description='Wee CommonCrawl Utlity (WECU) is a CLI tool which allows...')
subparsers = parser.add_subparsers(help='A sub-command to be executed')

parser_setup = subparsers.add_parser('setup', help='setup help')
parser_setup.add_argument('--check', action="store_true", help='TODO')

parser_list = subparsers.add_parser('list', help='list help')
parser_list.add_argument('object_to_list', type=str, choices=['machines', 'input_files'], help='TODO')
parser_list.add_argument('--all', action='store_true', help='TODO')

execture_list = subparsers.add_parser('execute', help='execute help')
execture_list.add_argument('command', type=str)
execture_list.add_argument('--file', action="store_true", help="TODO")
execture_list.add_argument('--tranfer_file', action="store_true", help="TODO")

mapred_list = subparsers.add_parser('mapred', help="TODO")
mapred_list.add_argument('mapper', type=str, help='TODO')
mapred_list.add_argument('reducer', type=str, help='TODO')

sac_list = subparsers.add_parser('sac', help='Scan-and-count help')
sac_list.add_argument('pattern', type=str, nargs='+')
sac_list.add_argument('--regex', action="store_true", help="TODO")
sac_list.add_argument('--by-file', action="store_true", help="TODO")
sac_list.add_argument('--jobs-per-worker', type=int, help="TODO")

if(len(sys.argv) < 2):
    parser.print_help()
    sys.exit(0)

args = parser.parse_args()
print(args)

# if args.command == 'setup':
#     print('Beginning setup')
# elif args.command == 'list':
#     print(args)