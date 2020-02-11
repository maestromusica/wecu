time parallel \
    --will-cite \
    --jobs 8 \
    --workdir $PWD \
    -a input_paths  \
    curl -s -N "https://commoncrawl.s3.amazonaws.com/{}" | unpigz -dp 1 -c | ./mapper.py
    # --sshloginfile hosts \
