import sys
from datetime import datetime
from collections import Counter, defaultdict

entries: list[tuple[datetime, str]] = []
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        time_str, message = line[1:].split("] ")
        timestamp = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        entries.append((timestamp, message))
entries.sort()

guard_min_counts = defaultdict(Counter)
guard_id = start = -1    # Fixes Pylance unbound flag, causes program to fail if they're not reassigned
for timestamp, message in entries:
    if "Guard" in message:
        guard_id = int(message.split()[1][1:])
    elif "falls" in message:
        start = timestamp.minute
    elif "wakes" in message:
        guard_min_counts[guard_id].update(range(start, timestamp.minute))

# Part 1
sleepiest = max(guard_min_counts.keys(), key=lambda g: sum(guard_min_counts[g].values()))
min_asleep = guard_min_counts[sleepiest].most_common(1)[0][0]
print(f"Part 1: {sleepiest * min_asleep}")

# Part 2
guard, g_min = max(guard_min_counts.items(), key=lambda x: x[1].most_common(1)[0][1])
print(f"Part 2: {guard * g_min.most_common(1)[0][0]}")