#!/bin/sh

docker exec -it redis1 redis-cli --cluster create \
	172.18.101.11:6379 172.18.101.12:6379 \
	172.18.101.13:6379 172.18.101.14:6379 \
	172.18.101.15:6379 172.18.101.16:6379 \
	--cluster-replicas 1
