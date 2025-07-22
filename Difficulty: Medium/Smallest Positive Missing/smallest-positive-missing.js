// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    // Function to find the smallest positive number missing from the array.
    missingNumber(arr) {
        // your code here
        const set  = new Set(arr);
        for(let i = 1; i <= 10 **5;i++){
            if(!set.has(i)){
                return i;
            }
        }
        
    }
}