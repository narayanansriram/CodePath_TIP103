# The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that returns a new string with the orders reversed.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def reverse_orders(orders):
    arr = orders.split(" ")
    def reverser(arr,idx):
        curr = ""
        for i in range(idx,len(arr)):
            if arr[i] == " ":
                # print(idx,curr)
                return reverser(arr,i+1) +" "+ curr
            curr+=arr[i]
        # print(idx,curr)
        return curr
    return reverser(orders,0)

# Example Usage:

print(reverse_orders("Bagel Sandwich Coffee"))

# Example Output:

# Coffee Sandwich Bagel
