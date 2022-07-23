# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Example

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Solution 1 with O(mlogn) aka quicksort
def searchMatrixSort(matrix, target):
    print('Solution 1')
    for array in matrix:
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = int((low+high)/2)
            guess = array[mid]
            if guess == target:
                return True
            if guess > target:
                high = mid - 1
            if guess < target:
                low = mid + 1
    return False


print(searchMatrixSort([[1,3,5,7],[10,11,16,20],[23,30,34,60]],60))
# print True

# Solution 2 with O(logM + logN). This solution is faster than solution 1 but longer to implement  
def searchMatrix(matrix,target):
    print('\nSolution 2')
    low = 0 
    high = len(matrix) - 1
    array = []

    # Apply binary search on the matrix
    while low <= high:
        mid = int((low+high)/2)
        mid_array = matrix[mid]
        if target >= mid_array[0] and target <= mid_array[-1]:
            array = mid_array
            break
        elif mid_array[0] > target:
            high = mid - 1
        else:
            low = mid + 1

    # Apply binary search on the most likely row to have to the target
    if len(array) != 0:
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = int((low+high)/2)
            guess = array[mid]
            if target == guess:
                return True
            if guess > target:
                high = mid - 1
            if guess < target:
                low = mid + 1
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],60))
# print False