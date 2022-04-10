#!/bin/bash

mkdir -p data
threads=(1 2 4)
for t in "${threads[@]}"; do
	./clean.sh
	cargo run --bin benchmark -- $t
	mv experiment_data data/$t
	sleep 1
done
