// Question

// Given an array of integers nums which is sorted in ascending order, 
// and an integer target, write a function to search target in nums. 
// If target exists, then return its index. Otherwise, return -1.
// You must write an algorithm with O(log n) runtime complexity.


// Example

// Input: nums = [-1,0,3,5,9,12], target = 9
// Output: 4
// Explanation: 9 exists in nums and its index is 4

const search = function(nums, target) {
	let low = 0
	let high = nums.length - 1
	while (low <= high){
		let mid = Math.floor((low+high)/2);
		let guess = nums[mid]
		if (guess == target){
			console.log(`${target} exists in nums and its index is ${mid}`)
			return mid
		}
		else if (guess > target){
			high = mid - 1
		}
		else {
			low = mid + 1
		}
	}
	return -1
};

console.log(search([-1,0,3,5,9,12],12))

