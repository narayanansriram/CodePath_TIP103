def find_treasure_indices(gold_amounts, target):
    s = {}
    for idx,gold_amount in enumerate(gold_amounts):
        if target - gold_amount in s:
            return [s[target-gold_amount],idx]
        s[gold_amount]=idx
    

# Example Usage:

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  

# Example Output:

# [0, 1]
# [1, 2]
# [0, 1]
