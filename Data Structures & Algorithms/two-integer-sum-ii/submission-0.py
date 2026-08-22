class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        counter_left = 0
        counter_right = len(numbers) -1
        while counter_left < counter_right:
            counter_sum = numbers[counter_left] + numbers[counter_right]
            if counter_sum == target:
                return [counter_left + 1, counter_right + 1]
            elif counter_sum < target:
                counter_left += 1
            elif counter_sum > target:
                counter_right -=1
        
        