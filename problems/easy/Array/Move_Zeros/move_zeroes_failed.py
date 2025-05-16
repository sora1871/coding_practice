from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Initial failed attempt: logic mismanages index bounds and doesn't handle sequences of 0s correctly.

        ❌ 問題点：
        - nums[i + 1] や nums[i + j] に安全にアクセスできないケースがある（IndexError）
        - 0が複数続く場合、jの使い方が不正確で期待通りに動かない
        - 実質的に非ゼロ要素の順序を保てていない
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                j += 1
                if i + j < len(nums) and nums[i + 1] != 0:
                    nums[i] = nums[i + j]
                    nums[i + j] = 0
