def find_common_artifacts(artifacts1, artifacts2):
    hash_table = {}
    for artifact in artifacts1:
        hash_table[artifact] = 1 
    for artifact in artifacts2:
        if artifact in hash_table:
            hash_table[artifact] += 1
    # print(hash_set)
    return [artifact for artifact,count in hash_table.items() if count>1]

# Example Usage:

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))

# Example Output:

#  ["Golden Vase", "Bronze Shield"]
