#!/bin/bash

# Remove file1.txt if it exists to start fresh
if [ -f file1.txt ]; then
    rm file1.txt
fi

# Generate 1000 random numbers and write/append to file1.txt
for i in {1..1000}
do
    echo $RANDOM >> file1.txt
done