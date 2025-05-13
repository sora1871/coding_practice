# ✅ 解法4：固定長配列を使った最速版（英小文字限定）
class SolutionArray:
    def isAnagram(self, s: str, t: str) -> bool:
        # 英小文字a-zに限定される場合に最速（O(n), O(1)）
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in s:
            count[ord(i) - ord("a")] += 1
        for i in t:
            count[ord(i) - ord("a")] -= 1

        for val in count:
            if val != 0:
                return False

        return True
    

# 💬 注意点・ポイント
# - sorted(): 実装は簡単だがO(n log n)。実行時間が少し遅め。
# - dict: 柔軟でUnicodeにも対応。一般用途向け。
# - defaultdict: get()を使わずスマートに書ける。
# - 配列: 文字種が固定（a-z）の場合に最速。汎用性は低いが競技向き。

# 🔍 難しかった点：
# - Pythonの文字列はimmutableなので直接編集できない。
# - get()やdefaultdictなど、dictの初期化処理に工夫が必要。
# - ord()のインデックス変換は文字種を固定しないと使いにくい。
