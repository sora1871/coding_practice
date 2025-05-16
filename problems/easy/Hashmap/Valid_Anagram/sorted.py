# ✅ 解法1：sorted() を使ったシンプルな方法
class SolutionSorted:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted()はO(n log n)だが、実装が簡潔
        return sorted(s) == sorted(t)
