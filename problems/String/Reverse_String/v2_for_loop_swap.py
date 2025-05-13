# ✅ 2ポインタ的発想で forループを使う実装（動作は正しいが最適化の余地あり）
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s) - 1
        for i in range(len(s)):
            if i < j:
                s[i], s[j] = s[j], s[i]
                j -= 1
