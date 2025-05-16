# ✅ v2: 2ポインタで in-place に重複除去する最適解
# - j はユニークな要素を書き込む位置
# - i は走査ポインタ
# - nums[i] != nums[j] のときだけ j を進めて値を更新

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1
