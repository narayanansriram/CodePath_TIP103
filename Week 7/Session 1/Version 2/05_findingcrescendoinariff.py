def myster(arr,left,right):
    if left>right:
        return -1
    mid = left + (right-left)//2
    if arr[mid]<arr[right]:
        return myster(arr,mid+1,right)
    else:
        return myster(arr,left,mid-1)
    

def complex_recursive_function(arr,multiplier):
    if not arr:
        return 1
    return arr[0]*multiplier + complex_recursive_function(arr[1:], multiplier)

print(complex_recursive_function([1,2,3], 2))
print(complex_recursive_function([4,5], 3))

def binary_search(nums,target):
    if not nums:
        return -1
    mid = len(nums)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]>target:
        return binary_search(nums[:mid], target)
    else:
        result = binary_search(nums[mid+1:], target)
        return mid + 1 + result if result != -1 else -1

print(binary_search([2,4,6,8,10,12],10))
tests = [
    ([1,2,3,4,5], 5, 4),
    ([1,2,3,4,5], 1, 0),
    ([1,2,3,4,5], 3, 2),
    ([1,2,3,4,5], 0, -1),
    ([1,2,3,4,5], 6, -1),
    ([1,3,5,7,9], 9, 4),
    ([1,3,5], 6, -1),
    ([2,4,6,8,10,12], 10, 4),
    ([2,4,6,8,10,12], 2, 0),
    ([2,4,6,8,10,12], 12, 5),
    ([2,4,6,8,10,12], 6, 2),
    ([1], 1, 0),
    ([1], 5, -1),
    ([1,2], 1, 0),
    ([1,2], 2, 1),
    ([], 5, -1),
    ([5,10,15,20,25,30,35], 25, 4),
    ([5,10,15,20,25,30,35], 5, 0),
    ([5,10,15,20,25,30,35], 35, 6),
    ([5,10,15,20,25,30,35], 17, -1),
]

all_pass = True
for nums, target, expected in tests:
    actual = binary_search(list(nums), target)
    status = "CORRECT" if actual == expected else "INCORRECT"
    if status == "INCORRECT":
        all_pass = False
    print(f"{status}: binary_search({nums}, {target}) = {actual}, expected {expected}")
print("\nALL PASS" if all_pass else "\nSOME FAILED")