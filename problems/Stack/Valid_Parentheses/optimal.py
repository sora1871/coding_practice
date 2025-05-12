# ✅ 最適解（スタンダード）：閉じ括弧 → 開き括弧
# - 対応マップで逆引きチェック
# - pop() の前に stack の空チェック
# - return not stack でスタックが空＝全てペア成功を表す

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack.pop() != pairs[char]:
                    return False
        
        return not stack
