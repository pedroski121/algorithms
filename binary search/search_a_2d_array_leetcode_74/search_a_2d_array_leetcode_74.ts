//Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
//This matrix has the following properties:

//Integers in each row are sorted from left to right.
//The first integer of each row is greater than the last integer of the previous row.

//Example

//Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
//Output: true

function searchMatrix(matrix: number[][], target: number): boolean {
	let low = 0;
	let high= matrix.length - 1
	let array:number[] = [];
	while( low<=high ){
		let mid = Math.floor((low+high)/2);
		let guess:number[] = matrix[mid];
		if(guess[0] <= target && guess[guess.length - 1] >= target){
			array = guess;
			break;
		}
		if(guess[0] > target){
			high = mid - 1;
		}
		if(guess[guess.length - 1] < target){
			low = mid + 1
		}
	}
	if(array.length != 0){
		low = 0
		high = array.length - 1
		while(low<=high) {
			let mid = Math.floor((low+high)/2);
			let guess = array[mid]
			if(guess == target){
				console.log(`Your target ${target} was found`)
				return true;
			}
			if(guess < target) {
				low = mid + 1
			}
			if (guess > target) {
				high = mid - 1
			}
		}
	}
	console.log(`Your target ${target} was not found`)
	return false
};

searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],1)