def assign_unique_nicknames(nicknames):
    registry = {}
    output = []
    for nickname in nicknames:
        if nickname not in registry:
            output.append(nickname)
            registry[nickname]=1
        else:
            suff = registry[nickname]
            output.append(f"{nickname}({suff})")
            registry[nickname]+=1
    return output

# Example Usage:

nicknames1 = ["Champ","Diva","Champ","Ace"]
print(assign_unique_nicknames(nicknames1))

nicknames2 = ["Ace","Ace","Ace","Maverick"]
print(assign_unique_nicknames(nicknames2)) 

nicknames3 = ["Star","Star","Star","Star","Star"]
print(assign_unique_nicknames(nicknames3))

# Example Output:

# ["Champ","Diva","Champ(1)","Ace"]
# ["Ace","Ace(1)","Ace(2)","Maverick"]
# ["Star","Star(1)","Star(2)","Star(3)","Star(4)"]
