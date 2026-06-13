def detect_temporal_anomaly(time_points, k):
    d = {}
    for idx,tp in enumerate(time_points):
        if tp in d and (idx-d[tp])<=k:
            return True
        d[tp] = idx
    return False

# Example Usage:


time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 

# Example Output:

# True
# True
# False
