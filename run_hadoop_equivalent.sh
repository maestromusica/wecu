# This file can be used to run MapReduce jobs using Hadoop in order to compare performance with wecu

hadoop fs -rm -r /output

yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
    -D fs.s3a.aws.credentials.provider=org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider \
    -files mapper.py,reducer.py \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312025.20/warc/CC-MAIN-20190817203056-20190817225056-000* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312025.20/warc/CC-MAIN-20190817203056-20190817225056-001* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312025.20/warc/CC-MAIN-20190817203056-20190817225056-002* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312025.20/warc/CC-MAIN-20190817203056-20190817225056-003* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312025.20/warc/CC-MAIN-20190817203056-20190817225056-004* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312025.20/warc/CC-MAIN-20190817203056-20190817225056-005* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312128.3/warc/CC-MAIN-20190817102624-20190817124624-000* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312128.3/warc/CC-MAIN-20190817102624-20190817124624-001* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312128.3/warc/CC-MAIN-20190817102624-20190817124624-002* \
    -input s3a://commoncrawl/crawl-data/CC-MAIN-2019-35/segments/1566027312128.3/warc/CC-MAIN-20190817102624-20190817124624-003* \
    -output /output \
    -mapper mapper.py \
    -reducer reducer.py
