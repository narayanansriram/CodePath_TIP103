# As part of a digital wellbeing initiative, your goal is to help users optimize their break times throughout the day. Users have a list of activities they perform during breaks, each with a specified duration in minutes. You want to find two breaks that have the total duration closest to a target time.

# Write the find_best_break_pair() function, which takes a list of integers representing the duration of each break in minutes and a target time in minutes. The function should return the pair of break durations that sum closest to the target time. If there are multiple pairs with the same closest sum, return the pair with the smallest break durations. If the list has fewer than two breaks, return an empty tuple.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_best_break_pair(break_times, target):
    result = ()
    l = 0
    r = len(break_times)-1
    while l<r:
        if (break_times[l]+break_times[r])==target:
            result = (break_times[l],break_times[r])
        if (break_times[l]+break_times[r])<=target:
            l+=1
        else:
            r-=1
    return result

# Example Usage:

break_times = [10, 20, 35, 40, 50]
break_times_2 = [5, 10, 25, 30, 45]
break_times_3 = [15, 25, 35, 45]
break_times_4 = [30]

print(find_best_break_pair(break_times, 60))  
print(find_best_break_pair(break_times_2, 50))  
print(find_best_break_pair(break_times_3, 70))  
print(find_best_break_pair(break_times_4, 60))  

# Example Output:

# (20, 40)
# (5, 45)
# (25, 45)
# ()
