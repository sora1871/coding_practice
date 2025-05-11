# ✅ バージョン2：補助配列 nums3 を使って正しくマージ
# - 正しいが、インプレースでないため最適解ではない
# - 理解としては重要なステップ

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums3 = []
        j, k = 0, 0

        while j < m and k < n:
            if nums1[j] <= nums2[k]:
                nums3.append(nums1[j])
                j += 1
            else:
                nums3.append(nums2[k])
                k += 1

        while j < m:
            nums3.append(nums1[j])
            j += 1
        while k < n:
            nums3.append(nums2[k])
            k += 1

        for i in range(m + n):
            nums1[i] = nums3[i]
