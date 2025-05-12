# ❌ v1: 括弧の条件式に誤りがあるバージョン
# - if char == "(" or "[" or "{" は常にTrueになってしまう
# - .isalnum など関数呼び出し忘れと同じ構文ミス
# - スタックの積み方・比較のロジックも不安定

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char == "(" or "[" or "{":
                stack.append(char)
            elif char == ")" or "]" or "}":
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        
        return not stack
