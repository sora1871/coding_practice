#❌ v2_no_filter.py
# 記号や空白、句読点などの「非英数字」もそのまま比較してしまい、誤判定になる
# 「空白」「カンマ」などを除外する処理が必要だった
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
