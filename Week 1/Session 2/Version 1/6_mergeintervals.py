def merge_intervals(intervals):
    intervals.sort()
    newIntervals=[intervals[0]]
    for i in range(1,len(intervals)):
        x1,y1=newIntervals[-1]
        x2,y2=intervals[i]
        # print(x1,y1,x2,y2)
        if y1>=x2:
            newIntervals.pop()
            newIntervals.append([x1,y2])
        else:
            newIntervals.append([x2,y2])
    return newIntervals

# Example Usage

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(intervals)
assert [[1, 6], [8, 10], [15, 18]]==result, "[[1, 3], [2, 6], [8, 10], [15, 18]] should be [[1, 6], [8, 10], [15, 18]]"
print(result)

intervals = [[1, 4], [4, 5]]
result = merge_intervals(intervals)
assert [[1,5]] == result, "[[1, 4], [4, 5]] should be [[1,5]]"
print(result)

# Example Output:

# [[1, 6], [8, 10], [15, 18]]
# [[1, 5]]
