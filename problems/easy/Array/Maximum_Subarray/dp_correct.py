# 正しいDP実装：各位置 i で終わる最大部分配列の和を配列で管理する
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])  # 前までの結果を引き継ぐ or 再スタート
            max_sum = max(max_sum, dp[i])              # 最大値を追跡

        return max_sum
