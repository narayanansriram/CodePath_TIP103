# Given a string expression representing arbitrarily nested ternary expressions, evaluate the expression, and return its result as a string.

# You can always assume that the given expression is valid and only contains digits, '?', ':', 'T', and 'F' where 'T' is True and 'F' is False. All the numbers in the expression are one-digit numbers (i.e., in the range [0, 9]).

# Ternary expressions use the following syntax:

# condition ? true_choice : false_choice

#     condition is evaluate first and determines which choice to make.
#         true_choice is taken if condition evaluates to True
#         false_choice is taken if condition evaluates to False

# The conditional expressions group right-to-left, and the result of the expression will always evaluate to either a digit, 'T' or 'F'.

# We have provided an iterative solution that uses an explicit stack. Implement a recursive solution evaluate_ternary_expression_recursive().

def evaluate_ternary_expression_iterative(expression):
    stack = []
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        
        if stack and stack[-1] == '?':
            stack.pop()  # Remove the '?'
            true_expr = stack.pop()  # True expression
            stack.pop()  # Remove the ':'
            false_expr = stack.pop()  # False expression
            
            if char == 'T':
                stack.append(true_expr)
            else:
                stack.append(false_expr)
        else:
            stack.append(char)
    
    return stack[0]

def evaluate_ternary_expression_recursive(expression):
    pos = 0
    def evaluate():
        nonlocal pos
        c = expression[pos]
        pos += 1
        if pos>=len(expression) or expression[pos]!="?":
            return c
        if expression[pos]=="?":
            pos+=1
            t = evaluate()
        if expression[pos] == ":":
            pos+=1
            f = evaluate()
        return t or f
    return evaluate()
        




# Example Usage:

print(evaluate_ternary_expression_recursive("T?2:3"))
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))

# Example Output:

# 2
# Example 1 Explanation: If True, then result is 2; otherwise result is 3.

# 4
# Example Explanation: The conditional expressions group right-to-left. Using parentheses, 
# it is read/evaluated as:
# "(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
# or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"

# F
# Explanation: The conditional expressions group right-to-left. Using parentheses, 
# it is read/evaluated as:
# "(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
# "(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"
