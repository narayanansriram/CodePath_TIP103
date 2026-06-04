def final_value_after_operations(operations):
	increment = ["bouncy", "flouncy"]
	decrement = ["trouncy", "pouncy"]
	tigger = 1
	for operation in operations:
		if operation in increment:
			tigger+=1
		elif operation in decrement:
			tigger-=1
	return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))
assert 2 == final_value_after_operations(operations),'["trouncy", "flouncy", "flouncy"] should be 2'

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
assert 4 == final_value_after_operations(operations), '["bouncy", "bouncy", "flouncy"] should be 4'