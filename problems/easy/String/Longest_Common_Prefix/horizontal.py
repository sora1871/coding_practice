# 水平スキャン（手動比較版）
class HorizontalManual:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            min_len = min(len(s), len(prefix))
            while i < min_len and prefix[i] == s[i]:
                i += 1
            prefix = prefix[:i]
            if not prefix:
                return ""
        return prefix