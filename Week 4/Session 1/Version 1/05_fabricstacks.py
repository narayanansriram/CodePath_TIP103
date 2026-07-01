# You need to organize rolls of fabric in such a way that you can efficiently retrieve them based on their eco-friendliness rating. Fabrics are stacked one on top of the other, and you can only retrieve the top fabric in the stack.

# Write the organize_fabrics() function, which takes a list of fabrics (each with a name and an eco-friendliness rating) and returns a list of fabric names in the order they would be retrieved from the stack, starting with the least eco-friendly fabric.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def organize_fabrics(fabrics):
    stk = []
    for fabric in fabrics:
        if stk and stk[-1][1]>fabric[1]:
            temp = []
            while stk and stk[-1][1]>fabric[1]:
                temp.append(stk.pop())
            stk.append(fabric)
            while temp:
                stk.append(temp.pop())
        else:
            stk.append(fabric)
    result = []
    while stk:
        result.append(stk.pop()[0])
    return result

# Example Usage:

fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))

# Example Output:

# ['Hemp', 'Organic Cotton', 'Bamboo', 'Recycled Polyester']
# ['Recycled Wool', 'Tencel', 'Organic Cotton', 'Linen']
# ['Hemp', 'Bamboo', 'Recycled Polyester', 'Linen']
