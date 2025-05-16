# KMP (Knuth-Morris-Pratt) アルゴリズムによる部分一致検索
# 計算量: O(n + m)
# 特徴: 不一致時にneedleの比較をスキップ可能、最悪ケースでも高速
# 注意点:
#   - LPS配列構築がやや複雑
#   - whileループでi, jを慎重に操作

def build_lps(pattern: str) -> list[int]:
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        lps = build_lps(needle)
        i = j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
