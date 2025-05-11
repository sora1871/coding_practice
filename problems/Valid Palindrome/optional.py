# 2ポインタを使い、左右から英数字のみを比較
# `.isalnum()` でフィルタ、`.lower()` で大文字小文字を無視
# 文字列を前処理せずにそのまま走査する効率的な実装

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
