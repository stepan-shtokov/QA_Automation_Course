string = '1h 45m, 360s, 25m, 30m 120s, 2h 60s'
time_values = string.split(',')
total_minutes = 0
for time_value in time_values:
    segments = time_value.split()
    multiplier = 1

    for segment in segments:
        if segment[-1] in {'h', 'm', 's'}:
            num = int(segment[:-1]) if segment[:-1].isdigit() else 0
            if 'h' in segment:
                total_minutes += num * 60 * multiplier
            elif 'm' in segment:
                total_minutes += num * multiplier
            elif 's' in segment:
                total_minutes += num // 60 * multiplier
        else:
            multiplier = int(segment)

print(f"Total minutes: {total_minutes}")
