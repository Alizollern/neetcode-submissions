class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest = 0
        
        for n in num_set:
            # Проверяем, является ли число началом последовательности
            if (n - 1) not in num_set:
                length = 1
                # Считаем длину последовательности
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
                
        return longest