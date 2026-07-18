# The Jedi Council has tasked you with organizing a collection of ancient kyber crystals. Each crystal has a unique power level represented by an integer. The kyber crystals are stored in a holocron in a completely random order, but to harness their true power, they must be arranged in ascending order based on their power levels.

# Given an unsorted list of crystal power levels crystals, write a function that returns crystals as a sorted list. Your function must have O(nlog(n)) time complexity.

def sort_crystals(crystals):
    if len(crystals)<2:
        return crystals
    i = len(crystals)//2
    l = sort_crystals(crystals[:i])
    r = sort_crystals(crystals[i:])
    def merge(l_arr,r_arr):
        t = len(l_arr)+len(r_arr)
        arr = [0]*t
        l_ptr,r_ptr,ptr=0,0,0
        while l_ptr<len(l_arr) and r_ptr<len(r_arr):
            if l_arr[l_ptr]<r_arr[r_ptr]:
                arr[ptr]=l_arr[l_ptr]
                l_ptr+=1
            else:
                arr[ptr]=r_arr[r_ptr]
                r_ptr+=1
            ptr+=1
        while l_ptr<len(l_arr):
            arr[ptr]=l_arr[l_ptr]
            l_ptr+=1
            ptr+=1
        while r_ptr<len(r_arr):
            arr[ptr]= r_arr[r_ptr]
            r_ptr+=1
            ptr+=1
        return arr
    return merge(l,r)


# Example Usage:

print(sort_crystals([5, 2, 3, 1]))
print(sort_crystals([5, 1, 1, 2, 0, 0]))

# Example Output:

# [1, 2, 3, 5]
# [0, 0, 1, 1, 2, 5]
