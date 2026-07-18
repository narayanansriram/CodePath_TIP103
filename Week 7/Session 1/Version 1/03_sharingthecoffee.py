# The deli staff is in desperate need of caffeine to keep them going through their shift and has decided to divide the coffee supply equally among themselves. Each batch of coffee is stored in containers of different sizes. Write a recursive function can_split_coffee() that accepts a list of integers coffee representing the volume of each batch of coffee and returns True if the coffee can be split evenly by volume among n staff and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def can_split_coffee(coffee, n):
    def splitter(coffee,idx,n):
        if len(coffee)-1==idx:
            return coffee[idx]%n == 0
        else:
            for i in range(idx,len(coffee)):
                return coffee[i]%n==0 and splitter(coffee,i+1,n)
    return splitter(coffee,0,n)
# Example Usage:

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))

# Example Output:

True
False
