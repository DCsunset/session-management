# mariadb galera cluster

First, create a docker bridge:

```sh
docker network create --subnet 172.18.100.0/24 mariadb_net
```

Next, modify the config file for each node (make sure the owner is 999).

Then, start the node by its number (1, 2, 3):

```sh
./start.sh <num>
```

(1 means master node)


## Init database

To initialize it:

```
docker exec -it mariadb1 mysql -u root
create database session_rust;
exit
```

## Acknowledgement

Inspired by <https://github.com/hweidner/galera-docker>
