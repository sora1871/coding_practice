# ✅ 最適解（スライディングウィンドウ法）：O(n)
# - 最初の k 要素の合計を使って初期化
# - ウィンドウを1つずつ右にずらして合計を更新
# - O(n) 時間、O(1) 空間で最適解を実現

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[0:k])
        max_sum = current_sum

        for i in range(1, len(nums) - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum / k
