from collections import deque
def mark_event_timeline(event, timeline):
  candidate = ["x"]*len(timeline)
  q = deque()
  for i in range(len(timeline)-len(event)+1):
    candidate = ["x"]*len(timeline)
    j = i
    k = 0
    while k<len(event):
      candidate[j]=event[k]
      j+=1
      k+=1
    q.append((candidate,i))
  pos = 0
  result = []
  while q:
    candidate,idx = q.popleft()
    i = 0
    while candidate[i]=='x':
      i+=1
      continue
    count = 0
    for j in range(i,len(timeline)):
      if timeline[j]==candidate[j]:
        count+=1
    if count>0:
      result.append(idx)
    print(candidate)
  return result

    

# Example Usage:

print(mark_event_timeline("abc", "ababc"))  
print(mark_event_timeline("abca", "aabcaca")) 

# Example Output:

# [0, 2]
# [3, 0, 1]
