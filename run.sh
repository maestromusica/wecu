cores=`cat cores.txt`

time parallel \
    --sshloginfile hosts \
    --transferfile mapper.py \
    --transferfile reducer.py \
    --will-cite \
    --retries 3 \
    --jobs $cores \
    --workdir $PWD \
    -a input_paths  \
    'curl -s -N "https://commoncrawl.s3.amazonaws.com/{}" | unpigz -dp 1 -c | ./mapper.py' | \
    sort | \
    ./reducer.py

