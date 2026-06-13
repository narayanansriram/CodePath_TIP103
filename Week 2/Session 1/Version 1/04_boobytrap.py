def can_make_balanced(code):
    let_hm = {}
    for letter in code:
        if letter in let_hm.keys():
            let_hm[letter]+=1
        else:
            let_hm[letter]=1
    print(let_hm)
    count_of_counts = {}
    for _,ct in let_hm.items():
        if ct in count_of_counts:
            count_of_counts[ct]+=1
        else:
            count_of_counts[ct]=1
    if len(count_of_counts)>2:
        return False
    if 1 not in count_of_counts.values():
        return False
    return True

# Example Usage:

code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 

# Example Output:

# True
# Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

# False
# Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is