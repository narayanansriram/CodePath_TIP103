def maximum_value(items, x, y):
    stk = []
    first,second = "",""
    if x>y:
        first =["ab",x]
    else:
        first = ["ba",y]
    if first=="ab":
        second = ["ba",y]
    else:
        second = ["ab",x]
    def process(target,removal):
        score=0
        stk = []
        for i in target:
            if stk and stk[-1]==removal[0][0] and i==removal[0][1]:
                stk.pop()
                # print("hit",removal[1])
                score+=removal[1]
            else:
                stk.append(i)
        return [score,stk]
    score, output = process(items,first)
    additionalScore,result = process(output,second)
    return score+additionalScore

     


# Example Usage:

s1 = "cdbcbbaaabab"
x1, y1 = 4, 5
print(maximum_value(s1, x1, y1))

s2 = "aabbaaxybbaabb"
x2, y2 = 5, 4
print(maximum_value(s2, x2, y2)) 

# Example Output:

# 19
# 20
