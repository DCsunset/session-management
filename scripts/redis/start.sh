#!/bin/bash
set -e

for i in {1..6}; do
	PORT="490$i"

	docker run -d \
		--name redis$i \
		--net redis_net \
		--ip 172.18.101.1$i \
		-p $PORT:6379 \
		-v $PWD/redis.conf:/redis.conf \
		redis:6.2 \
		redis-server /redis.conf
done
