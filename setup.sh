#!/bin/sh

cp /etc/hadoop/conf/slaves ./hosts

# Dependencies
sudo apt-get install parallel
sudo apt-get install pigz
sudo apt install sshpass
# pip install -U beautifulsoup4

# TODO remove password from here
xargs -I '{}' sshpass -p $1 ssh -o "StrictHostKeyChecking no" {} "sudo apt install pigz" < hosts