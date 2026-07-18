# You are helping a friend find a concert ticket they can afford in a sorted list ticket_prices. Return the index of the ticket with a price closest to, but not greater than their budget.

# Your solution must have O(log n) time complexity.

def find_affordable_ticket(ticket_prices, budget):
    lo,hi = 0, len(ticket_prices)-1
    while lo<=hi:
        mid = lo + (hi - lo)//2
        if ticket_prices[mid]<=budget:
            lo = mid +1
        elif ticket_prices[mid]>budget:
            hi = mid - 1
    return hi

# Example Usage:

print(find_affordable_ticket([50, 75, 100, 150], 90))

# Example Output:

# 1
# Explantion: 75 is the closest ticket price less than or equal to 90. 
# It has index 1. 
