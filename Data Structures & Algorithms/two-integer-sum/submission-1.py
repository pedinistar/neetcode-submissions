class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_dict = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in the_dict:
                return [the_dict[diff], idx]
            
            the_dict[num] = idx