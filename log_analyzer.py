#!/usr/bin/env python3
import argparse
import re
import pandas as pd
from datetime import datetime
from collections import Counter

def parse_logs(logfile):
    with open(logfile, "r") as f:
        logs = f.readlines()

    # Example regex for typical error logs: [2025-08-25 12:34:56] ERROR Something broke
    log_pattern = re.compile(r"\[(.*?)\]\s+(ERROR|WARN|INFO)\s+(.*)")
    parsed = []

    for line in logs:
        match = log_pattern.match(line)
        if match:
            timestamp = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
            level = match.group(2)
            message = match.group(3)
            parsed.append([timestamp, level, message])

    df = pd.DataFrame(parsed, columns=["timestamp", "level", "message"])
    return df

def detect_error_spikes(df, threshold=5):
    # Count errors per minute
    df["minute"] = df["timestamp"].dt.floor("T")
    counts = df[df["level"]=="ERROR"].groupby("minute").size()

    spikes = counts[counts > threshold]
    return spikes

def main():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI")
    parser.add_argument("--log", required=True, help="Path to log file")
    parser.add_argument("--output", default="report.csv", help="Report file")
    parser.add_argument("--threshold", type=int, default=5, help="Error spike threshold")
    args = parser.parse_args()

    df = parse_logs(args.log)
    spikes = detect_error_spikes(df, args.threshold)

    df.to_csv(args.output, index=False)
    print(f"✅ Report saved to {args.output}")

    if not spikes.empty:
        print("\n🚨 Error Spikes Detected:")
        print(spikes)

if __name__ == "__main__":
    main()
