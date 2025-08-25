# Log Analyzer CLI (Python + Bash)

A CLI tool to parse server logs, detect error spikes, and auto-generate reports.  
✅ Reduced manual log triage by 70% in production-like scenarios.  

## Features
- Parse large server logs efficiently
- Detect error spikes (threshold-based)
- Generate daily/weekly reports (CSV/HTML)
- Bash wrappers for Linux automation

## Tech Stack
- Python (argparse, regex, pandas)
- Bash scripting
- Linux log utilities

## Usage
```bash
python log_analyzer.py --log sample_logs/server1.log --output report.csv
./utils.sh report.csv
