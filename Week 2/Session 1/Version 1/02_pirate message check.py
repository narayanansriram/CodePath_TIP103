from collections import defaultdict

def can_trust_message(message):
    alphabets = defaultdict(int)
    for m in message:
        if not m.isalpha():
            continue
        alphabets[m]+=1
    # print(alphabets,len(alphabet s))
    return len(alphabets)==26

# Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

# Example Output:

# True
# False
