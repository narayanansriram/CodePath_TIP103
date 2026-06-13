from collections import Counter
import heapq

def declutter(souvenirs, threshold):
    souvenir_count = Counter(souvenirs)
    result = []
    for k,v in souvenir_count.items():
        if v<threshold:
            result.extend([k]*v)
    return result

# Example Usage:

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3

print(declutter(souvenirs1, threshold1))

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold = 2

print(declutter(souvenirs2, threshold))

# Example Output:

# ["alien egg", "map", "map", "statue"]
# ["sword"]
