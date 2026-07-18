# You're in charge of distributing merchandise to different booths at a music festival, and there are n booths, each stocked with different amounts of merchandise. The ith booth has booths[i] items. You have h hours before the festival closes, and your job is to distribute all the merchandise to the attendees.

# You can set a maximum distribution rate r, which represents the number of items you can distribute per hour. Each hour, you visit one booth and distribute r items from that booth. If the booth has fewer than r items left, you distribute all remaining items in that booth during that hour and then move on to the next hour.

# Given a list of integers booths where each element represents the number of merchandise items at the ith booth, return the minimum distribution rate r such that you can distribute all the items within h hours.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
import math
def min_distribution_rate(booths, h):
    def hours_needed(r):
        if r ==0:
            return 0
        out = 0
        for booth in booths:
            # print(booth,r,booth/r, math.ceil(booth/r),booth//r)
            out+=math.ceil(booth/r)
        return out
    lo = 1
    hi = max(booths)
    while lo<hi:
        mid = lo + (hi-lo)//2
        r = hours_needed(mid)
        # print(r)
        if r<=h:
            hi = mid
        else:
            lo = mid+1
    return hi
# Example Usage:

print(min_distribution_rate([3, 6, 7, 11], 8))
print(min_distribution_rate([30,11,23,4,20], 5))
print(min_distribution_rate([30,11,23,4,20], 6))
print(min_distribution_rate([100], 5))
print(min_distribution_rate([5], 100))

# Example Output:

# 4
# 30
# 23
