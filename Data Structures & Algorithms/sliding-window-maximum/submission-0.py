class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        if not n or k == 0:
            return []
        if k == 1:
            return nums

        res = [0] * (n - k + 1)
        dq = [0] * n  
        l = r = 0

        for i in range(n):
            while r > l and nums[dq[r - 1]] < nums[i]:
                r -= 1
            dq[r] = i
            r += 1

            if dq[l] <= i - k:
                l += 1

            if i >= k - 1:
                res[i - k + 1] = nums[dq[l]]

        return res