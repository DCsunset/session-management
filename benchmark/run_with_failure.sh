#!/bin/bash

mkdir -p data
if [ "$#" -lt "1" ]; then
	echo "Usage: ./run_with_failure.sh <failed_node>"
	exit 1
fi

./clean.sh
cargo run --bin benchmark_failure -- 4 &
pid=$!
sleep 0.1
ssh 10.10.0.1 docker kill $1
# wait for stop
wait $pid

mv experiment_data data/4
