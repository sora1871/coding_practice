# ✅ 解法：辞書を使ってnums1に含まれる要素を記録し、nums2を走査
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}

        # nums1に出てくる要素をTrueとして記録
        for i in nums1:
            count[i] = True

        output = []

        # nums2の各要素がnums1にあれば結果に追加（1回だけ）
        for i in nums2:
            if i in count and count[i] == True:
                output.append(i)
                count[i] = False  # 重複を防ぐため、一度追加したらFalseに

        return output

# 💡 意識したこと：
# - `count[i] = True` で辞書に存在記録を持たせる
# - `i in count and count[i] == True` で可読性を重視
# - 一度追加した要素はフラグをFalseにすることで重複排除
# - 結果の順序は問われていないのでsetの代用として使える
# - Pythonらしさと読みやすさを両立した解法
