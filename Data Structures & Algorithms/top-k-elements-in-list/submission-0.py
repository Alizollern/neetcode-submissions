class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = dict()
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1 + count_map.get(num, 0)
        sorted_keys = sorted(count_map, key=count_map.get, reverse=True)
        return sorted_keys[:k]
        
