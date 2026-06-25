# You want to help users identify which apps they spend the most time on throughout the day. Based on the screen time logs, your task is to find the app with the highest total screen time.

# Write the most_used_app() function, which takes a dictionary containing the app names and the total time spent on each app. The function should return the app with the highest screen time. If multiple apps have the same highest screen time, return any one of them.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def most_used_app(screen_time):
    maxSoFar = ("boiler",float('-inf'))
    for app,t in screen_time.items():
        if t>maxSoFar[1]:
            maxSoFar = (app,t)
    return maxSoFar[0]

# Example Usage:

screen_time = {"Instagram": 55, "YouTube": 30, "Snapchat": 15}
screen_time_2 = {"Twitter": 25, "Reddit": 20, "Instagram": 35}
screen_time_3 = {"TikTok": 90, "YouTube": 90, "Snapchat": 25}

print(most_used_app(screen_time))
print(most_used_app(screen_time_2))
print(most_used_app(screen_time_3))

# Example Output:

# Instagram
# Instagram
# TikTok
