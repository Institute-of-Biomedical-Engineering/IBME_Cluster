#!/bin/bash

sleep 3 # hold for 60 seconds

module load all/CUDA/13.1.1
nvcc --version


echo "This job is running on node:"
hostname
