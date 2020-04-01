cores=`cat cores.txt`

time parallel \
    --sshloginfile hosts \
    --transferfile "$1" \
    --transferfile "$2" \
    --will-cite \
    --jobs $cores \
    --retries 3 \
    --workdir $PWD \
    -a input_paths  \
    "curl -s -N 'https://commoncrawl.s3.amazonaws.com/{}' | unpigz -dp 1 -c | $1" 2>&1 | grep -v 'Authorized uses only' | \
    sort | \
    eval $2

