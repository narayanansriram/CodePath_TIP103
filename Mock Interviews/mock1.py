# Problem: The Study Break Optimizer

# You are trying to maximize your productivity before finals week. There are several "Focus Room" sessions happening on the campus Discord server, each with a specific start and end time.

# To get the "Deep Work" badge, you want to attend as many full sessions as possible. However, you can only be in one Focus Room at a time. If two sessions overlap, you must skip at least one of them. (Note: If a session ends at the exact same time another starts, like 1:00-2:00 and 2:00-3:00, they are not considered overlapping).

# Given an array of session intervals where sessions[i] = [start_i, end_i], return the minimum number of sessions you need to skip to ensure that all the sessions you attend are non-overlapping.

# Example 1:

#     Input: sessions = [[1, 2], [2, 3], [3, 4], [1, 3]]
#     Output: 1
#     Explanation: You need to skip [1, 3]. After removing it, the remaining sessions are [[1, 2], [2, 3], [3, 4]], which don't overlap.

# Example 2:

#     Input: sessions = [[1, 2], [1, 2], [1, 2]]
#     Output: 2
#     Explanation: You can only attend one of these three identical sessions. You must skip the other two.

# Example 3:

#     Input: sessions = [[1, 10], [2, 3], [3, 4]]
#     Output: 1
#     Explanation: Even though [1, 10] starts first, it lasts so long that it overlaps with everything. It's better to skip the one long session so you can attend the two shorter ones.

# Constraints:

#     1 <= sessions.length <= 10^5
#     sessions[i].length == 2
#     5 * 10^4 <= start_i < end_i <= 5 * 10^4

def studybreakoptimizer(intervals):
    intervals.sort(key=lambda x: x[1])
    
    stk = [intervals[0]]
    skip = 0
    for i in range(1,len(intervals)):
        curr_x,curr_y = intervals[i]
        prev_x,prev_y = stk[-1]
        if curr_x<prev_y:
            skip+=1
        else:
            stk.append(intervals[i])
    return skip


sessions = [[1, 10], [2, 3], [3, 4]]
print(studybreakoptimizer(sessions))

sessions = [[1, 2], [1, 2], [1, 2]]
print(studybreakoptimizer(sessions))

sessions = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(studybreakoptimizer(sessions))