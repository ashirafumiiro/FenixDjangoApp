#!/usr/bin/env bash

SOURCE="${BASH_SOURCE[0]}"
DIR="$( dirname "$SOURCE" )"
cd $DIR

crontab -l > /tmp/jobs.txt   #save existing jobs
echo "0 0 1 * * python3 $(pwd)/manage.py monthly_increment" >> /tmp/jobs.txt  #add the desired job for 1st every month
crontab /tmp/jobs.txt    #import all jobs
