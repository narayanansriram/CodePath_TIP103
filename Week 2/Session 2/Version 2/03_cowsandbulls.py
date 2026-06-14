from collections import defaultdict
def get_hint(secret, guess):
    seen = defaultdict(list)
    cows,bulls = 0,0
    # bullsAcowsB
    for idx,s in enumerate(secret):
        if secret[idx]==guess[idx]:
            continue
        seen[s].append(idx)
    for idx,(x,y) in enumerate(zip(secret,guess)):
        if x==y:
            bulls+=1
        elif y in seen and idx not in seen[y]:
            # print(seen,idx,x,y)
            seen[y].pop()
            if len(seen[y])<1:
                del seen[y]
            # print(seen)
            cows+=1
    return f"{bulls}A{cows}B"



# Example Input:

secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(get_hint(secret1, guess1))
print(get_hint(secret2, guess2))

# Example Output:

# 1A3B
# Example 1 Explanation: 
# Bulls are connected with a '|' and cows are marked with an asterisk:
# "1807"
#   |
# "7810"
#  * **

# 1A1B
# Example 2 Explanation:
# Bulls are connected with a '|' and cows are marked with an asterisk:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
#    *              *
# Note that only one of the two unmatched 1s is counted as a cow since the 
# non-bull digits can only be rearranged to allow one 1 to be a bull.
