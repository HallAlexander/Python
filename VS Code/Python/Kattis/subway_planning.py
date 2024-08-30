import math

def calculate_angle_and_arc(x, y, d):
    distance = math.sqrt(x**2 + y**2)
    angle = math.atan2(y, x)
    
    if distance <= d:
        return [(0, 2 * math.pi)]
    
    theta = math.asin(d / distance)
    start_angle = angle - theta
    end_angle = angle + theta
    
    start_angle %= 2 * math.pi
    end_angle %= 2 * math.pi
    
    if start_angle > end_angle:
        return [(start_angle, 2 * math.pi), (0, end_angle)]
    else:
        return [(start_angle, end_angle)]

def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged

runs = int(input())
for _ in range(runs):
    n, d = map(int, input().split())
    intervals = []
    
    for _ in range(n):
        x, y = map(int, input().split())
        intervals.extend(calculate_angle_and_arc(x, y, d))
    
    merged_intervals = merge_intervals(intervals)
    
    # Handle wrap-around case
    if len(merged_intervals) > 1 and merged_intervals[0][0] == 0 and merged_intervals[-1][1] == 2 * math.pi:
        merged_intervals[-1] = (merged_intervals[-1][0], merged_intervals[0][1])
        merged_intervals.pop(0)
    
    print(len(merged_intervals))
