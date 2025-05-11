# ❌ v1: rangeの終点指定ミスによるループ未実行バージョン
# - for i in range(1, len(nums) - (k + 1)) により空のループ範囲になってしまう
# - sum()の使い方は正しいが、ループが動かないため何も更新されない
# - max_sumの初期値とreturn値の扱いは正しい

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ave = 0
        current_sum = sum(nums[0:0 + k])
        max_sum = current_sum
        for i in range(1, len(nums) - (k + 1)):  # ❌ 正しくは len(nums) - k + 1
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            if current_sum > max_sum:
                max_sum = current_sum
        ave = max_sum / k
        return ave
