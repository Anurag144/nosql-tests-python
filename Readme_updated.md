#NoSQL Performance Tests using docker containers of databases

This repository contains the performance evaluation tests for different nosql databases. The repository is developed and owned by Claudius Weinberger. The original repository makes use of standalone databases installed on the local machine. In our implementation we will make use of docker containers of different databases.Currently only mangodb database is supported.

##Setting up the docker containers

Install docker desktop from [here](https://www.docker.com/products/docker-desktop).

###mongodb

####Search dockehub for mongodb

docker search mongo

####Running a mongodb docker container
```` bash
docker container run \
                --detach                                        # run docker in background
                --name  <container_name>                        # container name
                --publish= "27017:27017" \                      # which port to use <choice>:<default>
                --volume= $HOME/mongodb_data/db:/data/db \      # where to store data
                mongo
````
####Example command to run mongodb container might look like as follows
```` bash
docker container run -d --name=mongodb_test -p 27017:27017 -e PGDATA=C:/Users/Anurag/mongodb_data/db -v C:/Users/Anurag/mongodb_data/db:/pgdata mongo
````

##NoSQL Performance Tests

The files are structured as follows:

`benchmark.js` contains the test driver and all the test cases. Currently, the following tests are implemented: `shortest`, `hardPath`, `neighbors`, `neighbors2`, `neighbors2data`, `singleRead`, `singleWrite` and `aggregation`. Use `all` to run all tests inclusive warmup.

`mongodb`is a directory containing the files `description.js`, `setup.sh` and `import.sh`. The description file implements the database specific parts of the tests. The setup and import files are used to set up the database and import the needed dataset for the test.

`data` contains the test data used for the read and write tests and the start and end vertices for the shortest path.

### Installation

#### Client

We need additional services to install:

    $ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
    $ sudo apt-get install -y make build-essential nodejs

Clone the test repo and uncompress the test data files.

    $ git clone https://github.com/weinberger/nosql-tests.git
    $ cd nosql-tests
    $ npm install
    $ npm run data
    
#### Server

The server also needs the nosql-tests repo checked out. The folder on client and server are required to have the same path!

    $ git clone https://github.com/weinberger/nosql-tests.git

For the complete setup with all databases we need several additional services:

    $ sudo apt-get install -y unzip default-jre binutils numactl collectd nodejs
    
To install all databases and import the test dataset:

    $ ./setupAll.sh
    
###Location of the bash shell

Every script in this repository starts with the line of the code which tells the script where the bash shell is located. If required please replace the path of the bash shell according to your machine.    
    
### Run single test (Currently only supports mongodb)

To run a single test against one database, we execute `benchmark.js` over node.

    & node benchmark.js -h
    Usage: benchmark.js <command> [options]

    Commands:
      arangodb            ArangoDB benchmark
      arangodb-mmfiles    ArangoDB benchmark
      mongodb             MongoDB benchmark
      neo4j               neo4j benchmark
      orientdb            orientdb benchmark
      postgresql          postgresql JSON benchmark
      postgresql_tabular  postgresql tabular benchmark

    Options:
      --version               Show version number                          [boolean]
      -t, --tests             tests to run separated by comma: shortest, neighbors,
                              neighbors2, neighbors2data, singleRead, singleWrite,
                              aggregation, hardPath, singleWriteSync
                                                           [string] [default: "all"]
      -s, --restrict          restrict to that many elements (0=no restriction)
                                                                        [default: 0]
      -l, --neighbors         look at that many neighbors            [default: 1000]
      --ld, --neighbors2data  look at that many neighbors2 with profiles
                                                                      [default: 100]
      -a, --address           server host            [string] [default: "127.0.0.1"]
      -h                      Show help                                    [boolean]
