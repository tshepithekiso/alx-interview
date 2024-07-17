#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

# Regular expression to match the log format
log_pattern = re.compile(
    r'^\d+\.\d+\.\d+\.\d+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d+) '
    r'(\d+)$'
)


def print_stats():
    """Prints the current statistics"""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption signal"""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
for line in sys.stdin:
    match = log_pattern.match(line)
    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))

        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

# Print final stats
print_stats()
