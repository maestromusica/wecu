# Wee Common Crawl Utility (`wecu`)

Apache Hadoop is seen by many as the default choice for batch processing large scale data but, compared to alternatives like Apache Spark, its performance often leaves a lot to be desired - even for non-iterative workloads.
This utility uses efficient bash utilities to allow you to use your existing Hadoop Streaming scripts without the overheads and complicated configuration of Apache Hadoop.

`wecu` can be configured manually to run on any cluster you might have access to, but it works best on Azure HDInsight clusters as it will configure itself and install the required dependencies automatically.

`wecu` will stream the Common Crawl files from Amazon AWS (where the dataset is hosted) and run the required computation, as detailed below. 

# Usage
To automatically configure the cluster (if you are using Azure HDInsight) run:

## Setup and configuration
```bash
git clone https://github.com/maestromusica/wecu
# `cd` to the wecu directory and use ./wecu or add the directory to $PATH

# To configure the tool and install dependencies
wecu setup [cluster_password] 

# To check that the required files are in place
wecu setup [cluster_password] --check_files 
```

### Choosing a sample of Common Crawl files
```bash
# Opens a wizzard that will present you with a list of crawls available for
# streaming, let you choose file type (WARC/WAT/WET), the size of the sample,
# and whether you want a random sample or just the first N files.
wecu generate-sample
```

### Viewing configuration 
```bash
# Display a list of files
wecu list machines

# Display the currently chosen month & number of files
wecu list input_files

# Display the filenames of all choosen files
wecu list input_files --all
```

# Arbitrary commands 
Execute the same command on all machines in the cluster
```
wecu execute "sudo apt-get install foobar"
wecu execute "./setup.sh" --transfer_file setup.sh
```
# MapReduce/Hadoop Streaming jobs
Run exisitng Hadoop Streaming code or write new MapReduce jobs easily in any programming language.
```
wecu mapred ./mapper.py ./reducer.py

# You can adjust the number of simultaneous map tasks (default = # logical cores)
wecu mapred --jobs-per-worker 12 ./mapper.py ./reducer.py
```

# ''Scan-and-count" jobs without  writing any code
I dubbed the workloads that go through ("**scan**") a sample of Common Crawl and **count** the occurrences of a given string, or count the number of matches of a certain regular expression.
Those workloads are very common when analysing Common Crawl, and can be run using `wecu` without writing any code:

```
# Count occurences of "foo" and "bar"
wecu sac "foo" "bar"

# Count the number of matches for the "^WARC-Type: response" regex
wecu sac --regex "^WARC-Type: response"

# You can use as many regex/strings as you want - runtime grows
# linearly with the number of regex/strings you provide
wecu sac --regex \
         "^WARC-Type: response" \
         "^WARC-Type: request"

# You can display the results per file, without aggregating the results
wecu sac --regex \
         --by-file \
         "^WARC-Type: response" \
         "^WARC-Type: request"

# You can adjust the number of simultaneous map tasks (default = # logical cores)
wecu sac --jobs-per-worker 8 "keyword"
```

# Monitor CPU utilisation
You can monitor CPU utilisation on all worker machines simultaneously - the output from each machine will be saved to a fine on the head node (from which you should run this command), and the utilisation will be plotted and the graph will be saved under the location you provided.
```
wecu utilisation graph_filename.png

# Adjust how long the utilisation will be monitored for (default = 120 seconds)
wecu utilisation --seconds 600 graph_filename.png
```
