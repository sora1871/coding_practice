# ✅ 別解（逆ペアバージョン）：開き括弧 → 閉じ括弧
# - 開き括弧を見たとき、対応する閉じ括弧をstackに積む
# - 閉じ括弧が出てきたとき、それがstackの先頭と一致するかを見る

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            elif char in ")]}":
                if not stack or stack.pop() != char:
                    return False
        
        return not stack
