# You are given the head of a linked list contestant_scores with n nodes where each node represents the current score of a contestant in the game.

# For each node in the list, find the value of the contestant with the next highest score. That is, for each score, find the value of the first node that is next to it and has a strictly larger value than it.

# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def next_highest_scoring_contestant(contestant_scores):
    arr = []
    stk = []
    values = []
    idx = 0
    while contestant_scores:
        values.append(contestant_scores.value)
        arr.append(0)
        if stk and values[stk[-1]]<contestant_scores.value:
            while stk and values[stk[-1]]<contestant_scores.value:
                i = stk.pop()
                arr[i] = contestant_scores.value
            stk.append((idx))
        else:
            stk.append(idx)
        contestant_scores = contestant_scores.next
        idx+=1
    # print(stk)
    # while stk:
    #     arr.append(stk.pop()[1])
    return arr
    # arr = []
    # curr = contestant_scores
    # while curr:
    #     sec = curr.next
    #     value_add = False
    #     while sec:
    #         if sec.value>curr.value:
    #             arr.append(sec.value)
    #             value_add = True
    #             break
    #         sec = sec.next
    #     curr = curr.next
    #     if not value_add:
    #         arr.append(0)
    # return arr
            

# Example Usage:

# Example 1 Linked List contestant_scores1 with dotted arrows to next greatest node

# Example 2 Linked List contestant_scores2 with dotted arrows to next greatest node

contestant_scores1 = Node(2, Node(1, Node(5)))
contestant_scores2 = Node(2, Node(7, Node(4, Node(3, Node(5)))))

print(next_highest_scoring_contestant(contestant_scores1))
print(next_highest_scoring_contestant(contestant_scores2))

# Example Output:

# [5, 5, 0]
# [7, 0, 5, 5, 0]
