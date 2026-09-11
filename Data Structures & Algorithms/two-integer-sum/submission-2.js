class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = new Map()

        for (let i = 0; i < nums.length; i++ ) {
            const neededNum = target - nums[i]

            if (seen.has(neededNum)) {
                return [i, seen.get(neededNum)]
            }

            seen.set(nums[i], i)

        }
    }
}
