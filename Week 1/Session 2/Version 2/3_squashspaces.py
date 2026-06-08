def squash_spaces(s):
    output = ""
    p = 0
    e = len(s)-1
    while s[p]==" ":
        p+=1
    while s[e]==" ":
        e-=1
    while p<=e:
        if p>0 and s[p]==" " and s[p-1]==" ":
            p+=1
        else:
            output+=s[p]
            p+=1
    return output
        
    
# Example Usage

s = "   Up,     up,   and  away! "
result = squash_spaces(s)
print(f"--->{result}<----")

s = "With great power comes great responsibility."
result = squash_spaces(s)
print(f"--->{result}<----")

# Example Output:

# "Up, up, and away!"
# "With great power comes great responsibility."
