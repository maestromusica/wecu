time parallel \
    --sshloginfile hosts \
    --transferfile "$1" \
    --transferfile "$2" \
    --will-cite \
    --jobs 8 \
    --workdir $PWD \
    -a input_paths  \
    "curl -s -N 'https://commoncrawl.s3.amazonaws.com/{}' | unpigz -dp 1 -c | $1" | \
    sort | \
    eval $2

