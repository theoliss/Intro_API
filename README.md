# First API using Docker

You first need to build the docker file :

```bash

docker build . -t <name_you_chose>

```

To execute the Dockerfile you have to execute the command :

```bash

docker run -it -p 8000:8000 <name_you_chose> 

```