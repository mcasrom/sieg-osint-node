#!/bin/bash

BASE=~/sieg-osint
LOG=$BASE/logs/pipeline.log

echo "[$(date)] START" >> $LOG

cd $BASE/scripts

python3 fetch_data.py
python3 process_data.py
python3 generate_outputs.py

echo "[$(date)] END" >> $LOG
