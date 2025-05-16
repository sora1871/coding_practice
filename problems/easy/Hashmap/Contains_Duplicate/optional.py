# ✅ 最適解：set（集合）を使った重複検出
# - 計算量：O(n)
# - 空間計算量：O(n)
# - 各要素を set に追加しながら、すでに存在していれば重複ありと判定
# - 非常に効率がよく、実務でもよく使われるパターン

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
