def insert_interval(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort()
    result = [intervals[0]]
    for i in range(1,len(intervals)):
        x1,y1=result[-1]
        x2,y2=intervals[i]
        if y1>=x2:
            # print(x1,y1,x2,y2)
            result.pop()
            result.append([x1,max(y1,y2)])
        else:
            result.append(intervals[i])
    return result
# Example Usage

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insert_interval(intervals, new_interval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
print(insert_interval(intervals, new_interval))

# Example Output:

# [[1, 5], [6, 9]]
# [[1, 2], [3, 10], [12, 16]]
