def reverse_list(lst):
    f = 0
    b = len(lst)-1
    while f<b:
        lst[f],lst[b]=lst[b],lst[f]
        f+=1
        b-=1
    return lst

# Example Usage

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
result = reverse_list(lst)
print(result)
assert ["eeyore", "roo", "piglet", "christopher robin", "pooh"] == result, '["pooh", "christopher robin", "piglet", "roo", "eeyore"] reverses to ["eeyore", "roo", "piglet", "christopher robin", "pooh"]'

# Example Output:

# ["eeyore", "roo", "piglet", "christopher robin", "pooh"]
