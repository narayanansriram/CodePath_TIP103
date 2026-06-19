def build_skyscrapers(floors):
    top = floors[0]
    count = 1
    for i in range(1,len(floors)):
        if floors[i]>top:
            count+=1
        top = floors[i]
    return count

# Example Usage:

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

# Example Output:

# 4
# 4
# 2
