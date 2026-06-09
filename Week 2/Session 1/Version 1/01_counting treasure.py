def total_treasure(treasure_map):
    return sum(treasure_map.values())

# Example Usage:

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasure(treasure_map1)) 
print(total_treasure(treasure_map2)) 

# Example Output:

# 15
# 50
