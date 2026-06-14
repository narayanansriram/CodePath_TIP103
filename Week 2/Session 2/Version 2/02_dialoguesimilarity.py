def is_similar(sentence1, sentence2, similar_pairs):
    if len(sentence1)!=len(sentence2):
        return False
    lookup = {}
    for w1,w2 in zip(sentence1,sentence2):
        if w1 in lookup:
            continue
        lookup[w1]=w2
    for s1,s2 in similar_pairs:
        if lookup[s1]!=s2:
            return False
    return True

# Example Usage:

sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))

# Example Output:

# True
# Example 1 Explanation: "my" and "type" are similar to themselves. The words at 
# indices 2 and 3 of sentence1 are similar to words at indices 2 and 3 of 
# sentence2 according to the similar_pairs array. 

# False
# Example 2 Explanation: Sentences are of different length.
