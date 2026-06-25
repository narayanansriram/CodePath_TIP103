def match_buyers_and_sellers(buyers, sellers):
  def sortInput(x):
    stk = []
    for i in x:
      if stk and stk[-1]>i:
        temp = []
        while stk and stk[-1]>i:
          temp.append(stk.pop())
        stk.append(i)
        while temp:
          stk.append(temp.pop())
      else:
        stk.append(i)
    return stk
  buyList = sortInput(buyers)
  sellList = sortInput(sellers)
  count = 0
  b,s = 0,0
  while b<len(buyList):
    while s<len(sellList):
      if buyList[b]>=sellList[s]:
        count+=1
        s+=1
        break
      s+=1
    b+=1
      
  # print(buyList,sellList)
  return count
# Example Usage:

buyers1 = [4, 7, 9]
sellers1 = [8, 2, 5, 8]
print(match_buyers_and_sellers(buyers1, sellers1)) 

buyers2 = [1, 1, 1]
sellers2 = [10]
print(match_buyers_and_sellers(buyers2, sellers2))

# Example Output:

# 3
# 0
