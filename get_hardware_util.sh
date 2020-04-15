seconds=$1
wait_seconds=$(expr $1+5)

echo $seconds
echo $wait_seconds

# Get hardware utilisation at each machine 
parallel --sshloginfile hosts --nonall --jobs 1 --will-cite "rm -f usage_raw.txt usage_cpu.txt"
parallel --sshloginfile hosts --nonall --jobs 1 --will-cite "iostat -x 1 $seconds > usage_raw.txt &"
sleep $wait_seconds
parallel --sshloginfile hosts --onall --jobs 1 --will-cite 'cat usage_raw.txt | grep "avg-cpu" -A 1 | grep -oP "^.*?\d+.\d+\s" | grep -oP {} > usage_cpu.txt' ::: '[\w\.]+'
cat hosts | xargs -i scp -o "StrictHostKeyChecking no" {}:/home/cc/usage_cpu.txt ./{}.usage.txt
