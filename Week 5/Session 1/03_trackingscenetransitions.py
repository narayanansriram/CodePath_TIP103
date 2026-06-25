# Given a list of scenes in a story, use a queue to keep track of the transitions from one scene to the next. You need to simulate the transitions by processing each scene in the order they appear and print out each transition from the current scene to the next.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

from collections import deque
def track_scene_transitions(scenes):
  q = deque(scenes)
  curr = deque()
  while q:
    if not curr:
        curr.append(q.popleft())
    curr.append(q.popleft())
    print(f"Transition from {curr[0]} to {curr[1]}")
    curr.popleft()


# Example Usage:

scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)

scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)

# Example Output:

# Transition from Opening to Rising Action
# Transition from Rising Action to Climax
# Transition from Climax to Falling Action
# Transition from Falling Action to Resolution

# Transition from Introduction to Conflict
# Transition from Conflict to Climax
# Transition from Climax to Denouement
