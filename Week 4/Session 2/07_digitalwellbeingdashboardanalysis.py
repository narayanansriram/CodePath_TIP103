# You're building a digital wellbeing dashboard that tracks users' daily app usage and helps them identify patterns and areas for improvement. Each user has a log of their daily app usage, which includes various activities like Social Media, Entertainment, Productivity, and so on. The goal is to analyze this data to provide insights into their usage patterns.

# Write the analyze_weekly_usage() function, which takes a dictionary where each key is a day of the week (e.g., "Monday", "Tuesday") and the value is another dictionary. This nested dictionary's keys represent app categories (e.g., "Social Media", "Entertainment") and its values represent the time spent (in minutes) on that category during that day.

# Your function should return:

#     The total time spent on each category across the entire week.

#     The day with the highest total usage.

#     The most-used category of the week.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
from collections import defaultdict
def analyze_weekly_usage(weekly_usage):
    highest_total_usage = {i:0 for i in weekly_usage.keys()}
    category = defaultdict(int)
    for day in weekly_usage:
        highest_total_usage[day] = sum(weekly_usage[day].values())
        for cate,hours in weekly_usage[day].items():
            category[cate] += hours
    most_used_category = sorted(category.items(),key=lambda x:x[1],reverse=True)[0][0]
    busiest_day = sorted(highest_total_usage.items(),key=lambda x:x[1],reverse=True)[0][0]
    return {"total_category_hours":category, 
              "most_used_category":most_used_category,
              "busiest_day":busiest_day}

# Example Usage:

weekly_usage = {
    "Monday": {"Social Media": 120, "Entertainment": 60, "Productivity": 90},
    "Tuesday": {"Social Media": 100, "Entertainment": 80, "Productivity": 70},
    "Wednesday": {"Social Media": 130, "Entertainment": 70, "Productivity": 60},
    "Thursday": {"Social Media": 90, "Entertainment": 60, "Productivity": 80},
    "Friday": {"Social Media": 110, "Entertainment": 100, "Productivity": 50},
    "Saturday": {"Social Media": 180, "Entertainment": 120, "Productivity": 40},
    "Sunday": {"Social Media": 160, "Entertainment": 140, "Productivity": 30}
}
print(analyze_weekly_usage(weekly_usage))

# Example Output:

# {'total_category_usage': {'Social Media': 890, 'Entertainment': 630, 'Productivity': 420}, 'busiest_day': 'Saturday', 'most_used_category': 'Social Media'}
