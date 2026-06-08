def is_palindrome(s):
    l = 0
    r = len(s)-1
    while l<=r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

# Example Usage

s = "madam"
result = is_palindrome(s)
print(result)
assert True == result, "madam is a palindrome"

s = "madamweb"
result = is_palindrome(s)
print(result)
assert False == result, "madamweb is NOT a palindrome"

# Example Output:

# True
# False
