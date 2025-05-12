# ✅ FizzBuzz 基本問題（LeetCode #412）
# - 3の倍数 → "Fizz"
# - 5の倍数 → "Buzz"
# - 両方の倍数 → "FizzBuzz"
# - それ以外は数値を文字列化
# - if → elif → elif → else の順番で排他的分岐

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                out.append("FizzBuzz")
            elif i % 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out
