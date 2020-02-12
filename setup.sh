#!/bin/sh

# Usage:
#   Pass password to cluster as parameter 1

cp /etc/hadoop/conf/slaves ./hosts

# Dependencies
sudo apt-get install parallel
sudo apt-get install pigz
sudo apt install sshpass

# TODO remove password from here
xargs -I '{}' sshpass -p $1 ssh -o "StrictHostKeyChecking no" {} "sudo apt install pigz" < hosts

# Set up password-less communication
ssh-keygen -t rsa -f /home/cc/.ssh/id_rsa -P ""
cat hosts | parallel "cat /home/cc/.ssh/id_rsa.pub | sshpass -p '$1' ssh {} 'cat >> .ssh/authorized_keys'"


#time parallel \
#    --sshloginfile hosts \
#    --transferfile mapper.py \
#    --will-cite \
#    --jobs 8 \
#    --workdir $PWD \
#    -a input_paths  \
#    'curl -s -N "https://commoncrawl.s3.amazonaws.com/{}" | unpigz -dp 1 -c | ./mapper.py'
