cores=`cat cores.txt`
if [ "$1" -ne "-1" ]; 
then
    cores=$1
fi

time parallel \
    --sshloginfile hosts \
    --transferfile "$2" \
    --transferfile "$3" \
    --will-cite \
    --jobs $cores \
    --retries 3 \
    --workdir $PWD \
    -a input_paths  \
    "curl -s -N 'https://commoncrawl.s3.amazonaws.com/{}' | unpigz -dp 1 -c | $2" 2>&1 | grep -v 'Authorized uses only' | \
    sort | \
    eval $2

