def minimum_boxes(meals, capacity):
	meals.sort()
	capacity.sort()
	m = len(meals)-1
	c = len(capacity)-1
	ct = 0
	while c>=0:
		currCap = capacity[c]
		
		while currCap>0 and m>=0:
			currCap-=meals[m]
			if currCap>=0:
				m-=1
			else:
				break
		if m==0:
			return (len(capacity)-c+1)
		c-=1
		ct+=1
	# print(c,m, currCap)
	return ct
	

# Example Usage:

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity))

# Example Output:

# 2
# 4
