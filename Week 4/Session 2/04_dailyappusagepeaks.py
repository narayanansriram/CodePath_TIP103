# You want to help users identify the peak hours of their app usage during the day. Users log their app usage every hour, and your task is to determine the highest total screen time recorded during any three consecutive hours.

# Write the peak_usage_hours() function that takes a list of 24 integers, where each integer represents the number of minutes spent on apps during a specific hour (from hour 0 to hour 23). The function should return the start hour and the total screen time for the three-hour period with the highest total usage. If multiple periods have the same total, return the earliest one.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def peak_usage_hours(screen_time):
  maxHour = (0,0)
  for hour in range(len(screen_time)-2):
    curr = sum(screen_time[hour:hour+3])
    if curr>maxHour[1]:
      maxHour = (hour,curr)
  return maxHour

# Example Usage:

screen_time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
screen_time_2 = [5, 15, 10, 20, 30, 25, 50, 40, 35, 45, 60, 55, 65, 75, 70, 85, 95, 90, 100, 110, 105, 115, 120, 125]
screen_time_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(peak_usage_hours(screen_time))
print(peak_usage_hours(screen_time_2))    
print(peak_usage_hours(screen_time_3)) 

# Example Output:

# (21, 690)
# (21, 360)
# (0, 0)
