def linear_search(items, target):
	for i,j in enumerate(items):
		if j==target:
			return i
	return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

assert 3==linear_search(items, target), "hunny is found"

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))

assert -1==linear_search(items, target), "nothing is found"