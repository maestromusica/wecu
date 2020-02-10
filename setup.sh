#!/bin/sh

cp /etc/hadoop/conf/slaves ./hosts

# Dependencies
sudo apt-get install parallel
# pip install -U beautifulsoup4