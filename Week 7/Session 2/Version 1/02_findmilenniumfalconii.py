# If you implemented your check_stock() function from the previous problem iteratively, implement it recursively. If you implemented it recursively, implement it iteratively.

def check_stock(inventory, part_id):
    lo = 0
    hi = len(inventory)-1
    while lo<=hi:
        mid = lo + (hi-lo)//2
        if inventory[mid]>part_id:
            return check_stock(inventory[:mid-1],part_id)
        elif inventory[mid]<part_id:
            return check_stock(inventory[mid+1:],part_id)
        else:
            return True
    return False
            

# Example Usage:

print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))
print(check_stock([1, 2, 5, 12, 20], 1))
print(check_stock([1, 2, 5, 12, 20], -1))

# Example Ouput:

True
False
