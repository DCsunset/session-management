# redis cluster

First, create a docker bridge:

```sh
docker network create --subnet 172.18.101.0/24 redis_net
```

Then run `start.sh` to start nodes.

Next, run `start-cluster.sh` to create a cluster.

