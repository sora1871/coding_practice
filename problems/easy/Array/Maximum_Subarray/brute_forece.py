# Brute Force: すべての部分配列の合計を全探索（非効率だが理解に最適）
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum
