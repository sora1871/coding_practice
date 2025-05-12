# ✅ バージョン2：i < j のペアだけ比較して無駄を減らした版
# - 計算量：O(n²)
# - 比較の重複は減るが、根本的な非効率さは残っている
# - シンプルで理解しやすいが、大きな入力ではパフォーマンスに問題

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
