
# Get hardware utilisation at each machine 
parallel --sshloginfile hosts --onall --jobs 1 --will-cite "iostat -x 1 {} > usage_raw.txt" ::: "10"
parallel --sshloginfile hosts --onall --jobs 1 --will-cite 'cat usage.txt | grep "avg-cpu" -A 1 | grep -oP "^.*?\d+.\d+\s" | grep -oP' ::: '"[\w\.]+"'
cat hosts | xargs -i scp -o "StrictHostKeyChecking no" {}:/home/cc/usage_cpu.txt ./{}.usage.txt