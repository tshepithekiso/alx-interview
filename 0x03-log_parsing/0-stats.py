#!/usr/bin/python3
import sys
import re
import signal


# Define a signal handler for CTRL+C
def signal_handler(signal, frame):
    print_metrics()
    sys.exit(0)


# Initialize metrics
total_file_size = 0
status_codes = {}


# Define a function to print the metrics
def print_metrics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")


# Set the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)


# Read and process the input lines
line_count = 0
while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break

        # Validate the format of the line
        match = re.match(
            r"(\d+\.\d+\.\d+\.\d+) - \[(.*)\] \"GET /projects/260 HTTP/1.1\" "
            r"(\d+) (\d+)",
            line
        )
        if not match:
            continue

        # Extract the data points
        ip_address, date, status_code, file_size = match.groups()
        status_code = int(status_code)
        file_size = int(file_size)

        # Update the metrics
        total_file_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_metrics()

    except (ValueError, KeyboardInterrupt):
        print_metrics()
        break
    except Exception as e:
        print(f"Error: {e}")
        continue
