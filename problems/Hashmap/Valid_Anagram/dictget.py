# ✅ 解法2：dict.get() を使った文字カウント法
class SolutionDict:
    def isAnagram(self, s: str, t: str) -> bool:
        # 各文字の出現回数を辞書で記録（柔軟性あり）
        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1

        for i in t:
            count[i] = count.get(i, 0) - 1

        for val in count.values():
            if val != 0:
                return False

        return True
