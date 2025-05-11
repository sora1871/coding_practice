# ❌ バージョン1：ロジック・構文のミスあり
# - j, k をループ内で初期化 → 毎回リセットされる
# - nums3 に直接インデックス代入しようとして IndexError
# - if条件も境界チェックが不足

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m + n):
            j, k = 0, 0
            nums3 = []
            if nums1[j] <= nums2[k]:
                nums3[i] = nums1[j]
                j += 1
            else:
                nums3[i] = nums2[k]
                k += 1

        for i in range(m + n):
            nums1[i] = nums3[i]
