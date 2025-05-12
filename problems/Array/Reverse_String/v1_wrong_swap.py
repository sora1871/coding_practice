# ❌ ミス：インデックスや制御構造の扱いに不備がある
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s)  # ❌ jは len(s) - 1 にすべき
        for i in range(len(s)):
            if i < j:
                s[i], s[j] = s[j], s[i]  # ❌ IndexErrorの可能性、swapも不正確
                i += 1  # ❌ forループ中にiを変更しても効果がない
                j -= 1
