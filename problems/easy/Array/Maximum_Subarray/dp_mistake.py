# ❌ 誤ったDP実装：dp[0]を固定参照してしまい、前回の状態が使えていない
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1,n):
            dp[i] = max(nums[i], dp[0] + nums[i])  # ← dp[i-1] を使うべき
            max_sum = max(dp[i], max_sum)
        return max_sum
