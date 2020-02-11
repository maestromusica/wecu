#!/bin/sh

cp /etc/hadoop/conf/slaves ./hosts

# Dependencies
sudo apt-get install parallel
sudo apt-get install pigz
# pip install -U beautifulsoup4