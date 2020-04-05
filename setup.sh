#!/bin/sh

# Usage:
#   Pass password to cluster as parameter 1

cp /etc/hadoop/conf/slaves ./hosts

# Dependencies
sudo apt-get install parallel
sudo apt-get install pigz
sudo apt install sshpass

# Matplot lib
python -m pip install -U pip
sudo python -m pip install -U matplotlib

xargs -I '{}' sshpass -p $1 ssh -o "StrictHostKeyChecking no" {} "sudo apt install pigz" < hosts

# Set up password-less communication
ssh-keygen -t rsa -f /home/cc/.ssh/id_rsa -P ""
cat hosts | parallel "cat /home/cc/.ssh/id_rsa.pub | sshpass -p '$1' ssh {} 'cat >> .ssh/authorized_keys'"
parallel --sshloginfile hosts --onall --jobs 1 --will-cite "grep -c ^processor" ::: "/proc/cpuinfo" 2>/dev/null | head -1 > cores.txt
