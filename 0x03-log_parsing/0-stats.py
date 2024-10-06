#!/usr/bin/python3
import sys
import signal
import re

# Global variables to track total file size and status codes counts
file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """ Prints the total file size and counts of status codes """
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """ Signal handler for keyboard interruption (Ctrl + C) """
    print_stats()
    sys.exit(0)

# Updated regular expression to match the required log format
log_pattern = r'^\S+ - \[\d{1,2}/[a-zA-Z]{3}/\d{4} \d{2}:\d{2}:\d{2}\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'

# Function to process each line
def process_line(line):
    global file_size, line_count  # Corrected placement of 'global'
    match = re.match(log_pattern, line)
    if match:
        # Extract status code and file size
        status_code = int(match.group(1))
        file_size += int(match.group(2))
        
        # Update the status code count if it's a valid one
        if status_code in status_codes:
            status_codes[status_code] += 1

    line_count += 1  # Increment line count here

if __name__ == "__main__":
    # Register the signal handler for SIGINT (Ctrl + C)
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        # Process input line by line
        for line in sys.stdin:
            process_line(line.strip())  # Process each line

            # After every 10 lines, print the stats
            if line_count % 10 == 0:
                print_stats()
                
    except KeyboardInterrupt:
        # Handle any keyboard interruptions cleanly
        print_stats()
        sys.exit(0)

    # Print final stats when stdin is done (EOF)
    print_stats()
