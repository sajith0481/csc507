#!/bin/bash

SECONDS=0  # Start the timer

> newfile1.txt  # Ensure newfile1.txt is empty before writing

while read -r number; do
  echo $((number * 2)) >> newfile1.txt
done < file1.txt

duration=$SECONDS  # Capture time taken

echo "Execution time: $duration seconds"