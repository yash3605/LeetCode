var twoSum = function(nums, target) {
    for (let i = 1; i < nums.length; i++) {
        for (let j = i; j < nums.length; j++) {
            if (nums[j] + nums[j - i] === target) {
                return [j - i, j];
            }
        }
    }
    return []; // Empty array if no solution found
};
