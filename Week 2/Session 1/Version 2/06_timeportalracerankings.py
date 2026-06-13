from collections import defaultdict
def find_travelers(races):
    winners = defaultdict(int)
    losers = defaultdict(int)
    for win,lose in races:
        winners[win]+=1
        losers[lose]+=1
    answer = [[],[]]
    for winner,count in winners.items():
        if winner not in losers:
            answer[0].append(winner)
    for loser,count in losers.items():
        if count == 1:
            answer[1].append(loser)
    return answer


races1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
races2 = [[2, 3], [1, 3], [5, 4], [6, 4]]

print(find_travelers(races1))  
print(find_travelers(races2)) 

# Example Output

[[1, 2, 10], [4, 5, 7, 8]]
[[1, 2, 5, 6], []]
