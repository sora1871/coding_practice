#  `.isalnum` に `()` をつけ忘れたことで、関数として呼び出せておらずバグ
# `s[left].isalnum` → `s[left].isalnum()` が正解
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum:  # ← ミス
                left += 1
            while left < right and not s[right].isalnum:  # ← ミス
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
