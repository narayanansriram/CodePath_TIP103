def words_with_char(words, x):
	result = []
	for idx,word in enumerate(words):
		if x in word:
			result.append(idx)
	return result
# Example Usage:

words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))

# Example Output:

# [0, 1]
# [0, 2]
# []
