#!/bin/bash

DIR="$1"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
REPORT="$DIR/log_summary_$TIMESTAMP.txt"
ARCHIVE="$DIR/archive_$TIMESTAMP.tar.gz"

echo "Log Summary - $(date)" > "$REPORT"

for file in "$DIR"/*.log; do
    lines=$(wc -l < "$file")
    echo "$file: $lines lines" >> "$REPORT"
done

tar -czf "$ARCHIVE" "$DIR"/*.log

cat "$REPORT"
