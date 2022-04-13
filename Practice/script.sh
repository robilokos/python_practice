#!/bin/bash

message=$1
branch_name=$(git branch --show-current)

if ((branch_name == Robi)); then
    git add .
    git commit -m "RL $message"
    git push
elif ((branch_name == David)); then
    git add .
    git commit -m "GD $message"
    git push
else
    echo "Rossz branch-ben vagy!"
fi