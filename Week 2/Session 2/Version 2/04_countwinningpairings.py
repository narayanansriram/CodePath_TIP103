def count_winning_pairings(star_power):
    total = 0
    def ispoweroftwo(num):
        count = 0
        while num>0:
            count+=num%2
            num//=2
        return count == 1
    for i in range(len(star_power)):
        for j in range(i+1,len(star_power)):
            curr = star_power[i]+star_power[j]
            if ispoweroftwo(curr):
                total+=1
    return total

# Example Usage:

star_power1 = [1, 3, 5, 7, 9]
print(count_winning_pairings(star_power1))

star_power2 = [1, 1, 1, 3, 3, 3, 7]
print(count_winning_pairings(star_power2))

# Example Output:

# 4
# 15
