from collections import Counter

def organize_exhibition(collection):
    t = Counter(collection)

    result = []
    while len(t)>0:
        curr = []
        remove = []
        for k,_ in t.items():
            curr.append(k)
            t[k]-=1
            if t[k] == 0:
                remove.append(k)
        result.append(curr)
        for k in remove:
            del t[k]
        # print(t)
    return result

# Example Usage:

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))

# Example Output:

# [
#   ["O'Keefe", "Kahlo", "Picasso", "Warhol"],
#   ["O'Keefe", "Kahlo"],
#   ["O'Keefe"]
# ]
# Example 1 Explanation:
# All elements of collections were used, and each row of the 2D array contains 
# distinct strings, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.

# [["Kusama", "Monet", "Ofili", "Banksy"]]
# Example 2 Explanation: 
# All elements of the array are distinct, so we can keep all of them in the first 
# row of the 2D array.
