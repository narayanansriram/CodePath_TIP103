def score_of_mystical_market_chains(chain):
    count = 0
    stk = []
    for c in chain:
        if c==")":
            if stk:
                stk.pop()
                count+=1
        elif c == "(":
            stk.append(")")
    return count

# Example Usage:

print(score_of_mystical_market_chains("()"))  
print(score_of_mystical_market_chains("(())"))
print(score_of_mystical_market_chains("()()")) 

# Example Output:

# 1
# 2
# 2
