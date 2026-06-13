from collections import defaultdict
def counting_pirates_action_minutes(logs, k):
    trackMinutes = defaultdict(set)
    countPirates = defaultdict(int)
    for pid,time in logs:
        trackMinutes[pid].add(time)
    for pid,timeCount in trackMinutes.items():
        countPirates[len(timeCount)]+=1
    result = [0]*k
    # print(countPirates)
    for idx,ct in countPirates.items():
        result[idx-1]=ct
    return result

# Example Usage:

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))

# Example Output:

# [0, 2, 0, 0, 0]
# [1, 1, 0, 0]
