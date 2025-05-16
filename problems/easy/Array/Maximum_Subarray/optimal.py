# Kadane's Algorithm: 空間効率の良い最適解（状態を1変数で持つ）
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # 足を引っ張る場合はリセット
            max_sum = max(max_sum, current_sum)
        return max_sum
