#!/bin/python

from urllib.request import Request, urlopen, URLopener
import sys
import json
import subprocess
import os


def get_list_of_crawls():
    req = Request('https://index.commoncrawl.org/collinfo.json')
    resp = urlopen(req).read().decode('utf-8')
    crawls_obj = json.loads(resp)

    crawls = []
    for c in crawls_obj:
        crawls.append((c['name'], c['id']))

    return crawls

def print_crawls(crawls):
    i = 0
    for c in crawls:
        if 'ARC' not in c[0]:
            print('{}. {}'.format(i, c[0].replace('Index', '')))
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

    return crawls[crawl_no][0]

########
# MAIN #
########


name_of_crawl = choose_crawl_and_download_paths()

full_size_str = input("Full crawl or sample? [f/s]: ")
if full_size_str == 'f':
    os.system('mv paths input_paths')
else:
    #Sample selection
    subset_size = 0
    try:
        subset_size = int(input("Choose subset size: "))
    except:
        print("Enter a valid integer")
        sys.exit(1)

    random_str = input("Random sample? [y/n]: ")
    if random_str == 'y':
        os.system('shuf -n {} paths > input_paths'.format(subset_size))
    else:
        subprocess.call("head -{} paths > input_paths".format(subset_size), shell=True)
    
with open("crawl_name.txt", "w+") as cn_f:
    cn_f.write(name_of_crawl.replace("Index", ""))