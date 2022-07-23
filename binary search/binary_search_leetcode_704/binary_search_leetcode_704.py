
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


# Example

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4


def binary_search(nums,target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((low+high)/2)
        guess = nums[mid]
        if guess == target:
            print(f"{target} exists in nums and its index is {mid}")
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low =  mid + 1
    return -1
    
binary_search([-1,0,3,5,9,12],9)
