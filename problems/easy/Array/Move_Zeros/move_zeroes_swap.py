from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Optimal solution using the swap method.

        ✅ 長所：
        - 非ゼロを順にスワップして前に詰めることで、順序を保ちつつ0を後方へ移動できる
        - in-place かつ O(n) 時間で動作

        ✅ 特徴：
        - nums[i] != 0 のときのみスワップ
        - j: 次の非ゼロを詰める位置
        - i: 配列全体を走査
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
