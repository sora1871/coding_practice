# ❌ バージョン1：全ての組み合わせ (i, j) を比較（i != j）
# - 計算量：O(n²)
# - 無駄な比較が多い（(i, j) と (j, i) の重複を両方調べてしまう）
# - かろうじて正解は出るが、非常に非効率

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False
