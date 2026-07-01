# As part of a digital wellbeing initiative, you're designing a system to manage screen time sessions on a device. The device tracks various apps being opened and closed throughout the day. Each app opening starts a new session, and each closing ends that session. The system should ensure that for every app opened, there is a corresponding closure.

# Write the manage_screen_time_sessions() function, which takes a list of actions representing app openings and closures throughout the day. Each action is either "OPEN <app>" or "CLOSE <app>". The function should return True if all the app sessions are properly managed (i.e., every opened app has a corresponding close in the correct order), and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def manage_screen_time_sessions(actions):
    stk = []
    for action in actions:
        a,name = action.split(" ")
        if a=="OPEN":
            stk.append(name)
        else:
            if not stk:
                return False
            if stk[-1]!=name:
                return False
            stk.pop()
    return len(stk)==0
            

# Example Usage:

actions = ["OPEN Instagram", "OPEN Facebook", "CLOSE Facebook", "CLOSE Instagram"]
actions_2 = ["OPEN Instagram", "CLOSE Instagram", "CLOSE Facebook"]
actions_3 = ["OPEN Instagram", "OPEN Facebook", "CLOSE Instagram", "CLOSE Facebook"]

print(manage_screen_time_sessions(actions))  
print(manage_screen_time_sessions(actions_2))  
print(manage_screen_time_sessions(actions_3)) 

# Example Output:

# True
# False
# False

