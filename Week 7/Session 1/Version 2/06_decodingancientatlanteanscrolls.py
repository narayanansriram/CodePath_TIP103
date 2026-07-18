# In the mystical city of Atlantis, ancient scrolls have been discovered that contain encoded messages. These messages follow a specific encoding rule: k[encoded_message], where the encoded_message inside the square brackets is repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string scroll is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4]. Your task is to decode these messages to reveal their original form.

# We have provided an iterative solution that uses a stack. Write a function decode_scroll_recursive() that provides a recursive solution.

def decode_scroll(scroll):
    stack = []
    current_string = ""
    current_num = 0
    
    for char in scroll:
        if char.isdigit():
            # Build the number (could be more than one digit)
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push the current number and current string to the stack
            stack.append((current_string, current_num))
            # Reset the current string and number
            current_string = ""
            current_num = 0
        elif char == ']':
            # Pop the last string and number from the stack
            prev_string, num = stack.pop()
            # Repeat the current string num times and add it to the previous string
            current_string = prev_string + current_string * num
        else:
            # Regular character, just add it to the current string
            current_string += char
    
    return current_string

def decode_scroll_recursive(scroll):
    idx = 0
    def helper():
        nonlocal idx 
        curr_string,num = "",0
        while idx < len(scroll):
            c=scroll[idx]
            if c.isdigit():
                num = num*10+int(c)
                idx+=1
            elif c == "[":
                idx+=1
                inner = helper()
                curr_string+=inner*num
                num = 0
            elif c == "]":
                idx+=1
                return curr_string
            else:
                idx+=1
                curr_string+=c
        return curr_string
    return helper()





# Example Usage:

scroll = "3[Coral2[Shell]]"
print(decode_scroll_recursive(scroll))

scroll = "2[Poseidon3[Sea]]"
print(decode_scroll_recursive(scroll))

# Example Output:

# CoralShellShellCoralShellShellCoralShellShell
# PoseidonSeaSeaSeaPoseidonSeaSeaSea
