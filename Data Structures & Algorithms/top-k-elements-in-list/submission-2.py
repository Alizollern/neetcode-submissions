from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Counter считает всё за долю секунды на C
        count_map = Counter(nums)
        
        # 2. heapq.nlargest использует "кучу", чтобы моментально вытащить 
        # k самых частых элементов за O(n log k)
        return heapq.nlargest(k, count_map.keys(), key=count_map.get)