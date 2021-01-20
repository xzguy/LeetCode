def merge(intervals: [[int]]) -> [[int]]:
    # sort the intervals by its first value
    intervals.sort(key = lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])
    return merged

input = [[1,3],[2,6],[8,10],[15,18]]
print(merge(input))
