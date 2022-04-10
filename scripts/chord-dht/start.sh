#!/bin/bash
set -e

for i in {1..3}; do
	PORT="590$i"
	FLAGS="--join 172.18.101.11:3000"
	if [ "$1" -eq "1" ]; then
		# first node
		FLAGS=""
	fi

	docker run -d \
		--name chord_dht_$i \
		--net chord_dht_net \
		--ip 172.18.101.1$i \
		-p $PORT:3000 \
		chord-dht \
		server 0.0.0.0:3000 $FLAGS
done
