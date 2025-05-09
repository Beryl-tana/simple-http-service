import re
from datetime import datetime

log_file = "service.log"

timestamps = []
successes = 0
failures = 0

with open(log_file) as f:
    for line in f:
        match = re.search(r'\[(.*?)\].*"(GET /health.*?)" (\d+)', line)
        if match:
            ts = match.group(1)
            status = int(match.group(3))
            try:
                dt = datetime.strptime(ts, '%d/%b/%Y:%H:%M:%S %z')
                timestamps.append(dt)
                if status == 200:
                    successes += 1
                else:
                    failures += 1
            except ValueError:
                continue

# Calculate average interval
intervals = [
    (timestamps[i] - timestamps[i - 1]).total_seconds()
    for i in range(1, len(timestamps))
]
avg_interval = sum(intervals) / len(intervals) if intervals else 0

print(f"Total checks: {len(timestamps)}")
print(f"Successes: {successes}, Failures: {failures}")
print(f"Average interval between checks: {avg_interval:.2f} seconds")
