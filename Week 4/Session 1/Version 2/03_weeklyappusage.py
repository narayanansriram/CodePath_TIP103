# Users want to know how much time they are spending on each app over the course of a week. Your task is to summarize the total weekly usage for each app and then identify the app with the most varied usage pattern throughout the week. The varied usage pattern can be measured by the difference between the maximum and minimum daily usage for each app.

# Write the most_varied_app() function, which takes a dictionary containing the app names and daily usage over seven days. The function should return the app with the highest difference between the maximum and minimum usage over the week. If multiple apps have the same difference, return any one of them.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def most_varied_app(app_usage):
    d = []
    for app,t in app_usage.items():
        di = max(t)-min(t)
        if d and d[-1][-1]<di:
            temp = []
            while d and d[-1][-1]<di:
                temp.append(d.pop())
            d.append((app,di))
        else:
            d.append((app,di))
    return d[0][0]

# Example Usage:

app_usage = {
    "Instagram": [60, 55, 65, 60, 70, 55, 60],
    "YouTube": [100, 120, 110, 100, 115, 105, 120],
    "Snapchat": [30, 35, 25, 30, 40, 35, 30]
}

app_usage_2 = {
    "Twitter": [15, 15, 15, 15, 15, 15, 15],
    "Reddit": [45, 50, 55, 50, 45, 50, 55],
    "Facebook": [80, 85, 80, 85, 80, 85, 80]
}

app_usage_3 = {
    "TikTok": [80, 100, 90, 85, 95, 105, 90],
    "Spotify": [40, 45, 50, 45, 40, 45, 50],
    "WhatsApp": [60, 60, 60, 60, 60, 60, 60]
}

print(most_varied_app(app_usage))
print(most_varied_app(app_usage_2))
print(most_varied_app(app_usage_3))

# Example Output:

# YouTube
# Reddit
# TikTok
