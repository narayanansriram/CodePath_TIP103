# Character arcs are crucial to maintaining a coherent narrative. These arcs often involve a series of events or changes that must occur in a specific order. As the story progresses, you may need to add, remove, or update these events to ensure the character's development follows the intended sequence.

# Your task is to simulate managing character arcs using a stack. Given a series of events representing a character's development, use a stack to process these events. Add events to the stack as they occur and pop them off when they are completed or no longer relevant, ensuring that the character arc maintains the correct sequence.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def manage_character_arc(events):
  stk = []
  for event in reversed(events):
    stk.append(event)
  result = []
  while stk:
    result.append(stk.pop())
  return result

# Example Usage:

events = [
    "Character is introduced.",
    "Character faces a dilemma.",
    "Character makes a decision.",
    "Character grows stronger.",
    "Character achieves goal."
]

processed_arc = manage_character_arc(events)
print(processed_arc)

events = [
    "Character enters a new world.",
    "Character struggles to adapt.",
    "Character finds a mentor.",
    "Character gains new skills.",
    "Character faces a major setback.",
    "Character overcomes the setback."
]

processed_arc = manage_character_arc(events)
print(processed_arc)

# Example Output:

# ['Character is introduced.', 'Character faces a dilemma.', 'Character makes a decision.', 'Character grows stronger.', 'Character achieves goal.']
# ['Character enters a new world.', 'Character struggles to adapt.', 'Character finds a mentor.', 'Character gains new skills.', 'Character faces a major setback.', 'Character overcomes the setback.']
