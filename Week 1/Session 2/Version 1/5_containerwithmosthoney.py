def most_honey(heights):
    f = 0
    b = len(heights)-1
    maxArea = 0
    while f<b:
        area=(b-f)*min(heights[f],heights[b])
        if heights[f]>heights[b]:
            b-=1
        else:
            f+=1
        maxArea = max(area,maxArea)
    return maxArea
			
    
		

# Example Usage

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = most_honey(height)
assert 49 == result, "[1, 8, 6, 2, 5, 4, 8, 3, 7] should be 49"
print(result)

height = [1, 1]
result = most_honey(height)
assert 1 == result, "[1,1] should be 1"
print(result)

# Example Output:

# 49
# 1
