cores=`cat cores.txt`

time parallel \
    --sshloginfile hosts \
    --retries 3 \
    --transferfile ./sac_mapper.py \
    --will-cite \
    --jobs $cores \
    --workdir $PWD \
    -a input_paths \
    "curl -s -N 'https://commoncrawl.s3.amazonaws.com/{}' | unpigz -dp 1 -c | ./sac_mapper.py $*" 2>&1 | grep -v 'Authorized uses only' | \
    ./sac_reducer.py
