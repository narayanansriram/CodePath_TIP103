def wealthiest_customer(accounts):
	result = [0,0]
	for idx,account in enumerate(accounts):
		totAccount = sum(account)
		if totAccount>result[1]:
			result = [idx,totAccount]
	return result

# Example Usage:

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
print(wealthiest_customer(accounts))

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
print(wealthiest_customer(accounts))

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
print(wealthiest_customer(accounts))

# Example Output:

# [0, 6]
# [1, 10]
# [0, 17]
