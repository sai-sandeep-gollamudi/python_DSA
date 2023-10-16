# finding the kth smallest element in list using max heap

def find_kth_smallest(nums,k):
    h=MaxHeap()
    for i in nums:
        h.insert(i)
        if(len(h.heap)>k):
            h.remove()
    return h.remove()

#Maximum element in a stream using max heap

def stream_max(nums):
    h=MaxHeap()
    ans = []
    for i in nums:
        h.insert(i)
        ans.append(h.heap[0])
    return ans

#factorial - recursion

def factorial(num):
    if(num==1 or num==0):
        return 1
    return num * factorial(num-1)

num = int(input("Enter the number you want to find factorial for: "))
print(f"The factorial of {num} is: {factorial(num)}")
