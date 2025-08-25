#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import sys

def generate_chart(csv_file, output="report.png"):
    df = pd.read_csv(csv_file, parse_dates=["timestamp"])
    df["minute"] = pd.to_datetime(df["timestamp"]).dt.floor("T")

    error_counts = df[df["level"]=="ERROR"].groupby("minute").size()

    plt.figure(figsize=(10,5))
    error_counts.plot(kind="bar")
    plt.title("Error Frequency by Minute")
    plt.xlabel("Time (minute)")
    plt.ylabel("Error Count")
    plt.tight_layout()
    plt.savefig(output)
    print(f"📊 Chart saved as {output}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python report_generator.py report.csv")
        sys.exit(1)
    generate_chart(sys.argv[1])
