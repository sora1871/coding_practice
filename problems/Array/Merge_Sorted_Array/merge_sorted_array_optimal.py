from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        最適解：末尾から2ポインターでマージする。
        nums1の後半に空きがある前提を利用して、
        大きい方から後ろに埋めていく。

        計算量: 時間 O(m+n), 空間 O(1)
        """
        i = m - 1  # nums1 の実データ末尾
        j = n - 1  # nums2 の末尾
        k = m + n - 1  # 挿入位置（末尾から）

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1  # if/elseの外！

        # nums2 が残っていた場合だけコピー（nums1側は既に正位置にある）
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
