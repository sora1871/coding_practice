# Naive法による部分文字列検索
# 計算量: O((n - m + 1) * m)
# → 最悪ケースでは遅いが、実装が非常にシンプルで学習に最適
# 注意: needleが空文字の場合は0を返す仕様（LeetCode仕様に合わせる）

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1
