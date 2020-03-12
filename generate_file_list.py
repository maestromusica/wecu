#!/bin/python

from urllib.request import Request, urlopen, URLopener
import sys
import json
import subprocess


def get_list_of_crawls():
    req = Request('https://index.commoncrawl.org/collinfo.json')
    resp = urlopen(req).read().decode('utf-8')
    print(str(resp))
    crawls_obj = json.loads(resp)

    crawls = []
    for c in crawls_obj:
        crawls.append((c['name'], c['id']))

    return crawls

def print_crawls(crawls):
    i = 0
    for c in crawls:
        print('{}. {}'.format(i, c[0]))
        i += 1

def choose_crawl_and_download_paths():
    crawls = get_list_of_crawls()
    print("Select a crawl [0-{}]:".format(len(crawls)))
    print_crawls(crawls)
    try:
        crawl_no = int(input("Crawl number [0-{}]:".format(len(crawls))))
    except:
        print('Error: Enter a valid crawl number')
        sys.exit(1)

    file_type = input("File Type [wat/wet/warc]:").lower()

    if file_type not in ['warc', 'wat', 'wet']:
        print("Error: Enter a valid file type")
        sys.exit(1)

    url_to_fetch = "https://commoncrawl.s3.amazonaws.com/crawl-data/{}/{}.paths.gz".format(crawls[crawl_no][1], file_type)
    path_file_opener = URLopener()
    path_file_opener.retrieve(url_to_fetch, "paths.gz")

    subprocess.check_output(['gunzip', '--force', 'paths.gz'])

########
# MAIN #
########


choose_crawl_and_download_paths()

# TODO allow random subset or full set

subset_size = 0
try:
    subset_size = int(input("Choose subset size: "))
except:
    print("Enter a valid integer")
    sys.exit(1)

subprocess.call("head -{} paths > input_paths".format(subset_size), shell=True)
    

