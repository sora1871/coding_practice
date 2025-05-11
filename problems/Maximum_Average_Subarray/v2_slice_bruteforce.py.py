# ✅ v2: スライスを使った素直な全探索
# - 毎回 sum(nums[i:i+k]) を呼ぶことで O(n * k) の計算量
# - コードの可読性が高く、初学者には理解しやすい
# - 入力が小さい場合は実用的、ただし大規模データには不向き

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        for i in range(len(nums) - k + 1):
            current_sum = sum(nums[i:i + k])
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum / k
