time parallel \
    --sshloginfile hosts \
    --transferfile ./sac_mapper.py \
    --will-cite \
    --jobs 8 \
    --workdir $PWD \
    -a input_paths  \
    "curl -s -N 'https://commoncrawl.s3.amazonaws.com/{}' | unpigz -dp 1 -c | ./sac_mapper.py" \
    | ./sac_reducer.py