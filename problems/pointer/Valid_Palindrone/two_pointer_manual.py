class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 文字、数値以外だったらスキップする関数
        def is_alnum(c):
            return ("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9")

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not is_alnum(s[left]):
                left += 1
            while left < right and not is_alnum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
