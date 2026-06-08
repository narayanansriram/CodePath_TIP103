def shuffle(message, indices):
	output = ""
	for idx in indices:
		output+=message[idx]
	return output

# Example Usage:

message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices))

# Example Output:

# "lvie"
# "findme"
