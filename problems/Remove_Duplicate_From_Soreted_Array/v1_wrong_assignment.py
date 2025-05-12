# ❌ v1: 比較に代入演算子を使ってしまったバージョン
# - `if i = j:` は構文エラー（比較は == を使う）
# - また、インデックス比較ではなく値の比較をする必要がある

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = nums[0]
        for i in range(1, len(nums)):
            if i = j:  # ❌ 構文エラー & 意図と異なる比較
                # この先のロジックが書けない
                pass
