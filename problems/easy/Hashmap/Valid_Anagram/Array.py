# ✅ 解法3：collections.defaultdict を使ってよりスッキリ
from collections import defaultdict

class SolutionDefaultDict:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for i in s:
            count[i] += 1
        for i in t:
            count[i] -= 1

        return all(v == 0 for v in count.values())