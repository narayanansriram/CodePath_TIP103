# Scenes often contain descriptions that set the tone or provide important information. However, certain scenes may need to be filtered out based on keywords that are either irrelevant to the current narrative path or that the user wishes to avoid. Write a function that, given a list of scene descriptions and a keyword, filters out the scenes that contain the specified keyword.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def filter_scenes_by_keyword(scenes, keyword):
  result = []
  for scene in scenes:
    print(scene,scene.find(keyword), keyword in scene)
    if scene.find(keyword)==-1:
      result.append(scene)
  return result

# Example Usage:

scenes = [
    "The hero enters the dark forest.",
    "A mysterious figure appears.",
    "The hero finds a hidden treasure.",
    "An eerie silence fills the air."
]
keyword = "hero"

filtered_scenes = filter_scenes_by_keyword(scenes, keyword)
print(filtered_scenes)

scenes = [
    "The spaceship lands on an alien planet.",
    "A strange creature approaches the crew.",
    "The crew prepares to explore the new world."
]
keyword = "crew"

filtered_scenes = filter_scenes_by_keyword(scenes, keyword)
print(filtered_scenes)

# Example Output:

# ['An eerie silence fills the air.', 'A mysterious figure appears.']
# ['The spaceship lands on an alien planet.']
