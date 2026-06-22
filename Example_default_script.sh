#!/bin/bash

sleep 3 # hold for 60 seconds

module load cuda
nvcc --version


echo "This job is running on node:"
hostname

