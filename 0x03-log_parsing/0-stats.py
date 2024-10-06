#!/usr/bin/python3
import sys
import re
import signal

# Initialize metrics
total_file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

def signal_handler(sig, frame):
    """Handles keyboard interrupt (CTRL + C) to print final statistics."""
    print_statistics()
    sys.exit(0)

def print_statistics():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Regular expression pattern to validate log line format
log_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'

for line in sys.stdin:
    line = line.rstrip()  # Remove trailing whitespace
    match = re.match(log_pattern, line)

    if match:
        # Extract status code and file size
        status_code = match.group(3)
        file_size = int(match.group(4))

        # Update metrics
        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()
    else:
        # Skip lines that do not match the format
        continue

# Final print of statistics if input ends
print_statistics()
