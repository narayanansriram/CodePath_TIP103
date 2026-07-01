# Users want to identify patterns in their app usage over the course of a day. Specifically, they are interested in finding out if they have periods of repetitive behavior, where they switch between the same set of apps in a recurring pattern. Your task is to detect the longest repeating pattern of app usage within a 24-hour period.

# Write the find_longest_repeating_pattern() function, which takes a list of app usage logs, where each element in the list represents the app used in a particular hour (from hour 0 to hour 23). The function should return the longest repeating pattern of apps and how many times the pattern repeats. If there are multiple patterns of the same length, return the first one found.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
from collections import Counter
from collections import defaultdict
def find_longest_repeating_pattern(app_logs):
    i = len(app_logs)//2
    while i>0:
        count = ["",0]
        for j in range(0,len(app_logs), i):
            # print(i,app_logs[j:j+i])
            if len(app_logs[j:j+i])<i:
                continue
            if (app_logs[0:i] == app_logs[j:j+i]):
                count[0] = app_logs[j:j+i]
                count[1]+=1
        if count[1]>=2:
            return count
        i-=1
        
# Example Usage:

app_logs = ["Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Facebook", "Twitter", "Instagram"]
app_logs_2 = ["Facebook", "Instagram", "Facebook", "Instagram", "Facebook", "Instagram", "Snapchat", "Snapchat", "Snapchat", "Instagram"]
app_logs_3 = ["WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook", "WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook"]

print(find_longest_repeating_pattern(app_logs))
print(find_longest_repeating_pattern(app_logs_2))
print(find_longest_repeating_pattern(app_logs_3))

# Example Output:

# (['Instagram', 'YouTube', 'Snapchat'], 3)
# (['Facebook', 'Instagram'], 3)
# (['WhatsApp', 'TikTok', 'Instagram', 'YouTube', 'Snapchat', 'Twitter', 'Facebook'], 2)
