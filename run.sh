time parallel--sshloginfile hosts --jobs 8 --workdir $PWD -a input_file_urls curl -s -N "https://commoncrawl.s3.amazonaws.com/{}" | unpigz -dp 1 -c | grep -a -c "WARC-Type: response"
