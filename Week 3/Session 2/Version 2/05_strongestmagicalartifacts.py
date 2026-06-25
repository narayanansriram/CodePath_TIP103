def get_strongest_artifacts(artifacts, k):
    median = 0
    artifacts.sort()
    if len(artifacts)%2:
        median = artifacts[len(artifacts)//2]
    else:
        median = (artifacts[len(artifacts)//2]+artifacts[len(artifacts)//2-1])/2
    
    m_diff = sorted(artifacts,key=lambda x: [abs(x-median),x], reverse=True)
    # print(m_diff)
    return m_diff[:k]

# Example Usage:

print(get_strongest_artifacts([1, 2, 3, 4, 5], 2)) 
print(get_strongest_artifacts([1, 1, 3, 5, 5], 2)) 
print(get_strongest_artifacts([6, 7, 11, 7, 6, 8], 5)) 

# Example Output:

# [5, 1]
# [5, 5]
# [11, 8, 6, 6, 7]
