from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Copy-forward approach: avoids swaps.

        ✅ 長所：
        - 値のスワップを避けて非ゼロを前に詰めるシンプルな方法
        - その後に0で埋めるという2段階構成

        ⚠️ 注意点：
        - スワップしないが、元と同じ値でも上書きするため、不要な書き込みが増える可能性あり
        - 非ゼロ要素の順序は維持される
        """
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
