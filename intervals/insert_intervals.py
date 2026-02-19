def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    # 1️⃣ Add all intervals before overlap
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # 2️⃣ Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # 3️⃣ Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
