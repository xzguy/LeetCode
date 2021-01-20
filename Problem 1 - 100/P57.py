def insert(intervals: [[int]], newInterval: [int]) -> [[int]]:
    start = newInterval[0]
    end = newInterval[1]

    i = 0
    inserted = []
    while i < len(intervals):
        if start <= intervals[i][1]:
            if end < intervals[i][0]:
                break
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
        else:
            inserted.append(intervals[i])
        i += 1
    inserted.append([start, end])
    inserted.extend(intervals[i:])
    return inserted


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))