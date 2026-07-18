# You are a starship pilot navigating the galaxy and have a list of planets, each with its distance from your current position on your star map. Given an array of planet distances planets sorted in ascending order and your target destination distance target_distance, return an array with the k planets that are closest to your target distance. The result should also be sorted in ascending order.

# Planet with distance a is closer to target_distance than planet with distance b if:

#     |a - target_distance| < |b - target_distance|
#     |a - target_distance| == |b - target_distance| and a < b

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_closest_planets(planets, target_distance, k):
    orig = {v:i for i,v in enumerate(planets)}
    planets.sort(key=lambda x: abs(x-target_distance))
    result = planets[:k]
    result.sort()
    return result

# Example Usage:

planets1 = [100, 200, 300, 400, 500]
planets2 = [10, 20, 30, 40, 50]

print(find_closest_planets(planets1, 350, 3))
print(find_closest_planets(planets2, 25, 2))

# Example Output:

# [200, 300, 400]
# [20, 30]
