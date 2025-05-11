# ✅ 最適解：後ろからインプレースでマージ（O(1) 空間）
# - 3つのポインタを使って、nums1 の末尾から詰めていく
# - nums2 に残りがあればそれだけ詰める（nums1は無視してOK）

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
