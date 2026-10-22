class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Бинарный поиск делаем по меньшему массиву для O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = total_left - i

            # Границы для nums1
            nums1_left = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i] if i < m else float("inf")

            # Границы для nums2
            nums2_left = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j] if j < n else float("inf")

            # Проверка корректности разбиения
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return float(max(nums1_left, nums2_left))
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right:
                # Взяли слишком много из nums1 — сдвигаемся влево
                high = i - 1
            else:
                # Взяли слишком мало из nums1 — сдвигаемся вправо
                low = i + 1

        return 0.0