def good_pairs(pile1, pile2, k):
	good = 0
	for p1 in pile1:
		for p2 in pile2:
			if p1%(p2*k) == 0:
				good+=1
	return good

# Example Usage:

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))

# Example Output:

# 5
# 2
