# Maintaining a coherent and continuous storyline is crucial for immersion. A storyline may consist of several scenes, each associated with a timestamp that indicates when the event occurs in the narrative. Write a function that, given a list of scene records with timestamps, determines if there are any gaps in the storyline continuity by checking if each scene follows in chronological order.

# Iterate through the scenes and verify that the timestamps of consecutive scenes are in increasing order. If any scene is found to be out of sequence, your function should return False, indicating a gap in continuity; otherwise, it should return True.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def analyze_storyline_continuity(scenes):
    i = 0
    j = i+1
    while j<len(scenes):
        first = scenes[i]['timestamp']
        second = scenes[j]['timestamp']
        if first>second:
            return False
        i+=1
        j+=1
    return True

# Example Usage:

scenes = [
    {"scene": "The hero enters the dark forest.", "timestamp": 1},
    {"scene": "A mysterious figure appears.", "timestamp": 2},
    {"scene": "The hero faces his fears.", "timestamp": 3},
    {"scene": "The hero finds a hidden treasure.", "timestamp": 4},
    {"scene": "An eerie silence fills the air.", "timestamp": 5}
]

continuity = analyze_storyline_continuity(scenes)
print(continuity)

scenes = [
    {"scene": "The spaceship lands on an alien planet.", "timestamp": 3},
    {"scene": "A strange creature approaches.", "timestamp": 2},
    {"scene": "The crew explores the new world.", "timestamp": 4},
    {"scene": "The crew encounters hostile forces.", "timestamp": 5},
    {"scene": "The crew makes a narrow escape.", "timestamp": 6}
]

continuity = analyze_storyline_continuity(scenes)
print(continuity)

scenes = [
    {"scene": "The adventure begins.", "timestamp": 2},
    {"scene": "Things escalate.", "timestamp": 3},
    {"scene": "The finale.", "timestamp": 4},
]
print(analyze_storyline_continuity(scenes))

# Example Output:

# True
# False
# True
