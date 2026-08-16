class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                prev_val = prev_map[diff]
                return [prev_val,i]
            else:
                prev_map[num] = i

        