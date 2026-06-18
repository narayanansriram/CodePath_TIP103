def rearrange_guests(guests):
    o,e=1,0
    while o<len(guests) and e<len(guests):
        if guests[o]>0 and guests[e]<0:
            guests[o],guests[e]=guests[e],guests[o]
            o+=2
            e+=2
        elif guests[o]<0:
            o+=2
        else:
            e+=2
    return guests


# Example Usage:

print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 

# Example Output:

# [3,-2,1,-5,2,-4]
# [1,-1]
