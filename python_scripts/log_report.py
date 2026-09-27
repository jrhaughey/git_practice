#!/usr/bin/env python3

import sys
import os
import glob
import tarfile
from datetime import datetime

directory = sys.argv[1]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_path = os.path.join(directory, f"log_summary_{timestamp}.txt")
archive_path = os.path.join(os.getcwd(), f"archive_{timestamp}.tar.gz")

log_files = glob.glob(os.path.join(directory, "*.log"))

with open(report_path, "w") as report:
    report.write(f"Log Summary - {datetime.now()}\n")
    for file in log_files:
        with open(file) as f:
            lines = sum(1 for _ in f)
        report.write(f"{file}: {lines} lines\n")

with tarfile.open(archive_path, "w:gz") as tar:
    for file in log_files:
        tar.add(file)

with open(report_path) as report:
    print(report.read())
