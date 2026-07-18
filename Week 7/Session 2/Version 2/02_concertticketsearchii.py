# If you solved the above problem iteratively, solve it recursively. If you solved it recursively, solve it iteratively.

def find_affordable_ticket(ticket_prices, budget):
    if budget<ticket_prices[0]:
        return -1
    def helper(lo,hi):
        if lo>=hi:
            return hi
        mid = lo+(hi-lo)//2
        if ticket_prices[mid]<=budget:
            return helper(mid+1,hi)
        else:
            return helper(lo,mid-1)
    result = helper(0, len(ticket_prices)-1)
    return result

# Example Usage:

print(find_affordable_ticket([50, 75, 100, 150], 90))
print(find_affordable_ticket([50, 75, 100, 150], 40))
print(find_affordable_ticket([50, 75, 100, 150,180,300,400], 200))

# Example Output:

# 2 
# Explantion: 75 is the closest ticket price less than or equal to 90. 
# It has index 2. 
