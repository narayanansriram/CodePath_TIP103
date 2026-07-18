# Poseidon, the ruler of Atlantis, has a map that shows various chambers hidden deep beneath the ocean. The map is currently stored as a nested list sections, with each section containing smaller subsections. Write a recursive function map_chambers() that converts the map into a nested dictionary, where each section and subsection is a key-value pair.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def map_chambers(sections):
    def der(arr):
        curr = ""
        for i in arr:
            # print(i)
            if type(i)==list:
                return {curr: der(i)}
            else:
                curr = i
        return curr
    return der(sections)

# Example Usage:

sections = ["Atlantis", ["Coral Cave", ["Pearl Chamber"]]]
print(map_chambers(sections))

# Example Output

# {'Atlantis': {'Coral Cave': 'Pearl Chamber'}}
