class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for i, num in enumerate(nums):
            key = target - num
            if target - num in compliment:
                return i, compliment[target - num]
            compliment[num] = i