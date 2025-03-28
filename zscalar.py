s = [1, 2, 3, 4]

def max_value(nums):
    big = nums[0]  # Start with the first number as the biggest
    for num in nums:
        if num > big:
            big = num  # Update 'big' with the current number if it's larger
    return big  # Return the largest number found

#print(max_value(s))

def min_value(nums):
    small = nums[0]
    for num in nums:
        if num< small:
            small = num
    return small
    
#print(min_value(s))

def add(nums):
    first= 0
    for num in nums:
        first+=num
    return first

#print(add(s))

stack =[]
pairs ={'}':'{',']':'[',')':'('}

def arrange(s):
    for char in s:
        if char in pairs.values:
            stack.append(char)
        elif not stack or stack[-1]!= pairs[char]:
            return False
        else:
            return False
    return len(stack)==0

def __init__(self):
    self.stack1= []
    self.stack2= []
    
def push(self,x):
    self.stack1.append(x)
    
def peek(self):
    if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
    return self.stack2[-1]

def pop(self):
    self.peek()
    return self.stack2.pop()       

def empty(self):
        return not self.stack1 and not self.stack2  # True if both stacks are empty
    
    
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()  # Using a queue

    def push(self, x):
        self.queue.append(x)  # Push element
        # Rotate the queue to make the last element the first
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()  # Pop the front element (which is the last pushed)

    def top(self):
        return self.queue[0]  # The front of the queue is the top of the stack

    def empty(self):
        return not self.queue  # Check if queue is empty

# Test cases
s = MyStack()
s.push(1)
s.push(2)
print(s.top())  # 2
print(s.pop())  # 2
print(s.empty()) # False

