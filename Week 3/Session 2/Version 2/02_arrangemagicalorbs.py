def arrange_magical_orbs(orbs):
    r = 0
    b = len(orbs)-1
    w = 0
    while w<=b:
        if orbs[w]==0:
            orbs[r],orbs[w]=orbs[w],orbs[r]
            r+=1
            w+=1
        elif orbs[w]==2:
            orbs[b],orbs[w]=orbs[w],orbs[b]
            w+=1
            b-=1
        else:
            w+=1
    return orbs

# Example Usage:

orbs1 = [2, 0, 2, 1, 1, 0]
arrange_magical_orbs(orbs1)
print(orbs1) 

orbs2 = [2, 0, 1]
arrange_magical_orbs(orbs2)
print(orbs2) 

# Example Output:

# [0, 0, 1, 1, 2, 2]
# [0, 1, 2]
