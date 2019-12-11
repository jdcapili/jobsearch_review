/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
    nums.sort()
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] + 1 != nums[i + 1]) return nums[i] + 1;
    }
};