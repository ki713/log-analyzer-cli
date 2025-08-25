#!/bin/bash
# Simple helper script to automate analysis

LOGFILE=$1
if [ -z "$LOGFILE" ]; then
  echo "Usage: ./utils.sh logfile"
  exit 1
fi

python3 log_analyzer.py --log $LOGFILE --output report.csv
python3 report_generator.py report.csv
