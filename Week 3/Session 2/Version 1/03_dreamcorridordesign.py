def max_corridor_area(segments):
    l = 0
    r = len(segments)-1
    area = (r-l)*min(segments[l],segments[r])
    while l<r:
        area = max(area,(r-l)*min(segments[l],segments[r]))
        if segments[l]<segments[r]:
            l+=1
        else:
            r-=1
    return area

# Example Usage:

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 

# Example Output:

# 49
# 1
