from collections import Counter
def max_attempts(ingredients, target_meal):
    ingredientCount = Counter(ingredients)
    minCount = float('inf')
    for ingredient in target_meal:
        if ingredient not in ingredientCount:
            return 0
        minCount = min(minCount,ingredientCount[ingredient])
    return minCount

# Example Input:

ingredients1 = "aabbbcccc"
target_meal1 = "abc"
print(max_attempts(ingredients1, target_meal1))

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"
print(max_attempts(ingredients2, target_meal2))

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"
print(max_attempts(ingredients3, target_meal3))

# Example Output:

# 2
# 3
# 1
