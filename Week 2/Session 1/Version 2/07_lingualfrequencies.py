from collections import defaultdict
import heapq
def find_most_frequent_word(text, illegibles):
    arr = text.split(" ")
    counter = defaultdict(int)
    for element in arr:
        sanitized_element = "".join([x.lower() for x in element if x.isalpha()])
        if sanitized_element not in illegibles:
            counter[sanitized_element]+=1
    h = [(-ct,word) for word,ct in counter.items()]
    # print(h,counter)
    heapq.heapify(h)
    ct,word = heapq.heappop(h)
    return word

# Example Usage:

paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 

# Example Output:

# a

# ball
# Example 2 Explanation:
# "hit" occurs 3 times, but it is an unknown word.
# "ball" occurs twice (and no other word does), so it is the most frequent legible word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is illegible.
