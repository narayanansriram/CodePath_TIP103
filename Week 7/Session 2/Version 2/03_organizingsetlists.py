# You are planning a series of concerts and have a list of potential songs for the setlist, each with a specific duration. You want to create a setlist that maximizes the number of songs while ensuring that the total duration of the setlist does not exceed the time limit set for the concert.

# Given an integer array song_durations where each element represents the duration of a song and an integer array concert_limits where each element represents the total time limit available for a concert, return an array setlist_sizes where setlist_sizes[i] is the maximum number of songs you can include in the playlist for concert i such that the total duration of the setlist is less than or equal to concert_limits[i].

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def concert_playlists(song_durations, concert_limits):
    song_durations.sort()
    prefixSum = [0]*len(song_durations)
    prefix = 0
    for i,song_duration in enumerate(song_durations):
        prefix+=song_duration
        prefixSum[i]=prefix
    
    def binary(arr,target):
        lo,hi = 0, len(arr)-1
        while lo<=hi:
            mid = lo + (hi - lo)//2
            if arr[mid]<target:
                lo = mid + 1
            elif arr[mid]>target:
                hi = mid - 1
            else:
                return mid
        return hi
    output = []
    for i,concert_limit in enumerate(concert_limits):
        output.append(binary(prefixSum, concert_limit)+1)
    return output

# Example Usage:

song_durations1 = [4, 3, 1, 2]
concert_limits1 = [5, 10, 15]

song_durations2 = [2, 3, 4, 5]
concert_limits2 = [1]

print(concert_playlists(song_durations1, concert_limits1))
print(concert_playlists(song_durations2, concert_limits2))

# Example Output:

# [2, 4, 4]
# Example 1 Explanation: 
# - [3, 2] has a sum less than or equal to 5, thus 2 songs can be played at concert 1.
# - [4, 3, 1, 2] has a sum less than or equal to 10, thus 4 songs can be played at concert 2.
# - [4, 3, 1, 2] has a sum less than or equal to 15, thus 4 songs can be played at concert 2.

# [0]
# Example 2 Explanation: 
# - No songs are less than 1 minute long, so zero songs can be played at the concert. 
