# mariadb galera cluster

First, create a docker bridge:

```sh
docker network create --subnet 172.18.100.0/24 mariadb_net
```

Next, modify the config file for each node.

Then, start the node by its number (1, 2, 3):

```sh
./start.sh <num>
```

(1 means master node)

## Acknowledgement

Inspired by <https://github.com/hweidner/galera-docker>
