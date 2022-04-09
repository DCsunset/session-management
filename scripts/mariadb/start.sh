#!/bin/sh
set -e

if [ "$#" -lt "1" ]; then
	echo "Usage: ./start.sh <num>"
	exit 1
fi

FLAGS=""
if [ "$1" -eq "1" ]; then
	# master
	FLAGS="--wsrep-new-cluster"
fi

PORT="390$1"

docker run -d \
	--name mariadb$1 \
	--net mariadb_net \
	--ip 172.18.100.1$1 \
	-p $PORT:3306 \
	-e MYSQL_ALLOW_EMPTY_PASSWORD=1 \
	-v $PWD/galera$1.cnf:/etc/mysql/conf.d/galera.cnf \
	mariadb:10.7 \
	mysqld $FLAGS
