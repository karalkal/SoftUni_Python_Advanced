from collections import deque

nums = deque(input().split())
while len(nums) > 0:
    print(nums.pop(), end=" ")