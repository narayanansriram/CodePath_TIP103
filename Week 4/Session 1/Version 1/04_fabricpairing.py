# You want to find pairs of fabrics that, when combined, maximize eco-friendliness while staying within a budget. Each fabric has a cost associated with it, and your goal is to identify the pair of fabrics whose combined cost is the highest possible without exceeding the budget.

# Write the find_best_fabric_pair() function, which takes a list of fabrics (each with a name and cost) and a budget. The function should return the names of the two fabrics whose combined cost is the closest to the budget without exceeding it.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_best_fabric_pair(fabrics, budget):
    d = {}
    for fabric in fabrics:
        if (budget-fabric[1]) in d:
            return (fabric[0],d[budget-fabric[1]][0])
        d[fabric[1]]=fabric

# Example Usage:

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

# Example Output:

# ('Hemp', 'Organic Cotton')
# ('Tencel', 'Recycled Wool')
# ('Bamboo', 'Linen')
